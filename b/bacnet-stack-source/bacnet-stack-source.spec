Name: bacnet-stack-source
Version: 0.8.5
Release: alt1.r3187

Summary: Data Communication Protocol for Building Automation and Control Networks
License: GPLv2+
Group: Development/Other
Url:https://sourceforge.net/projects/bacnet

Packager: Anton Midyukov <antohami@altlinux.org>

Source: bacnet-stack-%version.tar
Patch: fix-compile.patch

Buildarch: noarch

%description
BACnet - Data Communication Protocol for Building Automation and Control Networks
- see www.bacnet.org. This BACnet library provides an application layer, network
layer and MAC layer communications services for Win32, Linux, RTOS, or
microcontroller.

%prep
%setup -n bacnet-stack-%version
%patch -p2

%build

%install
mkdir -p %buildroot%_prefix/src/bacnet-stack
cp -r * %buildroot%_prefix/src/bacnet-stack
rm -fr %buildroot%_prefix/src/bacnet-stack/doc
rm -fr %buildroot%_prefix/src/bacnet-stack/demo/perl
rm -fr %buildroot%_prefix/src/bacnet-stack/*.{sh,bat}

%files
%_prefix/src/bacnet-stack
%doc doc/

%changelog
* Sun Aug 12 2018 Anton Midyukov <antohami@altlinux.org> 0.8.5-alt1.r3187
- Initial build for ALT Sisyphus
