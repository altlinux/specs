Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          jaxb2-maven-plugin
Version:       1.6
Release:       alt1_4jpp8
Summary:       JAXB-2 Maven Plugin
License:       ASL 2.0
Url:           http://www.mojohaus.org/jaxb2-maven-plugin/
# Source code avialable @ https://github.com/mojohaus/jaxb2-maven-plugin
Source0:       http://repo2.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires: mojo-parent
BuildRequires: glassfish-jaxb
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.sonatype.plexus:plexus-build-api)

# test deps
BuildRequires: aopalliance
BuildRequires: cglib
BuildRequires: junit
BuildRequires: maven-plugin-testing-harness
BuildRequires: xmlunit

BuildRequires: maven-local
BuildRequires: maven-invoker-plugin
BuildRequires: maven-plugin-plugin

BuildArch:     noarch
Source44: import.info

%description
Mojo's JAXB-2 Maven plugin is used to create an object graph from
XSDs based on the JAXB 2.1 implementation and to generate XSDs from
JAXB-annotated Java classes.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

sed -i 's/\r//' LICENSE.txt

# used only mvn3 apis
%pom_remove_dep org.apache.maven:maven-project
%pom_add_dep org.apache.maven:maven-compat

# missing build deps
# om_add_dep org.glassfish.jaxb:jaxb-runtime
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId ='jaxb-jxc']/pom:groupId" org.glassfish.jaxb
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId ='jaxb-xjc']/pom:groupId" org.glassfish.jaxb

# missing test deps
%pom_add_dep aopalliance:aopalliance::test
%pom_add_dep net.sf.cglib:cglib::test

# Disable integration tests
%pom_xpath_remove "pom:profiles"

%mvn_file :%{name} %{name}

%build

%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_4jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_3jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1jpp7
- new release

