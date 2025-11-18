%define _unpackaged_files_terminate_build 1
%def_with check

Name: plumelib-plume-util
Version: 1.12.2
Release: alt1

Summary: Utility libraries for Java 
License: MIT
Group: Development/Java
Url: https://github.com/plume-lib/plume-util
Vcs: https://github.com/plume-lib/plume-util.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-17-compat
BuildRequires: xgradle
BuildRequires: checker-qual
BuildRequires: plumelib-hashmap-util
BuildRequires: plumelib-reflection-util
%if_with check
BuildRequires: junit5
%endif

%{?javadoc_package}

%description
Plume Util is a comprehensive collection of utility libraries for Java that
complements and extends popular Java utility libraries like Guava, Apache
Commons, and Eclipse Collections.  It provides additional utility classes and
methods that are commonly needed in Java development but not covered by other
utility libraries.

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
* Tue Nov 18 2025 Ivan Khanas <xeno@altlinux.org> 1.12.2-alt1
- First build for ALT.
