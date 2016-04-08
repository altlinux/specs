Name: libabw
Version: 0.1.1
Release: alt1.qa1
Summary: A library for import of AbiWord files

Group: System/Libraries
License: MPLv2.0
Url: http://www.freedesktop.org/wiki/Software/libabw/
Source: %name-%version.tar.xz

BuildRequires: gcc-c++
BuildRequires: boost-devel-headers
BuildRequires: pkgconfig(librevenge-0.0) pkgconfig(librevenge-stream-0.0) pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(zlib)

BuildRequires: doxygen help2man
BuildRequires: gperf

%description
%name is a library for import of AbiWord files.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation of %name API
Group: Documentation
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Summary: Tools to transform AbiWord files into other formats
Group: Publishing
Requires: %name%{?_isa} = %version-%release

%description tools
Tools to transform AbiWord files into other formats. Currently
supported: XHTML, raw, text.

%prep
%setup

%build
mkdir -p m4
%autoreconf
%configure --disable-silent-rules --disable-static --disable-werror
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

export LD_LIBRARY_PATH=`pwd`/src/lib/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
help2man -N -n 'debug the conversion library' -o abw2raw.1 ./src/conv/raw/.libs/abw2raw
help2man -N -n 'convert AbiWord document into HTML' -o abw2html.1 ./src/conv/html/.libs/abw2html
help2man -N -n 'convert AbiWord document into plain text' -o abw2text.1 ./src/conv/text/.libs/abw2text

%install
%makeinstall_std
make install DESTDIR=%buildroot
# we install API docs directly from build
rm -rf %buildroot/%_docdir/%name

mkdir -p %buildroot/%_mandir/man1
install -m 0644 abw2*.1 %buildroot/%_mandir/man1

%files
%doc CREDITS COPYING.MPL README
%_libdir/*.so.*

%files devel
%doc ChangeLog
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%files doc
%doc COPYING.MPL
%doc docs/doxygen/html

%files tools
%_bindir/abw2raw
%_bindir/abw2text
%_bindir/abw2html
%_mandir/man1/abw2raw.1*
%_mandir/man1/abw2text.1*
%_mandir/man1/abw2html.1*

%changelog
* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.1.1-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 0.1.1-alt1
- Autobuild version bump to 0.1.1

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- 0.1.0

* Thu Mar 20 2014 Fr. Br. George <george@altlinux.ru> 0.0.2-alt1
- Autobuild version bump to 0.0.2

* Thu Mar 20 2014 Fr. Br. George <george@altlinux.ru> 0.0.1-alt1
- Initial build from FC

* Mon Feb 10 2014 David Tardon <dtardon@redhat.com> - 0.0.2-1
- new upstream release 0.0.2
- generate man pages for the tools

* Wed Jan 15 2014 David Tardon <dtardon@redhat.com> - 0.0.1-1
- new upstream release

* Mon Jan 13 2014 David Tardon <dtardon@redhat.com> - 0.0.0-1
- initial import
