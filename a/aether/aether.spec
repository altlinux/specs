Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global vertag v20150114

Name:           aether
Epoch:          1
Version:        1.0.2
Release:        alt1_4jpp8
Summary:        Library to resolve, install and deploy artifacts the Maven way
License:        EPL
URL:            http://eclipse.org/aether
BuildArch:      noarch

Source0:        http://git.eclipse.org/c/%{name}/%{name}-core.git/snapshot/%{name}-%{version}.%{vertag}.tar.bz2

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.inject:guice::no_aop:)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin) >= 1.7
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
Source44: import.info

%description
Aether is a standalone library to resolve, install and deploy artifacts
the Maven way.

%package api
Group: Development/Java
Summary: Aether API

%description api
Aether is a standalone library to resolve, install and deploy
artifacts the Maven way.  This package provides application
programming interface for Aether repository system.

%package connector-basic
Group: Development/Java
Summary: Aether Connector Basic

%description connector-basic
Aether is a standalone library to resolve, install and deploy
artifacts the Maven way.  This package provides repository connector
implementation for repositories using URI-based layouts.

%package impl
Group: Development/Java
Summary: Implementation of Aether repository system

%description impl
Aether is a standalone library to resolve, install and deploy
artifacts the Maven way.  This package provides implementation of
Aether repository system.

%package spi
Group: Development/Java
Summary: Aether SPI

%description spi
Aether is a standalone library to resolve, install and deploy
artifacts the Maven way.  This package contains Aether service
provider interface (SPI) for repository system implementations and
repository connectors.

%package test-util
Group: Development/Java
Summary: Aether test utilities

%description test-util
Aether is a standalone library to resolve, install and deploy
artifacts the Maven way.  This package provides collection of utility
classes that ease testing of Aether repository system.

%package transport-classpath
Group: Development/Java
Summary: Aether Transport Classpath

%description transport-classpath
Aether is a standalone library to resolve, install and deploy
artifacts the Maven way.  This package provides a transport
implementation for repositories using classpath:// URLs.

%package transport-file
Group: Development/Java
Summary: Aether Transport File
Obsoletes: %{name}-connector-file < %{epoch}:%{version}-%{release}

%description transport-file
Aether is a standalone library to resolve, install and deploy
artifacts the Maven way.  This package provides a transport
implementation for repositories using file:// URLs.

%package transport-http
Group: Development/Java
Summary: Aether Transport HTTP
Obsoletes: %{name}-connector-asynchttpclient < %{epoch}:%{version}-%{release}

%description transport-http
Aether is a standalone library to resolve, install and deploy
artifacts the Maven way.  This package provides a transport
implementation for repositories using http:// and https:// URLs.

%package transport-wagon
Group: Development/Java
Summary: Aether Transport Wagon
Obsoletes: %{name}-connector-wagon < %{epoch}:%{version}-%{release}

%description transport-wagon
Aether is a standalone library to resolve, install and deploy
artifacts the Maven way.  This package provides a transport
implementation based on Maven Wagon.

%package util
Group: Development/Java
Summary: Aether utilities

%description util
Aether is a standalone library to resolve, install and deploy
artifacts the Maven way.  This package provides a collection of
utility classes to ease usage of Aether repository system.

%package javadoc
Group: Development/Java
Summary: Java API documentation for Aether
BuildArch: noarch

%description javadoc
Aether is a standalone library to resolve, install and deploy
artifacts the Maven way.  This package provides Java API documentation
for Aether.

%prep
%setup -q -n %{name}-%{version}.%{vertag}

# Remove clirr plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_remove_plugin :clirr-maven-plugin aether-api
%pom_remove_plugin :clirr-maven-plugin aether-util
%pom_remove_plugin :clirr-maven-plugin aether-spi

# Animal sniffer is not useful in Fedora
for module in . aether-api aether-connector-basic aether-impl   \
              aether-spi aether-test-util aether-transport-file \
              aether-transport-classpath aether-transport-http  \
              aether-transport-wagon aether-util; do
    %pom_remove_plugin :animal-sniffer-maven-plugin $module
done

# HTTP transport tests require Jetty 7 and networking.
rm -rf aether-transport-http/src/test
%pom_xpath_remove "pom:dependency[pom:scope='test']" aether-transport-http

%pom_remove_plugin :maven-enforcer-plugin

# Upstream uses Sisu 0.0.0.M4, but Fedora has 0.0.0.M5.  In M5 scope
# of Guice dependency was changed from "compile" to "provided".
%pom_add_dep com.google.inject:guice::provided . "<classifier>no_aop</classifier>"

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}
%doc README.md
%doc epl-v10.html notice.html

%files api -f .mfiles-%{name}-api
%doc README.md
%doc epl-v10.html notice.html
%dir %{_javadir}/%{name}

%files connector-basic -f .mfiles-%{name}-connector-basic
%files impl -f .mfiles-%{name}-impl
%files spi -f .mfiles-%{name}-spi
%files test-util -f .mfiles-%{name}-test-util
%files transport-classpath -f .mfiles-%{name}-transport-classpath
%files transport-file -f .mfiles-%{name}-transport-file
%files transport-http -f .mfiles-%{name}-transport-http
%files transport-wagon -f .mfiles-%{name}-transport-wagon
%files util -f .mfiles-%{name}-util
%files javadoc -f .mfiles-javadoc
%doc epl-v10.html notice.html

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_4jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_2jpp8
- new version

* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sun Aug 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt6_7jpp7
- xmvn build

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt6_4jpp7
- more compat symlinks added

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt5_4jpp7
- added compat symlink

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt4_4jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt3_4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt1_4jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

