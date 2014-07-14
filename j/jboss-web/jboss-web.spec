BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-web
%define version 7.0.13
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-web
Version:          7.0.13
Release:          alt2_5jpp7
Summary:          JBoss Web
Group:            Development/Java
License:          LGPLv2+ and ASL 2.0 and MIT and (LGPLv2+ or ASL 2.0)
URL:              http://www.jboss.org/jbossweb

# svn export http://anonsvn.jboss.org/repos/jbossweb/tags/JBOSSWEB_7_0_13_FINAL/ jboss-web-7.0.13.Final
# rm -rf jboss-web-7.0.13.Final/java/javax
# tar cafJ jboss-web-7.0.13.Final.tar.xz jboss-web-7.0.13.Final
Source0:          %{name}-%{namedversion}.tar.xz
Source1:          %{name}-%{namedversion}-pom.xml
Source2:          build-javadoc.xml

Patch0:           %{name}-%{namedversion}-build.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    jboss-annotations-1.1-api
BuildRequires:    jboss-el-2.2-api
BuildRequires:    jboss-jsp-2.2-api
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    ant
BuildRequires:    junit4
BuildRequires:    ecj

Requires:         jpackage-utils
Requires:         jboss-annotations-1.1-api
Requires:         jboss-el-2.2-api
Requires:         jboss-jsp-2.2-api
Requires:         jboss-servlet-3.0-api
Source44: import.info

%description
JBoss Web Server is an enterprise ready web server based on Tomcat.

%package doc
Summary:          User guide for %{name}
Group:            Development/Java

%description doc
This package contains user guide for %{name}.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
cp %{SOURCE2} .
ln -s $(build-classpath jboss-annotations-1.1-api) lib
ln -s $(build-classpath jboss-el-2.2-api) lib
ln -s $(build-classpath jboss-jsp-2.2-api) lib
ln -s $(build-classpath jboss-servlet-3.0-api) lib

%patch0 -p1

%build
export CLASSPATH=$(build-classpath ecj)
ant
ant -f build-javadoc.xml

%install
# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 output/jars/jbossweb.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom


# APIDOCS
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc LICENSE

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%files doc
%doc LICENSE
%doc output/build/webapps/docs/*

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 7.0.13-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 7.0.13-alt1_5jpp7
- new version

