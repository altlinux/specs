BuildRequires: maven-file-management
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global section		devel

Summary:	The Most Powerful Multi-Pass Java Preprocessor
Name:		java-comment-preprocessor
Version:	6.0.1
Release:	alt2_5jpp8
License:	ASL 2.0

URL:		https://github.com/raydac/java-comment-preprocessor
Source0:	https://github.com/raydac/java-comment-preprocessor/archive/%{version}.tar.gz

BuildArch:		noarch
BuildRequires:	maven-local
BuildRequires:	maven-plugin-plugin
BuildRequires:	maven-source-plugin
BuildRequires:	exec-maven-plugin
# Test requirements
BuildRequires:	maven-plugin-testing-harness
BuildRequires:	maven-shared-jar
BuildRequires:	ant-testutil
BuildRequires:	maven-verifier
BuildRequires:	mockito
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


# remove unpackaged and dangerous deps
%pom_remove_plugin :animal-sniffer-maven-plugin pom.xml
%pom_remove_plugin :maven-shade-plugin pom.xml

# remove any binary libs
find -name "*.jar" -or -name "*.class" | xargs rm -f

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc texts/LICENSE-2.0.txt
%doc texts/readme.txt

%files javadoc -f .mfiles-javadoc
%doc texts/LICENSE-2.0.txt

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt2_5jpp8
- added BR: maven-file-management for javapackages 5

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_5jpp8
- new jpp release

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_3jpp8
- new version

