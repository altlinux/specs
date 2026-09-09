Name:    apache-zookeeper
Version: 3.8.6
Release: alt1
Summary: The Apache ZooKeeper system for distributed coordination is a high-performance service for building distributed applications

Group:   Development/Java
License: Apache-2.0
URL:     https://zookeeper.apache.org/
Source0: %name-%version.tar
Source1: m2.tar
Patch0: apache-zookeeper-pathes.patch

BuildRequires(pre): rpm-build-java
BuildRequires: java-devel >= 1.6.0
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.apache.maven:maven-profile)
BuildRequires: mvn(org.apache.maven:maven-plugin-registry)
BuildRequires: mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires: mvn(org.apache.maven:maven-toolchain)
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(io.netty:netty-handler)
BuildRequires: mvn(org.apache.yetus:audience-annotations)
BuildRequires: mvn(ch.qos.logback:logback-core)
BuildRequires: mvn(io.netty:netty-transport-native-epoll)
BuildRequires: mvn(io.dropwizard.metrics:metrics-core)
BuildRequires: mvn(org.eclipse.jetty:jetty-security)
BuildRequires: mvn(org.eclipse.jetty:jetty-server)
BuildRequires: mvn(org.eclipse.jetty:jetty-util)

BuildArch: noarch
Requires: java >= 1.6.0

Provides: zookeeper = %EVR
Obsoletes: zookeeper < %EVR

Requires: jetty9-server
Requires: jetty9-security
Requires: jetty9-util
Requires: metrics
Requires: snappy-java

%description
ZooKeeper is a centralized service for maintaining configuration information,
naming, providing distributed synchronization, and providing group services.

#{?javadoc_package}

%prep
%setup
%patch0 -p2
test -d ~/.m2 && rm -rf ~/.m2
tar xf %SOURCE1 -C ~
%pom_remove_parent
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :checksum-maven-plugin
subst '/-Werror/d' pom.xml
# Installation fail
%pom_disable_module zookeeper-assembly
# Unable to package requirements for zookeeper-prometheus-metrics
%pom_disable_module zookeeper-metrics-providers

%build
%mvn_build -f -j

%install
%mvn_install
install -Dp bin/*.sh --target-directory %buildroot%_bindir
install -Dpm0644 conf/zoo_sample.cfg %buildroot%_sysconfdir/zookeeper/zoo.cfg
mkdir -p %buildroot%_unitdir
cat > %buildroot%_unitdir/zookeeper.service << END
[Unit]
Description=Apache ZooKeeper Distributed Coordination Service
After=network.target

[Service]
Type=forking
User=zookeeper
Group=zookeeper
SyslogIdentifier=zookeeper
ExecStart=zkServer.sh start
ExecStop=zkServer.sh stop
ExecReload=zkServer.sh restart
TimeoutSec=300
Restart=on-failure
PIDFile=/var/lib/zookeeper/zookeeper_server.pid

[Install]
WantedBy=multi-user.target
END
mkdir -p %buildroot%_sharedstatedir/zookeeper

%pre
getent group zookeeper >/dev/null || /usr/sbin/groupadd -r zookeeper
getent passwd zookeeper >/dev/null || /usr/sbin/useradd -r \
  -g zookeeper -d %_sharedstatedir/zookeeper -s /bin/bash -c "Zookeeper" zookeeper

%preun
%preun_service zookeeper.service

%post
%post_service zookeeper.service

%files -f .mfiles
%doc *.md
%config(noreplace) %_sysconfdir/zookeeper/zoo.cfg
%_bindir/*.sh
%_unitdir/zookeeper.service
%attr(0750,zookeeper,zookeeper) %dir %_sharedstatedir/zookeeper

%changelog
* Wed Sep 09 2026 Andrey Cherepanov <cas@altlinux.org> 3.8.6-alt1
- Initial build for Sisyphus.
