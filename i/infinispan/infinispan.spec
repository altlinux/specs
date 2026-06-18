Name:    infinispan
Version: 13.0.22
Release: alt6
Summary: Infinispan is an open source data grid platform and highly scalable NoSQL cloud data store.

Group:   Development/Java
License: Apache-2.0
URL:     https://github.com/infinispan/infinispan

Source0: %name-%version.tar
Source1: m2.tar
Source2: remove_duplicate.py
Patch0: infinispan-alt-classpathes.patch
Patch1: infinispan-alt-use-openjdk17-runtime.patch
Patch2: infinispan-alt-fix-scripts.patch

BuildRequires(pre): rpm-build-java
BuildRequires: jpackage-17-compat
BuildRequires: java-devel >= 17.0.0
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-archetype-packaging
BuildRequires: maven-scm
BuildRequires: os-maven-plugin
BuildRequires: maven-artifact-manager
BuildRequires: maven-profile
BuildRequires: maven-plugin-registry
BuildRequires: maven-dependency-plugin
BuildRequires: maven-failsafe-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: svnkit
BuildRequires: python3(lxml)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.apache.taglibs:taglibs-standard:pom:)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(commons:commons-compress)
BuildRequires: mvn(bsh:bsh)
BuildRequires: mvn(org.twdata.maven:mojo-executor)
BuildRequires: mvn(org.apache.maven:maven-project)
BuildRequires: mvn(org.apache.maven:maven-parent:pom:)
BuildRequires: mvn(jakarta.enterprise:jakarta.enterprise.cdi-api)

ExclusiveArch: x86_64 aarch64 loongarch64
AutoReqProv: yes, noosgi-fc
Requires: java-17-openjdk-headless

%description
Infinispan is an open-source in-memory database that offers flexible deployment
options and robust capabilities for storing, managing, and processing data.

Infinispan provides a key/value data store that can hold all types of data,
from Java objects to plain text.

Infinispan distributes your data across elastically scalable clusters to
guarantee high availability and fault tolerance, whether you use Infinispan as
a volatile cache or a persistent data store.

%prep
%setup
%autopatch -p1
test -d ~/.m2 && rm -rf ~/.m2
tar xf %SOURCE1 -C ~
# Disable tests build
%pom_disable_module server/tests
%pom_disable_module integrationtests
%pom_disable_module integrationtests/endpoints-interop-it
%pom_disable_module integrationtests/jboss-marshalling-it
%pom_disable_module integrationtests/cdi-jcache-it
%pom_disable_module integrationtests/security-it
%pom_disable_module integrationtests/security-manager-it
%pom_disable_module integrationtests/cdi-weld-se-it
%pom_disable_module integrationtests/spring-boot-it
%pom_disable_module integrationtests/server-integration
%pom_disable_module integrationtests/server-integration/server-integration-commons
%pom_disable_module integrationtests/server-integration/wildfly-modules
%pom_disable_module integrationtests/server-integration/third-party-server
%pom_remove_dep org.jboss.naming: hibernate
#pom_xpath_remove "pom:dependency[pom:scope='test']" hibernate/cache-v60
rm -rf hibernate/cache-*/src/test
# Disable WildFly Feature Pack
%pom_disable_module wildfly/feature-pack
# Disable get version from git
%pom_remove_plugin :buildnumber-maven-plugin

# Remove broken tests
rm -f query/src/test/java/org/infinispan/query/startup/IndexStartupModeTest.java

cat %SOURCE2 | sed 's/@VERSION@/%version/' > remove_duplicate.py

%build
%mvn_build -j -- -am -DskipTests
# Remove duplicate target for %%mvn_install
python3 remove_duplicate.py

%install
%mvn_install
# Remove javadoc and poms for vendoring libraries
subst '/\/usr\/share\/maven-/d' .mfiles
subst '/\/usr\/share\/javadoc/d' .mfiles
rm -rf %buildroot%_mavenpomdir
rm -rf %buildroot%_datadir/maven-metadata
rm -rf %buildroot%_datadir/javadoc

mkdir -p %buildroot%_libexecdir/infinispan
cp -a server/runtime/target/infinispan-server-%version.Final/* %buildroot%_libexecdir/infinispan
# Move log and conf dir to proper places
mkdir -p %buildroot{%_sysconfdir,%_logdir,%_localstatedir}/%name
mv %buildroot%_libexecdir/infinispan/server/conf/* %buildroot%_sysconfdir/%name
mv %buildroot%_libexecdir/infinispan/bin/server.conf %buildroot%_sysconfdir/%name
rm -rf %buildroot%_libexecdir/infinispan/server/{conf,log,data}
ln -s %_sysconfdir/%name %buildroot%_libexecdir/infinispan/server/conf
ln -s %_logdir/%name %buildroot%_libexecdir/infinispan/server/log
ln -s %_localstatedir/%name %buildroot%_libexecdir/infinispan/server/data
ln -s %_sysconfdir/%name/server.conf %buildroot%_libexecdir/infinispan/bin/server.conf
# Package some vendoring libraries
cp -a /usr/src/.m2/repository/javax/cache/cache-api/1.1.0/cache-api-1.1.0.jar %buildroot%_libexecdir/infinispan/lib
# Make symlink to /usr/share/java/commons-compress.jar
ln -s %_javadir/commons-compress.jar %buildroot%_libexecdir/infinispan/lib
echo '%_libexecdir/infinispan/lib/commons-compress.jar' >> .mfiles

# Install service file
mkdir -p %buildroot%_unitdir
sed 's|/opt|%_libexecdir|' %buildroot%_libexecdir/%name/docs/systemd/%name.service > %buildroot%_unitdir/%name.service

# Remove jstack because there is in java-devel
subst '/jstack/d' %buildroot%_libexecdir/infinispan/bin/report*.sh

%pre
getent group infinispan >/dev/null || /usr/sbin/groupadd -r infinispan
getent passwd infinispan >/dev/null || /usr/sbin/useradd -r \
  -g infinispan -d %_sharedstatedir/%name -s /bin/bash -c "Infinispan" infinispan

%preun
%preun_service %name.service

%post
%post_service %name.service

%files -f .mfiles
%doc *.md
%config(noreplace) %_sysconfdir/%name/*
%_libexecdir/infinispan
%_unitdir/%name.service
%attr(0755,infinispan,infinispan) %dir %_logdir/%name
%attr(0755,infinispan,infinispan) %dir %_localstatedir/%name

%changelog
* Thu Jun 18 2026 Anton Meleshnikov <alton@altlinux.org> 13.0.22-alt6
- Added new jar dependency for build.

* Thu Oct 09 2025 Andrey Cherepanov <cas@altlinux.org> 13.0.22-alt5
- Required strictly jar dependencies for build.

* Wed Oct 08 2025 Andrey Cherepanov <cas@altlinux.org> 13.0.22-alt4
- Required commons-compress.jar for cli.sh.
- Used CLASSPATH from common.sh in cli.sh.

* Tue Oct 07 2025 Andrey Cherepanov <cas@altlinux.org> 13.0.22-alt3
- Fixed path to /usr/lib/jvm/jre-17-openjdk/bin/java.
- Removed jstack because there is in java-devel.

* Mon Sep 22 2025 Andrey Cherepanov <cas@altlinux.org> 13.0.22-alt2
- Added additional vendoring libraries for p10 and c10f2.
- Automatically detected namespace of .xmvn-reactor.
- ExclusiveArch: x86_64 aarch64 loongarch64.

* Fri Sep 19 2025 Andrey Cherepanov <cas@altlinux.org> 13.0.22-alt1
- Return to Sisyphus.
- Completely rewrite spec file.

* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 8.2.4-alt2_5jpp8
- build with lucene5 (it does not build with lucene7)

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 8.2.4-alt1_5jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 8.2.4-alt1_4jpp8
- fixed build with new lucene

* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 8.2.4-alt1_3jpp8
- fixed build with new checkstyle

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 8.2.4-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.2-alt1_8jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.2-alt1_7jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_3jpp7
- new version

