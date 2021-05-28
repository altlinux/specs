Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jaxb2-maven-plugin
Version:       1.6
Release:       alt1_12jpp11
Summary:       JAXB-2 Maven Plugin
License:       ASL 2.0
Url:           http://www.mojohaus.org/jaxb2-maven-plugin/
# Source code avialable @ https://github.com/mojohaus/jaxb2-maven-plugin
Source0:       http://repo2.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires: maven-local
BuildRequires: mvn(aopalliance:aopalliance)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.sf.cglib:cglib)
BuildRequires: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven:maven-artifact:2.2.1)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model:2.2.1)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires: mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-jxc)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-xjc)
BuildRequires: mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires: mvn(xmlunit:xmlunit)

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
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId ='jaxb-jxc']/pom:groupId" org.glassfish.jaxb
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId ='jaxb-xjc']/pom:groupId" org.glassfish.jaxb

# missing test deps
%pom_add_dep aopalliance:aopalliance::test
%pom_add_dep net.sf.cglib:cglib::test

# Disable integration tests
%pom_xpath_remove "pom:profiles"

%mvn_file :%{name} %{name}

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 1.6-alt1_12jpp11
- fixed build

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_8jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_4jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_3jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1jpp7
- new release

