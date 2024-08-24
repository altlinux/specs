%define _libexecdir %_prefix/libexec

%define binary_name jasmine

Name: %binary_name-gjs
Version: 3.10.1
Release: alt1

Summary: A behavior-driven development framework for GJS
License: MIT
Group: Development/Tools
Url: https://github.com/ptomato/jasmine-gjs

Source: https://github.com/ptomato/jasmine-gjs/releases/download/%version/%name-%version.tar.xz

BuildArch: noarch

%define gjs_ver 1.68

Requires: libgjs >= %gjs_ver /usr/bin/gjs-console
Requires: gobject-introspection

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: libgjs >= %gjs_ver /usr/bin/gjs-console
BuildRequires: gobject-introspection-devel

%description
This module allows you to run Jasmine specs for your GJS code.
The output will be displayed in your terminal.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/%binary_name
%_libexecdir/%name/
%_datadir/%name/
%_man1dir/%binary_name.1*
%doc README.md NEWS.md


%changelog
* Sat Aug 24 2024 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- first build for Sisyphus

