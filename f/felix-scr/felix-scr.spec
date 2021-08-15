Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global bundle  org.apache.felix.scr

Name:          felix-scr
Version:       2.1.26
Release:       alt1_2jpp11
Summary:       Apache Felix Service Component Runtime (SCR)
License:       ASL 2.0
URL:           https://felix.apache.org/documentation/subprojects/apache-felix-service-component-runtime.html

Source0:       http://archive.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

# Don't embed deps, use import-package instead
Patch0: 0001-Use-import-package-instead-of-embedding-dependencies.patch

BuildArch:     noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.gogo.runtime)
BuildRequires:  mvn(org.osgi:osgi.annotation)
BuildRequires:  mvn(org.osgi:osgi.cmpn) >= 7.0.0
BuildRequires:  mvn(org.osgi:osgi.core) >= 7.0.0
Source44: import.info

%description
Implementation of the OSGi Declarative Services Specification Version 1.4 (R7).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{bundle}-%{version}
%patch0 -p1

# All these OSGi deps are provided in the compendium jar
%pom_add_dep org.osgi:osgi.cmpn:7.0.0:provided
%pom_remove_dep org.osgi:org.osgi.service.component
%pom_remove_dep org.osgi:org.osgi.service.cm
%pom_remove_dep org.osgi:org.osgi.service.log
%pom_remove_dep org.osgi:org.osgi.service.metatype
%pom_remove_dep org.osgi:org.osgi.namespace.extender
%pom_remove_dep org.osgi:org.osgi.util.promise
%pom_remove_dep org.osgi:org.osgi.util.function

# Many test deps are not in Fedora
%pom_xpath_remove "pom:project/pom:dependencies/pom:dependency[pom:scope='test']"
%pom_remove_dep org.ops4j.base:
%pom_remove_plugin :maven-failsafe-plugin

# Animal sniffer is unnecessary since we always know JRE level on Fedora
%pom_remove_dep :animal-sniffer-annotations
sed -i -e '/IgnoreJRERequirement/d' src/main/java/org/apache/felix/scr/impl/manager/ThreadDump.java

%mvn_file : felix/%{bundle}

%build
# No test deps availables e.g org.ops4j.pax.url:pax-url-wrap
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dfelix.java.version=8

%install
%mvn_install

%files -f .mfiles
%doc changelog.txt
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 2.1.26-alt1_2jpp11
- new version

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 2.1.16-alt1_8jpp11
- new version

