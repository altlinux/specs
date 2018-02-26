Name: tvflash
Version: 0.9.0
Release: alt1
Summary: Tool to manage Mellanox HCA firmware flash memory
License: %gpl2only
Group: System/Configuration/Hardware
Url: http://openib.org
Source: %name-%version.tar
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: libpci-devel zlib-devel

%description
%name is used to query and update the firmware flash memory attached
to Mellanox InfiniBand HCAs.


%prep
%setup
touch AUTHORS


%build
%autoreconf
%configure
%make_build


%install
%make_install DESTDIR=%buildroot install


%files
%doc README NEWS
%_sbindir/*

%changelog
* Mon Oct 27 2008 Led <led@altlinux.ru> 0.9.0-alt1
- initial build
