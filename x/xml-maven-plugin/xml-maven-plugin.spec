BuildRequires: maven-plugin-plugin
BuildRequires: maven-antrun-plugin maven-clean-plugin
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          xml-maven-plugin
Version:       1.0
Release:       alt4_4jpp7
Summary:       Maven XML Plugin
Group:         Development/Java
License:       ASL 2.0
Url:           http://mojo.codehaus.org/xml-maven-plugin/
Source0:       http://repo2.maven.org/maven2/org/codehaus/mojo/xml-maven-plugin/1.0/xml-maven-plugin-1.0-source-release.zip
Patch0:        remove-failing-it.patch	       
BuildRequires: jpackage-utils
BuildRequires: mojo-parent

BuildRequires: apache-rat-plugin
BuildRequires: maven
BuildRequires: maven-changes-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-surefire-plugin
BuildRequires: maven-plugin-cobertura

BuildRequires: plexus-component-api
BuildRequires: plexus-io
BuildRequires: plexus-resources
BuildRequires: plexus-utils
BuildRequires: saxon
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis
BuildRequires: xml-commons-resolver

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
A plugin for various XML related tasks like validation and transformation.

%package javadoc
Summary:       Javadocs for %{name}
Group:         Development/Java
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p0 
for d in LICENSE NOTICE ; do
  iconv -f iso8859-1 -t utf-8 $d.txt > $d.txt.conv && mv -f $d.txt.conv $d.txt
  sed -i 's/\r//' $d.txt
done
rm -rf src/it/it8
rm -rf src/it/mojo-1438-validate

%build
mvn-rpmbuild -e -X -DskipTests -Dmaven.test.skip=true -DskipITs install javadoc:aggregate

%install
mkdir -p %{buildroot}%{_javadir}
install -pm 644 target/xml-maven-plugin-%{version}.jar \
  %{buildroot}%{_javadir}/xml-maven-plugin.jar
  
mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-xml-maven-plugin.pom
%add_maven_depmap JPP-xml-maven-plugin.pom xml-maven-plugin.jar

mkdir -p %{buildroot}%{_javadocdir}/xml-maven-plugin
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/xml-maven-plugin



%files
%{_javadir}/xml-maven-plugin.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE.txt NOTICE.txt

%files javadoc
%{_javadocdir}/xml-maven-plugin
%doc LICENSE.txt NOTICE.txt

%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_4jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_4jpp7
- fixed build

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_4jpp7
- new version

