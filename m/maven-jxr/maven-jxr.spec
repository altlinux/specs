Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-jxr
Version:        2.5
Release:        alt1_4jpp8
Epoch:          0
Summary:        Source cross referencing tool
# BSD: maven-jxr/src/main/java/org/apache/maven/jxr/JavaCodeTransform.java
License:        ASL 2.0 and BSD
URL:            http://maven.apache.org/doxia/

Source0:        http://repo2.maven.org/maven2/org/apache/maven/jxr/jxr/%{version}/jxr-%{version}-source-release.zip
# taken from maven-jxr/src/main/java/org/apache/maven/jxr/JavaCodeTransform.java
Source1:        LICENSE-BSD

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven:maven-model:2.2.1)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(oro:oro)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xml-apis:xml-apis)
Source44: import.info

%description
Maven JXR is a source cross referencing tool.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package -n maven-plugin-jxr
Group: Development/Java
Summary:        Maven plugin for JXR
Requires:       %{name} = %{version}

%description -n maven-plugin-jxr
Maven plugin for JXR.

%prep
%setup -q -n jxr-%{version}

cp %{SOURCE1} .

# Missing dependency
%pom_add_dep oro:oro maven-jxr

%mvn_package :maven-jxr-plugin maven-plugin-jxr

# maven-core has scope "provided" in Plugin Testing Harness, so we
# need to provide it or tests will fail to compile.  This works for
# upstream because upstream uses a different version of Plugin Testing
# Harness in which scope of maven-core dependency is "compile".
%pom_add_dep org.apache.maven:maven-core::test

%build
# The test failures seem to have something to do with:
# https://issues.apache.org/jira/browse/MCHANGES-88
# We can investigate when we upgrade to 2.2.x to see if they still occur.
# Update: Seems that tests fail because they are trying to access
# plexus component descriptors which seem to be different?
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE LICENSE-BSD NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE LICENSE-BSD NOTICE

%files -n maven-plugin-jxr -f .mfiles-maven-plugin-jxr

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_3jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt3_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt3_7jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt3_3jpp7
- fixed build

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_3jpp7
- applied repocop patches

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_3jpp7
- new fc release

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_2jpp7
- complete build

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

