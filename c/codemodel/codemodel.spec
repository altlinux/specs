BuildRequires: /proc
BuildRequires: jpackage-compat
Name: codemodel
Version: 2.6
Release: alt1_4jpp7
Summary: Java library for code generators
Group: Development/Java
License: CDDL and GPLv2
URL: http://codemodel.java.net

# svn export https://svn.java.net/svn/codemodel~svn/tags/codemodel-project-2.6/ codemodel-2.6
# tar -zcvf codemodel-2.6.tar.gz codemodel-2.6
Source0: %{name}-%{version}.tar.gz

# Remove the dependency on istack-commons (otherwise it will be a
# recursive dependency with the upcoming changes to that package):
Patch0: %{name}-remove-istack-commons-dependency.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: jvnet-parent

Requires: jpackage-utils
Requires: jvnet-parent
Source44: import.info


%description
CodeModel is a Java library for code generators; it provides a way to
generate Java programs in a way much nicer than PrintStream.println().
This project is a spin-off from the JAXB RI for its schema compiler
to generate Java source files.


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.


%prep

# Unpack and patch the original source:
%setup -q
%patch0 -p1

# Remove bundled jar files:
find . -name '*.jar' -print -delete


%build
mvn-rpmbuild \
  -Dproject.build.sourceEncoding=UTF-8 \
  install \
  javadoc:aggregate


%install
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}

# JAR
cp -p codemodel/target/codemodel-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
cp -p codemodel-annotation-compiler/target/codemodel-annotation-compiler-%{version}.jar %{buildroot}%{_javadir}/%{name}-annotation-compiler.jar

# JAVADOC
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# POM
cp -p pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-project.pom
cp -p codemodel/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
cp -p codemodel-annotation-compiler/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-annotation-compiler.pom

# DEPMAP
%add_maven_depmap JPP-%{name}-project.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap JPP-%{name}-annotation-compiler.pom %{name}-annotation-compiler.jar


%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc LICENSE.html


%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.html


%changelog
* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_4jpp7
- new version

