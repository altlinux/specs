%define _unpackaged_files_terminate_build 1
%define _without_javadoc 1

Name: emoji-java
Version: 5.1.1
Release: alt1

Summary: Java library for working with emoji characters
License: MIT
Group: Development/Java
URL: https://github.com/vdurmont/emoji-java
VCS: https://github.com/vdurmont/emoji-java

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.json:json)

BuildArch: noarch

%description
emoji-java is a Java library for finding, parsing and working with emoji using
aliases, tags and Unicode characters.

%prep
%setup -q
%pom_xpath_set \
    'pom:project/pom:dependencies/pom:dependency[pom:groupId="org.json"]/pom:version' \
    20260814

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.md
%doc EMOJIS.md

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 5.1.1-alt1
- Initial build for ALT.
