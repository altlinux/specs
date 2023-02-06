%def_without flexiblas
%def_with openmpi

Name: gretl
Version: 2022c
Release: alt1

Summary: A tool for econometric analysis

License: GPLv3+ and BSD and MIT
Group: Sciences/Mathematics
Url: http://gretl.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://downloads.sourceforge.net/%name/%name-%version.tar.xz
Source: %name-%version.tar

BuildRequires: bash-completion

%if_with flexiblas
BuildRequires: flexiblas-devel
%else
BuildRequires: libblas-devel, liblapack-devel
%endif

BuildRequires: libgsf-devel

BuildRequires: desktop-file-utils
BuildRequires: libfftw3-devel
BuildRequires: gcc-c++
BuildRequires: gettext-tools
BuildRequires: glib2-devel
BuildRequires: gmp-devel
BuildRequires: gnuplot
BuildRequires: libgtk+3-devel
BuildRequires: libgtksourceview3-devel
BuildRequires: libjson-glib-devel
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
BuildRequires: libgnomeui-devel
BuildRequires: libmpfr-devel
BuildRequires: libncurses-devel
%if_with openmpi
BuildRequires: openmpi-devel
%endif
BuildRequires: libreadline-devel
BuildRequires: xdg-utils

Requires: gnuplot

%description
A cross-platform software package for econometric analysis,
written in the C programming language.

%package devel
Group: Development/C
Summary: Development files for %name
Requires: %name = %EVR
Requires: pkg-config

%description devel
This package contains the development files for %name.

%package openmpi
Group: Sciences/Mathematics
Summary: Binary openmpi files for %name
BuildRequires: openmpi-devel
BuildRequires: make
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires: openmpi
Requires: %name = %EVR

%description openmpi
This package contains the binary openmpi files for %name.

%prep
%setup

CC=mpicc
CXX=mpic++
FC=mpifort

%if_with flexiblas
%__subst 's/-lblas/-lflexiblas/g' -e 's/-llapack/-lflexiblas/g' configure
%endif

%build
# Build OpenMPI version
#_openmpi_load
export LAPACK_LIBS="-llapack"
%if_with openmpi
. %_libdir/openmpi/bin/mpivars.sh
%endif
%configure \
	--disable-static \
	--disable-rpath \
	--disable-avx \
%if_with openmpi
	--with-mpi \
	--with-mpi-lib=%_libdir/openmpi/lib/ \
	--with-mpi-include=%_libdir/openmpi/include/ \
%endif
	--enable-build-editor
# FIXME: --disable-rpath is broken?
sed -ri 's/^(hardcode_libdir_flag_spec|hardcode_libdir_flag_spec_CXX|runpath_var)=.*/\1=/' libtool
export LD_LIBRARY_PATH=$(pwd)/lib/.libs:$LD_LIBRARY_PATH
%make_build

%install
%makeinstall_std
%find_lang %name
rm -rv %buildroot/%_libdir/libgretl*.la
rm -rv %buildroot/%_datadir/%name/doc

%if_with openmpi
#Fix the openmpi binary
mkdir -p %buildroot%_libdir/openmpi/bin
mv %buildroot/%_bindir/gretlmpi %buildroot/%_libdir/openmpi/bin/gretl_openmpi
%endif

desktop-file-install						\
--remove-category="Application;Science;Econometrics" \
--add-category="Education;Science;Math;Economy;"  \
--dir=%buildroot%_desktopdir     \
%buildroot/%_desktopdir/gretl.desktop
#_openmpi_unload
#ldconfig_scriptlets

%files -f %name.lang
%_bindir/gretl
%_bindir/gretlcli
%_bindir/gretl_edit
%_bindir/gretl_x11
%_libdir/gretl-gtk3
%_datadir/%name/
%_man1dir/*
%_libdir/libgretl-1.0.so.*
%_datadir/mime/packages/gretl.xml
%_iconsdir/hicolor/32x32/apps/gretl.png
%_iconsdir/hicolor/32x32/mimetypes/*.png
%_iconsdir/hicolor/48x48/apps/gretl.png
%_iconsdir/hicolor/64x64/apps/gretl.png
%_desktopdir/gretl*
%_datadir/appdata/gretl.appdata.xml

%doc ChangeLog CompatLog README

%files devel
%_pkgconfigdir/gretl.pc
%_libdir/libgretl*.so
%_includedir/%name/

%if_with openmpi
%files openmpi
%_libdir/openmpi/bin/gretl_openmpi
%endif

%changelog
* Sun Feb 05 2023 Vitaly Lipatov <lav@altlinux.ru> 2022c-alt1
- initial build for ALT Sisyphus (thanks, Fedora!)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 02 2022 Johannes Lips <hannes@fedoraproject.org> - 2022c-1
- Update to 2022c

* Wed Aug 10 2022 Johannes Lips <hannes@fedoraproject.org> - 2022b-1
- Update to 2022b
- new gretl edit binary for quick hansl development

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 02 2022 Johannes Lips <hannes@fedoraproject.org> - 2022a-1
- Update to 2022a

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 02 2021 Johannes Lips <hannes@fedoraproject.org> - 2021d-1
- Update to 2021d

* Wed Sep 01 2021 Johannes Lips <hannes@fedoraproject.org> - 2021c-1
- Update to 2021c

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 05 2021 Johannes Lips <hannes@fedoraproject.org> - 2021b-1
- Update to 2021b

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Johannes Lips <hannes@fedoraproject.org> - 2021a-1
- Update to 2021a

* Sun Nov 22 2020 Johannes Lips <hannes@fedoraproject.org> - 2020e-1
- Update to 2020e

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 2020d-2
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Fri Aug 07 2020 Johannes Lips <hannes@fedoraproject.org> - 2020d-1
- Update to 2020d

* Fri Jul 31 2020 Johannes Lips <hannes@fedoraproject.org> - 2020c-1
- Update to 2020c

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 12 2020 Johannes Lips <hannes@fedoraproject.org> - 2020b-1
- Update to 2020b
- changelog cleanup

* Thu Mar 05 2020 Johannes Lips <hannes@fedoraproject.org> - 2020a-1
- Update to 2020a

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Johannes Lips <hannes@fedoraproject.org> - 2019d-1
- Update to 2019d

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 2019c-3
- Rebuild for mpfr 4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Johannes Lips <hannes@fedoraproject.org> - 2019c-1
- Update to 2019c

* Tue May 21 2019 Johannes Lips <hannes@fedoraproject.org> - 2019b-1
- Update to 2019b

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2019a-4
- Rebuild for readline 8.0

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 2019a-3
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Johannes Lips <hannes@fedoraproject.org> - 2019a-1
- Update to 2019a

* Sat Dec 22 2018 Johannes Lips <hannes@fedoraproject.org> - 2018d-1
- Update to 2018d

* Tue Sep 04 2018 Johannes Lips <hannes@fedoraproject.org> - 2018c-1
- Update to 2018c

* Fri Aug 17 2018 Johannes Lips <hannes@fedoraproject.org> - 2018b-1
- Update to 2018b

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 17 2018 Johannes Lips <hannes@fedoraproject.org> - 2018a-1
- Update to 2018a
- removed cephes-patch

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017d-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017d-2
- Remove obsolete scriptlets
