Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          jaxb2-common-basics
Version:       0.6.3
Release:       alt2_12jpp8
Summary:       JAXB2 Basics
License:       BSD
Url:           http://java.net/projects/jaxb2-commons/pages/Home
# svn export https://svn.java.net/svn/jaxb2-commons~svn/basics/tags/0.6.3 jaxb2-common-basics-0.6.3
# tar czf jaxb2-common-basics-0.6.3-src-svn.tar.gz jaxb2-common-basics-0.6.3
Source0:       %{name}-%{version}-src-svn.tar.gz
# from http://confluence.highsource.org/display/J2B/License
# jaxb2-common-basics package don't include the license file
# but jaxb2-commons developers allowed us to redistribute their
# work only if we include this notice. So we HAVE TO include these notices.
Source1:       %{name}-LICENSE
# remove 
#    org.springframework spring 2.0.7
#   test deps
#    org.jvnet.jaxb2.maven2 maven-jaxb2-plugin-testing
#    com.vividsolutions jts 1.8
# change
#    groupId ant in org.apache.ant
#    artifactId ant-optional in ant
#    version 1.5.3-1 in 1.8.2
Patch0:        %{name}-0.6.3-fixbuild.patch
# todo BR/R org.springframework spring-beans spring-context-support 2.5.6
#atch1:        jaxb2-common-basics-0.6.2-spring2.patch

BuildRequires: sonatype-oss-parent

BuildRequires: annox
BuildRequires: ant
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: glassfish-jaxb
BuildRequires: junit
BuildRequires: xmlunit

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-jaxb2-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin

BuildArch:     noarch
Source44: import.info

%description
JAXB2 Basics is a part of JAXB2 Commons project which
implements plugins and tools for JAXB 2.x reference
implementation.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
find \( -name '*.jar' -o -name '*.class' -o -name '*.bat' \) -exec rm -f '{}' \;

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

%patch0 -p1
# require jts 1.8
rm -rf runtime/src/test/java/org/jvnet/jaxb2_commons/lang/tests/CopyStrategyTest.java
# require maven-jaxb2-plugin-testing
rm -rf basic/src/test/*
rm -rf annotate/src/test/java/org/jvnet/jaxb2_commons/plugin/annotate/tests/*
# require spring framework
rm -rf tools/src/main/java/org/jvnet/jaxb2_commons/plugin/spring/*

sed -i "s|com.sun.tools.xjc.outline.Aspect|com.sun.tools.xjc.model.Aspect|" \
 tools/src/main/java/org/jvnet/jaxb2_commons/xjc/model/concrete/XJCCMInfoFactory.java

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt2_12jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt1_4jpp7
- new version

