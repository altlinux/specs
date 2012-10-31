Summary: Somagic EasyCAP tools
Name: somagic-easycap-tools
Version: 1.0
Release: alt1
Packager: Igor Vlasenko <viy@altlinux.ru>
License: GPL
Group: Graphics
URL: http://code.google.com/p/easycap-somagic-linux/
Source0: %name-%version.tar

BuildRequires: libgcrypt-devel

%description
Linux capture program for the Somagic variants of the EasyCAP:
	* EasyCAP Model DC60, with CVBS, S-VIDEO, AUDIO(L), and AUDIO(R)
          inputs. The uninitialized device shows in lsusb as
          "1c88:0007 Somagic, Inc.". Once initialized, it shows as 
          "1c88:003c Somagic, Inc".
	* EasyCAP Model 002 (or EasyCAP002), with 1, 2, 3, 4, and 
          unlabeled microphone inputs. The uninitialized device shows in
          lsusb as "1c88:0007 Somagic, Inc.". Once initialized, it shows
          as either "1c88:003e Somagic, Inc" or 
          "1c88:003f Somagic, Inc".
	. 
	This package provides somagic-extract-firmware (to extract 
        firmware from a Windows driver).

%prep
%setup -q

%build
#pushd tools/somagic-extract-firmware
%make_build
#popd

%install
#pushd tools/somagic-extract-firmware
%makeinstall_std PREFIX=%buildroot/usr
#popd

%files 
%_bindir/*
%_man1dir/*

%changelog
* Wed Oct 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- first build for sisyphus

