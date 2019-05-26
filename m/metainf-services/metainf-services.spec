Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           metainf-services
Version:        1.7
Release:        alt1_6jpp8
Summary:        Small java library for generating META-INF/services files

# License is specified in pom file
License:        MIT
URL:            https://github.com/kohsuke/metainf-services
Source0:        https://github.com/kohsuke/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        https://raw.github.com/kohsuke/youdebug/youdebug-1.5/LICENSE.txt

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.kohsuke:pom:pom:)
Source44: import.info

%description
This package contains small Java library which can be used
for automatic generation of META-INF/services files.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}-%{name}-%{version}

cp %{SOURCE1} LICENSE

%pom_xpath_remove "pom:plugin[pom:artifactId[text()='animal-sniffer-maven-plugin']]"

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc LICENSE
%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_6jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_6jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_5jpp8
- new version

* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt4_0jpp6
- NMU: BR: maven-local

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_0jpp6
- migrated to mvn-rpmbuild

* Thu Feb 28 2013 Paul Wolneykien <manowar@altlinux.ru> 1.4-alt2_0jpp6
- Fix the groupId in the generated POM part.

* Thu Feb 28 2013 Paul Wolneykien <manowar@altlinux.org> 1.4-alt1_0jpp6
- Initial build for ALT Linux.
