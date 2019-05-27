Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          maven-shared-resources
Version:       2
Release:       alt1_8jpp8
Summary:       A collection of templates that are specific to the Maven project
License:       ASL 2.0
URL:           http://maven.apache.org/shared/maven-shared-resources/
Source0:       http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildRequires: maven-local
BuildRequires: maven-remote-resources-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires: mvn(org.apache.rat:apache-rat-plugin)
BuildArch:     noarch
Source44: import.info

%description
This is a collection of templates that are specific to the Maven project.
They are probably not of interest to projects other than Apache Maven.

%prep
%setup -q

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 2-alt1_8jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 2-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2-alt1_3jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 2-alt1_2jpp8
- new version

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1-alt1_1jpp7
- update

* Sun Aug 24 2014 Igor Vlasenko <viy@altlinux.ru> 1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

