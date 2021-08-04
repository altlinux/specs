Epoch: 0
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

Name:           felix-parent
Version:        7
Release:        alt1_6jpp11
Summary:        Parent POM file for Apache Felix Specs
License:        ASL 2.0
URL:            https://felix.apache.org/
Source0:        https://repo1.maven.org/maven2/org/apache/felix/felix-parent/%{version}/%{name}-%{version}-source-release.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache:apache:pom:)
%endif
Source44: import.info

%description
Parent POM file for Apache Felix Specs.

%prep
%setup -q -n felix-parent-%{version}
%mvn_alias : :felix
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin org.codehaus.mojo:ianal-maven-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin

# wagon ssh dependency unneeded
%pom_xpath_remove pom:extensions

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:7-alt1_6jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:7-alt1_3jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:4-alt1_9jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:4-alt1_7jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:4-alt1_6jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:4-alt1_5jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:4-alt1_4jpp8
- new fc release

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 0:4-alt1_3jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_13jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_10jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_9jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_8jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt5_11jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt5_8jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt4_8jpp7
- new release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt4_5jpp6
- use maven-plugin-build-helper

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt3_5jpp6
- fixed build with maven3

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt2_5jpp6
- new jpp release

* Wed Jun 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt2_3jpp6
- dropped mojo-maven2-* dependency

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_3jpp6
- fixed repolib

