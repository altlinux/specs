Name: libpagemaker
Version: 0.0.4
Release: alt1
Summary: A library for import of Adobe PageMaker documents
Group: System/Libraries

License: MPLv2.0
Url: http://wiki.documentfoundation.org/DLP/Libraries/libpagemaker
Source: %name-%version.tar.xz

# Automatically added by buildreq on Tue Feb 03 2015
BuildRequires: boost-devel-headers doxygen gcc-c++ help2man librevenge-devel

%description
libpagemaker is library providing ability to interpret and import
Adobe PageMaker documents into various applications.

%package devel
Summary: Development files for %name
Requires: %name%{?_isa} = %version-%release
Group: Development/C++

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation of %name API
BuildArch: noarch
Group: Development/C++

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Summary: Tools to transform Adobe PageMaker documents into other formats
Requires: %name%{?_isa} = %version-%release
Group: Publishing

%description tools
Tools to transform Adobe PageMaker documents into other formats.
Currently supported: SVG, raw.

%prep
%setup

%build
%configure --disable-silent-rules --disable-static --disable-werror
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

export LD_LIBRARY_PATH=`pwd`/src/lib/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
help2man -N -n 'debug the conversion library' -o pmd2raw.1 ./src/conv/raw/.libs/pmd2raw
help2man -N -n 'convert PageMaker document into SVG' -o pmd2svg.1 ./src/conv/svg/.libs/pmd2svg

%install
make install DESTDIR=%buildroot
rm -f %buildroot/%_libdir/*.la
# we install API docs directly from build
rm -rf %buildroot/%_docdir/%name

install -m 0755 -d %buildroot/%_man1dir
install -m 0644 pmd2*.1 %buildroot/%_man1dir

%files
%doc AUTHORS COPYING NEWS
%_libdir/%name-*.so.*

%files devel
%doc ChangeLog
%_includedir/%name-*
%_libdir/%name-*.so
%_libdir/pkgconfig/%name-*.pc

%files doc
%doc COPYING
%doc docs/doxygen/html

%files tools
%_bindir/*
%_man1dir/*

%changelog
* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 0.0.4-alt1
- Autobuild version bump to 0.0.4

* Mon Jul 31 2017 Fr. Br. George <george@altlinux.ru> 0.0.3-alt2
- Rebuild with boost 1.63.0

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 0.0.3-alt1
- Autobuild version bump to 0.0.3

* Wed Apr 13 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.0.2-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Tue Feb 03 2015 Fr. Br. George <george@altlinux.ru> 0.0.2-alt1
- Initial build for ALT

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.0.2-2
- Rebuild for boost 1.57.0

* Fri Dec 05 2014 David Tardon <dtardon@redhat.com> - 0.0.2-1
- new upstream release

* Thu Aug 21 2014 David Tardon <dtardon@redhat.com> - 0.0.1-1
- new upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 26 2014 David Tardon <dtardon@redhat.com> 0.0.0-1
- initial import
