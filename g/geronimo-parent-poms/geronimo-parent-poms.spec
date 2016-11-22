Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           geronimo-parent-poms
Version:        1.6
Release:        alt3_21jpp8
Summary:        Parent POM files for geronimo-specs
License:        ASL 2.0
URL:            http://geronimo.apache.org/
BuildArch:      noarch

# Following the parent chain all the way up ...
Source0:        http://svn.apache.org/repos/asf/geronimo/specs/tags/specs-parent-%{version}/pom.xml
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local

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
# IDEA plugin is not really useful in Fedora
%pom_remove_plugin :maven-idea-plugin

%build
%mvn_alias : org.apache.geronimo.specs:specs
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt3_21jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt3_20jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_16jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_14jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_10jpp7
- new fc release

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_7jpp7
- full version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

