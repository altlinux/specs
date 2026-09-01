%define _unpackaged_files_terminate_build 1

# Tests use Spock/Groovy framework not available in Sisyphus
%def_without check

Name: generics-resolver
Version: 3.0.3
Release: alt2

Summary: Java generics runtime resolver
License: MIT
Group: Development/Java
Url: https://github.com/xvik/generics-resolver
Vcs: https://github.com/xvik/generics-resolver

BuildArch: noarch

Source0: %name-%version.tar

Patch0: generics-resolver-3.0.3-alt-remove-external-plugins.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: xgradle

%description
Java generics runtime resolver. Allows to resolve actual type of
generic classes, methods and fields at runtime. Useful for
frameworks and libraries that need to work with generic types.

%package javadoc
Group: Development/Java
Summary: API documentation for %name
BuildArch: noarch
Requires: %name = %EVR

%description javadoc
This package provides %summary.

%prep
%setup
%autopatch -p1

%build
%gradle_publish -Prelease

%install
%gradle_register --remove-parent=all
%gradle_register_javadoc

%gradle_install

%files -f .mfiles
%doc README.md LICENSE

%files javadoc -f .mfiles-javadoc
%doc README.md LICENSE

%changelog
* Tue Sep 1 2026 Timofei Fedotov <sovtouch@altlinux.org> 3.0.3-alt2
- Fix FTBFS.

* Thu Jun 11 2026 Timofei Fedotov <sovtouch@altlinux.org> 3.0.3-alt1
- Initial build for ALT Sisyphus.
