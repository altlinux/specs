#BuildRequires: geronimo-jpa
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name eclipselink
%define version 2.3.2
%global reltag .v20111125-r10461
%global namedversion %{version}%{?reltag}
Name:          eclipselink
# for the next release is require hibernate-jpa-2.1-api unavailable at the moment
Version:       2.3.2
Release:       alt2_1jpp7
Summary:       Eclipse Persistence Services Project
Group:         Development/Java
License:       EPL and BSD
Url:           http://www.eclipse.org/eclipselink/
Source0:       http://www.mirrorservice.org/sites/download.eclipse.org/eclipseMirror/rt/%{name}/releases/%{version}/%{name}-src-%{namedversion}.zip
Source1:       %{name}-2.1.3-build.properties
Source2:       %{name}-%{version}-06-build.xml
Source3:       http://maven.eclipse.org/nexus/content/repositories/build/org/eclipse/persistence/%{name}/%{version}/%{name}-%{version}.pom
Source4:       http://maven.eclipse.org/nexus/content/repositories/build/org/eclipse/persistence/org.eclipse.persistence.core/%{version}/org.eclipse.persistence.core-%{version}.pom
Source5:       http://maven.eclipse.org/nexus/content/repositories/build/org/eclipse/persistence/org.eclipse.persistence.jpa/%{version}/org.eclipse.persistence.jpa-%{version}.pom

# use system libraries
Patch0:        %{name}-2.2.1-disable_antlr3_embedded_copy.patch
Patch1:        %{name}-%{version}-disable_asm_embedded_copy.patch
# change 
#    org.eclipse.persistence org.eclipse.persistence.asm in asm asm (and requires asm libraries)
#    org.eclipse.persistence org.eclipse.persistence.antlr in org.antlr antlr (and requires antlr3 libraries)
Patch2:        %{name}-%{version}-core-pom.patch
Patch3:        %{name}-%{version}-jpa-pom.patch

Patch4:        %{name}-%{version}-jdk7.patch
# the org.osgi.enterprise license is not free for Fedora
# this patch remove org.osgi.enterprise support only
Patch5:        %{name}-%{version}-disable-non-free-osgi-enterprise.patch

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: antlr3-java
BuildRequires: antlr3-tool
BuildRequires: felix-framework
BuildRequires: geronimo-jms
BuildRequires: geronimo-validation
BuildRequires: hibernate-jpa-2.0-api
BuildRequires: javamail
BuildRequires: jboss-connector-1.6-api
BuildRequires: jboss-transaction-1.1-api
BuildRequires: objectweb-asm
BuildRequires: tomcat-servlet-3.0-api
BuildRequires: tuscany-sdo-java
BuildRequires: wsdl4j

Requires:      antlr3-tool
Requires:      objectweb-asm

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
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

cp -p %{SOURCE1} build.properties
cp -p %{SOURCE2} build.xml

cp -p %{SOURCE4} .
cp -p %{SOURCE5} .

%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0

# fix non ASCII chars
for s in org/eclipse/persistence/jpa/internal/jpql/GrammarValidator.java\
  org/eclipse/persistence/platform/database/MaxDBPlatform.java\
  org/eclipse/persistence/jpa/internal/jpql/SemanticValidator.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

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
install -pm 644 %{SOURCE3} %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar

install -pm 644 org.eclipse.persistence.core-%{version}.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-org.eclipse.persistence.core.pom
%add_maven_depmap JPP.%{name}-org.eclipse.persistence.core.pom %{name}/org.eclipse.persistence.core.jar

install -pm 644 org.eclipse.persistence.jpa-%{version}.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-org.eclipse.persistence.jpa.pom
%add_maven_depmap JPP.%{name}-org.eclipse.persistence.jpa.pom %{name}/org.eclipse.persistence.jpa.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/api/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}
%{_mavenpomdir}/JPP.%{name}-*.pom
%{_mavendepmapfragdir}/%{name}
%doc about.html license.html readme.html

%files javadoc
%{_javadocdir}/%{name}
%doc license.html

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_1jpp7
- new release

