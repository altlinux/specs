Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          jsr-311
Version:       1.1.1
Release:       alt2_7jpp7
Summary:       JAX-RS: Java API for RESTful Web Services
License:       CDDL
URL:           http://jsr311.java.net
# svn export https://svn.java.net/svn/jsr311~svn/tags/jsr311-api-1.1.1 jsr-311-1.1.1
# tar cvzf jsr-311-1.1.1.tgz jsr-311-1.1.1
Source0:       %{name}-%{version}.tgz
# Patch the POM:
Patch0:        %{name}-pom.patch


BuildRequires: buildnumber-maven-plugin
BuildRequires: junit
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin

BuildArch:     noarch

Provides:      javax.ws.rs
Source44: import.info

%description
JAX-RS: Java API for RESTful Web Services

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0

%build

%mvn_file :jsr311-api %{name} javax.ws.rs/%{name}
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/javax.ws.rs/

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_2jpp7
- new version

