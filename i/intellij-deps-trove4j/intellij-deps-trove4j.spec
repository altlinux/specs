%define _unpackaged_files_terminate_build 1

Name: intellij-deps-trove4j
Version: 1.0.20200330
Release: alt1

Summary: Trove4J collections library used by IntelliJ Platform
License: LGPL-2.1-or-later
Group: Development/Java
URL: https://github.com/JetBrains/intellij-deps-trove4j
VCS: https://github.com/JetBrains/intellij-deps-trove4j

Source0: %name-%version.tar
Patch0: trove4j-alt-build.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel

BuildArch: noarch

%description
Trove4J is JetBrains' fork of the Trove collections library, published as
org.jetbrains.intellij.deps:trove4j and used by the IntelliJ Platform.

%prep
%setup -q
%patch0 -p1

%build
%gradle_publish

%install
%gradle_register
%gradle_install

%check
%gradle_check
java -ea -cp core/build/classes/java/main:core/build/classes/java/test gnu.trove.MapTest

%files -f .mfiles
%doc LICENSE.txt README-license.txt

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 1.0.20200330-alt1
- Initial build for ALT.
