Name: xoscope
Version: 2.2
Release: alt1

Summary: xoscope: digital oscilloscope

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://prdownloads.sourceforge.net/project/xoscope/xoscope/%version/xoscope-%version.tar.gz
Source: %name-%version.tar

Url: http://xoscope.sourceforge.net/
Group: Engineering
License: GPL

# Automatically added by buildreq on Fri Dec 29 2017
# optimized out: fontconfig fontconfig-devel glib2-devel glibc-kernheaders-x86 libX11-devel libatk-devel libaudiofile-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libpango-devel libwayland-client libwayland-server perl pkg-config python-base python-modules python3 python3-base shared-mime-info sssd-client xorg-xproto-devel
BuildRequires: libICE-devel libalsa-devel libcomedi-devel libesd-devel libfftw3-devel libgtkdatabox-devel

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
* Fri Dec 29 2017 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- initial build for ALT Sisyphus

