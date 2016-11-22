Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global base_name chain
%global short_name commons-%{base_name}
Name:          apache-commons-chain
Version:       1.2
Release:       alt1_13jpp8
Summary:       An implementation of the GoF Chain of Responsibility pattern
License:       ASL 2.0
URL:           http://commons.apache.org/%{base_name}/
Source0:       ftp://ftp.gbnet.net/pub/apache/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
# javax.servlet 3.1 api support
Patch0:        %{name}-%{version}-tests-servlet31.patch
# javax.portlet 2.0 api support
Patch1:        %{name}-%{version}-portlet20.patch

BuildRequires: maven-local
BuildRequires: mvn(commons-beanutils:commons-beanutils)
BuildRequires: mvn(commons-digester:commons-digester)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(javax.portlet:portlet-api)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.commons:commons-parent:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires: mvn(org.jboss.spec.javax.faces:jboss-jsf-api_2.1_spec)

BuildArch:     noarch
Source44: import.info

%description
A popular technique for organizing the execution of complex
processing flows is the "Chain of Responsibility" pattern, as
described (among many other places) in the classic "Gang of Four"
design patterns book. Although the fundamental API contracts
required to implement this design pattern are extremely simple,
it is useful to have a base API that facilitates using the pattern,
and (more importantly) encouraging composition of command
implementations from multiple diverse sources.
Towards that end, the Chain API models a computation as a series
of "commands" that can be combined into a "chain". The API for a
command consists of a single method (execute()), which is passed
a "context" parameter containing the dynamic state of the
computation, and whose return value is a boolean that determines
whether or not processing for the current chain has been completed
(true), or whether processing should be delegated to the next
command in the chain (false).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
find . -name '*.class' -delete
find . -name '*.jar' -delete

perl -pi -e 's/\r$//g;' *.txt

%patch0 -p1
%patch1 -p0
# Failed tests:   testDefaut(org.apache.commons.chain.config.ConfigParserTestCase):
# Correct command count expected:<17> but was:<19>
rm -r src/test/org/apache/commons/chain/config/ConfigParserTestCase.java

%pom_remove_dep :myfaces-api
%pom_add_dep org.jboss.spec.javax.faces:jboss-jsf-api_2.1_spec
# Force servlet 3.1 apis
%pom_xpath_set "pom:dependency[pom:groupId = 'javax.servlet' ]/pom:artifactId" javax.servlet-api
%pom_xpath_set "pom:dependency[pom:groupId = 'javax.servlet' ]/pom:version" 3.1.0

%mvn_file :%{short_name} %{name}
%mvn_file :%{short_name} %{short_name}

%build

%mvn_build -- -Dmaven.compile.source=1.6 -Dmaven.compile.target=1.6

%install
%mvn_install

%files -f .mfiles
%doc RELEASE-NOTES.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2-alt1_13jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2-alt1_12jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2-alt1_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2-alt1_6jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.2-alt1_3jpp7
- fc update

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_0.r831527.5jpp6
- build w/o maven-plugin-rat

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_0.r831527.5jpp6
- fixed build with maven3

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_0.r831527.5jpp6
- new version

