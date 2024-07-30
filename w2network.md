> [Start](../README.md) >> Network explain

# Network explain

![](_att/Pasted%20image%2020240729224219.png)

This picture is for Docker Engine, not Docker Desktop. Docker Desktop emulates Docker application like another WSL machine, but gives direct connect to containers from WSL only. 

With Docker Engine in WSL machine you don't need to run  Docker Desktop in Windows. 

That network chain doesn't allow Windows direct connect to default container hosts. However IPvlan network driver provides direct connection to Windows internal network skipping two layers. So that approach allows you made more understandable network between all levels but works only in Linux-Docker. 

Let's look what IP address WSL obtain from Windows.

```shell
ifconfig

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
		inet 172.23.165.244  netmask 255.255.240.0  broadcast 172.23.175.255


route

Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         DESKTOP-4OTDKL4 0.0.0.0         UG    0      0        0 eth0
10.200.0.0      0.0.0.0         255.255.255.0   U     0      0        0 docker0
10.201.0.0      0.0.0.0         255.255.255.0   U     0      0        0 br-27888a08640d
172.23.160.0    0.0.0.0         255.255.240.0   U     0      0        0 eth0
```

This range corresponds to network 172.23.160.0/20. 

Next adresses I chose for my postgres and dbt:

- 172.23.174.10 	for Postgres
- 172.23.174.20 	for dbt

Create new network at WSL level interface:

```shell
docker network create -d ipvlan \
	--attachable \
	--subnet=172.23.160.0/20	\
	--gateway=172.23.160.1 \
	-o ipvlan_mode=l2 \
	-o parent=eth0 \
	dbt-net
```


Check how it works:

```shell
docker run --rm -it -d --name pg16-superstore \
	-e POSTGRES_USER=pguser1 \
	-e POSTGRES_PASSWORD=pgpass123 \
	-e POSTGRES_DB=superstore_db \
	--network=dbt-net \
	--ip=172.23.174.50 \
	postgres:16 
```


```shell
docker run --rm -it -d --name pg16 \
    -e POSTGRES_USER=pguser1 \
    -e POSTGRES_PASSWORD=pgpass123 \
 	--network=dbt-net \
 	--ip=172.23.174.60 \
    postgres:16 /bin/sh
```

```shell
docker attach pg16

psql -U pguser1 -h 172.23.174.50 -d superstore_db
```

You have access from other container from same `dbt-net` network.

![](_att/Pasted%20image%2020240729234127.png)

You don't even need port forwarding `-p 5432:5432` for access through localhost.

But you docker hosts are unavailable from your WSL host.

![](_att/Pasted%20image%2020240729234412.png)

---

> [Start](../README.md) >> Network explain