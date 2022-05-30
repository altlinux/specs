Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           xbean
Version:        4.18
Release:        alt1_4jpp11
Summary:        Java plugin based web server
License:        ASL 2.0
URL:            https://geronimo.apache.org/xbean/
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/%{name}/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch1:         0001-Remove-unused-import.patch
Patch2:         0002-Unbundle-ASM.patch
Patch3:         0003-Remove-dependency-on-log4j-and-commons-logging.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.osgi:org.osgi.core)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.slf4j:slf4j-api)
%endif
Source44: import.info

%description
The goal of XBean project is to create a plugin based server
analogous to Eclipse being a plugin based IDE. XBean will be able to
discover, download and install server plugins from an Internet based
repository. In addition, we include support for multiple IoC systems,
support for running with no IoC system, JMX without JMX code,
lifecycle and class loader management, and a rock solid Spring
integration.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

cp xbean-asm-util/src/main/java/org/apache/xbean/asm9/original/commons/AsmConstants.java xbean-reflect/src/main/java/org/apache/xbean/recipe/

# Parent POM is not packaged
%pom_remove_parent

%pom_disable_module xbean-classloader
%pom_disable_module xbean-classpath
%pom_disable_module xbean-bundleutils
%pom_disable_module xbean-asm9-shaded
%pom_disable_module xbean-finder-shaded
%pom_disable_module xbean-naming
%pom_disable_module xbean-blueprint
%pom_disable_module xbean-spring
%pom_disable_module xbean-telnet
%pom_disable_module maven-xbean-plugin

%pom_remove_dep :commons-logging-api xbean-reflect
%pom_remove_dep :log4j xbean-reflect
%pom_remove_dep :xbean-asm9-shaded xbean-reflect
find -name CommonsLoggingConverter.java -delete
find -name Log4jConverter.java -delete

# Plugins useful for upstream only
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-source-plugin

%pom_remove_dep :xbean-bundleutils xbean-finder
rm -r xbean-finder/src/main/java/org/apache/xbean/finder{,/archive}/Bundle*

# Disable one test that fails on JDK 11
sed -i '/testGetBytecode/i@org.junit.Ignore' xbean-finder/src/test/java/org/apache/xbean/finder/archive/MJarJarArchiveTest.java

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Mon May 30 2022 Igor Vlasenko <viy@altlinux.org> 0:4.18-alt1_4jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:4.15-alt2_7jpp11
- fc34 update

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 0:4.15-alt2_5jpp11
- fixed build

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:4.15-alt1_5jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:4.14-alt1_1jpp8
- new version

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0:4.9-alt1_2jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:4.8-alt1_1jpp8
- java update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:4.5-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:4.5-alt1_8jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:4.5-alt1_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.5-alt1_3jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.4-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt1_1jpp8
- unbootsrap build

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.13-alt1_4jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.13-alt1_1jpp7
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.12-alt1_4jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt4_3jpp7
- fixed build

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt3_3jpp7
- restored rcp dep

* Sun Mar 31 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt2_3jpp7
- bootstrapping eclipse - dropped eclipse-rcp dep

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt1_3jpp7
- new version

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.8-alt1_2jpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.7-alt3_7jpp7
- fixed build

* Tue May 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.7-alt2_7jpp7
- added maven-xbean-plugin

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.7-alt1_7jpp7
- new version

* Tue Jan 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.4.3-alt1_2jpp6
- new version

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt1_1jpp5
- first build

