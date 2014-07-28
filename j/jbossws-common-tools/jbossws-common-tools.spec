# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbossws-common-tools
%define version 1.1.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-common-tools
Version:          1.1.0
Release:          alt1_7jpp7
Summary:          JBossWS Common Tools
Group:            Development/Java
License:          LGPLv2+ and ASL 2.0
URL:              http://www.jboss.org/jbossws

# svn export http://anonsvn.jboss.org/repos/jbossws/common-tools/tags/jbossws-common-tools-1.1.0.Final/ jbossws-common-tools-1.1.0.Final
# tar cafJ jbossws-common-tools-1.1.0.Final.tar.xz jbossws-common-tools-1.1.0.Final
Source0:          jbossws-common-tools-%{namedversion}.tar.xz
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    ant
BuildRequires:    maven-local
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    gnu-getopt
BuildRequires:    jbossws-spi >= 2.1.0
BuildRequires:    jbossws-api >= 1.0.1
BuildRequires:    jbossws-parent
BuildRequires:    log4j
BuildRequires:    junit

%if 0%{?fedora} > 17
BuildRequires:  plexus-pom
BuildRequires:  plexus-components-pom
%endif

Requires:         jpackage-utils
Requires:         ant
Requires:         gnu-getopt
Requires:         jbossws-spi >= 2.1.0
Requires:         jbossws-api >= 1.0.1
Requires:         log4j
Source44: import.info

%description
JBoss Web Services - Common Tools

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jbossws-common-tools-%{namedversion}

cp %{SOURCE1} .

%build
mvn-rpmbuild \
    -Dproject.build.sourceEncoding=UTF-8 \
    install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc LICENSE-2.0.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE-2.0.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_7jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_5jpp7
- update

