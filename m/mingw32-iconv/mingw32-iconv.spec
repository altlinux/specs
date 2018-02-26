Name: mingw32-iconv
Version: 1.12
Release: alt2
Summary: GNU libraries and utilities for character set conversion

License: GPLv2+ and LGPLv2+
Group: System/Libraries
Url: http://www.gnu.org/software/libiconv/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://ftp.gnu.org/pub/gnu/libiconv/libiconv-%version.tar.gz
BuildArch: noarch

BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils

# There's a quasi-circular dependency between mingw32-iconv and
# mingw32-gettext.  If gettext is installed when you build this then
# iconv will create *.mo files.  When this package is added to Fedora
# we can consider adding this circular dep:
BuildRequires: mingw32-gettext

%description
MinGW Windows Iconv library

%package static
Summary: Static version of the MinGW Windows Iconv library
Requires: %name = %version-%release
Group: System/Libraries

%description static
Static version of the MinGW Windows Iconv library.

%prep
%setup -q -n libiconv-%version

%build
%_mingw32_configure --enable-static --enable-shared
%make_build

%install
%makeinstall_std
# Remove documentation which duplicates what is already in
# Fedora native packages.
rm -rf %buildroot%_mingw32_docdir/libiconv/
rm -rf %buildroot%_mingw32_mandir

# If mingw32-gettext was installed during the build, remove the *.mo
# files.  If mingw32-gettext wasn't installed then there won't be any.
rm -rf %buildroot%_mingw32_datadir/locale

%files
%doc COPYING COPYING.LIB
%_mingw32_bindir/iconv
%_mingw32_bindir/libcharset-1.dll
%_mingw32_bindir/libiconv-2.dll
%_mingw32_includedir/iconv.h
%_mingw32_includedir/libcharset.h
%_mingw32_includedir/localcharset.h
%_mingw32_libdir/charset.alias
%_mingw32_libdir/libcharset.dll.a
%_mingw32_libdir/libcharset.la
%_mingw32_libdir/libiconv.dll.a
%_mingw32_libdir/libiconv.la

%files static
%_mingw32_libdir/libcharset.a
%_mingw32_libdir/libiconv.a

%changelog
* Sat Sep 19 2009 Boris Savelev <boris@altlinux.org> 1.12-alt2
- rebuild with gettext

* Sat Sep 19 2009 Boris Savelev <boris@altlinux.org> 1.12-alt1
- initial build for Sisyphus

* Mon Sep  7 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.12-11
- Fixed %%defattr line
- Added -static subpackage
- Use %%global instead of %%define
- Automatically generate debuginfo subpackage

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.12-8
- Rebuild for mingw32-gcc 4.4

* Fri Dec 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.12-7
- Include the license files in doc section.
- Fix the changelog entry numbering.

* Mon Nov  3 2008 Richard W.M. Jones <rjones@redhat.com> - 0.17-5
- Changed the summary (Bruno Haible).
- Note about mingw32-gettext / Remove *.mo files.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 0.17-4
- Rename mingw -> mingw32.

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 0.17-3
- Remove documentation which duplicates what is in Fedora native packages.

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 0.17-2
- Use RPM macros from mingw-filesystem.

* Tue Sep  2 2008 Daniel P. Berrange <berrange@redhat.com> - 0.17-1
- Initial RPM release, largely based on earlier work from several sources.
