# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global bootstrap 0

Name:           maven-javadoc-plugin
Version:        2.9.1
Release:        alt1_1.1jpp7
Summary:        Maven Javadoc Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-javadoc-plugin
Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         reduce-exceptions.patch

BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang
BuildRequires:  apache-commons-logging
BuildRequires:  httpcomponents-client
BuildRequires:  log4j
BuildRequires:  maven-local
BuildRequires:  maven-archiver
BuildRequires:  maven-artifact
BuildRequires:  maven-artifact-manager
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-common-artifact-filters
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-doxia
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-model
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-plugin-testing-harness
BuildRequires:  maven-project
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-settings
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-shared-invoker
BuildRequires:  maven-shared-reporting-api
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-toolchain
BuildRequires:  maven-wagon
BuildRequires:  modello
BuildRequires:  plexus-archiver
BuildRequires:  plexus-containers-container-default
BuildRequires:  plexus-interactivity
BuildRequires:  plexus-utils
BuildRequires:  qdox
%if ! %{bootstrap}
BuildRequires:  maven-javadoc-plugin
%endif        

Requires:       apache-commons-io
Requires:       apache-commons-lang
Requires:       apache-commons-logging
Requires:       httpcomponents-client
Requires:       log4j
Requires:       maven
Requires:       maven-archiver
Requires:       maven-artifact
Requires:       maven-artifact-manager
Requires:       maven-common-artifact-filters
Requires:       maven-doxia
Requires:       maven-doxia-sitetools
Requires:       maven-model
Requires:       maven-plugin-annotations
Requires:       maven-project
Requires:       maven-settings
Requires:       maven-shared-invoker
Requires:       maven-shared-reporting-api
Requires:       maven-toolchain
Requires:       maven-wagon
Requires:       plexus-archiver
Requires:       plexus-containers-container-default
Requires:       plexus-interactivity
Requires:       plexus-utils
Requires:       qdox

BuildArch: noarch

Obsoletes: maven2-plugin-javadoc <= 2.0.8
Provides:  maven2-plugin-javadoc = %{version}-%{release}
Source44: import.info

%description
The Maven Javadoc Plugin is a plugin that uses the javadoc tool for
generating javadocs for the specified project.
 
%if ! %{bootstrap}
%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.
%endif

%prep
%setup -q 
# Update source for use with newer doxia
%patch0

# Remove test dependencies because tests are skipped anyways.
%pom_xpath_remove "pom:dependency[pom:scope[text()='test']]"

%pom_add_dep org.codehaus.plexus:plexus-interactivity-api pom.xml "
<exclusions>
    <exclusion>
        <groupId>org.codehaus.plexus</groupId>
        <artifactId>plexus-component-api</artifactId>
    </exclusion>
</exclusions>"

sed -i -e "s|org.apache.maven.doxia.module.xhtml.decoration.render|org.apache.maven.doxia.sink.render|g" src/main/java/org/apache/maven/plugin/javadoc/JavadocReport.java

%build
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        install
%if ! %{bootstrap}
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        -Dproject.build.sourceEncoding=UTF-8 \
       javadoc:javadoc
%endif        

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%if ! %{bootstrap}
# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/
rm -rf target/site/api*
%endif

%files -f .mfiles
%doc LICENSE NOTICE 

%if ! %{bootstrap}
%files javadoc
%doc LICENSE NOTICE 
%{_javadocdir}/%{name}
%endif

%changelog
* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt1_1.1jpp7
- update

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt2_2jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_2jpp7
- new fc release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_1jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

