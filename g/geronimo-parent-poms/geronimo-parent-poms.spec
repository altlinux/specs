BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		geronimo-parent-poms
Version:	1.6
Release:	alt1_14jpp7
Summary:	Parent POM files for geronimo-specs
Group:		Development/Java
License:	ASL 2.0
URL:		http://geronimo.apache.org/
BuildArch:	noarch

# Following the parent chain all the way up ...
Source0:	http://svn.apache.org/repos/asf/geronimo/specs/tags/specs-parent-%{version}/pom.xml
Source1:	http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:	jpackage-utils

# Dependencies and plugins from the POM files
Provides:       geronimo-specs = %{version}-%{release}
Source44: import.info
Conflicts: geronimo-specs < 0:1.2-alt9_16jpp6

%description
The Project Object Model files for the geronimo-specs modules.

%prep
%setup -c -T
cp -p %{SOURCE0} .
cp -p %{SOURCE1} LICENSE
%pom_remove_parent

%build
%mvn_alias : org.apache.geronimo.specs:specs
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE


%changelog
* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_14jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_10jpp7
- new fc release

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_7jpp7
- full version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

