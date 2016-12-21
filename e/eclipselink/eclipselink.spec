Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
BuildRequires: rpm-build-java-osgi
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name eclipselink
%define version 2.6.3

%global reltag .v20160428-59c81c5
%global namedversion %{version}%{?reltag}

%global core org.eclipse.persistence.core
%global dbws org.eclipse.persistence.dbws
%global extension org.eclipse.persistence.extension
%global jpa org.eclipse.persistence.jpa
%global jpql org.eclipse.persistence.jpa.jpql
%global modelgen org.eclipse.persistence.jpa.modelgen.processor
%global moxy org.eclipse.persistence.moxy
%global sdo org.eclipse.persistence.sdo

Name:          eclipselink
Version:       2.6.3
Release:       alt1_1jpp8
Summary:       Eclipse Persistence Services Project
License:       EPL and BSD
Url:           http://www.eclipse.org/eclipselink/
# http://git.eclipse.org/c/eclipselink/eclipselink.runtime
Source0:       http://www.mirrorservice.org/sites/download.eclipse.org/eclipseMirror/rt/%{name}/releases/%{version}/%{name}-src-%{namedversion}.zip
Source1:       %{name}-%{version}-build.properties
Source2:       %{name}-%{version}-build.xml

Source3:       http://repo1.maven.org/maven2/org/eclipse/persistence/%{name}/%{version}/%{name}-%{version}.pom
Source4:       http://repo1.maven.org/maven2/org/eclipse/persistence/%{core}/%{version}/%{core}-%{version}.pom
Source5:       http://repo1.maven.org/maven2/org/eclipse/persistence/%{dbws}/%{version}/%{dbws}-%{version}.pom
Source6:       http://repo1.maven.org/maven2/org/eclipse/persistence/%{extension}/%{version}/%{extension}-%{version}.pom
Source7:       http://repo1.maven.org/maven2/org/eclipse/persistence/%{jpa}/%{version}/%{jpa}-%{version}.pom
Source8:       http://repo1.maven.org/maven2/org/eclipse/persistence/%{jpql}/%{version}/%{jpql}-%{version}.pom
Source9:       http://repo1.maven.org/maven2/org/eclipse/persistence/%{modelgen}/%{version}/%{modelgen}-%{version}.pom
Source10:      http://repo1.maven.org/maven2/org/eclipse/persistence/%{moxy}/%{version}/%{moxy}-%{version}.pom
Source11:      http://repo1.maven.org/maven2/org/eclipse/persistence/%{sdo}/%{version}/%{sdo}-%{version}.pom

BuildRequires: ant
BuildRequires: antlr3-java
BuildRequires: antlr3-tool
BuildRequires: aqute-bnd
BuildRequires: bean-validation-api
BuildRequires: cdi-api
BuildRequires: eclipse-equinox-osgi
BuildRequires: eclipselink-persistence-api
BuildRequires: glassfish-jaxb-api
BuildRequires: glassfish-jaxb-codemodel
BuildRequires: glassfish-jaxb-core
BuildRequires: glassfish-jaxb-jxc
BuildRequires: glassfish-servlet-api
BuildRequires: java-devel
BuildRequires: java-javadoc
BuildRequires: javamail
BuildRequires: javapackages-local
BuildRequires: jboss-connector-1.7-api
BuildRequires: jboss-jaxrs-2.0-api
BuildRequires: jboss-jms-2.0-api
BuildRequires: jboss-transaction-1.2-api
BuildRequires: jgroups
BuildRequires: jsonp
BuildRequires: objectweb-asm
BuildRequires: stringtemplate4
BuildRequires: tuscany-sdo-java
BuildRequires: xsom

BuildArch:     noarch
Source44: import.info

%description
Eclipse Persistence Services Project, more commonly known as EclipseLink,
is a Java comprehensive persistence framework delivering a set of persistence
services based around standards. This lets you rapidly build applications
that combine the best aspects of object technology and the specific data
source.

EclipseLink was started by a donation of the full source code and
test suites of Oracle's TopLink product.

EclipseLink's services currently include object-relational with JPA,
object-XML binding in MOXy (with support for JAXB), a Service Data Objects
(SDO) implementation and support for another technologies like: Database Web
Services (DWS), XML-Relational (XRM) and Non-Relational (EIS via JCA).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -c

rm -r org/eclipse/persistence/internal/libraries/*
find ./ -name "*.java" -exec sed -i "s/org.eclipse.persistence.internal.libraries.antlr/org.antlr/g" {} +
find ./ -name "*.java" -exec sed -i "s/org.eclipse.persistence.internal.libraries.asm/org.objectweb.asm/g" {} +

# temporary fix for antlr 3.5.2
sed -i "s|Token.EOF_TOKEN|Token.EOF|" \
 org/eclipse/persistence/internal/jpa/parsing/jpql/JPQLParser.java

cp -p %{SOURCE1} build.properties
cp -p %{SOURCE2} build.xml

cp -p %{SOURCE3} pom.xml
%pom_change_dep org.eclipse.persistence:commonj.sdo org.apache.tuscany.sdo:tuscany-sdo-api-r2.1:1.1.1

cp -p %{SOURCE4} core-pom.xml
%pom_change_dep org.eclipse.persistence:org.eclipse.persistence.asm org.ow2.asm:asm:5.0.4 core-pom.xml
%pom_add_dep org.ow2.asm:asm-commons:5.0.4:compile core-pom.xml
%pom_add_dep org.ow2.asm:asm-tree:5.0.4:compile core-pom.xml
%pom_add_dep org.ow2.asm:asm-tree:5.0.4:compile core-pom.xml
%pom_add_dep org.ow2.asm:asm-util:5.0.4:compile core-pom.xml
%pom_add_dep org.ow2.asm:asm-xml:5.0.4:compile core-pom.xml

cp -p %{SOURCE7} jpa-pom.xml
%pom_change_dep org.eclipse.persistence:org.eclipse.persistence.antlr org.antlr:antlr-runtime:3.5.2 jpa-pom.xml
%pom_change_dep org.eclipse.persistence:org.eclipse.persistence.asm org.ow2.asm:asm:5.0.4 jpa-pom.xml
%pom_add_dep org.ow2.asm:asm:5.0.4:compile jpa-pom.xml
%pom_add_dep org.ow2.asm:asm-commons:5.0.4:compile jpa-pom.xml
%pom_add_dep org.ow2.asm:asm-tree:5.0.4:compile jpa-pom.xml
%pom_add_dep org.ow2.asm:asm-tree:5.0.4:compile jpa-pom.xml
%pom_add_dep org.ow2.asm:asm-util:5.0.4:compile jpa-pom.xml
%pom_add_dep org.ow2.asm:asm-xml:5.0.4:compile jpa-pom.xml

cp -p %{SOURCE11} sdo-pom.xml
%pom_change_dep org.eclipse.persistence:commonj.sdo org.apache.tuscany.sdo:tuscany-sdo-api-r2.1:1.1.1 sdo-pom.xml

# fix non ASCII chars
for s in org/eclipse/persistence/internal/jpa/transaction/JTATransactionWrapper.java \
  org/eclipse/persistence/jpa/jpql/parser/AbstractExpression.java \
  org/eclipse/persistence/jpa/jpql/tools/DefaultGrammarValidator.java \
  org/eclipse/persistence/jpa/jpql/tools/model/IScalarExpressionStateObjectBuilder.java \
  org/eclipse/persistence/platform/database/HANAPlatform.java \
  org/eclipse/persistence/platform/database/MaxDBPlatform.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

%build

(
 cd org/eclipse/persistence/internal/oxm/record/json/
 antlr3 JSON.g
)

(
 cd org/eclipse/persistence/internal/jpa/parsing/jpql/antlr/
# error: variable node is already defined in method subselectIdentificationVariableDeclaration(List)
 sed -i '/Object node = null;/d' JPQL.g
 antlr3 JPQL.g
)

ant

%install
%mvn_artifact pom.xml target/%{name}.jar
%mvn_artifact core-pom.xml target/%{core}-%{version}.jar
%mvn_artifact %{SOURCE5} target/%{dbws}-%{version}.jar
%mvn_artifact %{SOURCE6} target/%{extension}-%{version}.jar
%mvn_artifact jpa-pom.xml target/%{jpa}-%{version}.jar
%mvn_artifact %{SOURCE8} target/%{jpql}-%{version}.jar
%mvn_artifact %{SOURCE9} target/%{modelgen}-%{version}.jar
%mvn_artifact %{SOURCE10} target/%{moxy}-%{version}.jar
%mvn_artifact sdo-pom.xml target/%{sdo}-%{version}.jar
%mvn_install -J target/api

%files -f .mfiles
%doc about.html readme.html
%doc license.html

%files javadoc -f .mfiles-javadoc
%doc license.html

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_2jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1_10jpp8
- java 8 mass update

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2_2jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_1jpp7
- new release

