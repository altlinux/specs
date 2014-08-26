# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name glassfish-management-api
%define version 3.2.0
%global namedreltag -b001
%global namedversion %{version}%{?namedreltag}
Name:          glassfish-management-api
Version:       3.2.0
Release:       alt1_0.1.b001jpp7
Summary:       GlassFish Common APIs
Group:         Development/Java
License:       CDDL or GPLv2 with exceptions
URL:           http://java.net/projects/gmbal/pages/Home
# hg clone -r VERSION-3.2.0-b001 https://hg.java.net/hg/gmbal~gf_common/ glassfish-management-api-3.2.0-b001
# tar czf glassfish-management-api-3.2.0-b001-src-hg.tar.gz glassfish-management-api-3.2.0-b001
# or
Source0:       http://central.maven.org/maven2/org/glassfish/external/management-api/%{namedversion}/management-api-%{namedversion}-sources.jar
Source1:       http://central.maven.org/maven2/org/glassfish/external/management-api/%{namedversion}/management-api-%{namedversion}.pom
# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# glassfish-management-api package don't include the license file
Source2:       glassfish-LICENSE.txt

Patch0:        %{name}-%{namedversion}-remove-gpg-plugin.patch

BuildRequires: jpackage-utils
BuildRequires: jvnet-parent

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
The GlassFish MBean Annotation Library (gmbal, pronounced "Gumball")
is a library for using annotations to create Open MBeans. There is similar
functionality in JSR 255 for JDK 7, but gmbal only requires JDK 5. Gmbal
also supports JSR 77 ObjectNames and the GlassFish Version 3 AMX 
requirements for MBeans. AS a consequence, gmbal-enabled classes
will be fully manageable in GlassFish v3 using the standard GlassFish
v3 admin tools, while still being manageable with generic MBean tools
when not run under GlassFish v3.

This package contains the gmbal Common APIs.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
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

cp -p %{SOURCE2} LICENSE.txt
sed -i 's/\r//' LICENSE.txt

%build

mvn-rpmbuild install

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/management-api-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt1_0.1.b001jpp7
- new release

