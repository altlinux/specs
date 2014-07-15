Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: rngom
Version: 201103
Release: alt2_0.5.20120119svnjpp7
Summary: Java library for parsing RELAX NG grammars
Group: Development/Java
License: MIT
URL: https://rngom.dev.java.net

# svn export -r 70 https://svn.java.net/svn/rngom~svn/trunk/rngom rngom-201103
# find rngom-201103/ -name '*.class' -delete
# find rngom-201103/ -name '*.jar' -delete
# tar czf rngom-201103.tar.gz rngom-201103
Source0: %{name}-%{version}.tar.gz
Patch0: %{name}-%{version}-pom.patch

BuildRequires: bsf
BuildRequires: bsh
BuildRequires: stax2-api
BuildRequires: javacc
BuildRequires: javacc-maven-plugin
BuildRequires: jpackage-utils
BuildRequires: junit4
BuildRequires: maven
BuildRequires: maven-clean-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: msv-xsdlib
BuildRequires: relaxngDatatype
BuildRequires: sonatype-oss-parent
BuildRequires: xmlunit

Requires: stax2-api
Requires: jpackage-utils
Requires: msv-xsdlib
Requires: relaxngDatatype

BuildArch: noarch
Source44: import.info


%description
RNGOM is an open-source Java library for parsing RELAX NG grammars.

In particular, RNGOM can:
* parse the XML syntax
* parse the compact syntax
* check all the semantic restrictions as specified in the specification
* parse RELAX NG into application-defined data structures
* build a default data structure based around the binarized simple syntax or
  another data structure that preserves more of the parsed information
* parse foreign elements/attributes in a schema
* parse comments in a schema


%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q
%patch0 -p1


%build
mvn-rpmbuild install javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
cp -p target/rngom-%{version}-SNAPSHOT.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
cp -p pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/.

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*


%files javadoc
%{_javadocdir}/*


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:201103-alt2_0.5.20120119svnjpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:201103-alt1_0.5.20120119svnjpp7
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt3_0.20061207.1jpp5
- fixes for java6 support

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt2_0.20061207.1jpp5
- fixed docdir ownership

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_0.20061207.1jpp5
- converted from JPackage by jppimport script

