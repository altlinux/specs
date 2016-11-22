Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name: rngom
Version: 201103
Release: alt2_0.13.20120119svnjpp8
Summary: Java library for parsing RELAX NG grammars
License: MIT
URL: https://java.net/projects/rngom

# svn export -r 70 https://svn.java.net/svn/rngom~svn/trunk/rngom rngom-201103
# find rngom-201103/ -name '*.class' -delete
# find rngom-201103/ -name '*.jar' -delete
# tar czf rngom-201103.tar.gz rngom-201103
Source0: %{name}-%{version}.tar.gz
Patch0: %{name}-%{version}-pom.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.sun.msv.datatype.xsd:xsdlib)
BuildRequires:  mvn(javax.xml.stream:stax-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(relaxngDatatype:relaxngDatatype)
BuildRequires:  mvn(xmlunit:xmlunit)

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
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc licenceheader.txt

%files javadoc -f .mfiles-javadoc
%doc licenceheader.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:201103-alt2_0.13.20120119svnjpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:201103-alt2_0.12.20120119svnjpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:201103-alt2_0.8.20120119svnjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:201103-alt2_0.7.20120119svnjpp7
- new release

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

