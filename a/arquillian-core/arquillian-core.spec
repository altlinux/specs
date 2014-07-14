BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name arquillian-core
%define version 1.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:           arquillian-core
Version:        1.0.2
Release:        alt2_1jpp7
Summary:        Arquillian is a revolutionary testing platform built on the JVM
Group:          Development/Java
License:        ASL 2.0
URL:            http://www.jboss.org/arquillian

# git clone https://github.com/arquillian/arquillian-core.git arquillian-core-1.0.2.Final
# cd arquillian-core-1.0.2.Final && git archive --format=tar --prefix=arquillian-core-1.0.2.Final/ 1.0.2.Final | xz > ../arquillian-core-1.0.2.Final.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    jboss-parent

BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-source-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    maven-surefire-provider-testng
BuildRequires:    maven-enforcer-plugin

BuildRequires:    apiviz
BuildRequires:    junit4

BuildRequires:    shrinkwrap
BuildRequires:    shrinkwrap-descriptors
BuildRequires:    shrinkwrap-resolver
BuildRequires:    cdi-api
BuildRequires:    weld-core
BuildRequires:    weld-parent
BuildRequires:    slf4j
BuildRequires:    testng
BuildRequires:    geronimo-ejb
BuildRequires:    geronimo-annotation
BuildRequires:    jboss-el-2.2-api
BuildRequires:    mockito
BuildRequires:    jboss-logging
BuildRequires:    jboss-logmanager
BuildRequires:    jboss-servlet-3.0-api

Requires:    shrinkwrap-descriptors
Requires:    shrinkwrap-resolver
Requires:    junit4
Requires:    shrinkwrap
Requires:    jboss-logging
Requires:    jboss-logmanager
Requires:    jboss-servlet-3.0-api
Requires:    cdi-api
Requires:    geronimo-ejb
Requires:    geronimo-annotation
Requires:    testng
Requires:    jpackage-utils
Source44: import.info

%description
Arquillian is a revolutionary testing platform built on the JVM that
substantially reduces the effort required to write and execute Java 
middleware integration and functional tests. No more mocks. 
No more container lifecycle and deployment hassles. Just real tests!


%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q  -n %{name}-%{namedversion}

%build
export MAVEN_OPTS="-Xms256m -Xmx768m -XX:PermSize=128m -XX:MaxPermSize=256m"
mvn-rpmbuild install javadoc:aggregate

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

for m in config-api \
         config-impl-base \
         config-spi \
         container-impl-base \
         container-spi \
         container-test-api \
         container-test-spi \
         container-test-impl-base \
         core-api \
         core-spi \
         core-impl-base \
         junit-container \
         junit-core \
         junit-standalone \
         test-api \
         test-spi \
         test-impl-base \
         testng-container \
         testng-core \
         testng-standalone \
         ; do
         # module path
         mp=`echo ${m} | sed "s/\-/\//"`;
         # JAR
         install -pm 644 ${mp}/target/arquillian-${m}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/arquillian-${m}.jar
         # POM
         install -pm 644 ${mp}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-${m}.pom
         # DEPMAP
         %add_maven_depmap JPP.%{name}-arquillian-${m}.pom %{name}/arquillian-${m}.jar
done

for m in protocols-jmx \
         protocols-servlet \
         testenrichers-cdi \
         testenrichers-ejb \
         testenrichers-initialcontext \
         testenrichers-resource \
         ; do
         # module path
         mp=`echo ${m} | sed "s/\-/\//"`;
         # module name, without 's'
         mn=`echo ${m} | sed "s/s\-/\-/"`;
         # JAR
         install -pm 644 ${mp}/target/arquillian-${mn}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/arquillian-${mn}.jar
         # POM
         install -pm 644 ${mp}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-${mn}.pom
         # DEPMAP
         %add_maven_depmap JPP.%{name}-arquillian-${mn}.pom %{name}/arquillian-${mn}.jar
done


# POMs and DEPMAP
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-parent.pom
%add_maven_depmap JPP.%{name}-arquillian-parent.pom
install -pm 644 bom/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-bom.pom
%add_maven_depmap JPP.%{name}-arquillian-bom.pom
install -pm 644 build/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-build.pom
%add_maven_depmap JPP.%{name}-arquillian-build.pom

## config parent
install -pm 644 config/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-config-parent.pom
%add_maven_depmap JPP.%{name}-arquillian-config-parent.pom

## container parent
install -pm 644 container/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-container-parent.pom
%add_maven_depmap JPP.%{name}-arquillian-container-parent.pom

## core parent
install -pm 644 core/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-core-parent.pom
%add_maven_depmap JPP.%{name}-arquillian-core-parent.pom

## junit parent
install -pm 644 junit/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-junit-parent.pom
%add_maven_depmap JPP.%{name}-arquillian-junit-parent.pom

## protocols parent
install -pm 644 protocols/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-protocols-parent.pom
%add_maven_depmap JPP.%{name}-arquillian-protocols-parent.pom

## test parent
install -pm 644 test/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-test-parent.pom
%add_maven_depmap JPP.%{name}-arquillian-test-parent.pom

## testenrichers parent
install -pm 644 testenrichers/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-testenrichers-parent.pom
%add_maven_depmap JPP.%{name}-arquillian-testenrichers-parent.pom

## testng parent
install -pm 644 testng/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-testng-parent.pom
%add_maven_depmap JPP.%{name}-arquillian-testng-parent.pom

# Javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}/*.jar
%{_mavenpomdir}/JPP.%{name}-*.pom
%{_mavendepmapfragdir}/%{name}
%doc license.txt apl.txt readme.txt

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt apl.txt


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_1jpp7
- new version

