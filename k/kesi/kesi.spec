%undefine __libtoolize

Name: kesi
Version: 0.9
Release: alt1.3

Summary: KESI Easy SQL Import - A tool to import CSV files into SQL tables
License: GPL
Group: Databases
Url: http://kesi.sourceforge.net/
Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.ru>

BuildRequires: gcc-c++ kdelibs-devel libjpeg-devel libpng-devel libqt3-devel xml-utils

%description
KESI Easy SQL Import - A tool to import CSV files into SQL tables.

%prep
%setup -q
make -f admin/Makefile.common cvs

%build
export "PATH=%_K3bindir:$PATH"
%add_optflags -I%_includedir/tqtinterface
%configure \
    --without-arts
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%make DESTDIR=%buildroot kde_htmldir=%_K3doc install
%K3find_lang --with-kde %name

%files -f %name.lang
%_bindir/*
%_datadir/applnk/Utilities/kesi.desktop
%_iconsdir/hicolor/*/apps/kesi.*

%changelog
* Fri Feb 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.3
- Removed bad RPATH

* Tue Apr 26 2011 Sergey V Turchin <zerg@altlinux.org> 0.9-alt1.2
- fix build requires

* Fri Mar 04 2011 Sergey V Turchin <zerg@altlinux.org> 0.9-alt1.1
- fix to build

* Thu Apr 27 2006 Igor Zubkov <icesik@altlinux.ru> 0.9-alt1
- Initial build for Sisyphus
