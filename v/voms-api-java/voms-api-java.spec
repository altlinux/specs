# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
# Use maven if it is available - otherwise fall back to ant
%if %{?fedora}%{!?fedora:0} >= 15 || %{?rhel}%{!?rhel:0} >= 7
%global maven 1
%else
%global maven 0
%endif

Name:		voms-api-java
Version:	2.0.10
%global tagver %(tr . _ <<< %{version})
Release:	alt1_4jpp7
Summary:	Virtual Organization Membership Service Java API

Group:		Development/Java
License:	ASL 2.0
URL:		https://wiki.italiangrid.it/VOMS
Source0:	https://github.com/italiangrid/%{name}/archive/%{tagver}.tar.gz
#		These are build instructions for ant generated from the maven
#		build instrutions using the maven ant plugin.
#		These are used for building on EPEL since there is no maven
#		available there.
Source1:	build.xml
Source2:	maven-build.xml
Source3:	maven-build.properties
Patch0:		%{name}-test.patch
BuildArch:	noarch

# There is no bouncycastle in EPEL 5 ppc and EPEL 6 ppc64
%if %{?rhel}%{!?rhel:0} == 5
ExcludeArch:	ppc
%endif
%if %{?rhel}%{!?rhel:0} == 6
ExcludeArch:	ppc64
%endif

Requires:	jpackage-utils
Requires:	bouncycastle >= 1.39
%if %{?fedora}%{!?fedora:0} >= 15 || %{?rhel}%{!?rhel:0} >= 7
Requires:	apache-commons-cli
Requires:	apache-commons-lang
%else
Requires:	jakarta-commons-cli
Requires:	jakarta-commons-lang
%endif
Requires:	log4j

Provides:	vomsjapi = %{version}-%{release}
Obsoletes:	vomsjapi < 2.0.7

BuildRequires:	jpackage-utils

%if %maven
BuildRequires:	maven-local
BuildRequires:	maven-compiler-plugin
BuildRequires:	maven-install-plugin
BuildRequires:	maven-jar-plugin
BuildRequires:	maven-javadoc-plugin
BuildRequires:	maven-release-plugin
BuildRequires:	maven-resources-plugin
BuildRequires:	maven-surefire-plugin
BuildRequires:	maven-surefire-provider-junit
%else
BuildRequires:	ant
BuildRequires:	ant-junit
%endif

BuildRequires:	bouncycastle >= 1.39
%if %{?fedora}%{!?fedora:0} >= 15 || %{?rhel}%{!?rhel:0} >= 7
BuildRequires:	apache-commons-cli
BuildRequires:	apache-commons-io
BuildRequires:	apache-commons-lang
%else
BuildRequires:	jakarta-commons-cli
BuildRequires:	jakarta-commons-io
BuildRequires:	jakarta-commons-lang
%endif
BuildRequires:	log4j
Source44: import.info

%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides a java client API for VOMS.

%package javadoc
Summary:	Virtual Organization Membership Service Java API Documentation
Group:		Development/Java
Requires:	jpackage-utils
Requires:	%{name} = %{version}-%{release}
Provides:	vomsjapi-javadoc = %{version}-%{release}
Obsoletes:	vomsjapi-javadoc < 2.0.7
BuildArch: noarch

%description javadoc
Virtual Organization Membership Service (VOMS) Java API Documentation.

%prep
%setup -q -n %{name}-%{tagver}
%patch0 -p1
install -m 644 %SOURCE1 .
install -m 644 %SOURCE2 .
install -m 644 %SOURCE3 .

sed -e s/bcprov-ext-jdk16/bcprov-jdk16/ -i pom.xml

%build
%if %{maven}
mvn-rpmbuild -Dbouncycastle.version=1.46 install javadoc:aggregate
%else
export CLASSPATH=$(build-classpath bcprov log4j commons-cli commons-io commons-lang)
ant -Dbuild.sysclasspath=last package javadoc
%endif

%install
mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/vomsjapi.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
%if %{maven}
cp -pr target/site/javadoc/apidocs %{buildroot}%{_javadocdir}/%{name}
%else
cp -pr target/site/apidocs %{buildroot}%{_javadocdir}/%{name}
%endif

%if %{maven}
mkdir -p %{buildroot}%{_mavenpomdir}
install -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a org.glite:vomsjapi
%endif

%files
%{_javadir}/%{name}.jar
%{_javadir}/vomsjapi.jar
%if %{maven}
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%endif
%doc AUTHORS LICENSE README.md

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_4jpp7
- new release

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_2jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.8-alt1_2jpp7
- new version

