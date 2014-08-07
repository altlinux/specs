BuildRequires: /proc
BuildRequires: jpackage-compat
%global tag a594629

Name:           sonatype-plugins-parent
Version:        8
Release:        alt2_1jpp7
Summary:        Sonatype Plugins Parent POM
BuildArch:      noarch
Group:          Development/Java
License:        ASL 2.0
URL:            https://github.com/sonatype/oss-parents
Source:         https://github.com/sonatype/oss-parents/tarball/plugins-parent-%{version}#/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  jpackage-utils
BuildRequires:  sonatype-forge-parent

Requires:       maven
Requires:       jpackage-utils
Requires:       sonatype-forge-parent
Source44: import.info

%description
This package provides Sonatype plugins parent POM used by other Sonatype
packages.

%prep
%setup -q -n sonatype-oss-parents-%{tag}

%install
cd ./plugins-parent
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom

%check
cd ./plugins-parent
mvn-rpmbuild verify

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 8-alt2_1jpp7
- rebuild with maven-local

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 8-alt1_1jpp7
- new version

