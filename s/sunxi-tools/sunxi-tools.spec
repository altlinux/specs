Name: sunxi-tools
Version: 1.5
Release: alt0.20231025
Epoch: 1

Summary: Tools for use with Allwinner SoC based devices
License: GPLv2
Group: System/Kernel and hardware
Url: http://linux-sunxi.org

Source0: %name-%version-%release.tar
Source1: boards-%version-%release.tar

BuildRequires: libfdt-devel libusb-devel zlib-devel
BuildRequires: arm-none-eabi-gcc u-boot-tools >= 2023.10-alt2

%description
Tools to help hacking Allwinner SoC (aka sunxi) based devices.

%prep
%setup

%build
%make_build tools binfiles

%install
%make_install DESTDIR=%buildroot PREFIX=%prefix install
mkdir -p %buildroot%_datadir/sunxi-tools
cp -pv *.sunxi %buildroot%_datadir/sunxi-tools/
tar xf %SOURCE1 -C %buildroot%_datadir/sunxi-tools

%files
%doc README.md
%_bindir/*
%_datadir/sunxi-tools
%_man1dir/sunxi-fel.1*

%changelog
* Tue Oct 31 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.5-alt0.20231025
- updated from git.91f9ccfc

* Fri Oct 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.5-alt0.20220729
- up to 5cf618a

* Wed Aug 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.5-alt0.20210315
- updated from git.6c02224

* Tue Jan 22 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.5-alt0.1
- 1.5 rc1

* Wed Nov 07 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.4.2-alt1
- 1.4.2

* Thu Oct 27 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.4-alt1
- 1.4 released

* Tue Feb 18 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 20140131-alt1
- updated from git.271130b3

* Wed Aug 07 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 20130727-alt1
- initial
