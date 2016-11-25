Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 25
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# Conditionals to help breaking eclipse <-> xbean dependency cycle
# when bootstrapping for new architectures
%if 0%{?fedora}
%bcond_without equinox
%bcond_without spring
%endif

Name:           xbean
Version:        4.4
Release:        alt1_2jpp8
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

BuildRequires:  java-devel
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-logging
BuildRequires:  objectweb-asm
BuildRequires:  ant
BuildRequires:  qdox
BuildRequires:  slf4j
BuildRequires:  maven-local
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-shade-plugin
%if %{with equinox}
BuildRequires:  eclipse-equinox-osgi
%else
BuildRequires:  felix-framework
%endif
%if %{with spring}
BuildRequires:  apache-commons-jexl
BuildRequires:  aries-blueprint
# test deps
BuildRequires:  cglib
BuildRequires:  felix-osgi-compendium
BuildRequires:  felix-osgi-core
BuildRequires:  geronimo-annotation
BuildRequires:  pax-logging

BuildRequires:  maven-archiver
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-project
BuildRequires:  plexus-archiver
BuildRequires:  plexus-utils
BuildRequires:  springframework
BuildRequires:  springframework-beans
BuildRequires:  springframework-context
BuildRequires:  springframework-web
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
Requires:       %{name} = %{version}

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

%pom_remove_dep -r :xbean-asm-util
%pom_remove_dep -r :xbean-asm5-shaded
%pom_remove_dep -r :xbean-finder-shaded
%pom_disable_module xbean-asm-util
%pom_disable_module xbean-asm5-shaded
%pom_disable_module xbean-finder-shaded

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
  # Replace Eclipse Equinox OSGi dependency with Apeche Felix
  rm -rf xbean-bundleutils/src/main/java/org/apache/xbean/osgi/bundle/util/equinox/
  %pom_remove_dep org.eclipse:osgi xbean-bundleutils
  %pom_add_dep org.apache.felix:org.apache.felix.framework xbean-bundleutils
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

