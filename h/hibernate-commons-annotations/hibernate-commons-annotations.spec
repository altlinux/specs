BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hibernate-commons-annotations
%define version 4.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             hibernate-commons-annotations
Version:          4.0.1
Release:          alt2_2jpp7
Summary:          Hibernate Annotations

Group:            Development/Java

# For details see:
# - https://github.com/hibernate/hibernate-commons-annotations/commit/4a902b4f97f923f9044a4127357b44fe5dc39cdc
# - https://github.com/hibernate/hibernate-commons-annotations/commit/a11c44cd65dadcedaf8981379b94a2c4e31428d1
License:          LGPLv2
URL:              http://www.hibernate.org/

# git clone git://github.com/hibernate/hibernate-commons-annotations.git
# cd hibernate-commons-annotations && git archive --format=tar --prefix=hibernate-commons-annotations-4.0.1.Final/ 4.0.1.Final | xz > hibernate-commons-annotations-4.0.1.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz
# corrects the position of the class LoggingToolsProcessor for the new jboss-logging-tools
Patch0:           hibernate-commons-annotations-4.0.1.Final-pom.patch
BuildArch:        noarch

Requires:         jboss-logging
Requires:         slf4j
Requires:         jpackage-utils

BuildRequires:    jboss-logging

BuildRequires:    jboss-logging-tools
BuildRequires:    junit
BuildRequires:    slf4j
BuildRequires:    apache-commons-logging
BuildRequires:    jpackage-utils
BuildRequires:    maven

BuildRequires:    maven-processor-plugin

BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-injection-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-source-plugin
BuildRequires:    maven-surefire-plugin
Source44: import.info

%description
Following the DRY (Don't Repeat Yourself) principle, 
Hibernate Validator let's you express your domain 
constraints once (and only once) and ensure their 
compliance at various level of your system 
automatically.

Common reflection code used in support of annotation processing.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p0

%build
mvn-rpmbuild install javadoc:aggregate

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}/hibernate
cp -p target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/hibernate/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp  target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.hibernate-%{name}.pom
%add_maven_depmap JPP.hibernate-%{name}.pom hibernate/%{name}.jar -a "org.hibernate:%{name}"

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc changelog.txt lgpl.txt readme.txt

%files javadoc
%{_javadocdir}/%{name}
%doc lgpl.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt1_2jpp7
- new version

