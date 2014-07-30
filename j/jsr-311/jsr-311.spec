# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: jsr-311
Version: 1.1.1
Release: alt2_4jpp7
Summary: JAX-RS: Java API for RESTful Web Services
Group: Development/Java
License: CDDL
Url: http://jsr311.java.net

# svn export https://svn.java.net/svn/jsr311~svn/tags/jsr311-api-1.1.1 jsr-311-1.1.1
# tar cvzf jsr-311-1.1.1.tgz jsr-311-1.1.1
Source0: %{name}-%{version}.tgz

# Patch the POM:
Patch0: %{name}-pom.patch

BuildRequires: jpackage-utils

BuildRequires: buildnumber-maven-plugin
BuildRequires: junit
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin

Requires: jpackage-utils

BuildArch: noarch
Source44: import.info


%description
JAX-RS: Java API for RESTful Web Services


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q
%patch0


%build
mvn-rpmbuild \
  -Dproject.build.sourceEncoding=UTF-8 \
  install \
  javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 target/jsr311-api-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/.

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%{_javadir}/*.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*


%files javadoc
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_2jpp7
- new version

