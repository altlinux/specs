Name:           slf4j
Epoch:          0
Version:        1.7.36
Release:        alt3

Summary:        Simple Logging Facade for Java
License:        MIT and Apache-2.0
Group:          Development/Java
URL:            http://www.slf4j.org/
VCS:            https://github.com/qos-ch/slf4j

Source0:        v_%version.tar.gz
Source1:        LICENSE-2.0.txt

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(ch.qos.reload4j:reload4j)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(ch.qos.cal10n:cal10n-api)
BuildRequires:  mvn(javassist:javassist)
BuildRequires:  mvn(commons-lang:commons-lang)

BuildArch:      noarch

%description
The Simple Logging Facade for Java or (SLF4J) is intended to serve
as a simple facade for various logging APIs allowing to the end-user
to plug in the desired implementation at deployment time. SLF4J also
allows for a gradual migration path away from
Jakarta Commons Logging (JCL).

Logging API implementations can either choose to implement the
SLF4J interfaces directly, e.g. NLOG4J or SimpleLogger. Alternatively,
it is possible (and rather easy) to write SLF4J adapters for the given
API implementation, e.g. Log4jLoggerAdapter or JDK14LoggerAdapter..

%package -n     jcl-over-slf4j
Summary:        JCL 1.2 implemented over SLF4J
Group:          Development/Java

%description -n jcl-over-slf4j
%summary.

%package -n     jul-to-slf4j
Summary:        JUL to SLF4J bridge
Group:          Development/Java

%description -n jul-to-slf4j
%summary.

%package -n     log4j-over-slf4j
Summary:        Log4j implemented over SLF4J
Group:          Development/Java

%description -n log4j-over-slf4j
%summary.

%package        ext
Summary:        SLF4J Extensions Module
Group:          Development/Java

%description    ext
%summary.

%package        jcl
Summary:        SLF4J JCL Binding
Group:          Development/Java

%description    jcl
%summary.

%package        jdk14
Summary:        SLF4J JDK14 Binding
Group:          Development/Java

%description    jdk14
%summary.

%package        reload4j
Summary:        SLF4J LOG4J-12 Binding
Group:          Development/Java

%description    reload4j
%summary.

%package        migrator
Summary:        SLF4J Migrator
Group:          Development/Java

%description    migrator
%summary.

%package        sources
Summary:        SLF4J Source JARs
Group:          Development/Java

%description    sources
%summary.

%javadoc_package

%prep
%setup -q -n %{name}-v_%{version}
find -name '*.jar' -delete
install -p -m 0644 %{SOURCE1} LICENSE-2.0.txt

# port to maven-antrun-plugin 3.0.0
sed -i s/tasks/target/ slf4j-api/pom.xml

%pom_disable_module slf4j-android
%pom_disable_module osgi-over-slf4j
%pom_disable_module integration
%pom_disable_module slf4j-log4j12

%mvn_package :%name-api
%mvn_package :%name-nop
%mvn_package :%name-simple

%mvn_package :::sources: sources

%mvn_package :%name-parent __noinstall
%mvn_package :%name-site __noinstall

%mvn_file ':slf4j-{*}' %name/slf4j-@1 %name/@1

%build
# tests fails cause there are problems with bindings
%mvn_build -f -s -- -Drequired.jdk.version=1.8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt README.md

%files -n jcl-over-slf4j -f .mfiles-jcl-over-slf4j
%files -n jul-to-slf4j -f .mfiles-jul-to-slf4j
%files -n log4j-over-slf4j -f .mfiles-log4j-over-slf4j
%files ext -f .mfiles-slf4j-ext
%files jcl -f .mfiles-slf4j-jcl
%files jdk14 -f .mfiles-slf4j-jdk14
%files reload4j -f .mfiles-slf4j-reload4j
%files migrator -f .mfiles-slf4j-migrator
%files sources -f .mfiles-sources
%doc LICENSE.txt README.md

%changelog
* Fri Jun 05 2026 Evgeniy Serov <scala@altlinux.org> 0:1.7.36-alt3
- Build with required JDK version set to 1.8.

* Wed Apr 08 2026 Evgeniy Serov <scala@altlinux.org> 0:1.7.36-alt2
- Enabled previously disabled modules.

* Wed Apr 30 2025 Anton Meleshnikov <alton@altlinux.org> 0:1.7.36-alt1
- New version 1.7.36.

* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 0:1.7.32-alt1_3jpp11
- new version

* Thu Jun 16 2022 Igor Vlasenko <viy@altlinux.org> 0:1.7.30-alt1_8jpp11
- build w/o log4j12

* Wed Jun 08 2022 Igor Vlasenko <viy@altlinux.org> 0:1.7.30-alt1_7jpp11
- Port to maven-antrun-plugin 3.0.0
- disabled slf4j-ext and slf4j-log4j12 subpackages

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 0:1.7.30-alt1_6jpp11
- fixed build

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 0:1.7.30-alt1_2jpp11
- new version

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.7.25-alt1_6jpp8
- fc update & java 8 build

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.7.25-alt1_4jpp8
- java update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7.25-alt1_2jpp8
- new jpp release

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7.22-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7.21-alt1_2jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7.18-alt1_1jpp8
- new version

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7.14-alt1_1jpp8
- added osgi provides

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7.12-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.5-alt1_3jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.4-alt1_1jpp7
- update

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt4_4jpp7
- more symlinks

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt3_4jpp7
- added compat symlinks

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt2_4jpp7
- rebuild with maven-local

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt1_4jpp7
- update

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt1_1jpp7
- new version

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.6-alt1_2jpp7
- new version

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt3_5jpp7
- fc version

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_5jpp7
- fc version

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_5jpp6
- new version

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_4jpp6
- new version (full build)

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_4jpp6
- new version (bootstrap)

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.8-alt1_1jpp6
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_2jpp5
- converted from JPackage by jppimport script

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_2jpp1.7
- updated to new jpackage release

* Mon Dec 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_1jpp1.7
- added dependency on new excalibur

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

