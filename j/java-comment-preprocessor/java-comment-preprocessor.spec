Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 29
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora}
%bcond_with tests
%else
%bcond_with tests
%endif

%global section		devel

Summary:	The Most Powerful Multi-Pass Java Preprocessor
Name:		java-comment-preprocessor
Version:	6.1.4
Release:	alt1_4jpp8
License:	ASL 2.0

URL:		https://github.com/raydac/java-comment-preprocessor
Source0:	https://github.com/raydac/%name/archive/%version/%name-%version.tar.gz

Patch0:		java-comment-preprocessor-6.1.4-revert-junit5.patch

BuildArch:		noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
%if %{with tests}
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant-testutil)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-jar)
BuildRequires:  mvn(org.apache.maven.shared:maven-verifier)
BuildRequires:  mvn(org.mockito:mockito-all)
BuildRequires:  mvn(org.powermock:powermock-api-mockito)
BuildRequires:  mvn(org.powermock:powermock-module-junit4)
%endif
Source44: import.info

%description
It is the most powerful multi-pass preprocessor for Java
but also it can be used everywhere for text processing
if the destination technology supports Java like comment definitions.

%package javadoc
Group: Development/Java
Summary:	API docs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API Documentation for %{name}.

%prep
%setup -q
%patch0 -p1

# remove unpackaged and dangerous deps
%pom_remove_plugin :animal-sniffer-maven-plugin pom.xml
%pom_remove_plugin :maven-shade-plugin pom.xml

# remove any binary libs
find -name "*.jar" -or -name "*.class" | xargs rm -f

%build
%if %{with tests}
%mvn_build    -- -P'!metacheck'
%else
%mvn_build -f -- -P'!metacheck'
%endif

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference texts/LICENSE-2.0.txt
%doc texts/readme.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference texts/LICENSE-2.0.txt

%changelog
* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 6.1.4-alt1_4jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt2_9jpp8
- java fc28+ update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt2_8jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt2_5jpp8
- added BR: maven-file-management for javapackages 5

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_5jpp8
- new jpp release

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_3jpp8
- new version

