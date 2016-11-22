Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global registry geronimo-osgi-registry
%global locator geronimo-osgi-locator

Name:             geronimo-osgi-support
Version:          1.0
Release:          alt2_18jpp8
Summary:          OSGI spec bundle support
License:          ASL 2.0 and W3C
URL:              http://geronimo.apache.org/

Source0:          http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{name}/%{version}/%{name}-%{version}-source-release.tar.gz
BuildArch:        noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    maven-local
BuildRequires:    felix-osgi-core
BuildRequires:    felix-osgi-compendium
BuildRequires:    geronimo-parent-poms
BuildRequires:    maven-resources-plugin


Provides:         geronimo-osgi-locator = %{version}-%{release}
Provides:         geronimo-osgi-registry = %{version}-%{release}
Source44: import.info

%description
This project is a set of bundles and integration tests for implementing
OSGi-specific lookup in the Geronimo spec projects.


%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
iconv -f iso8859-1 -t utf-8 LICENSE > LICENSE.conv && mv -f LICENSE.conv LICENSE
sed -i 's/\r//' LICENSE NOTICE
# Use parent pom files instead of unavailable 'genesis-java5-flava'
%pom_set_parent org.apache.geronimo.specs:specs:1.4

# Remove itests due to unavailable dependencies
%pom_disable_module geronimo-osgi-itesta
%pom_disable_module geronimo-osgi-itestb
%pom_disable_module geronimo-osgi-registry-itests
%pom_disable_module geronimo-osgi-locator-itests

%pom_xpath_inject "pom:plugin[pom:artifactId[text()='maven-bundle-plugin']]
                       /pom:configuration/pom:instructions" "
    <Export-Package>!*</Export-Package>" geronimo-osgi-locator

# preserve compatibility locations for jars
%mvn_file ':{*}' @1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_18jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_17jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_12jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_9jpp7
- new version

