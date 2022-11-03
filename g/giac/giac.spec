%define tarver 1.9.0-27
%define mainver %( echo %tarver | sed 's/-.*//' )
%define soname  0

%def_with cocoa

Name: giac
Version: 1.9.0.27
Release: alt1.1

Summary: Computer algebra system

License: GPL-3.0+
Group: Sciences/Mathematics
Url: http://www-fourier.ujf-grenoble.fr/~parisse/giac.html

Source: http://www-fourier.ujf-grenoble.fr/~parisse/debian/dists/stable/main/source/giac_%tarver.tar.gz

# Some files is not compiled with -fpic/-fPIC on armh and ppc64le.
ExcludeArch: armh ppc64le

BuildRequires: bison
BuildRequires: libblas-devel
BuildRequires: byacc
BuildRequires: flex
BuildRequires: libfltk-devel
BuildRequires: gcc-c++
%ifnarch %e2k
BuildRequires: gcc-fortran
%endif
BuildRequires: libglpk-devel
BuildRequires: libgmp-devel
BuildRequires: libecm-devel
BuildRequires: hicolor-icon-theme
BuildRequires: liblapack-devel
BuildRequires: latex2html
BuildRequires: libjpeg-devel
BuildRequires: libmpfi-devel
BuildRequires: libmpfr-devel
BuildRequires: nauty-devel
BuildRequires: libntl-devel
BuildRequires: pari-devel
BuildRequires: libreadline-devel
BuildRequires: shared-mime-info
BuildRequires: texlive
BuildRequires: fontconfig-devel
BuildRequires: libgio-devel
BuildRequires: libglvnd-devel
BuildRequires: libgsl-devel
BuildRequires: libcurl-devel
BuildRequires: libpng-devel
BuildRequires: libsamplerate-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXft-devel
BuildRequires: libXinerama-devel
%if !%{with cocoa}
BuildRequires: libao-devel
%endif

%description
A computer algebra system, compatible with existing CAS, as a C++
library with various user interfaces (GUI with formal spreadsheet and exact
dynamic geometry, on-line, readline, emacs, texmacs...).

%package -n xcas
Summary: Computer algebra interface
Group: Sciences/Mathematics
Requires: %name = %version

%description -n xcas
Xcas is an interface to perform computer algebra, function graphs,
interactive geometry (2-d and 3-d), spreadsheet and statistics
programmation. It may be used as a replacement for graphic calculators
for example on netbooks.

%package -n lib%name%soname
Summary: The core library for %name
Group: System/Libraries

%description -n lib%name%soname
A computer algebra system, compatible with existing CAS, as a C++
library with various user interfaces (GUI with formal spreadsheet and exact
dynamic geometry, on-line, readline, emacs, texmacs...).

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
This package contains header files and libraries needed to develop
application that use the GIAC computer algebra system.

%package doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description doc
This document describes the basic structure and provides information on
usage of giac, a computer algebra system.

%prep
%setup -n %name-%mainver
%ifarch %e2k
# name collision
sed -i "/gen _compare/i #undef __compare" src/misc.cc
sed -i "1i #include <alloca.h>" micropython-1.12/py/obj.h
%endif

# remove all hidden files
find . -type f -iname '.*' -delete

%build
# Fix crashes
export CXXFLAGS+=' -std=c++14 -Wp,-U_GLIBCXX_ASSERTIONS'
# %%ifarch armh ppc64le
# %%add_optflags -no-pie
# %%remove_optflags -fPIC
# %%endif
%configure \
    --enable-gui \
    --enable-static=no \
#

# Eliminate hardcoded rpaths
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -i libtool

%make_build

%install
%makeinstall_std
rm -f %buildroot/%_libdir/*.la

# use the freedesktop standard
rm -rf %buildroot%_datadir/application-registry
# install man page
find debian -type f -name \*.1 | while read i; do
	install -Dm 0644 $i "%buildroot/%_man1dir/${i##*/}"
done
# install mimeinfo
install -Dm 0644 debian/%name.sharedmimeinfo %buildroot%_datadir/mime/packages/%name.xml
# remove makefiles from %%doc
find %buildroot%_datadir/%name/doc -type f -iname "Makefile*" -delete
# remove zero-length
find %buildroot%_datadir/%name/doc -type f -empty -delete
# fix non-executable-script
chmod a+x %buildroot%_datadir/%name/doc/pari/gphtml
# fix script-without-shebang
chmod a-x %buildroot%_datadir/%name/examples/Exemples/*/*.xws
chmod a-x %buildroot%_datadir/%name/examples/geo/*.cas
chmod a-x %buildroot%_datadir/%name/examples/groebner/*
chmod a-x %buildroot%_datadir/%name/examples/lewisw/fermat_gcd_1var
chmod a-x %buildroot%_datadir/%name/examples/lewisw/fermat_gcd_mod_1var
# fix spurious-executable-perm
chmod a-x %buildroot%_datadir/%name/examples/tortue/*.cxx
# put docs in correct directory
if [ "%_docdir" != "%_datadir/doc" ]; then
mkdir -p %buildroot%_docdir
mv %buildroot%_docdir/%name %buildroot%_docdir
fi

rm %buildroot%_docdir/giac/Makefile.am

%find_lang %name

%files -f %name.lang
%doc COPYING
%doc AUTHORS
%_docdir/giac/README
%_bindir/giac
%_bindir/hevea2mml
%_bindir/icas
%_bindir/pgiac
%_bindir/cas_help
%_bindir/en_cas_help
%_bindir/es_cas_help
%_bindir/fr_cas_help
%_datadir/giac/
%_datadir/mime/packages/giac.xml
%_infodir/giac_es.info.xz
%_infodir/giac_us.info.xz
%_man1dir/cas_help.1.xz
%_man1dir/fr_cas_help.1.xz
%_man1dir/giac.1.xz
%_man1dir/icas.1.xz
%_man1dir/pgiac.1.xz
%exclude %_datadir/giac/doc/
%exclude %_datadir/giac/aide_cas
%exclude %_datadir/giac/examples/
%exclude %_docdir/giac/index.html
%exclude %_docdir/giac/*/

%files -n xcas
%doc COPYING
%_bindir/xcas
%_bindir/xcasnew
%_man1dir/xcas.1.xz
%_iconsdir/hicolor/*/apps/*xcas.png
%_iconsdir/hicolor/*/mimetypes/*xcas.png
%_pixmapsdir/xcas.xpm
%_desktopdir/xcas.desktop
%_datadir/metainfo/*.xml

%files -n lib%name%soname
%doc COPYING
%_libdir/libgiac.so.%{soname}*

%files devel
%doc COPYING
%_includedir/giac/
%_libdir/libgiac.so

%files doc
%doc COPYING
%_datadir/giac/doc/
%_datadir/giac/aide_cas
%_datadir/giac/examples/
%_docdir/giac/index.html
%_docdir/giac/*/

%changelog
* Thu Nov 03 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.9.0.27-alt1.1
- E2K: Fortran excluded from BuildRequires

* Tue Oct 25 2022 Leontiy Volodin <lvol@altlinux.org> 1.9.0.27-alt1
- New version.
- Fixed build with pari 2.15.0.

* Thu Apr 28 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.7.0.13-alt1.1
- Fixed build for Elbrus.

* Mon Nov 08 2021 Leontiy Volodin <lvol@altlinux.org> 1.7.0.13-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built as require for sagemath.
