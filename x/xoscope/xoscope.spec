Name: xoscope
Version: 2.2
Release: alt2

Summary: xoscope: digital oscilloscope

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://prdownloads.sourceforge.net/project/xoscope/xoscope/%version/xoscope-%version.tar.gz
Source: %name-%version.tar

Url: http://xoscope.sourceforge.net/
Group: Engineering
License: GPL

BuildRequires: libICE-devel libalsa-devel libcomedi-devel libfftw3-devel libgtkdatabox-devel

%description
xoscope: digital oscilloscope

%prep
%setup

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
* Thu Aug 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt2
- rebuild without esound support (libesd-devel)

* Fri Dec 29 2017 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- initial build for ALT Sisyphus

