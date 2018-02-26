Name: macchanger
Version: 1.5
Release: alt1

Summary: utility for viewing/manipulating the MAC address of network interfaces
License: GPL v2+
Group: Networking/Other
Url: http://www.alobbs.com/macchanger
Packager: Maxim Ivanov <redbaron@altlinux.org>

Source: %url/%name-%version.tar

%description
Features:
- Set specific MAC address of a network interface
- Set the MAC randomly
- Set a MAC of another vendor
- Set another MAC of the same vendor
- Set a MAC of the same kind (eg: wireless card)
- Display a vendor MAC list (today, 6800 items) to choose from
%prep
%setup

%build
#%autoreconf
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%_bindir/*
%_datadir/%name
%_man1dir/*
%_infodir/*
#%_sbindir/*
#%doc %_docdir/*

%changelog
* Sun Mar 01 2009 Maxim Ivaniv <redbaron at altlinux.org> 1.5-alt1
- Initial build for Sisyphus 

