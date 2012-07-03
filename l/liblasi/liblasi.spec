%define origname libLASi

Name: liblasi
Version: 1.1.1
Release: alt3

Summary: C++ stream output interface for creating Unicode PostScript documents
License: LGPL
Group: System/Libraries

Url: http://www.unifont.org/lasi
Source: %origname-%version.tar.gz
Source100: %name.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sat Mar 29 2008
BuildRequires: chrpath cmake gcc-c++ libpango-devel

%define pkgdocdir %_docdir/%name-%version

%description
libLASi is a library written by Larry Siden  that provides
a C++ stream output interface (with operator <<) for creating
Postscript documents that can contain characters from any of the
scripts and symbol blocks supported in Unicode  and by Owen
Taylor's Pango layout engine.

The library accomodates right-to-left scripts such as Arabic
and Hebrew as easily as left-to-right scripts. Indic and
Indic-derived Complex Text Layout (CTL) scripts, such as
Devanagari, Thai, Lao, and Tibetan are supported to the extent
provided by Pango and by the OpenType fonts installed on your
system. All of this is provided without need for any special
configuration or layout calculation on the programmer's part.

Although the capability to produce Unicode-based multilingual
Postscript documents exists in large Open Source application
framework libraries such as GTK+, QT, and KDE, libLASi was
designed for projects which require the ability to produce
Postscript independent of any one application framework.

%package devel
Summary: Development part of libLASi
License: GPL
Group: Development/C++
Requires: %name = %version-%release

%description devel
libLASi is a library that provides a C++ stream output interface
for creating Postscript documents.

This is the development environment to compile libLASi apps.

%prep
%setup -n %origname-%version

%build
cmake \
	-DCMAKE_INSTALL_PREFIX=%_prefix \
	-DCMAKE_INSTALL_LIBDIR=%_libdir
%make_build

%install
%makeinstall_std
chrpath -d %buildroot%_libdir/*.so.*
mkdir -p %buildroot%pkgdocdir
cp -a AUTHORS ChangeLog NEWS README %buildroot%pkgdocdir/
mv %buildroot%_datadir/lasi%version/examples/ %buildroot%pkgdocdir/

%files
%_libdir/*.so.*
%dir %pkgdocdir
%pkgdocdir/AUTHORS
%pkgdocdir/ChangeLog
%pkgdocdir/NEWS
%pkgdocdir/README

%files devel
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/*
%pkgdocdir/examples/

%changelog
* Tue Jul 03 2012 Michael Shigorin <mike@altlinux.org> 1.1.1-alt3
- added missed requires for devel subpackage of main lib package (led@)

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 1.1.1-alt2
- added watch file

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 1.1.1-alt1
- 1.1.1

* Thu Mar 10 2011 Michael Shigorin <mike@altlinux.org> 1.1.0-alt5
- rebuilt for debuginfo

* Wed Oct 13 2010 Michael Shigorin <mike@altlinux.org> 1.1.0-alt4
- hopefully eradicated %%buildroot in installed files
  (thanks viy@)

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.1.0-alt3
- applied repocop patch

* Sat Mar 29 2008 Michael Shigorin <mike@altlinux.org> 1.1.0-alt2
- fixed x86_64 build

* Sat Mar 29 2008 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1
- 1.1.0 (current stable release)
- build moved to cmake
- spec cleanup
- added, erm, examples to devel subpackage
- updated Summary:

* Thu Nov 09 2006 Michael Shigorin <mike@altlinux.org> 1.0.6-alt1
- 1.0.6 (NB: requires freetype >= 2.2)
- removed patch (merged upstream)

* Mon Jun 05 2006 Michael Shigorin <mike@altlinux.org> 1.0.5-alt1
- accepted gcc4 build fix and version update by icesik@
  + Mon Jun 05 2006 Igor Zubkov <icesik@altlinux.ru> 1.0.5-alt0

* Sun Mar 26 2006 Michael Shigorin <mike@altlinux.org> 1.0.4-alt2
- fixed build with --as-needed, kind of (better do it properly)

* Fri Feb 17 2006 Michael Shigorin <mike@altlinux.org> 1.0.4-alt1
- built for ALT Linux

