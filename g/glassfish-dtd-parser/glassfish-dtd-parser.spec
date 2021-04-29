Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname jaxb-dtd-parser

Name:          glassfish-dtd-parser
Version:       1.4
Release:       alt1_2jpp11
Summary:       Library for parsing XML DTDs
License:       CDDL-1.1 and GPLv2 with exceptions

# NOTE: The new upstream repository under the Eclipse EE4J umbrella is here:
# https://github.com/eclipse-ee4j/jaxb-dtd-parser
URL:           https://github.com/javaee/%{srcname}
Source0:       %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: mvn(net.java:jvnet-parent:pom:)
Source44: import.info

%description
Library for parsing XML DTDs.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{srcname}-%{version}

# builds fail if this file is present
rm dtd-parser/src/module-info.java

%build
pushd dtd-parser
%mvn_file :dtd-parser %{name}
%mvn_build -- -Dmaven.compile.source=1.8 -Dmaven.compile.target=1.8 -Dmaven.javadoc.source=1.8
popd

%install
pushd dtd-parser
%mvn_install
popd

%files -f dtd-parser/.mfiles
%doc --no-dereference LICENSE

%files javadoc -f dtd-parser/.mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.4-alt1_2jpp11
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.19.20120120svnjpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.18.20120120svnjpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.17.20120120svnjpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.16.20120120svnjpp8
- new fc release

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.15.20120120svnjpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.14.20120120svnjpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.13.20120120svnjpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.12.20120120svnjpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.8.20120120svnjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.6.20120120svnjpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.4.20120120svnjpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_0.4.20120120svnjpp7
- new version

