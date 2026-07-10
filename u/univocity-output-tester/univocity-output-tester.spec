Name:           univocity-output-tester
Version:        3.0
Release:        alt1

Summary:        Simple project to validate expected outputs of univocity parsers
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/uniVocity/univocity-output-tester
VCS:            https://github.com/uniVocity/univocity-output-tester

Source0:        %name-%version.tar

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildArch:      noarch

%description
This very simple project was created by univocity to help you validate
the expected results of test cases that produce data samples and
non-trivial outputs, such as XML, CSV, collections and arrays, etc.

It enforces a consistent and organized testing structure and enables
you to easily see what is going on with your tests if you want to.

%javadoc_package

%prep
%setup

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

sed -i -e 's|<source>1\.6</source>|<source>8</source>|' -e 's|<target>1\.6</target>|<target>8</target>|' pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.html README.md

%changelog
* Tue Jul 07 2026 Evgeniy Serov <scala@altlinux.org> 3.0-alt1
- Updated to 3.0.

* Mon May 10 2021 Igor Vlasenko <viy@altlinux.org> 2.1-alt1_5jpp11
- new version

