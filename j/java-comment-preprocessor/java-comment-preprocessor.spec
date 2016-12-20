Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global section		devel

Summary:	The Most Powerful Multi-Pass Java Preprocessor
Name:		java-comment-preprocessor
Version:	6.0.1
Release:	alt1_3jpp8
License:	ASL 2.0

URL:		https://github.com/raydac/java-comment-preprocessor
Source0:	https://github.com/raydac/java-comment-preprocessor/archive/%{version}.tar.gz

BuildArch:		noarch
BuildRequires:	maven-local
BuildRequires:	exec-maven-plugin
# Test requirements
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
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_3jpp8
- new version

