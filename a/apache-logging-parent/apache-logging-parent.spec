Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           apache-logging-parent
Summary:        Parent pom for Apache Logging Services projects
Version:        2
Release:        alt1_1jpp8
License:        ASL 2.0

URL:            https://logging.apache.org/
Source0:        https://repo1.maven.org/maven2/org/apache/logging/logging-parent/%{version}/logging-parent-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache:apache:pom:)
Source44: import.info

%description
Parent pom for Apache Logging Services projects.


%prep
%setup -q -n logging-parent-%{version}


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE NOTICE


%changelog
* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 2-alt1_1jpp8
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1-alt1_5jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1-alt1_4jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1-alt1_3jpp8
- java update

* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 1-alt1_2jpp8
- new version

