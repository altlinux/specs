BuildRequires: /proc
BuildRequires: jpackage-compat
%global short_name plexus-tools

Name:           %{short_name}-pom
Version:        1.0.11
Release:        alt2_7jpp7
Summary:        Plexus Tools POM
BuildArch:      noarch
Group:          Development/Java
License:        ASL 2.0
URL:            http://plexus.codehaus.org/%{short_name}
Source0:        http://repo.maven.apache.org/maven2/org/codehaus/plexus/%{short_name}/%{version}/%{short_name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  plexus-pom
Source44: import.info

%description
This package provides Plexus Tools parent POM used by different
Plexus packages.

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%pom_disable_module plexus-cdc
%pom_disable_module plexus-cdc-anno
%pom_disable_module plexus-cli
%pom_disable_module plexus-javadoc

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt2_7jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt2_2jpp7
- rebuild with maven-local

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt1_2jpp7
- update

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

