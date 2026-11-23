%define _unpackaged_files_terminate_build 1

Name: json-path
Version: 3.0.0
Release: alt1

Summary: Java implementation of JSONPath
License: Apache-2.0
Group: Development/Java
URL: https://github.com/json-path/JsonPath
VCS: https://github.com/json-path/JsonPath.git

Source: %name-%version.tar
Patch0: 0001-Use-the-system-Bnd-and-JSON-providers.patch
Patch1: 0002-Keep-JSON-P-tests-without-JSON-B.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: biz-aQute-bnd-gradle-plugins
BuildRequires: mvn(net.minidev:json-smart)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(tools.jackson.core:jackson-databind)
BuildRequires: mvn(org.codehaus.jettison:jettison)
BuildRequires: mvn(org.json:json)
BuildRequires: mvn(org.apache.tapestry:tapestry-json)
BuildRequires: jakarta-json2
BuildRequires: mvn(jakarta.json.bind:jakarta.json.bind-api)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(org.assertj:assertj-core)

%description
JsonPath is a Java library for reading and manipulating JSON documents
using XPath-like expressions. This package publishes the upstream
com.jayway.jsonpath:json-path and com.jayway.jsonpath:json-path-assert
artifacts.

%package assert
Summary: Assertions support for Java implementation of JSONPath
Group: Development/Java

%description assert
Assertion helpers for tests and applications using Java implementation of
JSONPath.

%prep
%setup -q
%autopatch -p1
%mvn_package com.jayway.jsonpath:json-path %name
%mvn_package com.jayway.jsonpath:json-path-assert assert

%build
%gradle_publish

%install
%gradle_register --artifacts=json-path-
%gradle_install

%check
%gradle_check

%files -f .mfiles-%name
%doc LICENSE

%files assert -f .mfiles-assert

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 3.0.0-alt1
- Initial build for ALT.
