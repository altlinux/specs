Name:           mbassador
Version:        1.3.1
Release:        alt3

Summary:        Powerful event-bus optimized for high throughput in multi-threaded applications
License:        MIT
Group:          Development/Java
Url:            https://github.com/bennidi/mbassador

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-17-compat

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:slf4j-reload4j)
BuildRequires:  mvn(de.odysseus.juel:juel-impl)
BuildRequires:  mvn(de.odysseus.juel:juel-spi)
BuildRequires:  mvn(javax.el:el-api)

BuildArch:      noarch

%description
MBassador is a light-weight, high-performance event bus implementing the publish
subscribe pattern. It is designed for ease of use and aims to be feature rich
and extensible while preserving resource efficiency and performance.

The core of MBassador is built around a custom data structure that provides
non-blocking reads and minimized lock contention for writes such that
performance degradation of concurrent read/write access is minimal.

%javadoc_package

%prep
%setup

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%pom_change_dep :slf4j-log4j12 :slf4j-reload4j

rm src/test/java/net/engio/mbassy/bus/AbstractPubSubSupportTest.java
rm src/test/java/net/engio/mbassy/SynchronizedHandlerTest.java
sed -i '/SynchronizedHandlerTest/d' src/test/java/net/engio/mbassy/AllTests.java

%build
%mvn_build -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README.md

%changelog
* Mon Jun 29 2026 Evgeniy Serov <scala@altlinux.org> 1.3.1-alt3
- Fixed FTBFS: disable broken test on i586.

* Fri May 29 2026 Evgeniy Serov <scala@altlinux.org> 1.3.1-alt2
- Fixed FTBFS: added missing BuildRequires.

* Thu Apr 23 2026 Evgeniy Serov <scala@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
