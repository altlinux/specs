Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global short_name spring-retry

Name:           springframework-retry
Version:        1.1.1
Release:        alt1_6jpp8
Summary:        Abstraction around retrying failed operations

License:        ASL 2.0
URL:            https://github.com/spring-projects/spring-retry
Source0:        https://github.com/spring-projects/%{short_name}/archive/%{version}.RELEASE.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j:1.2.17)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.aspectj:aspectjweaver)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.springframework:spring-context)
BuildRequires:  mvn(org.springframework:spring-test)
BuildRequires:  mvn(org.springframework:spring-tx)

Provides:       spring-retry = %{version}-%{release}
Obsoletes:      spring-retry < %{version}-%{release}

BuildArch:      noarch
Source44: import.info

%description
Spring Retry provides an abstraction around retrying failed operations, 
with an emphasis on declarative control of the process and policy-based 
bahaviour that is easy to extend and customize. For instance, you can 
configure a plain POJO operation to retry if it fails, based on the type 
of exception, and with a fixed or exponential backoff.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}

Provides:       spring-retry-javadoc = %{version}-%{release}
Obsoletes:      spring-retry-javadoc < %{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}.RELEASE

%pom_remove_dep org.springframework:spring-test

# bom dependency, we don't have it
%pom_remove_dep org.springframework:spring-framework-bom

%pom_remove_plugin :maven-javadoc-plugin

%pom_change_dep :log4j ::1.2.17

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_4jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_3jpp8
- java 8 mass update

