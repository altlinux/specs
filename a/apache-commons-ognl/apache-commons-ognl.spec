Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global short_name commons-ognl

Name:          apache-%{short_name}
Version:       3.0.2
Release:       alt2_11.20120313svn1102435jpp8
Summary:       Object Graph Navigation Library 
License:       ASL 2.0
URL:           http://commons.apache.org/ognl/
# svn export -r1102435 http://svn.apache.org/repos/asf/commons/proper/ognl/trunk/ apache-commons-ognl-3.0.2
# tar caf apache-commons-ognl-3.0.2.tar.xz apache-commons-ognl-3.0.2
Source0:       %{name}-%{version}.tar.xz
BuildArch:     noarch

BuildRequires: jna
BuildRequires: maven-local
BuildRequires: mvn(javassist:javassist)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.commons:commons-parent:pom:)
BuildRequires: mvn(org.easymock:easymock)
Source44: import.info

%description
OGNL is an expression language for getting and setting properties of
Java objects, plus other extras such as list projection and selection
and lambda expressions.

%package javadoc
Group: Development/Java
Summary:      API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%pom_remove_plugin com.mycila.maven-license-plugin:maven-license-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-clean-plugin

rm -r src/test/java/org/apache/commons/ognl/test/ArithmeticAndLogicalOperatorsTest.java \
  src/test/java/org/apache/commons/ognl/test/ArrayElementsTest.java \
  src/test/java/org/apache/commons/ognl/test/ASTPropertyTest.java \
  src/test/java/org/apache/commons/ognl/test/CollectionDirectPropertyTest.java \
  src/test/java/org/apache/commons/ognl/test/ConstantTest.java \
  src/test/java/org/apache/commons/ognl/test/MethodTest.java \
  src/test/java/org/apache/commons/ognl/test/PropertyArithmeticAndLogicalOperatorsTest.java \
  src/test/java/org/apache/commons/ognl/test/PropertyTest.java \
  src/test/java/org/apache/commons/ognl/test/enhance/TestExpressionCompiler.java

%mvn_file :%{short_name} %{short_name} %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_11.20120313svn1102435jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_10.20120313svn1102435jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_6.20120313svn1102435jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_4.20120313svn1102435jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_2.20120313svn1102435jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1_2.20120313svn1102435jpp7
- new version

