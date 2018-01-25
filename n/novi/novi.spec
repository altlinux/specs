Name: novi
Version: 2.1.2
Release: alt2

Summary: find the latest-version RPMs in a tree
License: Apache 2.0
Group: File tools

Url: http://www.exmachinatech.net/01/novi/
Source: %name-%version.tar.bz2
Patch1: novi-1.1.9-alt-makefile.patch
Patch2: novi-1.1.9-alt-DSO.patch
Patch3: novi-2.1.2-alt-build.patch

# Automatically added by buildreq on Sat Dec 05 2009
BuildRequires: gcc-c++ pkgconfig libexpat-devel librpm-devel zlib-devel

%description
novi searches directories for the latest-version RPMs of each product.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p2

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
* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.2-alt2
- Fixed build with new toolchain.

* Wed Aug 17 2016 Alexey Gladkov <legion@altlinux.ru> 2.1.2-alt1
- New version.

* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.9-alt1.1
- Fixed build

* Sat Dec 05 2009 Michael Shigorin <mike@altlinux.org> 1.1.9-alt1
- built for ALT Linux (thanks led@ for both the pointer and a patch)
- heavy cleanup of crappy upstream spec
- fixed crappy makefile
