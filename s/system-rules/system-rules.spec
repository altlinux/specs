%define _unpackaged_files_terminate_build 1

Name: system-rules
Version: 1.19.0
Release: alt1

Summary: A collection of JUnit rules for testing code which uses java.lang.System
License: CPL-1.0
Group: Development/Java
Url: https://stefanbirkner.github.io/system-rules
Vcs: https://github.com/stefanbirkner/system-rules.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: fishbowl
BuildRequires: junit
BuildRequires: assertj-core
BuildRequires: mockito-core

%description
System Rules is a collection of JUnit rules for testing code which uses
java.lang.System.
System Lambda is an alternative to System Rules that leverages the
possibilities of Java 8. It is independent of the test framework. You can use
it for example as a replacement for System Rules in JUnit Jupiter and TestNG.

%prep
%setup
%autopatch -p1

%pom_remove_parent

%pom_remove_plugin :animal-sniffer-maven-plugin

%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Wed Dec 03 2025 Ivan Khanas <xeno@altlinux.org> 1.19.0-alt1
- First build for ALT.
