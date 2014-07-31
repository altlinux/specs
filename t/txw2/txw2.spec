# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: txw2
Version: 20110809
Release: alt2_7jpp7
Summary: Typed XML writer for Java
Group: Development/Java
License: CDDL and GPLv2 with exceptions
URL: https://txw.dev.java.net

# svn export https://svn.java.net/svn/jaxb~version2/tags/txw2-project-20110809/ txw2-20110809
# tar -zcvf txw2-20110809.tar.gz txw2-20110809
Source0: %{name}-%{version}.tar.gz

# Remove the reference to the parent net.java:jvnet-parent, as no package
# contains that artifact:
Patch0: %{name}-%{version}-pom.patch

# Update to use the version of args4j available in the distribution:
Patch1: %{name}-%{version}-args4j.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local

BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-shared
BuildRequires: args4j
BuildRequires: xsom
BuildRequires: rngom
BuildRequires: codemodel

Requires: jpackage-utils
Requires: args4j
Requires: xsom
Requires: rngom
Requires: codemodel
Source44: import.info


%description
Typed XML writer for Java.


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1


%build
mvn-rpmbuild \
  -Dproject.build.sourceEncoding=UTF-8 \
  install \
  javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
cp -p runtime/target/txw2-%{version}.jar %{buildroot}%{_javadir}/txw2.jar
cp -p compiler/target/txwc2-%{version}.jar %{buildroot}%{_javadir}/txwc2.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
cp -p pom.xml %{buildroot}%{_mavenpomdir}/JPP-txw2-project.pom
cp -p runtime/pom.xml %{buildroot}%{_mavenpomdir}/JPP-txw2.pom
cp -p compiler/pom.xml %{buildroot}%{_mavenpomdir}/JPP-txwc2.pom

# Dependencies map:
%add_maven_depmap JPP-txw2-project.pom
%add_maven_depmap JPP-txw2.pom txw2.jar
%add_maven_depmap JPP-txwc2.pom txwc2.jar

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc license.txt


%files javadoc
%{_javadocdir}/%{name}
%doc license.txt


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 20110809-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 20110809-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 20110809-alt1_4jpp7
- new version

