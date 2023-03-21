Epoch: 1
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

%global jar_version 1.4
%global lh_version 1.1
%global id_version 1.1

Name:           apache-resource-bundles
Version:        36
Release:        alt1_2jpp11
Summary:        Apache Resource Bundles
License:        ASL 2.0
URL:            https://repo1.maven.org/maven2/org/apache/apache-resource-bundles/
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/apache/resources/%{name}/%{version}/%{name}-%{version}.pom
Source1:        https://repo1.maven.org/maven2/org/apache/apache-jar-resource-bundle/%{jar_version}/apache-jar-resource-bundle-%{jar_version}-sources.jar
Source2:        https://repo1.maven.org/maven2/org/apache/apache-jar-resource-bundle/%{jar_version}/apache-jar-resource-bundle-%{jar_version}.pom
Source3:        https://repo1.maven.org/maven2/org/apache/apache-license-header-resource-bundle/%{lh_version}/apache-license-header-resource-bundle-%{lh_version}-sources.jar
Source4:        https://repo1.maven.org/maven2/org/apache/apache-license-header-resource-bundle/%{lh_version}/apache-license-header-resource-bundle-%{lh_version}.pom
Source5:        https://repo1.maven.org/maven2/org/apache/apache-incubator-disclaimer-resource-bundle/%{id_version}/apache-incubator-disclaimer-resource-bundle-%{id_version}-sources.jar
Source6:        https://repo1.maven.org/maven2/org/apache/apache-incubator-disclaimer-resource-bundle/%{id_version}/apache-incubator-disclaimer-resource-bundle-%{id_version}.pom

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
%endif
Source44: import.info

%description
An archive which contains templates for generating the necessary license files
and notices for all Apache releases.

%prep
%setup -cT
cp -p %{SOURCE0} ./pom.xml
%pom_xpath_inject 'pom:project' '
<modules>
  <module>apache-jar-resource-bundle</module>
  <module>apache-license-header-resource-bundle</module>
  <module>apache-incubator-disclaimer-resource-bundle</module>
</modules>'

%pom_xpath_set 'pom:project/pom:parent/pom:relativePath' '../pom/maven/pom.xml'
%pom_xpath_set 'pom:project/pom:groupId' 'org.apache'

# jar
mkdir -p apache-jar-resource-bundle
pushd apache-jar-resource-bundle
jar xvf %{SOURCE1}
cp -p %{SOURCE2} ./pom.xml
%pom_xpath_set 'pom:project/pom:parent/pom:version' %{version}
mkdir -p src/main/resources
mv META-INF src/main/resources
popd

# license-header
mkdir -p apache-license-header-resource-bundle
pushd apache-license-header-resource-bundle
jar xvf %{SOURCE3}
cp -p %{SOURCE4} ./pom.xml
%pom_xpath_set 'pom:project/pom:parent/pom:version' %{version}
mkdir -p src/main/resources
mv META-INF src/main/resources
popd

# incubator-disclaimer
mkdir -p apache-incubator-disclaimer-resource-bundle
pushd apache-incubator-disclaimer-resource-bundle
jar xvf %{SOURCE5}
cp -p %{SOURCE6} ./pom.xml
%pom_xpath_set 'pom:project/pom:parent/pom:version' %{version}
mkdir -p src/main/resources
mv META-INF src/main/resources
popd

%mvn_file :apache-jar-resource-bundle apache-resource-bundles/jar
%mvn_file :apache-license-header-resource-bundle apache-resource-bundles/license-header
%mvn_file :apache-incubator-disclaimer-resource-bundle apache-resource-bundles/incubator-disclaimer

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1:36-alt1_2jpp11
- new version

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 1:30-alt1_3jpp11
- new version

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1:2-alt4_24jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1:2-alt4_22jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1:2-alt4_21jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1:2-alt4_20jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:2-alt4_19jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:2-alt4_18jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:2-alt4_17jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1:2-alt4_16jpp8
- new version

* Wed Jan 27 2016 Igor Vlasenko <viy@altlinux.ru> 1:2-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sun Sep 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:2-alt2_11jpp7
- fixed build

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:2-alt2_9jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1:2-alt2_8jpp7
- rebuild with maven-local

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 1:2-alt1_8jpp7
- update

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:3-alt3_2jpp6
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:3-alt2_2jpp6
- fixed build

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:3-alt1_2jpp6
- new jpp relase

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2-alt2_1jpp6
- apache-jar-resource-bundle is made compat package.

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:2-alt1_1jpp6
- new version
