Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             felix-gogo-parent
Version:          2
Release:          alt1_3jpp8
Summary:          Parent package for Felix Gogo
License:          ASL 2.0
URL:              http://felix.apache.org/documentation/subprojects/apache-felix-gogo.htm

Source0:          https://repo1.maven.org/maven2/org/apache/felix/gogo-parent/%{version}/gogo-parent-%{version}-source-release.tar.gz

BuildArch:        noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
Source44: import.info

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
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 2-alt1_2jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt3_15jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt3_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt3_13jpp8
- new version

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

