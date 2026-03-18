Name:           logback
Version:        1.2.13
Release:        alt1

Summary:        The reliable, generic, fast and flexible logging framework for Java
License:        Logback
Group:          Development/Java
URL:            http://logback.qos.ch/
VCS:            https://github.com/qos-ch/logback

Source0:        %name-%version.tar

Patch0:         0001-replace-javax-with-jakarta-mail.patch
Patch1:         0002-logback-avoid-sun-reflect-reflection.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.janino:janino)
BuildRequires:  mvn(jakarta.mail:jakarta.mail-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.ant:ant-junit)

BuildArch:      noarch

%description
Logback is intended as a successor to the popular log4j project. At present
time, logback is divided into three modules, logback-core, logback-classic
and logback-access.

The logback-core module lays the groundwork for the other two modules. The
logback-classic module can be assimilated to a significantly improved
version of log4j. Moreover, logback-classic natively implements the SLF4J
API so that you can readily switch back and forth between logback and other
logging frameworks such as log4j or java.util.logging (JUL).

The logback-access module integrates with Servlet containers, such as
Tomcat and Jetty, to provide HTTP-access log functionality. Note that you
could easily build your own module on top of logback-core.

%javadoc_package

%package classic
Group:         Development/Java
Summary:       Logback Classic Module

%description classic
Logback-classic module.

%prep
%setup
%autopatch -p1

%pom_remove_plugin :maven-source-plugin

%pom_change_dep -r javax.mail:mail jakarta.mail:jakarta.mail-api

# disabled, cause package use old tomcat
%pom_disable_module logback-access
%pom_disable_module logback-examples

%pom_disable_module logback-site

%mvn_package ":%name-classic" classic

%build

%mvn_build -f -- \
  -Dorg.slf4j:slf4j-api:jar=$(build-classpath slf4j/api) \
  -Dorg.apache.felix:org.apache.felix.main:jar=$(build-classpath felix/org.apache.felix.main) \
  -Dmaven.compiler.release=8 \

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt *.md

%files classic -f .mfiles-classic
%doc LICENSE.txt *.md

%changelog
* Thu Mar 12 2026 Evgeniy Serov <scala@altlinux.org> 1.2.13-alt1
- Updated to 1.2.13.
- Returned to Sisyphus.

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt1_6jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_2jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_5jpp8
- java 8 mass update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt2_2jpp7
- fixed build (use java6 due to reflection API change)

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt1_2jpp7
- fc update

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_3jpp7
- new version

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.27-alt1_1jpp6
- new version

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.14-alt2_2jpp6
- build with compat slf4j15

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.14-alt1_2jpp6
- new version

