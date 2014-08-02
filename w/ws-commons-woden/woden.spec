# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
%define oldname woden
BuildRequires: /proc
BuildRequires: jpackage-compat
%global oversion 1.0M9

Name:           ws-commons-woden
Version:        1.0
Release:        alt2_0.5.M9jpp7
Summary:        Web Service Description Language (WSDL) validating parser

Group:          Development/Java
License:        ASL 2.0
URL:            http://ws.apache.org/woden/
# svn export https://svn.apache.org/repos/asf/webservices/woden/tags/1.0M9/ woden-1.0M9
# tar caf woden-1.0M9.tar.xz woden-1.0M9
Source0:        %{oldname}-%{oversion}.tar.xz
# Disable modules whose dependencies are not present in Fedora.  
Patch0:         %{oldname}-disable-modules.patch
BuildArch:      noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-shared
BuildRequires: ws-commons-XmlSchema
BuildRequires: apache-commons-logging
BuildRequires: log4j
BuildRequires: xerces-j2
BuildRequires: ws-commons-axiom
Requires:      jpackage-utils
Requires:      wsdl4j
Requires:      ws-commons-XmlSchema
Requires:      apache-commons-logging
Requires:      log4j
Requires:      xerces-j2
Requires:      ws-commons-axiom
Source44: import.info

%description
The Woden project is a sub-project of the Apache Web Services Project
to develop a Java class library for reading, manipulating, creating
and writing WSDL documents, initially to support WSDL 2.0 but with the
longer term aim of supporting past, present and future versions of WSDL.

%package javadoc
Summary:      API documentation for %{oldname}
Group:        Development/Java
Requires:     jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{oldname}.

%prep
%setup -q -n %{oldname}-%{oversion}
%patch0 -p1

%build
mvn-rpmbuild install javadoc:aggregate

# Fix encoding
iconv -f iso8859-1 -t utf-8 LICENSE > LICENSE.utf8
mv LICENSE.utf8 LICENSE

%install
install -d -m 755 %{buildroot}%{_javadir}/%{oldname}
install -d -m 755 %{buildroot}%{_mavenpomdir}

# parent POM
cp pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{oldname}-parent.pom
%add_maven_depmap JPP.%{oldname}-parent.pom

# api
install -m 644 %{oldname}-api/target/%{oldname}-api-%{oversion}.jar %{buildroot}%{_javadir}/%{oldname}/%{oldname}-api.jar
cp %{oldname}-api/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{oldname}-%{oldname}-api.pom
%add_maven_depmap JPP.%{oldname}-%{oldname}-api.pom %{oldname}/%{oldname}-api.jar

# impl-commons
for mod in commons dom om; do
  install -m 644 %{oldname}-${mod}/target/%{oldname}-impl-${mod}-%{oversion}.jar %{buildroot}%{_javadir}/%{oldname}/%{oldname}-impl-${mod}.jar
  cp %{oldname}-${mod}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{oldname}-%{oldname}-impl-${mod}.pom
  %add_maven_depmap JPP.%{oldname}-%{oldname}-impl-${mod}.pom %{oldname}/%{oldname}-impl-${mod}.jar
done

install -d -m 755 %{buildroot}%{_javadocdir}/%{oldname}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{oldname}

%files
%doc LICENSE NOTICE
%{_javadir}/%{oldname}
%{_mavenpomdir}/JPP*.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE
%{_javadocdir}/%{oldname}


%changelog
* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.5.M9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.2.M9jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.2.M9jpp7
- new version

