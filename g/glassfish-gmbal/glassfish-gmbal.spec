Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name glassfish-gmbal
%define version 3.2.0
%global namedreltag -b003
%global namedversion %{version}%{?namedreltag}
Name:          glassfish-gmbal
Version:       3.2.0
Release:       alt1_0.3.b003jpp7
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

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: aqute-bnd
BuildRequires: junit

BuildRequires: glassfish-management-api
BuildRequires: glassfish-pfl

Requires:      glassfish-management-api
Requires:      glassfish-pfl

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

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

cp -p %{SOURCE1} build.xml

%build

%ant osgi javadoc test

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 dist/bundles/gmbal.jar  %{buildroot}%{_javadir}/%{name}.jar
install -m 644 dist/bundles/gmbal-api-only.jar  %{buildroot}%{_javadir}/%{name}-api-only.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 make/gmbal.pom %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
install -pm 644 make/gmbal-api-only.pom %{buildroot}%{_mavenpomdir}/JPP-%{name}-api-only.pom
%add_maven_depmap JPP-%{name}-api-only.pom %{name}-api-only.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}*.jar
%{_mavenpomdir}/JPP-%{name}*.pom
%{_mavendepmapfragdir}/%{name}
%doc legal/LICENSE.TXT

%files javadoc
%{_javadocdir}/%{name}
%doc legal/LICENSE.TXT

%changelog
* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt1_0.3.b003jpp7
- new release

