%global bundled_slf4j_version 1.7.36
%global apphomedir %_datadir/maven
%global confdir %_sysconfdir/maven

Name:           maven
Epoch:          1
Version:        3.9.9
Release:        alt1

Summary:        Apache Maven core
License:        Apache-2.0 and MIT
Group:          Development/Java
URL:            https://maven.apache.org/
VCS:            https://github.com/apache/maven

Source0:        %name-%version.tar
Source1:        maven-bash-completion
Source2:        mvn.1

Patch1:         0001-Adapt-mvn-script.patch
Patch3:         0003-Remove-dependency-on-powermock.patch
Patch6:         0006-Load-maven-resolver-named-locks.patch

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.xmlunit:xmlunit-core)
BuildRequires:  mvn(org.xmlunit:xmlunit-matchers)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(commons-jxpath:commons-jxpath)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(org.slf4j:slf4j-simple::sources:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-named-locks)

Requires:       %name-lib = %EVR

BuildArch:      noarch

%description
Maven is a software project management and comprehension tool. Based on the
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

%package        lib
Group:          Development/Java
Summary:        Core part of Maven
Requires:       xmvn-minimal
Provides:       bundled(slf4j) = %bundled_slf4j_version

%description lib
Core part of Apache Maven that can be used as a library.

%javadoc_package

%prep
%setup

sed -i 's/\r$//' apache-maven/src/bin/m2.conf
%autopatch -p1

%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :buildnumber-maven-plugin maven-core

%pom_remove_dep :powermock-reflect maven-model-builder

%mvn_package :apache-maven __noinstall
%mvn_alias :maven-resolver-provider :maven-aether-provider

%build
%mvn_build

mkdir -p m2home
tar --delay-directory-restore \
    -xf apache-maven/target/apache-maven-%version-bin.tar.gz \
    -C m2home

%install
%mvn_install

MAVEN_HOME=$(pwd)/m2home/apache-maven-%version

install -d -m 755 %buildroot%apphomedir/conf
install -d -m 755 %buildroot%confdir
install -d -m 755 %buildroot%_datadir/bash-completion/completions/

cp -a "$MAVEN_HOME"/{bin,lib,boot} %buildroot%apphomedir/

# Replace bundled JARs with links to system Java packages
xmvn-subst -s -R %buildroot -s %buildroot%apphomedir

rm -f %buildroot%apphomedir/bin/*.cmd
rm -f %buildroot%apphomedir/bin/mvnyjp

ln -s %_prefix/lib/jansi/libjansi.so \
    %buildroot%apphomedir/lib/jansi-native/

install -p -m 644 %SOURCE2 %buildroot%apphomedir/bin/
gzip -9n %buildroot%apphomedir/bin/mvn.1

install -d -m 755 %buildroot%_bindir
install -d -m 755 %buildroot%_man1dir

ln -s "$(relative %apphomedir/bin/mvn %_bindir/)" \
    %buildroot%_bindir/mvn
ln -s "$(relative %apphomedir/bin/mvnDebug %_bindir/)" \
    %buildroot%_bindir/mvnDebug
ln -s "$(relative %apphomedir/bin/mvn.1.gz %_man1dir/)" \
    %buildroot%_man1dir/mvn.1.gz

install -p -m 644 %SOURCE1 \
    %buildroot%_datadir/bash-completion/completions/mvn

# Store Maven configuration under /etc and link it from Maven home
install -p -m 644 "$MAVEN_HOME/bin/m2.conf" \
    %buildroot%_sysconfdir/m2.conf
ln -sfn %_sysconfdir/m2.conf %buildroot%apphomedir/bin/m2.conf

install -p -m 644 "$MAVEN_HOME/conf/settings.xml" %buildroot%confdir/
ln -sfn %confdir/settings.xml %buildroot%apphomedir/conf/settings.xml

cp -a "$MAVEN_HOME/conf/logging" %buildroot%confdir/
ln -sfn %confdir/logging %buildroot%apphomedir/conf/logging

touch %buildroot%_sysconfdir/mavenrc

%files lib -f .mfiles
%doc README.md LICENSE NOTICE
%apphomedir
%exclude %apphomedir/bin/mvn*
%dir %confdir
%dir %confdir/logging
%config(noreplace) %_sysconfdir/m2.conf
%config(noreplace) %confdir/settings.xml
%config(noreplace) %confdir/logging/simplelogger.properties

%files
%apphomedir/bin/mvn*
%_bindir/mvn
%_bindir/mvnDebug
%_datadir/bash-completion/completions/*
%_mandir/man1/mvn.1*
%config(noreplace,missingok) /etc/mavenrc

%changelog
* Tue Aug 18 2026 Evgeniy Serov <scala@altlinux.org> 1:3.9.9-alt1
- Updated to 3.9.9 (Closes: #48910, #51532).
- Updated build dependencies and removed obsolete patches.

* Mon Aug 17 2026 Evgeniy Serov <scala@altlinux.org> 1:3.8.8-alt6
- Added maven-resolver-named-locks to the Maven ClassWorlds configuration.

* Mon May 11 2026 Evgeniy Serov <scala@altlinux.org> 1:3.8.8-alt5
- Removed maven-enforcer-plugin from build.

* Thu Aug 21 2025 Andrey Cherepanov <cas@altlinux.org> 1:3.8.8-alt4
- Added aopalliance and asm to libraries.

* Tue Aug 05 2025 Andrey Cherepanov <cas@altlinux.org> 1:3.8.8-alt3
- End of bootstrap google-guice-5.1.0.

* Tue Jul 29 2025 Andrey Cherepanov <cas@altlinux.org> 1:3.8.8-alt2
- Boostrapped google-guice-5.1.0.
- Built without tests.

* Wed Apr 30 2025 Anton Meleshnikov <alton@altlinux.org> 1:3.8.8-alt1
- New version 3.8.8 (thanks CentOS for the patch).

* Sat Apr 19 2025 Anton Meleshnikov <alton@altlinux.org> 1:3.8.4-alt1
- New version 3.8.4.

* Fri Apr 18 2025 Anton Meleshnikov <alton@altlinux.org> 1:3.8.2-alt1
- new version

* Mon Apr 14 2025 Anton Meleshnikov <alton@altlinux.org> 1:3.8.1-alt1jpp11
- new version

* Sun Jun 12 2022 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt5_10jpp11
- maven-openjdkXX support

* Sat Jun 11 2022 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt4_10jpp11
- update

* Wed Jun 08 2022 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt4_9jpp11
- nobootstrap

* Tue Jun 07 2022 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt3_9jpp11
- jarlink bootstrap for guava update

* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt2_9jpp11
- support for new cdi-api
- added jarlink_bootstrap option

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt2_8jpp11
- fixed alternatives

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt1_8jpp11
- fc34 update

* Wed Jun 02 2021 Igor Vlasenko <viy@altlinux.org> 1:3.6.3-alt1_4jpp11
- new version

* Wed Jun 02 2021 Igor Vlasenko <viy@altlinux.org> 1:3.6.1-alt2_5jpp11
- fixed build with new modello

* Fri May 14 2021 Igor Vlasenko <viy@altlinux.org> 1:3.6.1-alt1_5jpp11
- new version

* Sun May 09 2021 Igor Vlasenko <viy@altlinux.org> 1:3.5.4-alt1_12jpp8
- update

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.5.4-alt1_10jpp8
- fixed build

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.5.4-alt1_7jpp8
- build with new mockito

* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.5.4-alt1_4jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.5.3-alt1_1jpp8
- new version

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt1_5jpp8
- fc 28 update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt1_1jpp8
- new version

* Sun Nov 19 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.5.0-alt1_6jpp8
- new version

* Sun Oct 29 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.3.9-alt1_9jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3.9-alt1_6jpp8
- new fc release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3.9-alt1_4jpp8
- new version

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3.3-alt1_3jpp8
- java 8 mass update

* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.5-alt1_3jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.5-alt0.2jpp
- rebuild to add provides

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

