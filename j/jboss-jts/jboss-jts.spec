# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat perl(Pod/Text.pm)
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jts
%define version 4.16.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name: jboss-jts
Version: 4.16.2
Release: alt1_11jpp7
Summary: Distributed Transaction Manager
Group: Development/Java
License: LGPLv2+
URL: https://community.jboss.org/wiki/JBossJTS

# svn export http://anonsvn.jboss.org/repos/labs/labs/jbosstm/tags/JBOSSTS_4_16_2_Final/ jboss-jts-4.16.2
# find jboss-jts-4.16.2 -name '*.jar' -delete
# tar cafJ jboss-jts-4.16.2.tar.xz jboss-jts-4.16.2
Source0: %{name}-%{namedversion}.tar.xz

Source1: https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/jbossts/jbossjts/%{namedversion}/jbossjts-%{namedversion}.pom
Source2: https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/jbossts/jbossjts-integration/%{namedversion}/jbossjts-integration-%{namedversion}.pom
Source3: https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/jbossts/jbosstxbridge/%{namedversion}/jbosstxbridge-%{namedversion}.pom
Source4: https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/jbossts/jbossxts/%{namedversion}/jbossxts-%{namedversion}.pom
Source5: https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/jbossts/jbossxts-api/%{namedversion}/jbossxts-api-%{namedversion}.pom

# Patched Ant xml files
# Removed com.arjuna.ats.jta.distributed.SimpleIsolatedServers test
# Removed some tests as they fail with Byteman
Patch0: %{name}-%{namedversion}-build.patch

# Added support for JBoss publican style shipped in Fedora
Patch1: %{name}-%{namedversion}-publican.patch

# Removed ArjunaCore/arjuna/classes/com/arjuna/ats/arjuna/tools/stats/TxPerfGraph.java because we don't have orson packaged
Patch2: %{name}-%{namedversion}-orson.patch

# The atsintegration built with JTS support needs one interface from jboss-corba-ots-spi project
# it does not make sense to package it, so let's remove the usage here
Patch3: jboss-jts-%{namedversion}-InboundTransactionCurrent-interface-removal.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: junit
BuildRequires: antlr-tool
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: ant-contrib
BuildRequires: apache-commons-codec
BuildRequires: avalon-logkit
BuildRequires: emma
BuildRequires: hibernate-jpa-2.0-api
BuildRequires: dom4j
BuildRequires: byteman
BuildRequires: ironjacamar
BuildRequires: jacorb
BuildRequires: jakarta-commons-httpclient
BuildRequires: jboss-logging
BuildRequires: jboss-logging-tools
BuildRequires: jboss-transaction-1.1-api
BuildRequires: jboss-transaction-spi
BuildRequires: jboss-servlet-3.0-api
BuildRequires: jboss-ejb-3.1-api
BuildRequires: jbossws-api
BuildRequires: hornetq
BuildRequires: jfreechart
BuildRequires: publican-jboss
BuildRequires: java-service-wrapper
BuildRequires: slf4j

Requires: jpackage-utils
Requires: antlr-tool
Requires: avalon-logkit
Requires: byteman
Requires: dom4j
Requires: emma
Requires: hibernate-jpa-2.0-api
Requires: ironjacamar
Requires: jacorb
Requires: jboss-logging
Requires: jboss-logging-tools
Requires: jboss-transaction-1.1-api
Requires: jboss-transaction-spi
Requires: jboss-servlet-3.0-api
Requires: jboss-ejb-3.1-api
Requires: jbossws-api
Requires: hornetq
Requires: jfreechart
Requires: java-service-wrapper
Requires: slf4j
Source44: import.info


%description
A set of JBoss modules that fully supports ACID transactions
spread across multiple resource managers and application servers.
It implements a Distributed Transaction Manager (DTM) with support
for two-phase commit (2PC) across XA resource managers, JBoss
server instances, and CORBA OTS resources.

JBossJTS implements the Java Transaction Service (JTS) and CORBA
Transaction Service (OTS) specifications.


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.


%prep

# Extract the source:
%setup -q -n %{name}-%{namedversion}

# Put the POM files in place now, as they require patching:
cp %{SOURCE1} jbossjts.pom
cp %{SOURCE2} jbossjts-integration.pom
cp %{SOURCE3} jbosstxbridge.pom
cp %{SOURCE4} jbossxts.pom
cp %{SOURCE5} jbossxts-api.pom

# https://bugzilla.redhat.com/show_bug.cgi?id=825782#c1
%pom_xpath_remove "pom:dependencyManagement" jbossjts.pom
%pom_xpath_remove "pom:dependencyManagement" jbossjts-integration.pom
%pom_xpath_remove "pom:dependencyManagement" jbosstxbridge.pom
%pom_xpath_remove "pom:dependencyManagement" jbossxts.pom
%pom_xpath_remove "pom:dependencyManagement" jbossxts-api.pom

# Apply the patches:
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# We do not want to execute maven, not necessary
sed -i 's|<antcall target="mvn-local-repository"/>||' build.xml

rm -f ArjunaJTS/jts/tests/classes/com/hp/mwtests/ts/jts/local/heuristics/HeuristicTest.java ArjunaJTS/jts/tests/classes/com/hp/mwtests/ts/jts/local/synchronizations/SynchTest.java

sed -i -e 's!<target name="dist.leafnode" depends="clean, init, compile, compile-tests, generateresourcebundle, run.tests">!<target name="dist.leafnode" depends="clean, init, compile, compile-tests, generateresourcebundle">!' sharedbuild.xml

%build

# Replace jar files with symlinks to their actual locations:
while read jar_name jar_path
do
  jar_file=$(build-classpath ${jar_name})
  jar_dir=$(dirname ${jar_path})
  if [ ! -d ${jar_dir} ]
  then
    mkdir -p ${jar_dir}
  fi
  ln -s ${jar_file} ${jar_path}
done <<'.'
apache-commons-codec ext/commons-codec.jar
junit common/lib/ext/junit.jar
junit ext/junit.jar
emma ext/emma.jar
emma_ant ext/emma_ant.jar
hibernate-jpa-2.0-api ext/hibernate-jpa-2.0-api.jar
dom4j ext/dom4j.jar
jboss-logging ext/jboss-logging.jar
jboss-logging-processor ext/jboss-logging-processor.jar
ironjacamar/ironjacamar-spec-api ext/ironjacamar-spec-api.jar
jboss-transaction-1.1-api ext/jboss-transaction-api_1.1_spec.jar
jboss-servlet-3.0-api ext/jboss-servlet-api_3.0_spec.jar
jboss-ejb-3.1-api ext/jboss-ejb-api_3.1_spec.jar
jakarta-commons-httpclient ext/commons-httpclient.jar
byteman/byteman ext/byteman.jar
byteman/byteman-bmunit ext/byteman-bmunit.jar
byteman/byteman-dtest ext/byteman-dtest.jar
byteman/byteman-install ext/byteman-install.jar
byteman/byteman-submit ext/byteman-submit.jar
jboss-transaction-spi ext/jboss-transaction-spi.jar
jfreechart/jfreechart ext/jfreechart-1.0.6.jar
hornetq/hornetq-core ext/hornetq-core.jar
jbossws-api ext/jbossws-api.jar
jacorb ext/jacorb.jar
jacorb ArjunaJTS/jacorb/lib/jacorb.jar
jacorb-idl-compiler ArjunaJTS/jacorb/lib/idl.jar
avalon-logkit ArjunaJTS/jacorb/lib/logkit.jar
slf4j/api ArjunaJTS/jacorb/lib/slf4j-api.jar
slf4j/jdk14 ArjunaJTS/jacorb/lib/slf4j-jdk14.jar
antlr ArjunaJTS/jacorb/lib/antlr.jar
.

# The above loop does not work for java service wrapper as the jar file is not
# installed in the expected location:
ln -s /usr/lib*/java-service-wrapper/wrapper.jar ext/wrapper.jar
ln -s /usr/lib*/java-service-wrapper/wrapper.jar ArjunaJTS/jacorb/lib/wrapper-3.1.0.jar

# Build the binaries:
ant -Dpublican=false jbossall

%if 0
# Build the documentation:
ant \
  -f docs/build.xml \
  install.docs \
  install.common.docs

# Move the HTML documentation to the same directory that contains the PDF
# files:
documents='
development_guide
failure_recovery_guide
transactions_overview_guide
txbridge_guide
'
for document in ${documents}
do
  mkdir -p docs/build/install/docs/${document}
  mv docs/${document}/target/publican/en-US/html/* docs/build/install/docs/${document}
done

# Release notes are placed in a different directory, so move them to the same
# directory than the rest of the documentation:
mv docs/build/release_notes/en-US/pdf/*.pdf docs/build/install/docs/.
mkdir -p docs/build/install/docs/release_notes
cp -rp docs/build/release_notes/en-US/html/* docs/build/install/docs/release_notes
%endif

%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -pm 644 install/lib/jbossjts.jar %{buildroot}%{_javadir}/%{name}/jbossjts.jar
install -pm 644 install/lib/jbossjts-integration.jar %{buildroot}%{_javadir}/%{name}/jbossjts-integration.jar
install -pm 644 install/txbridge/jbosstxbridge.jar %{buildroot}%{_javadir}/%{name}/jbosstxbridge.jar
install -pm 644 XTS/xts-install/lib/jbossxts.jar %{buildroot}%{_javadir}/%{name}/jbossxts.jar
install -pm 644 XTS/xts-install/lib/jbossxts-api.jar %{buildroot}%{_javadir}/%{name}/jbossxts-api.jar

# No POM's for these files:
install -pm 644 install/services/lib/jbossjts-services.jar %{buildroot}%{_javadir}/%{name}/jbossjts-services.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 jbossjts.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-jbossjts.pom
install -pm 644 jbossjts-integration.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-jbossjts-integration.pom
install -pm 644 jbosstxbridge.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-jbosstxbridge.pom
install -pm 644 jbossxts.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-jbossxts.pom
install -pm 644 jbossxts-api.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-jbossxts-api.pom

# Dependencies map:
%add_maven_depmap JPP.%{name}-jbossjts.pom %{name}/jbossjts.jar
%add_maven_depmap JPP.%{name}-jbossjts-integration.pom %{name}/jbossjts-integration.jar
%add_maven_depmap JPP.%{name}-jbosstxbridge.pom %{name}/jbosstxbridge.jar
%add_maven_depmap JPP.%{name}-jbossxts.pom %{name}/jbossxts.jar
%add_maven_depmap JPP.%{name}-jbossxts-api.pom %{name}/jbossxts-api.jar

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp install/htdocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
#doc docs/build/install/docs/*


%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 4.16.2-alt1_11jpp7
- new release

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 4.16.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

