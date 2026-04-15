%define _unpackaged_files_terminate_build 1
%def_with check

Name: autocomplete
Version: 3.3.3
Release: alt1

Summary: A code completion library
Group: Development/Java
License: BSD-3-Clause
Url: https://github.com/bobbylight/AutoComplete
Vcs: https://github.com/bobbylight/AutoComplete
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: rsyntaxtextarea
BuildRequires: biz-aQute-bnd-gradle-plugins
%if_with check
BuildRequires: junit5
%endif

%description
AutoComplete is a library allowing you to add IDE-like auto-completion to
any Swing JTextComponent. Special integration is added for RSyntaxTextArea,
since this feature is commonly needed when editing source code. Features
include: Drop-down completion choice list. Optional companion "description"
window, complete with full HTML support and navigable with hyperlinks.
Optional parameter completion assistance for functions and methods, ala
Eclipse and NetBeans. Completion information is typically specified in an XML
file, but can even be dynamic.

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

%files -f .mfiles

%changelog
* Wed Apr 15 2026 Arseniy Kostevich <faux@altlinux.org> 3.3.3-alt1
- Initial build for ALT.
