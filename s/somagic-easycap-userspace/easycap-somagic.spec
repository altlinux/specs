Summary: Somagic EasyCAP tools
Name: somagic-easycap-userspace
Version: 1.0
Release: alt1
Packager: Igor Vlasenko <viy@altlinux.ru>
License: GPL
Group: Graphics
URL: http://code.google.com/p/easycap-somagic-linux/
Source0: %name-%version.tar

BuildRequires: libgcrypt-devel libusb-devel

%description
Linux userspace capture program for the Somagic variants of the EasyCAP:
	* EasyCAP Model DC60, with CVBS, S-VIDEO, AUDIO(L), and AUDIO(R)
          inputs. The uninitialized device shows in lsusb as
          "1c88:0007 Somagic, Inc.". Once initialized, it shows as 
          "1c88:003c Somagic, Inc".
	* EasyCAP Model 002 (or EasyCAP002), with 1, 2, 3, 4, and 
          unlabeled microphone inputs. The uninitialized device shows in
          lsusb as "1c88:0007 Somagic, Inc.". Once initialized, it shows
          as either "1c88:003e Somagic, Inc" or 
          "1c88:003f Somagic, Inc".

This package provides somagic-init (performs user space firmware
upload to the device), and somagic-capture (performs user space
video capture).

This package will soon be obsolete by the proper kernel driver.

%prep
%setup -q

%build
%make_build

%install
%makeinstall_std PREFIX=%buildroot/usr

%files 
%_bindir/*
%_man1dir/*

%changelog
* Wed Oct 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- first build for sisyphus
