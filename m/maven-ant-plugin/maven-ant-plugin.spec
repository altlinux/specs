Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-ant-plugin
Version:        2.3
Release:        alt2_18jpp8
Summary:        Maven Ant Plugin
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-ant-plugin
BuildArch:      noarch

#svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-ant-plugin-2.3/
#tar jcf maven-ant-plugin-2.3.tar.bz2 maven-ant-plugin-2.3/
Source0:        %{name}-%{version}.tar.bz2
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         %{name}-pom.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-nodeps)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-plugin-testing-harness)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xml-apis:xml-apis)
Source44: import.info

%description
Generates an Ant build file from a POM.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q 
%patch0 -p0
cp -p %{SOURCE1} .

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt2_18jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt2_17jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.3-alt2_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.3-alt2_12jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.3-alt2_9jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_9jpp7
- new fc release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_8jpp7
- complete build

* Sat Mar 10 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

