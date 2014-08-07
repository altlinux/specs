BuildRequires: /proc
BuildRequires: jpackage-compat
%global tag c983737

Name:           sonatype-forge-parent
Version:        12
Release:        alt2_1jpp7
Summary:        Sonatype Forge Parent POM
BuildArch:      noarch
Group:          Development/Java
License:        ASL 2.0
URL:            https://github.com/sonatype/oss-parents
Source:         https://github.com/sonatype/oss-parents/tarball/forge-parent-%{version}#/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  jpackage-utils

Requires:       maven
Requires:       jpackage-utils
Source44: import.info

%description
This package provides Sonatype forge parent POM used by other Sonatype
packages.

%prep
%setup -q -n sonatype-oss-parents-%{tag}

%check
cd ./forge-parent
mvn-rpmbuild install

%install
cd ./forge-parent
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 12-alt2_1jpp7
- rebuild with maven-local

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 12-alt1_1jpp7
- new version

