# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             apache-juddi
Version:          3.1.4
Release:          alt1_1jpp7
Summary:          Client API for UDDI
Group:            Development/Java
License:          ASL 2.0
URL:              http://juddi.apache.org/

# svn export http://svn.apache.org/repos/asf/juddi/tags/juddi-3.1.4/ apache-juddi
# tar cafJ apache-juddi-3.1.4.tar.xz apache-juddi
Source0:          %{name}-%{version}.tar.xz

Patch1:           0001-Build-only-client-module.patch
Patch2:           0002-Change-jaxws-api-dependency.patch
Patch3:           0003-Disable-ReadWSDLTest.readFromJar.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    jboss-jaxws-2.2-api
BuildRequires:    wsdl4j

Requires:         jpackage-utils
Requires:         jboss-jaxws-2.2-api
Requires:         wsdl4j
Source44: import.info

%description
jUDDI is an open source Java implementation of the Universal Description,
Discovery, and Integration (UDDI v3) specification for Web Services.

This package includes only the client side of jUDDI.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.

%prep
%setup -q -n %{name}

%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
mvn-rpmbuild package javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

for m in uddi-ws juddi-client; do
  # JAR
  install -pm 644 ${m}/target/${m}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/${m}.jar

  # POM
  install -pm 644 ${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-${m}.pom

  # DEPMAP
  %add_maven_depmap JPP.%{name}-${m}.pom %{name}/${m}.jar
done

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-parent.pom

#DEPMAP
%add_maven_depmap JPP.%{name}-parent.pom

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc RELEASE_NOTES.html LICENSE NOTICE
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt1_1jpp7
- fc update

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 3.1.3-alt1_4jpp7
- new release

