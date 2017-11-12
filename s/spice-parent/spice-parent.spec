Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           spice-parent
Version:        26
Release:        alt1_7jpp8
Summary:        Sonatype Spice Components
License:        ASL 2.0
URL:            http://github.com/sonatype/oss-parents
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/sonatype/spice/%{name}/%{version}/%{name}-%{version}.pom
Source1:        http://apache.org/licenses/LICENSE-2.0.txt

Patch0:         pom.patch

BuildRequires:  maven-local
BuildRequires:  forge-parent
Source44: import.info

%description
Spice components and libraries are common components
used throughout the Sonatype Forge.

%prep
%setup -qcT
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} .

#Remove plexus-javadoc
%patch0

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 26-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 26-alt1_6jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 26-alt1_5jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 26-alt1_4jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 15-alt1_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 15-alt1_9jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 15-alt1_6jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 15-alt1_5jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 15-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

