Group: Development/Java
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

Name:           plexus-sec-dispatcher
Version:        2.0
Release:        alt1
Summary:        Plexus Security Dispatcher Component
License:        Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-sec-dispatcher
BuildArch:      noarch

Source0:        %url/archive/%name-%version/%name-%version.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.sonatype.plexus:plexus-cipher)
%endif
Source44: import.info

%description
Plexus Security Dispatcher Component

%{?javadoc_package}

%prep
%setup -q
cp %{SOURCE1} .

%pom_remove_parent
%pom_xpath_inject 'pom:project' '<groupId>org.codehaus.plexus</groupId>'
%mvn_file : plexus/%{name}
%mvn_alias org.codehaus.plexus: org.sonatype.plexus:

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -n %{?module_prefix}%{name} -f .mfiles
%doc --no-dereference LICENSE-2.0.txt

%changelog
* Thu Apr 17 2025 Anton Meleshnikov <alton@altlinux.org> 2.0-alt1
- New version 2.0.

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 1.4-alt4_34jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.4-alt4_29jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.4-alt4_27jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.4-alt4_24jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt4_23jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt4_22jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt4_21jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt4_20jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_10jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_7jpp7
- fixed build

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_4jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

