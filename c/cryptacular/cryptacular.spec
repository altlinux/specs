Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          cryptacular
Version:       1.1.0
Release:       alt1_1jpp8
Summary:       Java Library that complement to the Bouncy Castle crypto API
# See https://github.com/vt-middleware/cryptacular/issues/25
License:       ASL 2.0 or LGPLv3
URL:           http://www.cryptacular.org/
Source0:       https://github.com/vt-middleware/cryptacular/archive/v%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires: mvn(org.testng:testng)

BuildArch:     noarch
Source44: import.info

%description
Cryptacular in a nutshell:

A. Utilities to perform common crypto operations (hash, encrypt, encode).
A. Stateful, thread-safe bean components.
A. Components to facilitate strict adherence to standards.
A. Comprehensive documentation and examples.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

# Unneeded tasks
%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:executions"
%pom_remove_plugin :maven-checkstyle-plugin

%mvn_file org.%{name}:%{name} %{name}

%build
# Test disabled. Caused by: java.lang.ArrayIndexOutOfBoundsException: 1 (on koji builders only)
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE LICENSE-apache2 LICENSE-lgpl NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE LICENSE-apache2 LICENSE-lgpl NOTICE

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1jpp8
- new version

