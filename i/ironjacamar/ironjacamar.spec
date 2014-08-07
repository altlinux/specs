BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name ironjacamar
%define version 1.0.9
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             ironjacamar
Version:          1.0.9
Release:          alt3_4jpp7
Summary:          Java Connector Architecture 1.6 implementation
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/ironjacamar

# svn export http://anonsvn.jboss.org/repos/jbossas/projects/jboss-jca/tags/IRONJACAMAR_1_0_9_FINAL ironjacamar-1.0.9.Final
# find ironjacamar-1.0.9.Final -name '*.jar' -type f -delete
# rm -f ironjacamar-1.0.9.Final/common/src/main/resources/dtd/connector_1_0.dtd
# tar cafJ ironjacamar-1.0.9.Final-CLEAN.tar.xz ironjacamar-1.0.9.Final
# List of removed files: https://gist.github.com/2222757/77dda615e1b652afd16b470505e247d7faf1fc56
Source0:          %{name}-%{namedversion}-CLEAN.tar.xz

# Remote POM's...
# You can use below script:
#
# modules="deployers-common common-impl-papaki validator-cli common-impl validator core-impl jdbc common-spi validator-maven core-api validator-ant common-api spec-api"
# version="1.0.9"
#
# for m in $modules; do
#   curl https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ironjacamar/ironjacamar-${m}/${version}.Final/ironjacamar-${m}-${version}.Final.pom -o ironjacamar-${m}-${version}.Final.pom
# done
#
Source1:          https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ironjacamar/ironjacamar-deployers-common/1.0.9.Final/ironjacamar-deployers-common-%{version}.Final.pom
Source2:          https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ironjacamar/ironjacamar-deployers-common/1.0.9.Final/ironjacamar-common-impl-papaki-%{version}.Final.pom
Source3:          https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ironjacamar/ironjacamar-deployers-common/1.0.9.Final/ironjacamar-validator-cli-%{version}.Final.pom
Source4:          https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ironjacamar/ironjacamar-deployers-common/1.0.9.Final/ironjacamar-common-impl-%{version}.Final.pom
Source5:          https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ironjacamar/ironjacamar-deployers-common/1.0.9.Final/ironjacamar-validator-%{version}.Final.pom
Source6:          https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ironjacamar/ironjacamar-deployers-common/1.0.9.Final/ironjacamar-core-impl-%{version}.Final.pom
Source7:          https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ironjacamar/ironjacamar-deployers-common/1.0.9.Final/ironjacamar-jdbc-%{version}.Final.pom
Source8:          https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ironjacamar/ironjacamar-deployers-common/1.0.9.Final/ironjacamar-common-spi-%{version}.Final.pom
Source9:          https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ironjacamar/ironjacamar-deployers-common/1.0.9.Final/ironjacamar-validator-maven-%{version}.Final.pom
Source10:         https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ironjacamar/ironjacamar-deployers-common/1.0.9.Final/ironjacamar-core-api-%{version}.Final.pom
Source11:         https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ironjacamar/ironjacamar-deployers-common/1.0.9.Final/ironjacamar-validator-ant-%{version}.Final.pom
Source12:         https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ironjacamar/ironjacamar-deployers-common/1.0.9.Final/ironjacamar-common-api-%{version}.Final.pom
Source13:         https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ironjacamar/ironjacamar-deployers-common/1.0.9.Final/ironjacamar-spec-api-%{version}.Final.pom

# Commented out retrieving jars from Internet and limiting the jars to build
Patch0:           %{name}-%{namedversion}-ivy.patch

# Commented out trying to download Ivy from the Internet
Patch1:           %{name}-%{namedversion}-build.patch

# Commented out Class-Path directive in the Manifest of ironjacamar-validator.jar
Patch2:           %{name}-%{namedversion}-validator.patch

BuildArch:        noarch

BuildRequires:    ant
BuildRequires:    apache-ivy
BuildRequires:    apiviz
BuildRequires:    geronimo-validation
BuildRequires:    javamail
BuildRequires:    javassist
BuildRequires:    jboss-connector-1.6-api
BuildRequires:    jboss-jaspi-1.0-api >= 1.0.0-3
BuildRequires:    jboss-logging
BuildRequires:    jboss-threads >= 2.0.0-4
BuildRequires:    jboss-transaction-1.1-api
BuildRequires:    jboss-transaction-spi
BuildRequires:    jdepend
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    picketbox

Requires:         geronimo-validation
Requires:         javamail
Requires:         javassist
Requires:         jboss-connector-1.6-api
Requires:         jboss-jaspi-1.0-api
Requires:         jboss-logging
Requires:         jboss-threads
Requires:         jboss-transaction-1.1-api
Requires:         jboss-transaction-spi
Requires:         jpackage-utils
Requires:         picketbox
Source44: import.info

%description
The IronJacamar project implements the Java Connector Architecture 1.6
specification.

The Java Connector Architecture (JCA) defines a standard architecture for
connecting the Java EE platform to heterogeneous Enterprise Information
Systems (EIS). Examples of EISs include Enterprise Resource Planning (ERP),
mainframe transaction processing (TP), database and messaging systems.

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
%patch1 -p1
%patch2 -p1

# Yes, a bit ugly because we copy also the source code
cp %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{S:6} %{S:7} %{S:8} %{S:9} %{S:10} %{S:11} %{S:12} %{S:13} .
# Let's remove it
#rm -rf %{name}-%{namedversion}-CLEAN.tar.xz

# Fixing JDK7 ASCII issues
files='
api/src/main/java/javax/resource/spi/BootstrapContext.java
api/src/main/java/javax/resource/spi/work/SecurityContext.java
'

for f in ${files}; do
  native2ascii -encoding UTF8 ${f} ${f}
done

# Rename the license file
cp -r doc/licenses/lgpl-2.1.txt LICENSE.txt

%build
export OPT_JAR_LIST="ant apache-ivy"
ant -Dbrew nexus clean docs

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# common-impl-papaki validator-cli validator-maven validator-ant - not built in when nexus/brew target is selected
# deployers-fungal - no fungal package avaialble
for m in deployers-common common-impl validator core-impl jdbc common-spi core-api common-api spec-api; do
  # JAR
  install -pm 644 target/ironjacamar-${m}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${m}.jar
  # POM
  install -pm 644 ironjacamar-${m}-%{namedversion}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

# APIDOCS
cp -rp target/docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc README.txt LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt3_4jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1_4jpp7
- new version

