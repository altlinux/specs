Name: novi
Version: 1.1.9
Release: alt1.1

Summary: find the latest-version RPMs in a tree
License: Apache 2.0
Group: File tools

Url: http://www.exmachinatech.net/01/novi/
Source: %name-%version.tar.bz2
Patch0: novi-1.1.2-rpm4.0.patch
Patch1: novi-1.1.9-alt-makefile.patch
Patch2: novi-1.1.9-alt-DSO.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sat Dec 05 2009
BuildRequires: gcc-c++ libexpat-devel librpm-devel zlib-devel

%description
novi searches directories for the latest-version RPMs of each product.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p2

%build
%configure
%make_build

%install
%makeinstall_std ALT_ROOT_DIR=%buildroot

%files
%_bindir/*
%_man1dir/*
%doc EXAMPLES.TXT FAQ.TXT INSTALL.TXT LICENSE README.TXT WISHLIST.TXT
%doc doc/novi.1.html doc/novi_examples.1.html

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.9-alt1.1
- Fixed build

* Sat Dec 05 2009 Michael Shigorin <mike@altlinux.org> 1.1.9-alt1
- built for ALT Linux (thanks led@ for both the pointer and a patch)
- heavy cleanup of crappy upstream spec
- fixed crappy makefile
