BuildRequires: geronimo-saaj
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             apache-scout
Version:          1.2.6
Release:          alt2_3jpp7
Summary:          JSR 93 (JAXR) implementation
Group:            Development/Java
License:          ASL 2.0
URL:              http://juddi.apache.org/scout

# svn export http://svn.apache.org/repos/asf/juddi/scout/tags/scout-1.2.6/ apache-scout
# tar cafJ apache-scout-1.2.6.tar.xz apache-scout
Source0:          %{name}-%{version}.tar.xz

Patch0:           0001-Change-guid-aid-of-deps.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    axis
BuildRequires:    apache-juddi
BuildRequires:    geronimo-jaxrpc
BuildRequires:    jboss-jaxr-1.0-api
BuildRequires:    jboss-jaxb-2.2-api
BuildRequires:    axis
BuildRequires:    aspectjweaver
BuildRequires:    wsdl4j

Requires:         axis
Requires:         apache-juddi
Requires:         jpackage-utils
Requires:         geronimo-jaxrpc
Requires:         jboss-jaxr-1.0-api
Requires:         jboss-jaxb-2.2-api
Requires:         aspectjweaver
Requires:         wsdl4j
Source44: import.info

%description
Apache Scout is an implementation of the JSR 93 Java API For XML Registries
(JAXR). It provides an implementation to access UDDI registries (particularly
Apache jUDDI) in a standard way.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

%patch0 -p1

%build
# Skipped because of many test resources not packaged
mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 -Dmaven.test.skip=true package javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/scout-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc LICENSE README NOTICE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt1_3jpp7
- new version

