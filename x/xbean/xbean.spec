Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Conditionals to help breaking eclipse <-> xbean dependency cycle
# when bootstrapping for new architectures
%bcond_without equinox
%bcond_without groovy
%bcond_without spring

Name:           xbean
Version:        4.5
Release:        alt1_8jpp8
Summary:        Java plugin based web server
License:        ASL 2.0
URL:            http://geronimo.apache.org/xbean/
BuildArch:      noarch

Source0:        http://repo2.maven.org/maven2/org/apache/%{name}/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Fix dependency on xbean-asm4-shaded to original objectweb-asm
Patch0:         0001-Unshade-ASM.patch
# Compatibility with Eclipse Luna (rhbz#1087461)
Patch1:         0002-Port-to-Eclipse-Luna-OSGi.patch
Patch2:         0003-Port-to-QDox-2.0.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-logging:commons-logging-api)
BuildRequires:  mvn(log4j:log4j:1.2.12)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.osgi:org.osgi.core)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.slf4j:slf4j-api)

%if %{with equinox}
BuildRequires:  mvn(org.eclipse:osgi)
%endif

%if %{with groovy}
BuildRequires:  mvn(org.codehaus.groovy:groovy-all)
%endif

%if %{with spring}
BuildRequires:  mvn(ant:ant)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(com.thoughtworks.qdox:qdox)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.springframework:spring-beans)
BuildRequires:  mvn(org.springframework:spring-context)
BuildRequires:  mvn(org.springframework:spring-web)
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

%if %{with spring}
# For now blueprint module fails to compile. Disable it.
%if 0
%package        blueprint
Group: Development/Java
Summary:        Schema-driven namespace handler for Apache Aries Blueprint

%description    blueprint
This package provides %{summary}.
%endif

%package        classloader
Group: Development/Java
Summary:        A flexibie multi-parent classloader

%description    classloader
This package provides %{summary}.

%package        spring
Group: Development/Java
Summary:        Schema-driven namespace handler for spring contexts
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description    spring
This package provides %{summary}.

%package        -n maven-%{name}-plugin
Group: Development/Java
Summary:        XBean plugin for Apache Maven

%description    -n maven-%{name}-plugin
This package provides %{summary}.
%endif

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q
# build failing on this due to doxia-sitetools problems
rm src/site/site.xml

%patch0 -p1
%if %{with equinox}
%patch1 -p1
%endif
%patch2 -p1

%pom_remove_parent
%pom_remove_dep mx4j:mx4j

%pom_remove_dep -r :xbean-asm5-shaded
%pom_remove_dep -r :xbean-finder-shaded
%pom_disable_module xbean-asm5-shaded
%pom_disable_module xbean-finder-shaded

%pom_xpath_remove pom:scope xbean-asm-util
%pom_xpath_remove pom:optional xbean-asm-util

# Prevent modules depending on springframework from building.
%if %{without spring}
   %pom_remove_dep org.springframework:
   #%%pom_disable_module xbean-blueprint
   %pom_disable_module xbean-classloader
   %pom_disable_module xbean-spring
   %pom_disable_module maven-xbean-plugin
%else
   %mvn_package :xbean-classloader classloader
   %mvn_package :xbean-spring spring
   %mvn_package :maven-xbean-plugin maven-xbean-plugin
%endif
# blueprint FTBFS, disable for now
%pom_disable_module xbean-blueprint

%if %{without equinox}
  %pom_remove_dep :xbean-bundleutils xbean-finder
  rm -r xbean-finder/src/main/java/org/apache/xbean/finder{,/archive}/Bundle*
  %pom_disable_module xbean-bundleutils
%endif

%if %{without groovy}
%pom_disable_module xbean-telnet
%endif

# maven-xbean-plugin invocation makes no sense as there are no namespaces
%pom_remove_plugin :maven-xbean-plugin xbean-classloader

# As auditing tool RAT is useful for upstream only.
%pom_remove_plugin :apache-rat-plugin

# disable copy of internal aries-blueprint
sed -i "s|<Private-Package>|<!--Private-Package>|" xbean-blueprint/pom.xml
sed -i "s|</Private-Package>|</Private-Package-->|" xbean-blueprint/pom.xml

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE
%dir %{_javadir}/%{name}

%if %{with spring}
%if 0
%files blueprint -f .mfiles-blueprint
%doc LICENSE NOTICE %{name}-blueprint/target/restaurant.xsd*
%endif

%files classloader -f .mfiles-classloader
%doc LICENSE NOTICE

%files spring -f .mfiles-spring
%doc LICENSE NOTICE

%files -n maven-%{name}-plugin -f .mfiles-maven-%{name}-plugin
%doc LICENSE NOTICE
%endif

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
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

