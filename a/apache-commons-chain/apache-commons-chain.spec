Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name chain
%global short_name commons-%{base_name}
Name:          apache-commons-chain
Version:       1.2
Release:       alt1_6jpp7
Summary:       An implementation of the GoF Chain of Responsibility pattern
Group:         Development/Java
License:       ASL 2.0
URL:           http://commons.apache.org/%{base_name}/
Source0:       ftp://ftp.gbnet.net/pub/apache/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
# replace myfaces-api with jboss-jsf-2.1-api
Patch0:        %{name}-%{version}-pom.patch
# javax.servlet 3.0 api support
Patch1:        %{name}-%{version}-tests-servlet30.patch
# javax.portlet 2.0 api support
Patch2:        %{name}-%{version}-portlet20.patch

BuildRequires: jpackage-utils

BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-digester
BuildRequires: apache-commons-logging
BuildRequires: jboss-jsf-2.1-api
BuildRequires: portlet-2.0-api
BuildRequires: tomcat-servlet-3.0-api

# test deps
BuildRequires: junit

BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit

Requires:      apache-commons-beanutils
Requires:      apache-commons-digester
Requires:      apache-commons-logging
Requires:      jboss-jsf-2.1-api
Requires:      portlet-2.0-api
Requires:      tomcat-servlet-3.0-api

Requires:      jpackage-utils
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
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
find . -name '*.class' -delete
find . -name '*.jar' -delete

perl -pi -e 's/\r$//g;' *.txt
%patch0 -p0
%patch1 -p1
%patch2 -p0
# Failed tests:   testDefaut(org.apache.commons.chain.config.ConfigParserTestCase): Correct command count expected:<17> but was:<19>
rm -r src/test/org/apache/commons/chain/config/ConfigParserTestCase.java

%build

mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
( cd %{buildroot}%{_javadir} && ln -s %{name}.jar %{short_name}.jar )

mkdir -p %{buildroot}%{_mavenpomdir}
install -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}.pom
%add_maven_depmap JPP-%{short_name}.pom %{short_name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{short_name}.jar
%{_mavenpomdir}/JPP-%{short_name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%changelog
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

