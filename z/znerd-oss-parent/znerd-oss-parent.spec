Group: Development/C
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          znerd-oss-parent
Version:       3
Release:       alt2_15jpp8
Summary:       Znerd.org OSS Parent
License:       BSD
URL:           https://github.com/znerd/znerd-oss-parent
Source0:       https://github.com/znerd/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-release-plugin)
# required by enforcer-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildArch:     noarch
Source44: import.info

%description
Parent for znerd.org OSS Projects.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin org.apache.maven.plugins:maven-eclipse-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt README.txt
%doc --no-dereference COPYRIGHT.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 3-alt2_15jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3-alt2_14jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3-alt2_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3-alt2_11jpp8
- new version

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 3-alt1_5
- new version

