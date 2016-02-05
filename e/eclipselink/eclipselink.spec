Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
BuildRequires: rpm-build-java-osgi
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name eclipselink
%define version 2.4.2
%global reltag .v20130514-5956486
%global namedversion %{version}%{?reltag}
Name:          eclipselink
Version:       2.4.2
Release:       alt1_10jpp8
Summary:       Eclipse Persistence Services Project
License:       EPL and BSD
Url:           http://www.eclipse.org/eclipselink/
Source0:       http://www.mirrorservice.org/sites/download.eclipse.org/eclipseMirror/rt/%{name}/releases/%{version}/%{name}-src-%{namedversion}.zip
Source1:       %{name}-2.4.2-build.properties
Source2:       %{name}-2.4.2-build.xml
Source3:       http://maven.eclipse.org/nexus/content/repositories/build/org/eclipse/persistence/%{name}/%{version}/%{name}-%{version}.pom
Source4:       http://repo1.maven.org/maven2/org/eclipse/persistence/org.eclipse.persistence.core/%{version}/org.eclipse.persistence.core-%{version}.pom
Source5:       http://repo1.maven.org/maven2/org/eclipse/persistence/org.eclipse.persistence.jpa/%{version}/org.eclipse.persistence.jpa-%{version}.pom

# use system libraries asm and antlr3
Patch0:        %{name}-2.4.2-use-system-libraries.patch
# thanks to Andrew Ross ubuntu[at]rossfamily.co.uk
Patch1:        %{name}-2.4.2-QueryOperation.patch

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: ant-antlr3
BuildRequires: antlr3-java
BuildRequires: antlr3-tool
BuildRequires: codemodel
BuildRequires: stringtemplate4
BuildRequires: eclipse-equinox-osgi
BuildRequires: eclipselink-persistence-api
BuildRequires: geronimo-jms
BuildRequires: geronimo-validation
BuildRequires: glassfish-jaxb
BuildRequires: glassfish-jaxb-api
BuildRequires: javamail
BuildRequires: jboss-connector-1.6-api
BuildRequires: jboss-transaction-1.1-api
BuildRequires: jsr-311
BuildRequires: objectweb-asm3
BuildRequires: tomcat-servlet-3.1-api
BuildRequires: tuscany-sdo-java
BuildRequires: wsdl4j

Requires:      antlr3-tool
Requires:      eclipselink-persistence-api
Requires:      objectweb-asm3
Requires:      tuscany-sdo-java

Requires:      jpackage-utils
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
%patch0 -p1

# build fix for openjdk
sed -i "s|ctor = AccessController.doPrivileged|ctor = (Constructor) AccessController.doPrivileged|" \
 org/eclipse/persistence/internal/jaxb/XMLJavaTypeConverter.java
sed -i "s|fields = AccessController.doPrivileged|fields = (Field[]) AccessController.doPrivileged|" \
 org/eclipse/persistence/jpa/rs/PersistenceContext.java
%patch1 -p0

cp -p %{SOURCE1} build.properties
cp -p %{SOURCE2} build.xml

cp -p %{SOURCE3} pom.xml
%pom_remove_dep org.eclipse.persistence:commonj.sdo
%pom_add_dep org.apache.tuscany.sdo:tuscany-sdo-api-r2.1:1.1.1:compile

cp -p %{SOURCE4} core-pom.xml
%pom_remove_dep org.eclipse.persistence:org.eclipse.persistence.asm core-pom.xml
%pom_add_dep org.antlr:antlr-runtime:3.2:compile core-pom.xml
%pom_add_dep org.antlr:antlr:3.2:compile core-pom.xml
%pom_add_dep asm:asm:3.3.1:compile core-pom.xml
%pom_add_dep asm:asm-commons:3.3.1:compile core-pom.xml
%pom_add_dep asm:asm-tree:3.3.1:compile core-pom.xml
%pom_add_dep asm:asm-tree:3.3.1:compile core-pom.xml
%pom_add_dep asm:asm-util:3.3.1:compile core-pom.xml
%pom_add_dep asm:asm-xml:3.3.1:compile core-pom.xml

cp -p %{SOURCE5} jpa-pom.xml
%pom_remove_dep org.eclipse.persistence: jpa-pom.xml
%pom_add_dep org.eclipse.persistence:javax.persistence:2.0.5:compile
%pom_add_dep org.antlr:antlr-runtime:3.2:compile jpa-pom.xml
%pom_add_dep org.antlr:antlr:3.2:compile jpa-pom.xml
%pom_add_dep asm:asm:3.3.1:compile jpa-pom.xml
%pom_add_dep asm:asm-commons:3.3.1:compile jpa-pom.xml
%pom_add_dep asm:asm-tree:3.3.1:compile jpa-pom.xml
%pom_add_dep asm:asm-tree:3.3.1:compile jpa-pom.xml
%pom_add_dep asm:asm-util:3.3.1:compile jpa-pom.xml
%pom_add_dep asm:asm-xml:3.3.1:compile jpa-pom.xml

# fix non ASCII chars
for s in org/eclipse/persistence/jpa/jpql/parser/AbstractExpression.java \
  org/eclipse/persistence/jpa/jpql/model/IScalarExpressionStateObjectBuilder.java \
  org/eclipse/persistence/jpa/jpql/DefaultGrammarValidator.java \
  org/eclipse/persistence/platform/database/MaxDBPlatform.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done
# temporary fix for antlr 3.5.2
sed -i.antlr352 "s|Token.EOF_TOKEN|Token.EOF|" \
 org/eclipse/persistence/internal/jpa/parsing/jpql/JPQLParser.java

%build

ant

%install

mkdir -p %{buildroot}%{_javadir}/%{name}
install -m 644 target/%{name}.jar \
  %{buildroot}%{_javadir}/%{name}/%{name}.jar

(
  cd %{buildroot}%{_javadir}/%{name}
  ln -sf %{name}.jar org.eclipse.persistence.core.jar
  ln -sf %{name}.jar org.eclipse.persistence.jpa.jar
)

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar

install -pm 644 core-pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-org.eclipse.persistence.core.pom
%add_maven_depmap JPP.%{name}-org.eclipse.persistence.core.pom %{name}/org.eclipse.persistence.core.jar

install -pm 644 jpa-pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-org.eclipse.persistence.jpa.pom
%add_maven_depmap JPP.%{name}-org.eclipse.persistence.jpa.pom %{name}/org.eclipse.persistence.jpa.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/api/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc about.html readme.html
%doc license.html

%files javadoc
%{_javadocdir}/%{name}
%doc license.html

%changelog
* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1_10jpp8
- java 8 mass update

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2_2jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_1jpp7
- new release

