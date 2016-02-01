Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             felix-gogo-parent
Version:          0.6.0
Release:          alt2_13jpp8
Summary:          Parent package for Felix Gogo
License:          ASL 2.0
URL:              http://felix.apache.org/site/apache-felix-gogo.html

Source0:          http://apache.mirror.rbftpnetworks.com//felix/gogo-parent-0.6.0-project.tar.gz

BuildArch:        noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.mockito:mockito-all)
Source44: import.info
Provides: mvn(org.apache.felix:gogo-parent) = 0.6.0

%description
Apache Felix is a community effort to implement the OSGi R4 Service Platform
and other interesting OSGi-related technologies under the Apache license. The
OSGi specifications originally targeted embedded devices and home services
gateways, but they are ideally suited for any project interested in the
principles of modularity, component-orientation, and/or service-orientation.
OSGi technology combines aspects of these aforementioned principles to define a
dynamic service deployment framework that is amenable to remote management.

%prep
%setup -q -n gogo-parent-%{version}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Tue Aug 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_3jpp7
- new version

