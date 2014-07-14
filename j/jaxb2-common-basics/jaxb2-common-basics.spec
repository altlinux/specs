BuildRequires: /proc
BuildRequires: jpackage-compat

Name:          jaxb2-common-basics
Version:       0.6.3
Release:       alt2_4jpp7
Summary:       JAXB2 Basics
Group:         Development/Java
License:       BSD
Url:           http://java.net/projects/jaxb2-commons/pages/Home
# svn export https://svn.java.net/svn/jaxb2-commons~svn/basics/tags/0.6.3 jaxb2-common-basics-0.6.3
# tar czf jaxb2-common-basics-0.6.3-src-svn.tar.gz jaxb2-common-basics-0.6.3
Source0:       jaxb2-common-basics-0.6.3-src-svn.tar.gz
# from http://confluence.highsource.org/display/J2B/License
# jaxb2-common-basics package don't include the license file
# but jaxb2-commons developers allowed us to redistribute their
# work only if we include this notice. So we HAVE TO include these notices.
Source1:       jaxb2-common-basics-LICENSE


# remove 
#    org.springframework spring 2.0.7
#   test deps
#    org.jvnet.jaxb2.maven2 maven-jaxb2-plugin-testing
#    com.vividsolutions jts 1.8
# change
#    groupId ant in org.apache.ant
#    artifactId ant-optional in ant
#    version 1.5.3-1 in 1.8.2
Patch0:        jaxb2-common-basics-0.6.3-fixbuild.patch
# todo BR/R org.springframework spring-beans spring-context-support 2.5.6
#atch1:        jaxb2-common-basics-0.6.2-spring2.patch

BuildRequires: jpackage-utils
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

BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-jaxb2-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin

Requires:      annox
Requires:      ant
Requires:      apache-commons-beanutils
Requires:      apache-commons-io
Requires:      apache-commons-lang
Requires:      apache-commons-logging
Requires:      glassfish-jaxb
Requires:      glassfish-jaxb-api
Requires:      xmlunit

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
JAXB2 Basics is a part of JAXB2 Commons project which
implements plugins and tools for JAXB 2.x reference
implementation.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jaxb2-common-basics-%{version}
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


%build

mvn-rpmbuild install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}/%{name}
install -pm 644 annotate/target/jaxb2-basics-annotate-%{version}.jar %{buildroot}%{_javadir}/%{name}/jaxb2-basics-annotate.jar
install -pm 644 ant/target/jaxb2-basics-ant-%{version}.jar %{buildroot}%{_javadir}/%{name}/jaxb2-basics-ant.jar
install -pm 644 basic/target/jaxb2-basics-%{version}.jar %{buildroot}%{_javadir}/%{name}/jaxb2-basics.jar
install -pm 644 runtime/target/jaxb2-basics-runtime-%{version}.jar %{buildroot}%{_javadir}/%{name}/jaxb2-basics-runtime.jar
install -pm 644 testing/target/jaxb2-basics-testing-%{version}.jar %{buildroot}%{_javadir}/%{name}/jaxb2-basics-testing.jar
install -pm 644 tools/target/jaxb2-basics-tools-%{version}.jar %{buildroot}%{_javadir}/%{name}/jaxb2-basics-tools.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxb2-basics-project.pom
%add_maven_depmap JPP.%{name}-jaxb2-basics-project.pom
install -pm 644 annotate/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxb2-basics-annotate.pom
%add_maven_depmap JPP.%{name}-jaxb2-basics-annotate.pom %{name}/jaxb2-basics-annotate.jar
install -pm 644 ant/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxb2-basics-ant.pom
%add_maven_depmap JPP.%{name}-jaxb2-basics-ant.pom %{name}/jaxb2-basics-ant.jar
install -pm 644 basic/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxb2-basics.pom
%add_maven_depmap JPP.%{name}-jaxb2-basics.pom %{name}/jaxb2-basics.jar
install -pm 644 runtime/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxb2-basics-runtime.pom
%add_maven_depmap JPP.%{name}-jaxb2-basics-runtime.pom %{name}/jaxb2-basics-runtime.jar
install -pm 644 testing/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxb2-basics-testing.pom
%add_maven_depmap JPP.%{name}-jaxb2-basics-testing.pom %{name}/jaxb2-basics-testing.jar
install -pm 644 tools/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxb2-basics-tools.pom
%add_maven_depmap JPP.%{name}-jaxb2-basics-tools.pom %{name}/jaxb2-basics-tools.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}/jaxb2-basics.jar
%{_javadir}/%{name}/jaxb2-basics-annotate.jar
%{_javadir}/%{name}/jaxb2-basics-ant.jar
%{_javadir}/%{name}/jaxb2-basics-runtime.jar
%{_javadir}/%{name}/jaxb2-basics-testing.jar
%{_javadir}/%{name}/jaxb2-basics-tools.jar
%{_mavenpomdir}/JPP.%{name}-jaxb2-basics*.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt1_4jpp7
- new version

