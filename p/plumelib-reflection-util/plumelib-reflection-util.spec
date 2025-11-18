%define _unpackaged_files_terminate_build 1
%def_with check

Name: plumelib-reflection-util
Version: 1.1.5
Release: alt1

Summary: Utilities for Java reflection 
License: MIT
Group: Development/Java
Url: https://github.com/plume-lib/reflection-util
Vcs: https://github.com/plume-lib/reflection-util.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-17-compat
BuildRequires: xgradle
BuildRequires: checker-qual
%if_with check
BuildRequires: junit5
%endif

%description
Reflection Util is a Java library that provides utility classes and methods for
working with Java reflection, converting between string representations of Java
types, and other reflection-related tasks. It simplifies common reflection
operations that are often verbose and error-prone when using the standard Java
Reflection API directly.

%{?javadoc_package}

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register
%gradle_register_javadoc

%gradle_install

%check
%gradle_check -Dfile.encoding=UTF-8

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Tue Nov 18 2025 Ivan Khanas <xeno@altlinux.org> 1.1.5-alt1
- First build for ALT.
