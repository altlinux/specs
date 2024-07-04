Name:    kafka
Version: 3.7.1
Release: alt1.1

Summary: Apache Kafka is a distributed event store and stream-processing platform
License: Apache-2.0
Group:   System/Servers
Url:     https://github.com/apache/kafka

Packager: Andrey Cherepanov <cas@altlinux.org>

ExclusiveArch: x86_64 aarch64 loongarch64

Source: %name-%version.tar
Source1: gradle-8.7-rc-4-bin.zip
Source2: gradle-cache.tar
Source4: kafka.logrotate
Source5: kafka.service
Source6: kafka.sysconfig
Source7: zookeeper.service
Patch0: kafka-pathes.patch

BuildRequires(pre): /proc rpm-build-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: unzip

AutoReqProv: yes, noosgi-fc
Requires: java >= 17

%description
Apache Kafka is a distributed event store and stream-processing platform. It is
an open-source system developed by the Apache Software Foundation written in
Java and Scala. The project aims to provide a unified, high-throughput,
low-latency platform for handling real-time data feeds.

%prep
%setup
%patch0 -p1
unzip %SOURCE1
tar xf %SOURCE2 -C ~
rm -rf bin/windows

%build
export PATH=$PATH:$PWD/gradle-8.7-rc-4/bin
gradle releaseTarGz

%install
mkdir -p %buildroot%_libexecdir/%name
tar xf core/build/distributions/kafka_2.13-%version.tgz \
       -C %buildroot%_libexecdir/%name \
       --strip-components=1

# Move config to /etc
mkdir -p %buildroot%_sysconfdir
mv %buildroot%_libexecdir/%name/config %buildroot%_sysconfdir/%name
ln -s ../../../etc/kafka %buildroot%_libexecdir/%name/config

# Install other files
install -Dpm0644 %SOURCE4 %buildroot%_logrotatedir/%name
install -Dpm0644 %SOURCE5 %buildroot%_unitdir/%name.service
install -Dpm0644 %SOURCE6 %buildroot%_sysconfdir/sysconfig/%name
install -Dpm0644 %SOURCE7 %buildroot%_unitdir/zookeeper.service
mkdir -p %buildroot%_logdir/%name
mkdir -p %buildroot%_sharedstatedir/%name

%pre
getent group kafka >/dev/null || /usr/sbin/groupadd -r kafka
getent passwd kafka >/dev/null || /usr/sbin/useradd -r \
  -g kafka -d %{_prefix}/%{name} -s /bin/bash -c "Kafka" kafka

%preun
%preun_service %name.service
%preun_service zookeeper.service

%post
%post_service %name.service
%post_service zookeeper.service

%files
%doc README.md
%_libexecdir/%name
%_unitdir/%name.service
%_unitdir/zookeeper.service
%attr(0750,kafka,kafka) %dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_logrotatedir/%name
%attr(0755,kafka,kafka) %dir %_logdir/%name
%attr(0750,kafka,kafka) %dir %_sharedstatedir/%name

%changelog
* Thu Jul 04 2024 Ivan A. Melnikov <iv@altlinux.org> 3.7.1-alt1.1
- NMU: Buid on loongarch64.

* Tue Jul 02 2024 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt1
- New version.

* Fri May 24 2024 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus.
