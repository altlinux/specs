Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           objectweb-pom
Version:        1.5
Release:        alt1_9jpp8
Summary:        Objectweb POM
BuildArch:      noarch
License:        ASL 2.0
URL:            http://gitorious.ow2.org/ow2/pom/
Source0:        http://repo.maven.apache.org/maven2/org/ow2/ow2/%{version}/ow2-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
Source44: import.info

%description
This package provides Objectweb parent POM used by different
Objectweb packages.

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_9jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_3jpp8
- new version

* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

