%define binname zyGrib
%def_without system_qwt

Name: zygrib
Version: 8.0.1
Release: alt1

Summary: Visualisation of meteo data from files in GRIB formats

License: %gpl3plus
Group: Networking/Other
Url: http://www.zygrib.org
Source0: %binname-%version.tgz
Source1: %binname.png
Source2: %binname.desktop

Requires: fonts-ttf-liberation
Requires: %name-data = %{version}-%{release}

BuildRequires: qt5-base-devel bzlib-devel libjasper-devel libnova-devel libpng-devel libproj-devel

%if_with system_qwt
BuildRequires: libqwt6-qt5-devel
%endif

BuildRequires: rpm-build-licenses

%description
Visualization of meteo data from files in GRIB formats v1 and v2.
GRIB data are used to display weather data in detailed format for
a certain area of sea or land. ZYGrib is a QT5 program to display
and use GRIB data on Linux.

%package data
Summary: Architecture independent files for ZYGrib.
Group: Networking/Other
BuildArch: noarch

%description data
Architecture independent files for ZYGrib.

Included low resolution maps for ZYGrib (25 km, 5 km and 1 km)
and cities with population from 3000 to 10000 and more 10000.

data/gis/* have another license: %ccby30
home page: http://www.geonames.org/

%prep

%setup -q -n %binname-%version

# remove system-wide fonts
rm -rf data/fonts

%if_with system_qwt
#perl -p -e 's|cd src/qwt-6.0.1/src|# cd src/qwt-6.0.1/src|g;' -i $RPM_BUILD_DIR/%binname-%version/Makefile
sed 's|cd ..QWTDIR./src|# cd \$(QWTDIR)/src|' -i Makefile
%endif

%if "%(getconf LONG_BIT)" == "32"
sed -i "s|^CFLAGS= -O3 -g -m64 .*$|CFLAGS= -O3 -g \$(INC) \$(DEFS)|" src/g2clib/makefile
%endif

sed -i "s|QMAKE=/usr/bin/qmake|QMAKE=%_qt5_qmake|" Makefile

%build
%make QTBIN=%_qt5_bindir

%install

make -e INSTALLDIR=%{buildroot}%{_libdir}/%{binname} install
echo -e "#!/bin/sh\ncd %{_libdir}/%{binname}\nbin/%{binname} \"\$@\"" >%{buildroot}%{_libdir}/%{binname}/%{binname}
mkdir -p -m 755 %{buildroot}%{_bindir}
ln -sf %{_libdir}/%{binname}/%{binname} %{buildroot}%{_bindir}/%{binname}
mkdir -p -m 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps
mkdir -p -m 755 %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/applications

mkdir -p -m 755 %{buildroot}%{_datadir}/%{binname}
mv %{buildroot}%{_libdir}/%{binname}/data %{buildroot}%{_datadir}/%{binname}/
cd %{buildroot}%{_libdir}/%{binname}
ln -s %{_datadir}/%{binname}/data data

%post
# if "data" missed then this first installation
if ! [ -d %_libdir/%binname/data ] ; then
    cd %{_libdir}/%{binname}
    ln -s %{_datadir}/%{binname}/data data
fi

%triggerpostun -- zygrib < 5.0.6-alt2
# %_libdir/%binname/data must be symlink since 5.0.6-alt2
if [ -d %_libdir/%binname/data ] ; then
    if ! [ -L %_libdir/%binname/data ] ; then
	rm -rf %_libdir/%binname/data
	cd %{_libdir}/%{binname}
	ln -s %{_datadir}/%{binname}/data data
    fi
fi

%files
%dir %_libdir/%binname
%_libdir/%binname/bin
%_libdir/%binname/grib
%ghost %_libdir/%binname/data
%_libdir/%binname/%binname
%_bindir/%binname
%_datadir/pixmaps/%binname.png
%_datadir/applications/%binname.desktop

%files data
%dir %_datadir/%binname
%_datadir/%binname

%changelog
* Wed Nov 30 2016 Sergey Y. Afonin <asy@altlinux.ru> 8.0.1-alt1
- New version (switched to QT5; added GRIB v2 support)

* Thu Feb 04 2016 Sergey Y. Afonin <asy@altlinux.ru> 7.0.0-alt3
- rebuilt with libproj 4.9.2

* Tue Apr 14 2015 Sergey Y. Afonin <asy@altlinux.ru> 7.0.0-alt2
- rebuilt with internal qwt (ALT 30678#c2)

* Mon Feb 09 2015 Sergey Y. Afonin <asy@altlinux.ru> 7.0.0-alt1
- New version

* Tue Jan 28 2014 Sergey Y. Afonin <asy@altlinux.ru> 6.2.3-alt1
- New version

* Sat Jun 22 2013 Sergey Y. Afonin <asy@altlinux.ru> 6.1.4-alt1
- New version

* Fri Mar 22 2013 Sergey Y. Afonin <asy@altlinux.ru> 6.1.2-alt1
- New version

* Sun Dec 30 2012 Sergey Y. Afonin <asy@altlinux.ru> 6.1.0-alt1
- New version

* Mon May 07 2012 Sergey Y. Afonin <asy@altlinux.ru> 5.1.3-alt2
- fixed build with libproj 4.8.0 (thanks slazav@altlinux)

* Sun Apr 01 2012 Sergey Y. Afonin <asy@altlinux.ru> 5.1.3-alt1
- New version

* Thu Mar 08 2012 Sergey Y. Afonin <asy@altlinux.ru> 5.1.2-alt1
- New version

* Thu Jan 12 2012 Sergey Y. Afonin <asy@altlinux.ru> 5.1.1-alt2
- added version/release of %name-data subpackage to "Requires"

* Thu Jan 05 2012 Sergey Y. Afonin <asy@altlinux.ru> 5.1.1-alt1
- New version

* Mon Nov 14 2011 Sergey Y. Afonin <asy@altlinux.ru> 5.0.6-alt3
- fixed creating symlink "data" in first installation

* Sun Nov 13 2011 Sergey Y. Afonin <asy@altlinux.ru> 5.0.6-alt2
- moved %_libdir/%binname/data/* to %_datadir/%binname
- separate %name-data subpackage

* Sat Nov 05 2011 Sergey Y. Afonin <asy@altlinux.ru> 5.0.6-alt1
- Initial build for AltLinux
  (based on zyGrib's src.rpm of OpenSUSE and Fedora)
