Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           maven-compiler-plugin
Version:        3.8.1
Release:        alt1_10jpp11
Summary:        Maven Compiler Plugin
License:        ASL 2.0
URL:            https://maven.apache.org/plugins/maven-compiler-plugin
BuildArch:      noarch

Source0:        https://archive.apache.org/dist/maven/plugins/%{name}-%{version}-source-release.zip

# port to plexus-languages 1.0.3
Patch0:         0001-plexus-languages-1.0.patch

# Taken from upstream commit: https://github.com/apache/maven-compiler-plugin/commit/116b98153ef5ce7b13c0275324baa28bca8bc887
Patch1:         0002-MCOMPILER-359-Fix-for-NPE.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-incremental)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-javac)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-manager)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-java)
BuildRequires:  mvn(org.mockito:mockito-core)
%endif
Source44: import.info

%description
The Compiler Plugin is used to compile the sources of your project.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# Replace path to junit in a test case with the system wide .jar
sed -i 's|localRepository,\ "junit/junit/3.8.1/junit-3.8.1.jar"|"%(find-jar junit || find-jar javapackages-bootstrap/junit)"|' src/test/java/org/apache/maven/plugin/compiler/CompilerMojoTestCase.java

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 3.8.1-alt1_10jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.8.1-alt1_7jpp11
- update

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 3.8.1-alt1_4jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 3.8.1-alt1_2jpp8
- new version

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 3.8.0-alt1_2jpp8
- fc update & java 8 build

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 3.8.0-alt1_1jpp8
- new version

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 3.7.0-alt1_1jpp8
- java update

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 3.6.1-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 3.6.1-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.5.1-alt1_4jpp8
- new fc release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.5.1-alt1_1jpp8
- new version

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 3.3-alt1_2jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 3.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 3.0-alt2_2jpp7
- rebuild with maven.req

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_2jpp7
- new release

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt3_2jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt2_2jpp7
- fixed build

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt1_2jpp7
- new release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_5jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

