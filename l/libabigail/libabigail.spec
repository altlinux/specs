Name: libabigail
Version: 1.0
Release: alt0.2.rc0.1
Summary: Set of ABI analysis tools
Group: Development/Other

License: LGPLv3+
Url: https://sourceware.org/libabigail/
Source0: %name-%version.tar

# Automatically added by buildreq on Tue May 19 2015 (-ba)
# optimized out: elfutils fontconfig fonts-bitmap-misc libcloog-isl4 libelf-devel libstdc++-devel libwayland-client libwayland-server makeinfo pkg-config python-base python-module-BeautifulSoup python-module-PyStemmer python-module-Pygments python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-multiprocessing python-modules-unittest
BuildRequires: dos2unix doxygen elfutils-devel gcc-c++ graphviz libxml2-devel python-module-cssselect python-module-docutils python-module-html5lib time
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
The libabigail package comprises four command line utilities: abidiff,
abicompat, abidw and abilint.  The abidiff command line tool compares
the ABI of two ELF shared libraries and emits meaningful textual
reports about changes impacting exported functions, variables and
their types.  abicompat checks if a subsequent version of a shared
library is still compatible with an application that is linked
against it.  abidw emits an XML representation of the ABI of a given
ELF shared library. abilint checks that a given XML representation of
the ABI of a shared library is correct.

Install libabigail if you need to compare the ABI of ELF shared
libraries.

%package devel
Summary: Shared library and header files to write ABI analysis tools
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains a shared library and the associated header files
that are necessary to develop applications that use the C++ Libabigail
library.  The library provides facilities to analyze and compare
application binary interfaces of shared libraries in the ELF format.

%package doc
Summary: Man pages, texinfo files and html manuals of libabigail
Group: Development/Other
Requires(post): info
Requires(preun): info

%description doc
This package contains documentation for the libabigail tools in the
form of man pages, texinfo documentation and API documentation in html
format.

%prep
%setup

%build
%autoreconf
%configure --disable-silent-rules --disable-zip-archive --disable-static
%make_build

make -C doc html-doc
make -C doc/manuals html-doc
make -C doc/manuals man
make -C doc/manuals info

%install
%makeinstall_std
find %buildroot -name '*.la' -delete

# Install man and texinfo files as they are not installed by the
# default 'install' target of the makefile.
make -C doc/manuals install-man-and-info-doc DESTDIR=%buildroot
dos2unix doc/manuals/html/_static/jquery.js

%check
make check ||:

cat tests/test-suite.log

%files
%doc AUTHORS ChangeLog COPYING COPYING-LGPLV3 COPYING-GPLV3
%_bindir/abicompat
%_bindir/abidiff
%_bindir/abidw
%_bindir/abilint
%_libdir/libabigail.so.0
%_libdir/libabigail.so.0.0.0

%files devel
%_libdir/libabigail.so
%_libdir/pkgconfig/libabigail.pc
%_includedir/*
%_datadir/aclocal/abigail.m4

%files doc
%doc COPYING COPYING-LGPLV3 COPYING-GPLV3
%doc doc/manuals/html/*
%_mandir/man7/*
%_infodir/abigail.info*

%changelog
* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.2.rc0.1
- NMU: added BR: texinfo

* Thu Nov 19 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt0.2.rc0
- Updated to 1.0.rc0.

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt0.1.git088f077
- Initial build.
