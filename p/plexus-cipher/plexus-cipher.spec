Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: maven-local
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           plexus-cipher
Version:        2.0
Release:        alt1_2jpp11
Summary:        Plexus Cipher: encryption/decryption Component
License:        ASL 2.0
# project moved to GitHub and it looks like there is no official website anymore
URL:            https://github.com/codehaus-plexus/plexus-cipher
BuildArch:      noarch

Source0:        https://github.com/codehaus-plexus/plexus-cipher/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
%endif
Source44: import.info

%description
Plexus Cipher: encryption/decryption Component

%{?javadoc_package}

%prep
%setup -q -n %{name}-%{name}-%{version}
%mvn_file : plexus/%{name}
%mvn_alias org.codehaus.plexus: org.sonatype.plexus:

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Mon Apr 17 2023 Igor Vlasenko <viy@altlinux.org> 2.0-alt1_2jpp11
- update

* Sat Jul 02 2022 Igor Vlasenko <viy@altlinux.org> 1.8-alt1_3jpp11
- new version

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 1.7-alt3_24jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.7-alt3_21jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_18jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_16jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_14jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_13jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_11jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_10jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_2jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt3_11jpp7
- rebuild with maven-local

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_11jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_11jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_8jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_7jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

