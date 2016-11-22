Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-java
BuildRequires: gcc-c++ perl(Config.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(threads.pm) perl-devel python-devel
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
%global commit          601207e1151b2691112c431fc3b4130a85ac93b5
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global _hardened_build 1
%global skiptests       1

Name:          zookeeper
Version:       3.4.6
Release:       alt1_16jpp8
Summary:       A high-performance coordination service for distributed applications
License:       ASL 2.0 and BSD
URL:           http://zookeeper.apache.org/
Source0:       https://github.com/apache/zookeeper/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:       %{name}-ZooInspector-template.pom
Source2:       %{name}.service
Source3:       zkEnv.sh

Patch1:        %{name}-3.4.5-zktreeutil-gcc.patch
Patch2:        %{name}-3.4.6-ivy-build.patch
Patch3:        %{name}-3.4.6-server.patch
# patch accepted in 3.5.0
Patch4:        https://issues.apache.org/jira/secure/attachment/12570030/mt_adaptor.c.patch


BuildRequires: autoconf-common
BuildRequires: automake-common
BuildRequires: boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-signals-devel boost-wave-devel
BuildRequires: cppunit-devel
BuildRequires: dos2unix
BuildRequires: doxygen
BuildRequires: graphviz libgraphviz
BuildRequires: java-javadoc
BuildRequires: javapackages-tools rpm-build-java
BuildRequires: libtool-common
BuildRequires: libxml2-devel
BuildRequires: python-base python-dev

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: apache-ivy
BuildRequires: checkstyle
BuildRequires: ivy-local
BuildRequires: maven-local

BuildRequires: jtoaster
BuildRequires: junit
BuildRequires: jdiff
%if 0%{?fedora} >= 21
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: objectweb-pom
BuildRequires: jline1
BuildRequires: netty3
Requires:      log4j12
%else
BuildRequires: mvn(log4j:log4j)
BuildRequires: jline
BuildRequires: netty
Requires:      log4j
%endif

BuildRequires: json_simple

BuildRequires: mockito
BuildRequires: slf4j
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis

# remove later on.
BuildRequires: apache-commons-parent
BuildRequires: jetty-server
BuildRequires: jetty-servlet
BuildRequires: journalctl libsystemd-devel libudev-devel systemd systemd-analyze systemd-coredump systemd-networkd systemd-services systemd-utils

Requires:      checkstyle
Requires:      jline1
Requires:      jtoaster
Requires:      junit
Requires:      mockito
Requires:      netty3
Requires:      slf4j
Requires: javapackages-tools rpm-build-java
Requires:      %{name}-java = %{version}
Source44: import.info

%description
ZooKeeper is a centralized service for maintaining configuration information,
naming, providing distributed synchronization, and providing group services.

##############################################
%package devel
Group: Development/Java
Summary:       Development files for the %{name} library
Requires:      %{name}%{?_isa} = %{version}

%description devel
Development files for the ZooKeeper C client library.

##############################################
%package java
Summary:        Java interface for %{name}
Group:          Development/Other
Requires:       %{name}%{?_isa} = %{version}

%description java
The %{name}-java package contains Java bindings for %{name}.

##############################################
%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch:     noarch

%description javadoc
This package contains javadoc for %{name}.

%package -n python-module-zookeeper
Group: Development/Java
Summary:       Python support for %{name}
Requires:      %{name}%{?_isa} = %{version}
Provides:      zkpython%{?_isa} = %{version}-%{release}
Requires:      python

%description -n python-module-zookeeper
The python-%{name} package contains Python bindings for %{name}.

%prep
%setup -q -n %{name}-%{commit}

%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p0 -F2

iconv -f iso8859-1 -t utf-8 src/c/ChangeLog > src/c/ChangeLog.conv && mv -f src/c/ChangeLog.conv src/c/ChangeLog
sed -i 's/\r//' src/c/ChangeLog

sed -i 's|<exec executable="hostname" outputproperty="host.name"/>|<!--exec executable="hostname" outputproperty="host.name"/-->|' build.xml
sed -i 's|<attribute name="Built-On" value="${host.name}" />|<attribute name="Built-On" value="${user.name}" />|' build.xml

sed -i 's@^dataDir=.*$@dataDir=%{_sharedstatedir}/zookeeper/data\ndataLogDir=%{_sharedstatedir}/zookeeper/log@' conf/zoo_sample.cfg

%build
%ant -Divy.mode=local \
-DCLASSPATH=/usr/share/java/log4j12-1.2.17.jar \
-Dtarget.jdk=1.5 \
-Djavadoc.link.java=%{_javadocdir}/java \
-Dant.build.javac.source=1.5 \
-Dant.build.javac.target=1.5 \
package

pushd src/c
autoreconf -if
%configure --disable-static --disable-rpath
%{__make} %{?_smp_mflags}
popd

## TODO: install utilities?

%check
%if %skiptests
  echo "Testing disabled, please enable in mock"
%else
  %ant -Divy.mode=local test
%endif

%install

# the following is used to update zkEnv.sh
# find . -name "*.jar" -exec basename {} \; |sort|uniq
# remove items that don't belong and update execute build-classpath

#install the c tools
pushd src/c
%makeinstall_std
popd

# install the java dependencies.
mkdir -p %{buildroot}%{_javadir}/%{name}
install -pm 644 build/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
install -pm 644 build/%{name}-%{version}-test.jar %{buildroot}%{_javadir}/%{name}/%{name}-tests.jar
install -pm 644 build/contrib/ZooInspector/%{name}-%{version}-ZooInspector.jar %{buildroot}%{_javadir}/%{name}/%{name}-ZooInspector.jar

install -pm 755 bin/zkCleanup.sh %{buildroot}%{_bindir}
install -pm 755 bin/zkCli.sh %{buildroot}%{_bindir}
install -pm 755 bin/zkServer.sh %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libexecdir}
install -pm 755 %{SOURCE3} %{buildroot}%{_libexecdir}

%if 0%{?fedora} >= 21
mkdir -p %{buildroot}%{_datadir}/maven-metadata
mkdir -p %{buildroot}%{_datadir}/maven-poms
install -pm 644 build/%{name}-%{version}/dist-maven/%{name}-%{version}.pom %{buildroot}%{_datadir}/maven-poms/%{name}-%{name}.pom

%add_maven_depmap %{name}-%{name}.pom %{name}/%{name}.jar
%add_maven_depmap org.apache.zookeeper:zookeeper::tests:%{version} %{name}/%{name}-tests.jar

install -pm 644 %{SOURCE1} %{buildroot}%{_datadir}/maven-poms/%{name}-%{name}-ZooInspector.pom
sed -i "s|@version@|%{version}|" %{buildroot}%{_datadir}/maven-poms/%{name}-%{name}-ZooInspector.pom
%add_maven_depmap %{name}-%{name}-ZooInspector.pom %{name}/%{name}-ZooInspector.jar
%else
mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 build/%{name}-%{version}/dist-maven/%{name}-%{version}.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}.pom

%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar
%add_maven_depmap org.apache.zookeeper:zookeeper::tests:%{version} %{name}/%{name}-tests.jar

install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-ZooInspector.pom
sed -i "s|@version@|%{version}|" %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-ZooInspector.pom
%add_maven_depmap JPP.%{name}-%{name}-ZooInspector.pom %{name}/%{name}-ZooInspector.jar
%endif

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/docs/api/* %{buildroot}%{_javadocdir}/%{name}/

pushd src/contrib/zkpython
%{__python} src/python/setup.py build --build-base=$PWD/build \
install --root=%{buildroot} ;\
chmod 0755 %{buildroot}%{python_sitelibdir}/zookeeper.so
popd

find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/zookeeper
mkdir -p %{buildroot}%{_var}/log/zookeeper
mkdir -p %{buildroot}%{_sharedstatedir}/zookeeper
mkdir -p %{buildroot}%{_sharedstatedir}/zookeeper/data
mkdir -p %{buildroot}%{_sharedstatedir}/zookeeper/log
install -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}
install -p -m 0640 conf/log4j.properties %{buildroot}%{_sysconfdir}/zookeeper
install -p -m 0640 conf/zoo_sample.cfg %{buildroot}%{_sysconfdir}/zookeeper
touch %{buildroot}%{_sysconfdir}/zookeeper/zoo.cfg
touch %{buildroot}%{_sharedstatedir}/zookeeper/data/myid

# touching all ghosts; hack for rpm 4.0.4
for rpm_404_ghost in %{_sysconfdir}/zookeeper/zoo.cfg %{_sharedstatedir}/zookeeper/data/myid
do
    mkdir -p %buildroot`dirname "$rpm_404_ghost"`
    touch %buildroot"$rpm_404_ghost"
done


%pre
getent group zookeeper >/dev/null || groupadd -r zookeeper
getent passwd zookeeper >/dev/null || \
    useradd -r -g zookeeper -d %{_sharedstatedir}/zookeeper -s /sbin/nologin \
    -c "ZooKeeper service account" zookeeper

%post
%post_service zookeeper
: 

%preun
%preun_service zookeeper

%files
%{_bindir}/cli_mt
%{_bindir}/cli_st
%{_bindir}/load_gen
%{_bindir}/zk*.sh
%{_libexecdir}/zkEnv.sh
%{_libdir}/lib*.so.*

%attr(0755,root,root) %dir %{_sysconfdir}/zookeeper
%attr(0644,root,root) %ghost %config(noreplace) %{_sysconfdir}/zookeeper/zoo.cfg
%attr(0644,root,root) %{_sysconfdir}/zookeeper/zoo_sample.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/zookeeper/log4j.properties

%attr(0755,zookeeper,zookeeper) %dir %{_var}/log/zookeeper
%attr(0755,root,root) %dir %{_sharedstatedir}/zookeeper
%attr(0750,zookeeper,zookeeper) %dir %{_sharedstatedir}/zookeeper/data
%attr(0640,zookeeper,zookeeper) %ghost %{_sharedstatedir}/zookeeper/data/myid
%attr(0755,zookeeper,zookeeper) %dir %{_sharedstatedir}/zookeeper/log
%{_unitdir}/zookeeper.service
%doc CHANGES.txt LICENSE.txt NOTICE.txt README.txt

%files java
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}.jar
%{_javadir}/%{name}/%{name}-tests.jar
%{_javadir}/%{name}/%{name}-ZooInspector.jar
%if 0%{?fedora} >= 21
%{_datadir}/maven-poms/%{name}-%{name}.pom
%{_datadir}/maven-poms/%{name}-%{name}-ZooInspector.pom
%{_datadir}/maven-metadata/%{name}.xml
%else
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-ZooInspector.pom
%endif
%doc CHANGES.txt LICENSE.txt NOTICE.txt README.txt

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%doc src/c/LICENSE src/c/NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%files -n python-module-zookeeper
%{python_sitelibdir}/ZooKeeper-?.?-py%{__python_version}.egg-info
%{python_sitelibdir}/zookeeper.so
%doc LICENSE.txt NOTICE.txt src/contrib/zkpython/README

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.4.6-alt1_16jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 3.4.6-alt1_15jpp8
- new version

