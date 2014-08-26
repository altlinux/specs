# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          jaxb2-maven-plugin
Version:       1.5
Release:       alt1_1jpp7
Summary:       JAXB-2 Maven Plugin
Group:         Development/Java
License:       ASL 2.0
Url:           http://mojo.codehaus.org/jaxb2-maven-plugin/
# svn export https://svn.codehaus.org/mojo/tags/jaxb2-maven-plugin-1.5
# tar czf jaxb2-maven-plugin-1.5-src-svn.tar.gz jaxb2-maven-plugin-1.5
Source0:       http://repo2.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip
# jaxb2-maven-plugin package don't include the license file
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: mojo-parent

BuildRequires: glassfish-jaxb
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
#BuildRequires: mvn(org.apache.maven:maven-project)
#BuildRequires: mvn(org.codehaus.plexus:plexus-build-api)
BuildRequires: mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.sonatype.plexus:plexus-build-api)

# test deps
BuildRequires: aopalliance
BuildRequires: cglib
BuildRequires: junit
BuildRequires: maven-plugin-testing-harness
BuildRequires: xmlunit

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      glassfish-jaxb
Requires:      mvn(org.apache.maven:maven-artifact)
Requires:      mvn(org.apache.maven:maven-compat)
Requires:      mvn(org.apache.maven:maven-core)
Requires:      mvn(org.apache.maven:maven-model)
Requires:      mvn(org.apache.maven:maven-plugin-api)
#Requires:      mvn(org.apache.maven:maven-project)
#Requires:      mvn(org.codehaus.plexus:plexus-build-api)
Requires:      mvn(org.codehaus.plexus:plexus-compiler-api)
Requires:      mvn(org.codehaus.plexus:plexus-utils)
Requires:      mvn(org.sonatype.plexus:plexus-build-api)

BuildArch:     noarch
Source44: import.info

%description
Mojo's JAXB-2 Maven plugin is used to create an object graph from
XSDs based on the JAXB 2.1 implementation and to generate XSDs from
JAXB-annotated Java classes.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt
# updated plexus-build-api refs
#%%pom_xpath_remove "pom:dependencies/pom:dependency[pom:artifactId ='plexus-build-api']/pom:groupId"
#%%pom_xpath_inject "pom:dependencies/pom:dependency[pom:artifactId ='plexus-build-api']" "<groupId>org.sonatype.plexus</groupId>"
# used only mvn3 apis
%pom_remove_dep org.apache.maven:maven-project
%pom_add_dep org.apache.maven:maven-compat
%pom_add_dep org.apache.maven:maven-core
# missing build deps
%pom_add_dep com.sun.xml.bind:jaxb-impl

# missing test deps
%pom_add_dep aopalliance:aopalliance::test
%pom_add_dep net.sf.cglib:cglib::test

%build

mvn-rpmbuild package javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE-2.0.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE-2.0.txt

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1jpp7
- new release

