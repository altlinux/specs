Name: libqxp
Version: 0.0.3
Release: alt1

Summary: Library for import of QuarkXPress documents
Group: System/Libraries
License: MPL-2.0
Url: https://wiki.documentfoundation.org/DLP/Libraries/libqxp

Vcs: git://gerrit.libreoffice.org/libqxp

Source: https://dev-www.libreoffice.org/src/%name/%name-%version.tar.xz

BuildRequires: gcc-c++ cppunit-devel help2man
BuildRequires: libicu-devel librevenge-devel
BuildRequires: boost-devel-headers doxygen

%description
libqxp is library providing ability to interpret and import QuarkXPress
document formats into various applications. Currently it only supports
QuarkXPress 3.1-4.1.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
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
Summary: Tools to transform QuarkXPress documents into other formats
Requires: %name = %EVR
Group: Office

%description tools
Tools to transform QuarkXPress documents into other formats.
Currently supported: SVG, plain text, raw.

%prep
%setup

%build
%autoreconf
%configure --disable-silent-rules --disable-static
%make_build

# generate and install man pages
for tool in raw svg text; do
    LD_LIBRARY_PATH=`pwd`/src/lib/.libs/ \
    help2man -N -S '%name %version' -o qxp2${tool}.1 \
    src/conv/$tool/.libs/qxp2$tool
done

%install
%makeinstall_std
rm -f %buildroot/%_libdir/*.la
# we install API docs directly from build
rm -rf %buildroot/%_docdir/%name

install -m 0755 -d %buildroot/%_man1dir/
install -m 0644 qxp2*.1 %buildroot/%_man1dir/

%check
LD_LIBRARY_PATH=%buildroot/%_libdir${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}} \
%make -k check VERBOSE=1

%files
%doc AUTHORS NEWS README
%_libdir/%{name}*.so.*

%files devel
%doc ChangeLog NEWS
%_includedir/%{name}*
%_libdir/%{name}*.so
%_libdir/pkgconfig/%{name}*.pc

%files doc
%doc docs/doxygen/html

%files tools
%_bindir/qxp2raw
%_bindir/qxp2svg
%_bindir/qxp2text
%_mandir/man1/qxp2raw.1*
%_mandir/man1/qxp2svg.1*
%_mandir/man1/qxp2text.1*

%changelog
* Mon Jul 06 2026 Yuri N. Sedunov <aris@altlinux.org> 0.0.3-alt1
- 0.0.3

* Mon Feb 26 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.1-alt2
- drop libquadmath from BR, not really needed

* Mon Feb 19 2018 Fr. Br. George <george@altlinux.ru> 0.0.1-alt1
- Initial build from Fedora

