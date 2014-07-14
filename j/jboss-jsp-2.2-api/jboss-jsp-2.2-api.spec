BuildRequires: maven-enforcer-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jsp-2.2-api
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jsp-2.2-api
Version:          1.0.1
Release:          alt3_3jpp7
Summary:          JavaServer(TM) Pages 2.2 API
Group:            Development/Java
License:          CDDL or GPLv2 with exceptions
URL:              http://www.jboss.org/

# git clone git://github.com/jboss/jboss-jsp-api_spec.git jboss-jsp-2.2-api
# cd jboss-jsp-2.2-api/ && git archive --format=tar --prefix=jboss-jsp-2.2-api-1.0.1.Final/ jboss-jsp-api_2.2_spec-1.0.1.Final | xz > jboss-jsp-2.2-api-1.0.1.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

BuildRequires:    jboss-parent
BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    jboss-el-2.2-api
BuildRequires:    jboss-servlet-3.0-api

Requires:         jpackage-utils
Requires:         jboss-el-2.2-api
Requires:         jboss-servlet-3.0-api

BuildArch:        noarch
Source44: import.info

%description
JSR-000245: JavaServer(TM) Pages 2.2

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc	
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-jsp-api_2.2_spec-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "javax.servlet.jsp:jsp-api"

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE README

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE README

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_3jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_3jpp7
- fixed build

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp7
- new version

