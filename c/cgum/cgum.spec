%define _unpackaged_files_terminate_build 1

Name:    cgum
Version: 1.0.1
Release: alt1
Summary: The C parser for GumTree
Group:   Development/Other
License: GPLv2
Url:     https://github.com/GumTreeDiff/cgum

# https://github.com/GumTreeDiff/cgum.git
Source: %name-%version.tar

Patch1: %name-%version-alt-paths.patch

BuildRequires: ocaml
BuildRequires: ocaml-num-devel

Requires: coccinelle

%description
This project is a parser that converts C files to a XML format.
It is mainly used as a backend in GumTree diff tool.

%prep
%setup
%patch1 -p1

find . -type f | xargs sed -i \
	-e "s:@DATADIR@:%_datadir:g" \
	-e "s:@LIBDIR@:%_libdir:g" \
	%nil

%build
%make cgum.opt

%install
install -d %buildroot{%_bindir,%_datadir/cgum}
install -m755 cgum.opt %buildroot%_bindir/cgum
install -m755 cgumw %buildroot%_bindir/
install -m644 standard.h %buildroot%_datadir/cgum/

%files
%_bindir/*
%_datadir/cgum

%changelog
* Fri Nov 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Initial build for ALT.
