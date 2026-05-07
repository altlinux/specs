Name:           scribejava
Version:        8.3.3
Release:        alt1

Summary:        Simple OAuth library for Java
License:        MIT
Group:          Development/Java
VCS:            https://github.com/scribejava/scribejava
URL:            https://github.com/scribejava/scribejava

Source0:        %name-%version.tar

Patch0:         0001-Replace-javax-with-jakarta-xml-bind.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)

BuildArch:      noarch

%description
%summary.

%javadoc_package

%package        java8
Summary:        ScribeJava Java8
Group:          Development/Java

%description    java8
ScribeJava Java 8+ compatibility stuff.

%package        core
Summary:        ScribeJava Core
Group:          Development/Java

%description    core
%summary.

%prep
%setup
%autopatch -p1

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-checkstyle-plugin

%pom_remove_dep javax.xml.bind:jaxb-api scribejava-core

# missing async-http-client
%pom_disable_module scribejava-httpclient-ahc
%pom_disable_module scribejava-httpclient-ning
%pom_disable_module scribejava-httpclient-apache

# missing okhhtp dep (gradle)
%pom_disable_module scribejava-httpclient-okhttp

# missing armeria (gradle)
%pom_disable_module scribejava-httpclient-armeria

%mvn_package :%name-core core
%mvn_package :%name-java8 java8

%build
# tests disabled cause missing mockwebserver (gradle)
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt README.md

%files core -f .mfiles-core
%files java8 -f .mfiles-java8

%changelog
* Mon May 04 2026 Evgeniy Serov <scala@altlinux.org> 8.3.3-alt1
- Initial build for Sisyphus.
