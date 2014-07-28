# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global oname jaxb-api
Name:          glassfish-jaxb-api
Version:       2.2.7
Release:       alt2_3jpp7
Summary:       Java Architecture for XML Binding
Group:         Development/Java
License:       CDDL or GPLv2 with exception
URL:           http://jaxb.java.net/
# jaxb api and impl have different version
# svn export https://svn.java.net/svn/jaxb~version2/tags/jaxb-2_2_6/tools/lib/redist/jaxb-api-src.zip

Source0:       http://repo1.maven.org/maven2/javax/xml/bind/%{oname}/%{version}/%{oname}-%{version}-sources.jar
Source1:       http://repo1.maven.org/maven2/javax/xml/bind/%{oname}/%{version}/%{oname}-%{version}.pom

Patch0:        %{name}-2.2.6-osgi-support.patch

BuildRequires: jpackage-utils

BuildRequires: java-javadoc
BuildRequires: jvnet-parent

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-shared-osgi
BuildRequires: maven-surefire-plugin

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Glassfish - JAXB (JSR 222) API.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{oname}
Requires:      %{name} = %{version}-%{release}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
Glassfish - JAXB (JSR 222) API.

This package contains javadoc for %{name}.

%prep
%setup -T -q -c

# fixing incomplete source directory structure
mkdir -p src/main/java

(
  cd src/main/java
  unzip -qq %{SOURCE0}
  rm -rf META-INF
)

cp -p %{SOURCE1} pom.xml
%patch0 -p0

sed -i 's|<location>${basedir}/offline-javadoc</location>|<location>%{_javadocdir}/java</location>|' pom.xml

%build

mvn-rpmbuild install javadoc:javadoc

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{oname}-%{version}.jar %{buildroot}%{_javadir}/%{oname}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{oname}.pom
%add_maven_depmap JPP-%{oname}.pom %{oname}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{oname}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{oname}

%files
%{_javadir}/%{oname}.jar
%{_mavenpomdir}/JPP-%{oname}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{oname}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_1jpp7
- new version

