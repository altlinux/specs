Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-web
%define version 8.0.0
%global namedreltag .Alpha1
%global namedversion %{version}%{?namedreltag}

Name:             jboss-web
Version:          8.0.0
Release:          alt1_0.6.Alpha1jpp8
Summary:          JBoss Web
License:          LGPLv2+ and ASL 2.0 and MIT and (LGPLv2+ or ASL 2.0)
URL:              http://www.jboss.org/jbossweb

# svn export http://anonsvn.jboss.org/repos/jbossweb/tags/JBOSSWEB_8_0_0_ALPHA1/ jboss-web-8.0.0.Alpha1
# rm -rf jboss-web-8.0.0.Alpha1/java/javax
# tar cafJ jboss-web-8.0.0.Alpha1.tar.xz jboss-web-8.0.0.Alpha1
Source0:          jboss-web-%{namedversion}.tar.xz

# Support for the Beta1 Servlet API
Patch0:           servlet-beta1-changes.patch

BuildArch:        noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    jboss-annotations-1.1-api
BuildRequires:    jboss-el-2.2-api
BuildRequires:    jboss-jsp-2.2-api
BuildRequires:    jboss-servlet-3.1-api
BuildRequires:    ant
BuildRequires:    junit
BuildRequires:    ecj
BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools
BuildRequires:    jboss-logmanager
BuildRequires:    maven-local
BuildRequires:    maven-injection-plugin
BuildRequires:    glassfish-el
Source44: import.info

%description
JBoss Web Server is an enterprise ready web server based on Tomcat.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-web-%{namedversion}

%patch0 -p1

%pom_remove_dep "org.glassfish:javax.el"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_jnidir}/%{name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 8.0.0-alt1_0.6.Alpha1jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 8.0.0-alt1_0.5.Alpha1jpp8
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 7.0.13-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 7.0.13-alt1_5jpp7
- new version

