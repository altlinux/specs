Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++ java-devel-default rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name ironjacamar
%define version 1.1.10
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             ironjacamar
Version:          1.1.10
Release:          alt1_2jpp8
Summary:          Java Connector Architecture 1.7 implementation
License:          LGPLv2+
URL:              http://www.ironjacamar.org/

Source0:          https://github.com/ironjacamar/ironjacamar/archive/ironjacamar-%{version}.Final.tar.gz

# Remote POM's...
# Use spectool -g to get them
Source1:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/jboss/ironjacamar/ironjacamar-deployers-common/%{namedversion}/ironjacamar-deployers-common-%{namedversion}.pom
Source2:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/jboss/ironjacamar/ironjacamar-validator-cli/%{namedversion}/ironjacamar-validator-cli-%{namedversion}.pom
Source3:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/jboss/ironjacamar/ironjacamar-common-impl/%{namedversion}/ironjacamar-common-impl-%{namedversion}.pom
Source4:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/jboss/ironjacamar/ironjacamar-validator/%{namedversion}/ironjacamar-validator-%{namedversion}.pom
Source5:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/jboss/ironjacamar/ironjacamar-core-impl/%{namedversion}/ironjacamar-core-impl-%{namedversion}.pom
Source6:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/jboss/ironjacamar/ironjacamar-jdbc/%{namedversion}/ironjacamar-jdbc-%{namedversion}.pom
Source7:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/jboss/ironjacamar/ironjacamar-common-spi/%{namedversion}/ironjacamar-common-spi-%{namedversion}.pom
Source8:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/jboss/ironjacamar/ironjacamar-validator-maven/%{namedversion}/ironjacamar-validator-maven-%{namedversion}.pom
Source9:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/jboss/ironjacamar/ironjacamar-core-api/%{namedversion}/ironjacamar-core-api-%{namedversion}.pom
Source10:         https://repository.jboss.org/nexus/service/local/repositories/central/content/org/jboss/ironjacamar/ironjacamar-validator-ant/%{namedversion}/ironjacamar-validator-ant-%{namedversion}.pom
Source11:         https://repository.jboss.org/nexus/service/local/repositories/central/content/org/jboss/ironjacamar/ironjacamar-common-api/%{namedversion}/ironjacamar-common-api-%{namedversion}.pom
Source12:         https://repository.jboss.org/nexus/service/local/repositories/central/content/org/jboss/ironjacamar/ironjacamar-spec-api/%{namedversion}/ironjacamar-spec-api-%{namedversion}.pom

# Commented out trying to download Ivy from the Internet
Patch0:            0001-Use-Fedora-provided-IVY.patch
Patch1:            0002-Adjust-IVY-paths.patch

BuildArch:        noarch

BuildRequires:    ant
BuildRequires:    apache-ivy
BuildRequires:    apiviz
BuildRequires:    bean-validation-api
BuildRequires:    java-devel >= 1.6.0
BuildRequires:    javamail
BuildRequires:    javassist
BuildRequires:    jboss-connector-1.6-api
BuildRequires:    jboss-jaspi-1.0-api >= 1.0.1
BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools
BuildRequires:    jboss-logmanager
BuildRequires:    jboss-logmanager-log4j
BuildRequires:    jboss-threads >= 2.0.0
BuildRequires:    jboss-transaction-1.2-api
BuildRequires:    jboss-transaction-spi >= 7.1.0
BuildRequires:    jdepend
BuildRequires:    jpackage-utils
BuildRequires:    log4j-jboss-logmanager
BuildRequires:    maven-local
BuildRequires:    picketbox

Requires:         geronimo-validation
Requires:         javamail
Requires:         javassist
Requires:         jboss-connector-1.6-api
Requires:         jboss-jaspi-1.0-api
Requires:         jboss-logging
Requires:         jboss-threads
Requires:         jboss-transaction-1.2-api
Requires:         jboss-transaction-spi
Requires:         log4j-jboss-logmanager
Requires:         jpackage-utils
Requires:         picketbox
Source44: import.info

%description
The IronJacamar project implements the Java Connector Architecture 1.7
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
%setup -q -n %{name}-%{name}-%{namedversion}
%patch0 -p1
%patch1 -p1

# Yes, a bit ugly because we copy also the source code
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} .
# Let's remove it
rm $(basename %{SOURCE0})

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

mkdir lib

sed -i '/IronJacamar requires JDK7/d' build.xml

%build
ant -Das jars-base clean docs

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name} \
         $RPM_BUILD_ROOT%{_mavenpomdir} \
         $RPM_BUILD_ROOT%{_javadocdir}/%{name}

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

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc README.md
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt1_2jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt1_1jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt3_6jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt3_4jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1_4jpp7
- new version

