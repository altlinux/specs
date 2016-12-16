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
%define version 1.3.4
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          ironjacamar
Version:       1.3.4
Release:       alt1_2jpp8
Summary:       Java Connector Architecture 1.7 implementation
License:       LGPLv2+
URL:           http://www.ironjacamar.org/
Source0:       https://github.com/ironjacamar/ironjacamar/archive/%{name}-%{namedversion}.tar.gz

# Commented out trying to download Ivy from the Internet
Patch0:        ironjacamar-1.3.4.Final-Use-Fedora-provided-IVY.patch
Patch1:        0002-Adjust-IVY-paths.patch
Patch2:        ironjacamar-1.3.4-remove-ambiguous-reference-to-tracef.patch   

BuildRequires: ant
BuildRequires: apache-ivy
BuildRequires: graphviz libgraphviz
BuildRequires: ivy-local
BuildRequires: java-devel
BuildRequires: javapackages-local
BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(jdepend:jdepend)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.jboss:jandex)
BuildRequires: mvn(org.jboss:jboss-transaction-spi)
BuildRequires: mvn(org.jboss.apiviz:apiviz)
BuildRequires: mvn(org.jboss.jdeparser:jdeparser)
BuildRequires: mvn(org.jboss.logging:jboss-logging)
BuildRequires: mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires: mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires: mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires: mvn(org.jboss.logmanager:log4j-jboss-logmanager)
BuildRequires: mvn(org.jboss.spec.javax.security.auth.message:jboss-jaspi-api_1.0_spec)
BuildRequires: mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.2_spec)
BuildRequires: mvn(org.jboss.threads:jboss-threads)
BuildRequires: mvn(org.jgroups:jgroups)
BuildRequires: mvn(org.picketbox:picketbox)

# Runtime dependecies
Requires:      mvn(javax.validation:validation-api)
Requires:      mvn(org.jboss:jandex)
Requires:      mvn(org.jboss:jboss-transaction-spi)
Requires:      mvn(org.jboss.logging:jboss-logging)
Requires:      mvn(org.jboss.spec.javax.security.auth.message:jboss-jaspi-api_1.0_spec)
Requires:      mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.2_spec)
Requires:      mvn(org.jboss.threads:jboss-threads)
Requires:      mvn(org.jboss.logmanager:log4j-jboss-logmanager)
Requires:      mvn(org.picketbox:picketbox)

BuildArch:     noarch
Source44: import.info

%description
The IronJacamar project implements the Java Connector Architecture 1.7
specification.

The Java Connector Architecture (JCA) defines a standard architecture for
connecting the Java EE platform to heterogeneous Enterprise Information
Systems (EIS). Examples of EISs include Enterprise Resource Planning (ERP),
mainframe transaction processing (TP), database and messaging systems.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -qn %{name}-%{name}-%{namedversion}
# Cleanup
find -name "*.class" -print -delete
find -name "*.jar" -print -delete

%patch0 -p1
%patch1 -p1
%patch2 -p1

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
sed -i '/Nexus requires JDK7/d' build.xml
sed -i '/<deploy-file/d' build.xml
sed -i '/<install-file/d' build.xml

%build

ant -Divy.mode=local -Das jars-base clean docs nexus-base

# Fix malformed pom entries
%pom_change_dep org.jboss.spec.javax.transaction: :jboss-transaction-api_1.2_spec target/%{name}-core-api.xml
%pom_change_dep javax.validation: :validation-api target/%{name}-core-impl.xml
%pom_change_dep org.jboss.spec.javax.security.auth.message: :jboss-jaspi-api_1.0_spec target/%{name}-core-impl.xml
%pom_change_dep org.jboss.spec.javax.transaction: :jboss-transaction-api_1.2_spec target/%{name}-core-impl.xml
%pom_change_dep org.jboss.spec.javax.transaction: :jboss-transaction-api_1.2_spec target/%{name}-jdbc.xml
%pom_change_dep org.jboss.spec.javax.transaction: :jboss-transaction-api_1.2_spec target/%{name}-spec-api.xml

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name} \
         $RPM_BUILD_ROOT%{_mavenpomdir} \
         $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# common-impl-papaki validator-cli validator-maven validator-ant - not built in when nexus/brew target is selected
# deployers-fungal - no fungal package available
for m in common-api common-impl common-spi core-api core-impl deployers-common jdbc spec-api validator; do
# JAR
  install -pm 644 target/%{name}-${m}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${m}.jar
# POM
  install -pm 644 target/%{name}-${m}.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
# DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done
# APIDOCS
cp -rp target/docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files -f .mfiles
%doc README.md
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt1_2jpp8
- new version

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

