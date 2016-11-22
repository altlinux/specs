Group: Development/C
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          znerd-oss-parent
Version:       3
Release:       alt2_12jpp8
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
%doc COPYRIGHT.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3-alt2_11jpp8
- new version

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 3-alt1_5
- new version

