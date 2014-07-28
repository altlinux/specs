Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           axis2
Version:        1.6.1
Release:        alt2_7jpp7
Summary:        Java-based Web Services / SOAP / WSDL engine

Group:          Development/Java
License:        ASL 2.0
URL:            http://axis.apache.org/axis2/java/core/
Source0:        http://mirror.metrocast.net/apache//axis/axis2/java/core/1.6.1/axis2-1.6.1-src.zip
# Disable modules whose dependencies are not in Fedora.
Patch0:         %{name}-disable-modules.patch
# 1) Remove JSR deps which are now built into openjdk
# 2) Fix javamail dep
# 3) Remove gmaven code
Patch1:         %{name}-dep-fixes.patch
# wrap generated headers with ifndef/define/endif
Patch2:         %{name}-AXIS2-5349.patch
BuildArch:      noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-shared
BuildRequires: maven-clean-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: geronimo-jta
BuildRequires: geronimo-saaj
BuildRequires: geronimo-parent-poms
BuildRequires: ws-commons-XmlSchema
BuildRequires: apache-commons-logging
BuildRequires: ws-commons-axiom
BuildRequires: neethi
BuildRequires: jsr-311
BuildRequires: ws-commons-woden
BuildRequires: javamail
BuildRequires: dos2unix
BuildRequires: maven-remote-resources-plugin
BuildRequires: apache-commons-fileupload
BuildRequires: tomcat-servlet-3.0-api
BuildRequires: geronimo-saaj
Requires:      jpackage-utils
Requires:      ws-commons-XmlSchema
Requires:      apache-commons-logging
Requires:      log4j
Requires:      xerces-j2
Requires:      ws-commons-axiom
Requires:      neethi
Requires:      jsr-311
Requires:      ws-commons-woden
Requires:      javamail
Requires:      apache-commons-fileupload
Requires:      tomcat-servlet-3.0-api
Requires:      geronimo-saaj
Source44: import.info


%description
Apache Axis2 is a Web Services / SOAP / WSDL engine, the successor
to the widely used Apache Axis SOAP stack. There are two
implementations of the Apache Axis2 Web services engine - Apache 
Axis2/Java and Apache Axis2/C.  This is Axis2/Java.

%package javadoc
Summary:      API documentation for %{name}
Group:        Development/Java
Requires:     jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
# Tests currently use an auto-generated ant build xml file which
# fails due to incorrect setting of JAVA_HOME (to JRE instead of JDK home)
# I have not yet determined the fix for this.
mvn-rpmbuild install \
    -Dmaven.test.skip \
    -Dproject.build.sourceEncoding=UTF-8 \
    javadoc:aggregate
dos2unix NOTICE.txt

%install
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}

# parent POM
cp modules/parent/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-parent.pom

for mod in resource-bundle adb adb-codegen codegen kernel saaj; do
  install -m 644 modules/${mod}/target/%{name}-${mod}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${mod}.jar
  cp modules/${mod}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-${mod}.pom
  %add_maven_depmap JPP.%{name}-%{name}-${mod}.pom %{name}/%{name}-${mod}.jar
done

install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/api/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE.txt NOTICE.txt README.txt release-notes.html
%{_javadir}/%{name}
%{_mavenpomdir}/JPP*.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_7jpp7
- new release

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_4jpp7
- new version

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_4jpp7
- new version

