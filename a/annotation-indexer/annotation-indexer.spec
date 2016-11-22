Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           annotation-indexer
Version:        1.9
Release:        alt1_4jpp8
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
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_4jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_3jpp8
- java 8 mass update

