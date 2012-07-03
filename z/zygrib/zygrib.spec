%define binname zyGrib

Name: zygrib
Version: 5.1.3
Release: alt2

Summary: Visualisation of meteo data from files in GRIB Format 1

License: %gpl3plus
Group: Networking/Other
Url: http://www.zygrib.org
Source0: %binname-%version.tgz
Source1: %binname.png
Source2: %binname.desktop

Patch1: zyGrib-5.1.1-qwt.patch
Patch2: zyGrib-5.1.1-remove-system-libs.patch
Patch3: zyGrib-0001-fix-for-new-Proj.patch

Requires: fonts-ttf-liberation
Requires: %name-data = %{version}-%{release}

# Automatically added by buildreq on Sat Nov 05 2011
BuildRequires: bzlib-devel gcc-c++ libproj-devel libqt4-devel libqwt6-devel

BuildRequires: rpm-build-licenses

%description
Visualization of meteo data from files in GRIB Format 1
Grib data are used to display weather data in detailed format for
a certain area of sea. ZYGrib is a QT4 program to display and use
grib data on Linux.

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

#patch1 -p1

# remove system-wide libraries
%patch2 -p1
rm -rf src/bzip2
rm -rf src/zlib-*
rm -rf src/proj-*

%patch3 -p2

# remove system-wide fonts
rm -rf data/fonts

# remove precompiled binary
rm -f src/sha1/testsha1

%build

%make QTBIN=%_libdir/qt4/bin

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
