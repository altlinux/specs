Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           apache-commons-pool
Version:        1.6
Release:        alt2_29jpp11
Summary:        Apache Commons Pool Package
License:        ASL 2.0
URL:            http://commons.apache.org/pool/
BuildArch:      noarch

Source0:        http://www.apache.org/dist/commons/pool/source/commons-pool-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
Source44: import.info

%description
The goal of Pool package is it to create and maintain an object (instance)
pooling package to be distributed under the ASF license. The package should
support a variety of pool implementations, but encourage support of an
interface that makes these implementations interchangeable.

%{?javadoc_package}

%prep
%setup -q -n commons-pool-%{version}-src


# Compatibility links
%mvn_alias : org.apache.commons:commons-pool
%mvn_file : commons-pool %{name}

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt
%doc README.txt RELEASE-NOTES.txt

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:1.6-alt2_29jpp11
- update

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 0:1.6-alt2_22jpp11
- update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_19jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_17jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_16jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_15jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_14jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_13jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp7
- new version

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt3_6jpp6
- fixed build

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt2_6jpp6
- fixed build with maven3

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt1_6jpp6
- new version

