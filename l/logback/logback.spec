Name:           logback
Version:        1.6.7
Release:        alt1

Summary:        The reliable, generic, fast and flexible logging framework for Java
License:        Logback
Group:          Development/Java
URL:            http://logback.qos.ch/
VCS:            https://github.com/qos-ch/logback

Source0:        %name-%version.tar

Patch0:         jline-module-name.patch

BuildRequires(pre):  maven-local
BuildRequires:  java-21-openjdk-devel

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.janino:janino)
BuildRequires:  mvn(jakarta.mail:jakarta.mail-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.ant:ant-junitlauncher)
BuildRequires:  mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires:  slf4j2
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.jline:jansi-core)
BuildRequires:  mvn(org.tukaani:xz)
BuildRequires:  mvn(com.esotericsoftware.kryo:kryo5)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  jakarta-servlet

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

%package core-kryo
Group:         Development/Java
Summary:       Kryo serialization support for Logback Core

%description core-kryo
Kryo serialization support for the Logback Core module.

%package classic-kryo
Group:         Development/Java
Summary:       Kryo serialization support for Logback Classic

%description classic-kryo
Kryo serialization support for the Logback Classic module.

%prep
%setup
%autopatch -p1

%pom_remove_plugin :maven-source-plugin

%pom_remove_plugin :central-publishing-maven-plugin
%pom_xpath_remove pom:build/pom:extensions

# Use the system SLF4J 2 provider.
%pom_xpath_set pom:properties/pom:slf4j.version 2

# logback-access is released independently.
%pom_disable_module logback-access
%pom_disable_module logback-examples

# These modules contain only test fixtures.
%pom_disable_module logback-core-blackbox
%pom_disable_module logback-classic-misc
%pom_disable_module logback-classic-blackbox

%mvn_package ":%name-parent:pom:"
%mvn_package ":%name-core"
%mvn_package ":%name-core-kryo" core-kryo
%mvn_package ":%name-classic" classic
%mvn_package ":%name-classic-kryo" classic-kryo

%build

%mvn_build -f -s

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt *.md

%files core-kryo -f .mfiles-core-kryo

%files classic -f .mfiles-classic
%doc LICENSE.txt *.md

%files classic-kryo -f .mfiles-classic-kryo

%changelog
* Sat Nov 14 2026 Ivan Khanas <xeno@altlinux.org> 1.6.7-alt1
- New version.

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

