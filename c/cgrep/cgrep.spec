Name: cgrep
Version: 1.0
Release: alt1

Summary: Simple program output colorifer
License: GPL2
Group: Text tools
BuildArch: noarch

Packager: Alexey Gladkov <legion@altlinux.ru>

Requires: termutils libshell

Source0: %name-%version.tar

# Automatically added by buildreq on Thu Feb 19 2009
BuildRequires: help2man libshell ash

%description
This package contains simple wrapper to colorize output from any programs.

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*

%changelog
* Thu Feb 19 2009 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- Fist build.
