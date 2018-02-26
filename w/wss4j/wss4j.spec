BuildRequires: apache-jar-resource-bundle
Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           wss4j 
Version:        1.5.12
Release:        alt1_2jpp7
Summary:        Apache WS-Security implementation

Group:          Development/Java
License:        ASL 2.0
URL:            http://ws.apache.org/wss4j/
Source0:        http://www.apache.org/dyn/closer.cgi/ws/wss4j/1_5_12/wss4j-src-1.5.12.zip
# This plugin does not impact the build, and it currently raises this error:
# Reporting mojo's can only be called from ReportDocumentRender
Patch0:         %{name}-no-pmd.patch
# OpenSAML has several other dependencies which are not packaged, 
# so omit it for now
Patch1:         %{name}-no-opensaml.patch
# Remove opensaml dep, and work around broken axis deps for now.
Patch2:         %{name}-deps.patch
BuildArch:      noarch

BuildRequires:  axis
BuildRequires:  xml-security
BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  apache-resource-bundles
BuildRequires:  dos2unix

Requires:       jpackage-utils
Requires:       axis
Requires:       xml-security
Source44: import.info

%description
The Apache WSS4J project provides a Java implementation of the
primary security standards for Web Services. 

%package javadoc
Summary: Javadoc for %{name}
Group:   Development/Java
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n wss4j
%patch0 -p1 -b .sav0
%patch1 -p1 -b .sav1
%patch2 -p1 -b .sav2
# Remove bundled JARs
find . -type f -name '*.jar' -exec rm -f {} \;
# Remove classes requiring OpenSAML
find . -name *SAMLToken*.java -exec rm -f {} \;
rm -rf src/org/apache/ws/security/saml/

%build
# Tests need dependency fixes and opensaml tests will take
# some work to patch out.  Disable for now.
mvn-rpmbuild install -Dmaven.test.skip=true javadoc:javadoc
dos2unix NOTICE

%install
# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -m 0644 target/%{name}-%{version}.jar \
$RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 0644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc ChangeLog.txt NOTICE LICENSE.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt
%doc %{_javadocdir}/%{name}

%changelog
* Sat Apr 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.12-alt1_2jpp7
- fc version

* Mon Feb 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.10-alt1_1jpp6
- new jpp relase

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.8-alt1_7jpp6
- jpp 6 release

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt3_1jpp5
- fixes for java6 support

* Tue Jun 02 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt2_1jpp5
- fixed build

* Tue Oct 21 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt1_1jpp5
- jpackage 5.0

* Sat Jan 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt1_3jpp1.7
- converted from JPackage by jppimport script

