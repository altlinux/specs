Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          xmlbeans-maven-plugin
Version:       2.3.3
Release:       alt1_8jpp8
Summary:       Maven XML Beans Plugin
License:       ASL 2.0
Url:           http://mojo.codehaus.org/xmlbeans-maven-plugin/
# svn export https://svn.codehaus.org/mojo/tags/xmlbeans-maven-plugin-2.3.3
# tar cJf xmlbeans-maven-plugin-2.3.3.tar.xz xmlbeans-maven-plugin-2.3.3
Source0:       %{name}-%{version}.tar.xz
# xmlbeans-maven-plugin package don't include the license file
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.xmlbeans:xmlbeans)
BuildRequires: mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(stax:stax-api)
BuildRequires: mvn(xml-resolver:xml-resolver)

BuildArch:     noarch
Source44: import.info

%description
Maven XML Beans Plugin provides integration of the
Apache XML Beans for Maven. Runs the xmlbeans
parser/code generator against schemes in files and
dependent jars.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

# these test fails
# [INFO] XMLBeans discrete xsd's in a jar test for MXMLBEANS-21  FAILURE [0.665s]
# Caused by: org.sonatype.aether.transfer.ArtifactNotFoundException: 
# Could not find artifact org.codehaus.mojo:xmlbeans-maven-plugin:pom:latest
# in local.central (file:///..../BUILD/xmlbeans-maven-plugin-2.3.3/.m2)
rm -r src/it/mxmlbeans-21/*

%pom_remove_dep org.apache.maven:maven-project
%pom_add_dep org.apache.maven:maven-core:any:compile

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :jdepend-maven-plugin
rm -r pom.xml.orig

%mvn_file : %{name}

%build

%mvn_build -- -Dmojo.java.target=1.5

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_7jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_6jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_5jpp8
- java 8 mass update

