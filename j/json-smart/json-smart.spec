%define _unpackaged_files_terminate_build 1

Name: json-smart
Version: 2.5.2
Release: alt1

Summary: JSON Small and Fast Parser
Group: Development/Java
License: Apache-2.0
Url: https://github.com/netplex/json-smart-v2
Vcs: https://github.com/netplex/json-smart-v2
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: objectweb-asm
BuildRequires: junit5
BuildRequires: maven-source-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: jacoco-maven-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-deploy-plugin

%package -n accessors-smart
Summary: ASM based accessors helper used by json-smart
Group: Development/Java

%package action
Summary: JSON Small and Fast Parser
Group: Development/Java

%{?javadoc_package}

%description
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It is easy for humans to read and write. It is easy for machines to parse
and generate. It is based on a subset of the JavaScript Programming Language,
Standard ECMA-262 3rd Edition - December 1999. JSON is a text format that is
completely language independent but uses conventions that are familiar to
programmers of the C-family of languages, including C, C++, Java, etc.
These properties make JSON an ideal data-interchange language.

Json-smart is a performance focused, JSON processor lib.

%description -n accessors-smart
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It is easy for humans to read and write. It is easy for machines to parse
and generate. It is based on a subset of the JavaScript Programming Language,
Standard ECMA-262 3rd Edition - December 1999. JSON is a text format that is
completely language independent but uses conventions that are familiar to
programmers of the C-family of languages, including C, C++, Java, etc.
These properties make JSON an ideal data-interchange language.

Java reflect give poor performance on getter setter an constructor calls, accessors-smart use ASM to speed up those calls.

%description action
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It is easy for humans to read and write. It is easy for machines to parse
and generate. It is based on a subset of the JavaScript Programming Language,
Standard ECMA-262 3rd Edition - December 1999. JSON is a text format that is
completely language independent but uses conventions that are familiar to
programmers of the C-family of languages, including C, C++, Java, etc.
These properties make JSON an ideal data-interchange language.

JSON-smart-action is a small and fast parser.

%prep
%setup

for module in accessors-smart json-smart json-smart-action; do
    %pom_remove_plugin :maven-gpg-plugin $module
    %pom_remove_plugin :maven-javadoc-plugin $module
    %pom_remove_plugin :maven-release-plugin $module
done

# Without this parent POM, I would have to perform %mvn_install in the %build section.
cat > pom.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>net.minidev</groupId>
    <artifactId>json-smart-parent</artifactId>
    <version>%version</version>
    <packaging>pom</packaging>
    <modules>
        <module>accessors-smart</module>
        <module>json-smart</module>
        <module>json-smart-action</module>
    </modules>
</project>
EOF

%mvn_package :json-smart-parent __noinstall

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-json-smart

%files -n accessors-smart -f .mfiles-accessors-smart

%files action -f .mfiles-json-smart-action

%changelog
* Tue Mar 24 2026 Arseniy Kostevich <faux@altlinux.org> 2.5.2-alt1
- Initial build for ALT.
