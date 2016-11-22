Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name glassfish-management-api
%define version 3.2.1
%global namedreltag -b002
%global namedversion %{version}%{?namedreltag}
Name:          glassfish-management-api
Version:       3.2.1
Release:       alt1_0.3.b002jpp8
Summary:       GlassFish Common APIs
License:       CDDL or GPLv2 with exceptions
URL:           http://java.net/projects/gmbal/pages/Home
# hg clone -r management-api-3.2.1-b002 https://hg.java.net/hg/gmbal~gf_common/ glassfish-management-api-3.2.1-b002
# rm -rf glassfish-management-api-3.2.1-b002/.hg
# find glassfish-management-api-3.2.1-b002 -name "*.jar" -delete
# find glassfish-management-api-3.2.1-b002 -name "*.class" -delete
# tar cJf glassfish-management-api-3.2.1-b002.tar.xz glassfish-management-api-3.2.1-b002
# or
Source0:       http://central.maven.org/maven2/org/glassfish/external/management-api/%{namedversion}/management-api-%{namedversion}-sources.jar
Source1:       http://central.maven.org/maven2/org/glassfish/external/management-api/%{namedversion}/management-api-%{namedversion}.pom
# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# glassfish-management-api package don't include the license file
Source2:       glassfish-LICENSE.txt

BuildRequires: jvnet-parent

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin

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
Group: Development/Java
Summary:       Javadoc for %{name}
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
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:executions"

cp -p %{SOURCE2} LICENSE.txt
sed -i 's/\r//' LICENSE.txt

%mvn_file :management-api %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_0.3.b002jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_0.2.b002jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt1_0.1.b001jpp7
- new release

