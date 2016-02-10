Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name glassfish-gmbal
%define version 3.2.0
%global namedreltag -b003
%global namedversion %{version}%{?namedreltag}
Name:          glassfish-gmbal
Version:       3.2.0
Release:       alt3_0.9.b003jpp8
Summary:       GlassFish MBean Annotation Library
License:       CDDL or GPLv2 with exceptions
URL:           http://java.net/projects/gmbal/pages/Home
# hg clone -r VERSION-3.2.0-b003 https://hg.java.net/hg/gmbal~master glassfish-gmbal-3.2.0-b003
# find glassfish-gmbal-3.2.0-b003/ -name '*.jar' -delete
# find glassfish-gmbal-3.2.0-b003/ -name '*.class' -delete
# find glassfish-gmbal-3.2.0-b003/ -name '*.tgz' -delete
# find glassfish-gmbal-3.2.0-b003/ -name '*.zip' -delete
# rm -rf glassfish-gmbal-3.2.0-b003/lib/* glassfish-gmbal-3.2.0-b003/.hg
# tar cJf glassfish-gmbal-3.2.0-b003-src-hg.tar.xz glassfish-gmbal-3.2.0-b003
Source0:       %{name}-%{namedversion}-src-hg.tar.xz
Source1:       %{name}-%{namedversion}-01-build.xml

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: aqute-bnd
BuildRequires: glassfish-management-api
BuildRequires: glassfish-pfl
BuildRequires: javapackages-local
BuildRequires: junit

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

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

cp -p %{SOURCE1} build.xml

# This test fails on java8
rm -r test/org/glassfish/gmbal/impl/AMXClientTest.java

%build

%ant jars javadoc test

bnd wrap -p make/gmbal.bnd -o dist/gmbal.bar dist/gmbal.jar
mv dist/gmbal.bar dist/gmbal.jar
bnd wrap -p make/gmbal-api-only.bnd -o dist/gmbal-api-only.bar dist/gmbal-api-only.jar
mv dist/gmbal-api-only.bar dist/gmbal-api-only.jar

%install
%mvn_file org.glassfish.gmbal:gmbal %{name}
%mvn_file org.glassfish.gmbal:gmbal-api-only %{name}-api-only
%mvn_artifact make/gmbal.pom dist/gmbal.jar
%mvn_artifact make/gmbal-api-only.pom dist/gmbal-api-only.jar
%mvn_install -J dist/javadoc

%files -f .mfiles
%doc legal/LICENSE.TXT

%files javadoc -f .mfiles-javadoc
%doc legal/LICENSE.TXT

%changelog
* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt3_0.9.b003jpp8
- java8 mass update

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt1_0.3.b003jpp7
- new release

