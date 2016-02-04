Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           felix-gogo-shell
Version:        0.10.0
Release:        alt2_15jpp8
Summary:        Community OSGi R4 Service Platform Implementation - Basic Commands
License:        ASL 2.0
URL:            http://felix.apache.org/site/apache-felix-gogo.html
BuildArch:      noarch

Source0:        http://mirror.catn.com/pub/apache//felix/org.apache.felix.gogo.shell-0.10.0-project.tar.gz
  
# Changed GroupID from osgi to felix
Patch0:         %{name}-groupid.patch

Patch1:         ignoreActivatorException.patch
%define pkg_name %name
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:gogo-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.gogo.runtime)
BuildRequires:  mvn(org.apache.felix:org.osgi.compendium)
BuildRequires:  mvn(org.apache.felix:org.osgi.core)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.mockito:mockito-all)
Source44: import.info

%description
Apache Felix is a community effort to implement the OSGi R4 Service Platform
and other interesting OSGi-related technologies under the Apache license. The
OSGi specifications originally targeted embedded devices and home services
gateways, but they are ideally suited for any project interested in the
principles of modularity, component-orientation, and/or service-orientation.
OSGi technology combines aspects of these aforementioned principles to define a
dynamic service deployment framework that is amenable to remote management.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{pkg_name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n org.apache.felix.gogo.shell-%{version}
%patch0 -p1 -F3
%patch1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt2_15jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt2_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_4jpp7
- new release

