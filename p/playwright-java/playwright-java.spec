%define _unpackaged_files_terminate_build 1

Name: playwright-java
Version: 1.41.2
Release: alt1

Summary: Java version of the Playwright testing and automation library
License: Apache-2.0
Group: Development/Java
Url: https://playwright.dev/java
Vcs: https://github.com/microsoft/playwright-java.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: junit5
BuildRequires: java-websocket
BuildRequires: maven-source-plugin
BuildRequires: google-gson

%description
Playwright is a Java library to automate Chromium, Firefox and WebKit with a
single API. Playwright is built to enable cross-browser web automation that is
ever-green, capable, reliable and fast.

%prep
%setup
%autopatch -p1

%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Fri Dec 05 2025 Ivan Khanas <xeno@altlinux.org> 1.41.2-alt1
- First build for ALT.


