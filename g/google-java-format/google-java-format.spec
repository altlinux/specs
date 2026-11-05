%define _unpackaged_files_terminate_build 1

Name: google-java-format
Version: 2.0.0
Release: alt1

Summary: Reformats Java source code to comply with Google Java Style
License: Apache-2.0
Group: Development/Java
URL: https://github.com/google/google-java-format
VCS: https://github.com/google/google-java-format.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-source-plugin
BuildRequires: replacer
BuildRequires: maven-plugin-build-helper
BuildRequires: jspecify
BuildRequires: auto-value-annotations
BuildRequires: auto-value
BuildRequires: auto-service
BuildRequires: google-error-prone-annotations
BuildRequires: google-error-prone-core
BuildRequires: compile-testing
BuildRequires: guava-testlib
BuildRequires: truth
BuildRequires: guava
BuildRequires: junit
BuildRequires: commonmark
BuildRequires: commonmark-ext-gfm-tables

%description
Google's Java code formatter that parses Java source code and reformats it to
the Google Java Style Guide specification.  Supports command-line usage, Maven,
Gradle, and IDE integrations.

%prep
%setup
%pom_disable_module eclipse_plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_remove_plugin :maven-shade-plugin core
# Avoid two installed Error Prone checkers' Infinite cost crashes.
formatter_ep_options='-Xplugin:ErrorProne'
formatter_check='ArgumentSelectionDefectChecker'
formatter_ep_options="$formatter_ep_options -Xep:$formatter_check:OFF"
formatter_check='AssertEqualsArgumentOrderChecker'
formatter_ep_options="$formatter_ep_options -Xep:$formatter_check:OFF"
%pom_xpath_set -- '//pom:arg[text()="-Xplugin:ErrorProne"]' \
    "$formatter_ep_options"

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Nov 03 2026 Ivan Khanas <xeno@altlinux.org> 2.0.0-alt1
- New version.

* Mon Dec 1 2025 Ivan Khanas <xeno@altlinux.org> 1.32.0-alt1
- First build for ALT.
