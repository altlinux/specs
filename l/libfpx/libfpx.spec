# based on PLD libfpx $Revision: 1.35 $, $Date: 2003/11/12 18:36:15 $
Name: libfpx
Version: 1.3.0
Release: alt1
Summary: FlashPIX OpenSource Toolkit
License: distributable (see COPYING)
Group: System/Libraries
Url: http://www.i3a.org/i_flashpix.html
# This package is currently maintained by the ImageMagick Studio LLC,
# http://www.imagemagick.org/. It is available from
# ftp://ftp.imagemagick.org/pub/ImageMagick/delegates/ as well as via
# the 'fpx' module from ImageMagick CVS. All change history, starting
# with the original distribution is available in ImageMagick CVS.
# ftp://ftp.imagemagick.org/pub/ImageMagick/delegates/%name-%version.tar.xz
Source: %name-%version.tar
BuildRequires: gcc-c++

Patch: libfpx-1.2.0.9-linkage.patch

%description
This package is the Flashpix OpenSource Toolkit and is based on source
code obtained from the Digital Imaging Group Inc and the Eastman Kodak
Company.

%package devel
Summary: FlashPIX header file and documentation
Group: Development/C
Requires: %name = %version-%release

%description devel
FlashPIX header files and programmer's documentation.

%prep
%setup
%patch -p1

%build
%add_optflags -fno-strict-aliasing
%autoreconf
%configure \
	--disable-static \
	--enable-fast-install
%make_build

%install
%makeinstall_std

%files
%_libdir/lib*.so.*
%doc AUTHORS COPYING ChangeLog README

%files devel
%_libdir/lib*.so
%_includedir/*
%doc doc/*.pdf doc/readme.txt

%changelog
* Tue Apr 26 2011 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0.
- Cleaned up specfile.
- Build this package without optimizations based on strict aliasing rules.

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.2.0.9-alt2.1.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 1.2.0.9-alt2.1
- NMU (by repocop): the following fixes applied:
 * postun_ldconfig for libfpx
 * post_ldconfig for libfpx

* Fri Sep 28 2007 Igor Vlasenko <viy@altlinux.ru> 1.2.0.9-alt2
- fixed Group: tag

* Thu Sep 27 2007 Igor Vlasenko <viy@altlinux.ru> 1.2.0.9-alt1
- first build.
- The spec is based on PLD Team <@pld.org.pl> one
  of kloczek, radek, wiget, djurban at @pld.org.pl
