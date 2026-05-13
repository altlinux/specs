Name:           javadoc-parser
Version:        0.3.1
Release:        alt1

Summary:        Java library for parsing information from a structured Javadoc string
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/chhorz/javadoc-parser
VCS:            https://github.com/chhorz/javadoc-parser

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildArch:      noarch

%description
This library provides a parsing mechanism for Javadoc comments within java
files. An initial documentation of the Javadoc tool can be found on the pages
of Oracle: Javadoc Tool.

To get the parsing mechanism work properly the Javadoc comment has to follow a
specific structure. The structure should be as close as possible to the Writers
Guide from Oracle.

%javadoc_package

%prep
%setup

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

# No need
%pom_disable_module javadoc-parser-documentation

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt README.adoc

%changelog
* Fri May 08 2026 Evgeniy Serov <scala@altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus.
