Name: Wcalc
Version: 1.1
Release: alt2.1

Summary: Wcalc
License: GPL
Group: Development/Other
Url: http://wcalc.sf.net/

Packager: Alexander Gvozdev <gab@altlinux.ru>

Source0: %name-%version.tar.bz2
Patch0: %name-alt-link.patch

BuildRequires: gcc-c++ libX11-devel flex gtk+2 libgd2-devel libgd2 libdbus-devel libdbus libdbus-glib libdbus-glib-devel tk
BuildRequires: libgtk+2-devel libgtk+2 libjpeg libjpeg-devel gd2-utils libpng-devel zlib-devel libXpm-devel libfreetype-devel perl-XML-Parser desktop-file-utils
Requires(post,postun): shared-mime-info >= 0.15-alt2

%description
Wcalc is a tool for the analysis and synthesis of transmission line structures and
related components.  Wcalc provides the ability to analyze the electrical parameters
of a particular structure based on the physical dimensions and material parameters.
The synthesis portion calculates the required physical parameters to meet desired
electrical specifications.  Wcalc includes several models and places an emphasis on
accuracy.  Several frontends provide the user with several options for its use.

Models include:

 - single layer solenoid inductor
 - single microstrip and stripline
 - coupled microstrip and stripline
 - coplanar waveguide
 - metal-insulator-semiconductor microstrip
 - coaxial cable
 - self and mutual inductance of two parallel rectangular bars

##%description -l ru_RU.UTF-8

%package -n %name-devel
Summary: Include files for libwcalc.
Summary(ru_RU.UTF-8): Заголовочные файлы для libwcalc.
License: GPL
Group: Development/Other
Requires: %name = %version-%release

%description -n %name-devel
Include files for libwcalc.

%package -n %name-stdio-doc
Summary: Component library for PCB
Summary(ru_RU.UTF-8): Библиотеки компонентов для PCB
License: GPL
Group: Development/Other
Requires: %name = %version-%release

%description -n %name-stdio-doc
Documentation for command-line version of wcalc.

%prep
%setup -q

%patch0 -p2

%build

%configure	\
    --enable-htdocs

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%make DESTDIR=%buildroot install


%files -n %name
%_bindir/stdio-wcalc
%_bindir/wcalc
%_bindir/wcalc-config
%_libdir/libwcalc.a
%_libdir/libwcalc.so
%_libdir/libwcalc.so.1
%_libdir/libwcalc.so.1.0.0
%_libdir/pkgconfig/wcalc.pc
%doc /usr/share/man/man1/stdio-wcalc.1.gz
%doc /usr/share/man/man1/Wcalc.1.gz
%doc /usr/share/man/mann/*
%doc /usr/share/wcalc-1.1/*



%files -n %name-devel
%_includedir/wcalc-1.1/*

%files -n %name-stdio-doc
%doc /usr/share/wcalc/stdio-man/*

%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2.1
- Removed bad RPATH

* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2
- fix build

* Mon Mar 9 2009 Alexander Gvozdev <gab@altlinux.ru> 1.1-alt1
- Initial build
