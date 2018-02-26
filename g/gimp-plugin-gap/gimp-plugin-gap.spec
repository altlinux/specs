Name: gimp-plugin-gap
Version: 2.6.0
Release: alt4
Summary: The GIMP Animation Package
Group: Graphics
License: %gpl3only
Url: http://www.gimp.org

Packager: Yuriy Shirokov <yushi@altlinux.org>

PreReq: gimp >= 2.6
Obsoletes: gimp-plugin-gap < 2.6.0

Source: ftp://ftp.gimp.org/pub/gimp/plug-ins/v2.6/gap/gimp-gap-2.6.0.tar.bz2

Patch: gimp-gap-2.6.0-install-data-hook.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: intltool libgimp-devel libgtk+2-devel libjpeg-devel libpng-devel libxvid-devel nasm wavplay zlib-devel

%description
The GIMP-GAP (GIMP Animation Package) is a collection of Plug-Ins
to extend the GIMP with capabilities to edit and create
Animations as sequences of single frames.

%prep
%setup -q -n gimp-gap-2.6.0

tar -xzf extern_libs/libmpeg3.tar.gz -C extern_libs

%patch -p0

%build
pushd extern_libs/libmpeg3
%make
popd

%autoreconf
%configure \
	--with-preinstalled-libmpeg3incdir=%_builddir/gimp-gap-2.6.0/extern_libs/libmpeg3 \
	--with-preinstalled-libmpeg3=%_builddir/gimp-gap-2.6.0/extern_libs/libmpeg3/libs/libmpeg3.a
%make

%install
%make DESTDIR=%buildroot install

rm -f %buildroot%_datadir/gimp-gap-2.6/*.a

%find_lang --output=%name.lang gimp20-gap

%files -f %name.lang
%doc AUTHORS NEWS README
%_libdir/gimp/2.0/plug-ins/gap_*
%_datadir/gimp/2.0/scripts/*.scm
%_libdir/gimp-gap-2.6

%changelog
* Sun Mar 13 2011 Yuriy Shirokov <yushi@altlinux.org> 2.6.0-alt4
- New dependencies added (libpng, zlib)

* Tue Sep 21 2010 Yuriy Shirokov <yushi@altlinux.org> 2.6.0-alt3
- gimp-gap-2.6.0-alt-x86_64.patch removed; license information updated

* Thu Apr 22 2010 Yuriy Shirokov <yushi@altlinux.org> 2.6.0-alt2
- Wavplay moved to separated package; spec cleanup

* Thu Mar 25 2010 Yuriy Shirokov <yushi@altlinux.org> 2.6.0-alt1
- Release for ALT Linux again

* Sun Jul 5 2009 Yuriy Shirokov <yuriy.shirokov@gmail.com>  2.6.0-uri1
- 2.6.0
- quick and dirty build without many features

* Sun Mar 22 2009 Yuriy Shirokov <yuriy.shirokov@gmail.com>  2.4.0-alt1
- 2.4.0
- bug with -m486 fixed
- make_build for libmpeg3 changed to make

* Sun Mar 8 2009 Yuriy Shirokov <yuriy.shirokov@gmail.com>  2.2.2-uri1
- bug with gimp_proc_view_new fixed

* Sat Aug 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Mon Jan 16 2006 Anatoly Yakushin <jaa@altlinux.ru> 2.0.2-alt2
- spec minor bugs fixed

* Sat May 22 2004 Anatoly Yakushin <jaa@altlinux.ru> 2.0.2-alt1
- initial ALT package

* Wed Apr 14 2004 Nils Philippsen <nphilipp@redhat.com>
- version 2.0.0
- initial build

