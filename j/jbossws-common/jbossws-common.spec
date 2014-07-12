Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbossws-common
%define version 2.1.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-common
Version:          2.1.0
Release:          alt1_1jpp7
Summary:          JBossWS Common
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws

# svn export http://anonsvn.jboss.org/repos/jbossws/common/tags/jbossws-common-2.1.0.Final/ jbossws-common-2.1.0.Final
# tar cafJ jbossws-common-2.1.0.Final.tar.xz jbossws-common-2.1.0.Final
Source0:          jbossws-common-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    jboss-common-core
BuildRequires:    jboss-ejb-3.1-api
BuildRequires:    jboss-jaxb-intros
BuildRequires:    jboss-jaxws-2.2-api
BuildRequires:    jboss-jaxrpc-1.1-api
BuildRequires:    jboss-jms-1.1-api
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    jbossws-api
BuildRequires:    jbossws-spi
BuildRequires:    jbossws-parent
BuildRequires:    jboss-logging
BuildRequires:    wsdl4j

Requires:         jpackage-utils
Requires:         jboss-common-core
Requires:         jboss-ejb-3.1-api
Requires:         jboss-jaxb-intros
Requires:         jboss-jaxws-2.2-api
Requires:         jboss-jaxrpc-1.1-api
Requires:         jboss-jms-1.1-api
Requires:         jboss-servlet-3.0-api
Requires:         jbossws-api
Requires:         jbossws-spi
Requires:         jboss-logging
Source44: import.info

%description
JBoss Web Services - Common

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jbossws-common-%{namedversion}

# Add jaxrpc dependency, since it's required
%pom_xpath_inject "pom:dependencies" "<dependency><groupId>org.jboss.spec.javax.xml.rpc</groupId><artifactId>jboss-jaxrpc-api_1.1_spec</artifactId><version>1.0.1.Final</version></dependency>"

%build
mvn-rpmbuild \
    -Dproject.build.sourceEncoding=UTF-8 \
    install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jbossws-common-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

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

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_1jpp7
- update

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_4jpp7
- new version

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_2jpp5
- full version

* Fri Mar 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt0.1jpp
- bootstrap for jbossas

