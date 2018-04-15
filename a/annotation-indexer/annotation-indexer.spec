Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           annotation-indexer
Version:        1.9
Release:        alt1_7jpp8
Summary:        Jenkins annotation-indexer library

# License is specified in pom file
License:        MIT
URL:            https://github.com/jenkinsci/lib-annotation-indexer
Source0:        https://github.com/jenkinsci/lib-%{name}/archive/%{name}-%{version}.tar.gz
Source1:        https://raw.github.com/jenkinsci/jenkins/jenkins-1.510/LICENSE.txt

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.kohsuke.metainf-services:metainf-services)
Source44: import.info

%description
Annotation-indexer is a small java library
used for listing annotations at compile time.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n lib-%{name}-%{name}-%{version}

cp %{SOURCE1} LICENSE

# Nothing really interesting in parent
%pom_remove_parent
%pom_xpath_inject "pom:project" "<groupId>org.jenkins-ci</groupId>"

%build
# tests are disabled because of missing dependency (com.jolira:hickory)
%mvn_build -f

%install
%mvn_install


%files -f .mfiles
%doc LICENSE
%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_4jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_3jpp8
- java 8 mass update

