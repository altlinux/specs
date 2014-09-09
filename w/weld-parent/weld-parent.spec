BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             weld-parent
Version:          26
Release:          alt1_1jpp7
Summary:          Parent POM for Weld
Group:            Development/Java
License:          ASL 2.0
URL:              http://seamframework.org/Weld

Source0:          http://repo1.maven.org/maven2/org/jboss/weld/%{name}/%{version}/%{name}-%{version}.pom
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-shared
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-plugin-build-helper
BuildRequires:    maven-install-plugin
Source44: import.info

%description
Parent POM for Weld

%prep
cp %{SOURCE0} pom.xml
cp %{SOURCE1} LICENSE

%pom_remove_plugin ":maven-remote-resources-plugin"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 26-alt1_1jpp7
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 17-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 17-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 17-alt1_4jpp7
- new version

