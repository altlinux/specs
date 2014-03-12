Name:    libudev0
Version: 1.0
Release: alt1

Summary: Compatible library for legacy applications working with new udev
License: LGPLv2.1+
Group:   System/Libraries
URL:     http://altlinux.org
Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: libudev1

%description
Compatible library for legacy applications working with new udev.

%install
mkdir -p %buildroot/%_lib
cp -a /%_lib/libudev.so.1.* %buildroot/%_lib/
ln -s $(basename `ls %buildroot/%_lib/libudev.so.1.*`) \
       %buildroot/%_lib/libudev.so.0

%files
/%_lib/libudev.so.0
%exclude /%_lib/libudev.so.1*

%changelog
* Wed Mar 12 2014 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for ALT Linux
