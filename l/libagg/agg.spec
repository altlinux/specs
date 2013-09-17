Name: libagg
Version: 2.5
Release: alt4
Summary: Anti-Grain Geometry
Group: System/Libraries
URL: http://www.antigrain.com
License: GPL

Source: agg-%version.tar.gz
Patch1: agg-2.5-alt.patch


# fedora patches
Patch10: agg-2.4-depends.patch
Patch11: agg-2.5-pkgconfig.patch
Patch12: agg-2.5-autotools.patch

Patch101: 0001-Fix-non-terminating-loop-conditions-when-len-1.patch
Patch102: 0002-Cure-recursion-by-aborting-if-the-co-ordinates-are-t.patch
Patch103: 0003-Get-coordinates-from-previous-vertex-if-last-command.patch
Patch104: 0004-Make-rasterizer_outline_aa-ignore-close_polygon-when.patch
Patch105: 0005-Remove-VC-6-workaround.patch
Patch106: 0006-Implement-grain-merge-blending-mode-GIMP.patch
Patch107: 0007-Implement-grain-extract-blending-mode-GIMP.patch
Patch108: 0008-Declare-multiplication-and-division-operators-as-con.patch
Patch109: 0009-Add-a-static-identity-transformation.patch
Patch110: 0010-Add-renderer_scanline_aa_alpha.patch
Patch111: 0011-Avoid-division-by-zero-in-color-burn-mode.patch
Patch112: 0012-Avoid-pixel-artifacts-when-compositing.patch
Patch113: 0013-Modify-agg-conv-classes-to-allow-access-to-the-origi.patch
Patch114: 0014-Avoid-potential-zero-division-resulting-in-nan-in-ag.patch
Patch115: 0015-Ensure-first-value-in-the-gamma-table-is-always-zero.patch


BuildRequires: gcc-c++ libSDL-devel libX11-devel libfreetype-devel

%description
A High Quality Rendering Engine for C++

%package devel
Summary: Support files necessary to compile applications with agg
Group: Development/C++
Requires: %name = %version-%release

%description devel
Libraries, headers, and support files necessary to compile applications using agg

%prep
%setup -q -n agg-%version
# agg contains gpc.c, 'free for non-commercial use'
for file in copying.txt VERSIONS.TXT gpc.c gpc.h; do
   rm gpc/$file
done
rm -f include/agg_conv_gpc.h
sed -i -e 's/agg_conv_gpc\.h/              /g' include/Makefile.am

%patch1 -p1

# fedora patches
%patch10 -p1 -b .depends
%patch11 -p1 -b .pkgconfig
%patch12 -p0 -b .autotools
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1

%build
%autoreconf
%configure \
	--disable-static \
	--disable-gpc

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*.m4

%changelog
* Wed Sep 18 2013 Alexey Shabalin <shaba@altlinux.ru> 2.5-alt4
- add patches from fedora for build mapnik

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.5-alt3.qa1
- NMU: rebuilt for set-versioned provides.

* Mon Nov 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.5-alt3
- droped unused libs/headers

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.5-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Jan 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.5-alt1
- 2.5

* Tue May 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.4-alt1
- 2.4

* Sun Mar 19 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.3-alt2
- no build demos/examples
- updated build dependencies

* Wed Dec 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.3-alt1
- initial release

