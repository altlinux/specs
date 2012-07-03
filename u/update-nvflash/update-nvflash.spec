Name: update-nvflash
Version: 20110628
Release: alt1
Group: Development/Other
URL: http://ac100.grandou.net/nvflash#debian_ubuntu_package
Packager: Paul Wolneykien <manowar@altlinux.ru>
Summary: Nvidia flash tools for Tegra2 devices
License: GPL v2.0+

Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

%description
Nvflash is the nvidia tool used read and modify flash from tegra2 devices.

Unfortunately the communication protocol is not documented and nvflash is 
only distributed in the form of a binary package. No source are available.

This package does not contains the actual nvflash tool.
To downloaded it from the nvidia website use `update-nvflash' command.

%prep
%setup
%patch -p1

%install
install -m0755 -D update-nvflash %buildroot%_bindir/update-nvflash
install -m0644 -D files.conf %buildroot%_datadir/%name/files.conf
install -m0644 -D debian/nvflash.udev %buildroot/lib/udev/rules.d/60-nvflash.rules

%files
%_bindir/*
%_datadir/%name
/lib/udev/rules.d/*.rules
%doc debian/changelog

%changelog
* Thu Jan 05 2012 Paul Wolneykien <manowar@altlinux.ru> 20110628-alt1
- Initial build for ALT Linux.
