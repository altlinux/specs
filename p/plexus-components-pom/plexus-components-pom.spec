# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global short_name plexus-components

Name:           %{short_name}-pom
Version:        1.2
Release:        alt1_2jpp7
Summary:        Plexus Components POM
BuildArch:      noarch
Group:          Development/Java
License:        ASL 2.0
URL:            http://plexus.codehaus.org/%{short_name}
Source0:        http://repo.maven.apache.org/maven2/org/codehaus/plexus/%{short_name}/%{version}/%{short_name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  jpackage-utils
BuildRequires:  maven

Requires:       jpackage-utils
Source44: import.info

%description
This package provides Plexus Components parent POM used by different
Plexus packages.

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%check
mvn-rpmbuild verify

%install
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom

%files
%doc LICENSE
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_2jpp7
- update

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

