Name: u-boot-sunxi64
Version: 2018.05
Release: alt1

Summary: Das U-Boot
License: GPL
Group: System/Kernel and hardware
Url: http://linux-sunxi.org/U-Boot

ExclusiveArch: aarch64

Source: %name-%version-%release.tar

BuildRequires: bc ccache dtc >= 1.4
BuildRequires: python-devel swig
BuildRequires: python2.7(multiprocessing)
BuildRequires: atf-sunxi

%description
boot loader for embedded boards based on PowerPC, ARM, MIPS and several
other processors, which can be installed in a boot ROM and used to
initialize and test the hardware or to download and run application code.
This package supports various Allwinner H5 based boards.

%prep
%setup

%build
export BL31=%_datadir/atf/sun50iw1p1/bl31.bin
boards=$(grep -lr MACH_SUN50I configs |sed 's,^configs/\(.\+\)_defconfig,\1,')
for board in $boards; do
	mkdir build
	%make_build HOSTCC='ccache gcc' CC='ccache gcc' O=build ${board}_defconfig all
	install -pm0644 -D build/spl/sunxi-spl.bin out/${board}/sunxi-spl.bin
	install -pm0644 build/u-boot.itb out/${board}/u-boot.itb
	rm -rf build
done

%install
mkdir -p %buildroot%_datadir/u-boot
cd out
find . -type f | cpio -pmd %buildroot%_datadir/u-boot

%files
%doc README board/sunxi/README.sunxi64
%_datadir/u-boot/*

%changelog
* Fri Jun 29 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.05-alt1
- 2018.05 released

* Thu Apr 19 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2018.03-alt1
- 2018.03 released

* Sun Sep 24 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2017.09-alt1
- 2017.09 released

* Fri Feb 17 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2017.01-alt1
- 2017.01 released

* Sun Sep 04 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2016.07-alt1
- 2016.07 released

* Tue Apr 14 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2015.04-alt1
- 2015.04 released

* Tue Jan 13 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 2015.01-alt1
- 2015.01 released

* Tue Jun 10 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2014.04-alt1
- 2014.04-sunxi released

* Mon Feb 17 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 2013.10-alt1
- 2013.10-sunxi released

* Fri Sep 27 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2013.07-alt2
- 2013.07-sunxi released

* Wed Aug 07 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2013.07-alt1
- initial
