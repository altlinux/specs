%define __strip %_mingw32_strip
%define __objdump %_mingw32_objdump

Name: mingw32-expat
Version: 2.0.1
Release: alt1
Summary: MinGW Windows port of expat XML parser library

License: MIT
Group: System/Libraries
Url: http://www.libexpat.org/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://download.sourceforge.net/expat/expat-%version.tar.gz

BuildArch: noarch

BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils

%description
This is expat, the C library for parsing XML, written by James Clark. Expat
is a stream oriented XML parser. This means that you register handlers with
the parser prior to starting the parse. These handlers are called when the
parser discovers the associated structures in the document being parsed. A
start tag is an example of the kind of structures for which you may
register handlers.

%prep
%setup -q -n expat-%version

rm conftools/libtool.m4
chmod -x COPYING

%build
%autoreconf
%_mingw32_configure
%make_build

%install
%makeinstall_std

# Remove static libraries but DON'T remove *.dll.a files.
rm %buildroot%_mingw32_libdir/libexpat.a

# Remove documentation which duplicates that found in the native package.
rm -r %buildroot%_mingw32_mandir/man1

%files
%doc COPYING
%_mingw32_bindir/libexpat-1.dll
%_mingw32_bindir/xmlwf
%_mingw32_libdir/libexpat.dll.a
%_mingw32_libdir/libexpat.la
%_mingw32_includedir/expat.h
%_mingw32_includedir/expat_external.h

%changelog
* Wed Sep 23 2009 Boris Savelev <boris@altlinux.org> 2.0.1-alt1
- initial build for Sisyphus

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar  9 2009 Richard W.M. Jones <rjones@redhat.com> - 2.0.1-4
- Remove +x permissions on COPYING file.

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.0.1-3
- Rebuild for mingw32-gcc 4.4

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 2.0.1-2
- Include license.

* Fri Oct 31 2008 Richard W.M. Jones <rjones@redhat.com> - 2.0.1-1
- Initial RPM release.
