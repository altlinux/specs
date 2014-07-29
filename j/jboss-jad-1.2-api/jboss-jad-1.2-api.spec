Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jad-1.2-api
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-jad-1.2-api
Version:       1.0.1
Release:       alt2_5jpp7
Summary:       JavaEE Application Deployment 1.2 API
Group:         Development/Java
License:       CDDL or GPLv2 with exceptions
URL:           http://www.jboss.org

# git clone git://github.com/jboss/jboss-jad-api_spec.git
# cd jboss-jad-api_spec/ && git archive --format=tar --prefix=jboss-jad-1.2-api/ jboss-jad-api_1.2_spec-1.0.1.Final | xz > jboss-jad-1.2-api-1.0.1.Final.tar.xz
Source0:       jboss-jad-1.2-api-%{namedversion}.tar.xz

BuildRequires: jpackage-utils
BuildRequires: jboss-common-core
BuildRequires: jboss-logging
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-checkstyle-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-dependency-plugin
BuildRequires: maven-ear-plugin
BuildRequires: maven-eclipse-plugin
BuildRequires: maven-ejb-plugin

Requires:      jboss-common-core
Requires:      jboss-logging
Requires:      jpackage-utils

BuildArch:     noarch
Source44: import.info

%description
The JavaEE Application Deployment 1.2 API classes.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jad-1.2-api

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-jad-api_1.2_spec-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc README LICENSE

%files javadoc
%{_javadocdir}/%{name}
%doc README LICENSE

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_3jpp7
- new version

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt4_2jpp6
- fixed build

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt3_2jpp6
- build w/o jms-1.1-api

* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt2_2jpp6
- built with patched assembly plugin

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt1_2jpp6
- new version

