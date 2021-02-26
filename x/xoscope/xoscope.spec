# TODO: see https://github.com/imrehg/xoscope

Name: xoscope
Version: 2.2
Release: alt3

Summary: xoscope: digital oscilloscope

Url: http://xoscope.sourceforge.net/
Group: Engineering
License: GPL

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://prdownloads.sourceforge.net/project/xoscope/xoscope/%version/xoscope-%version.tar.gz
Source: %name-%version.tar

Patch1: %name-gcc10.patch

BuildRequires: libICE-devel libalsa-devel libcomedi-devel libfftw3-devel libgtkdatabox-devel

%description
xoscope: digital oscilloscope

%prep
%setup
%patch1 -p1

%build
%configure
%make_build

%install
%makeinstall_std


%files
%_bindir/xoscope
%_desktopdir/*.desktop
%_man1dir/*
%_datadir/metainfo/*
%_pixmapsdir/*
%doc README AUTHORS NEWS TODO

%changelog
* Fri Feb 26 2021 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt3
- fix build with gcc10

* Thu Aug 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt2
- rebuild without esound support (libesd-devel)

* Fri Dec 29 2017 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- initial build for ALT Sisyphus

