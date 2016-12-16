Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-javadoc-plugin
Version:        2.10.4
Release:        alt1_1jpp8
Summary:        Maven Javadoc Plugin
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-javadoc-plugin
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:         reduce-exceptions.patch
Patch1:         doxia-sitetools-1.6.patch

BuildRequires:  maven-local
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang
BuildRequires:  apache-commons-logging
BuildRequires:  httpcomponents-client
BuildRequires:  log4j
BuildRequires:  maven
BuildRequires:  maven-archiver
BuildRequires:  maven-common-artifact-filters
BuildRequires:  maven-doxia-sink-api
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-invoker
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-plugins-pom
BuildRequires:  maven-reporting-api
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-wagon-provider-api
BuildRequires:  modello
BuildRequires:  plexus-archiver
BuildRequires:  plexus-containers-container-default
BuildRequires:  plexus-interactivity-api
BuildRequires:  plexus-utils
BuildRequires:  qdox
Source44: import.info

%description
The Maven Javadoc Plugin is a plugin that uses the javadoc tool for
generating javadocs for the specified project.
 
%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q 
%patch0
%patch1

# Remove test dependencies because tests are skipped anyways.
%pom_xpath_remove "pom:dependency[pom:scope[text()='test']]"

%pom_add_dep org.codehaus.plexus:plexus-interactivity-api pom.xml "
<exclusions>
    <exclusion>
        <groupId>org.codehaus.plexus</groupId>
        <artifactId>plexus-component-api</artifactId>
    </exclusion>
</exclusions>"

# Don't use maven2 modules
%pom_remove_dep :maven-project
%pom_remove_dep :maven-artifact-manager
%pom_remove_dep :maven-toolchain

sed -i -e "s|org.apache.maven.doxia.module.xhtml.decoration.render|org.apache.maven.doxia.siterenderer|g" src/main/java/org/apache/maven/plugin/javadoc/JavadocReport.java

# XXX remove javadoc:fix MOJO for now
# TODO: port to QDox 2.0
rm -f src/main/java/org/apache/maven/plugin/javadoc/*FixJavadocMojo.java
%pom_remove_dep :qdox

%build
%mvn_build -f -- -DmavenVersion=3.1.1

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE 

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE 

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.3-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.3-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt1_2jpp7
- new release

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

