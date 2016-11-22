Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jra
%define version 1.0
%global namedreltag -alpha-4
%global namedversion %{version}%{?namedreltag}

Name:          jra
Version:       1.0
Release:       alt2_0.11.alpha4jpp8
Summary:       Java REST Annotations
License:       ASL 2.0
Group:         Development/Other
URL:           http://jra.codehaus.org/

# svn export https://svn.codehaus.org/jra/branches/jra-1.0-alpha-4/ jra-1.0-alpha-4
# tar cafJ jra-1.0-alpha-4.tar.xz jra-1.0-alpha-4

Source0:       %{name}-%{namedversion}.tar.xz

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
Source44: import.info

%description
The Java REST annotations are annotations to help service creators build REST
style services. Frameworks which wish to support REST can reuse these
annotations just like the JSR181 & JAX-WS annotations are used across
implementations. However, the idea with JRA is that many different frameworks
(web, XML/SOAP, etc) may want to expose REST style services.

%package javadoc
Summary:       Javadocs for %{name}
Group:         Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_xpath_remove pom:build/pom:extensions

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc src/main/resources/META-INF/LICENSE

%files javadoc -f .mfiles-javadoc
%doc src/main/resources/META-INF/LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.11.alpha4jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.10.alpha4jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.6.alpha4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.5.alpha4jpp7
- new release

* Fri Mar 15 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.2.alpha4jpp7
- fc update

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a4.1jpp5
- new version

