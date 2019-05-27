Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           mojo-parent
Version:        40
Release:        alt1_8jpp8
Summary:        Codehaus MOJO parent project pom file

License:        ASL 2.0
URL:            http://www.mojohaus.org/mojo-parent/
Source0:        https://github.com/mojohaus/mojo-parent/archive/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  maven-local
Source44: import.info

%description
Codehaus MOJO parent project pom file

%prep
%setup -q -n %{name}-%{name}-%{version}
# Cobertura plugin is executed only during clean Maven phase.
%pom_remove_plugin :cobertura-maven-plugin
# Not needed in Fedora.
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-checkstyle-plugin

cp %SOURCE1 .

%build
%mvn_alias : org.codehaus.mojo:mojo
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:40-alt1_8jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:40-alt1_5jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:40-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:39-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:38-alt1_2jpp8
- new version

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 0:34-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:32-alt1_4jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:32-alt1_2jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:30-alt4_2jpp7
- rebuild with maven-local

* Sat Jul 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:30-alt3_2jpp7
- fixed 1.4 java mojo target in pom

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:30-alt2_2jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:30-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Tue Aug 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:30-alt1_1jpp7
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:20-alt1_2jpp6
- new version

