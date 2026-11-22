%define _unpackaged_files_terminate_build 1

Name: intellij-deps-java-compatibility
Version: 1.0.1
Release: alt1

Summary: JDK 8 classes excluded from JDK 9 used by IntelliJ
License: GPL-2.0-only WITH Classpath-exception-2.0 AND Apache-2.0
Group: Development/Java
URL: https://github.com/JetBrains/intellij-deps-java-compatibility
VCS: https://github.com/JetBrains/intellij-deps-java-compatibility

Source0: java-compatibility-%version.tar
Patch0: java-compatibility-system.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel

BuildArch: noarch

%description
This library provides seven JDK 8 classes that were removed from JDK 9 and
remain used by IntelliJ Platform and IntelliJ based IDEs.

%prep
%setup -q -n java-compatibility-%version
%patch0 -p1

%build
%gradle_publish

%install
%gradle_register --artifacts=java-compatibility
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE LICENSE-APACHE-2.0

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 1.0.1-alt1
- Initial build for ALT.
