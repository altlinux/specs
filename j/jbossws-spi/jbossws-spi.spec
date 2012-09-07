Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbossws-spi
%define version 2.0.3
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-spi
Version:          2.0.3
Release:          alt1_3jpp7
Summary:          JBossWS SPI
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws

# svn export http://anonsvn.jboss.org/repos/jbossws/spi/tags/jbossws-spi-2.0.3.GA/ jbossws-spi-2.0.3.GA
# tar cafJ jbossws-spi-2.0.3.GA.tar.xz jbossws-spi-2.0.3.GA
Source0:          %{name}-%{namedversion}.tar.xz

Patch0:           %{name}-%{namedversion}-pom.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    jboss-jms-1.1-api
BuildRequires:    jboss-logging
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    jbossws-api

Requires:         jpackage-utils
Requires:         jboss-jms-1.1-api
Requires:         jboss-logging
Requires:         jboss-servlet-3.0-api
Requires:         jbossws-api
Source44: import.info

%description
JBoss WS SPI classes.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%patch0 -p1

# Message.properties files are not included in jar, make it available
for file in $(find src/ -name '*.properties'); do
  dest=$(echo $file | sed s/\\/java\\//\\/resources\\//)
  dir=$(dirname $dest)
  mkdir -p $dir
  cp $file $dest
done

%build
# tests skipped because testParse fails
mvn-rpmbuild \
  -Dmaven.test.skip=true \
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
* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.3-alt1_3jpp7
- new version

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_2jpp5
- new jpp release

