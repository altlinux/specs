Summary: utility to change location / fault LED for enclosure
Name: encled
Version: 2015
Release: alt1
License: GPLv2
Group: System/Configuration/Hardware
Url: https://github.com/amarao/sdled
Source0: %name-%version.tar
BuildArch: noarch

%description
Encled - utility to change location / fault LED for enclosure.

I'm not sure if it works with every avaible enclosures, but at least it
works with Supermicro chases with SAS enclosures (LSI).

Encled heavily depends on linux kernel's /sys/class/enclosure

Previous name was sdled, but now it supports not only 'sd' devices
but empty disk slots too.

    Usage:

    encled (without options) - display all slots devices status and disk letter
    encled enclosure/slot - display status of requested device
    encled enclosure/slot fault - set led indicator to 'faulty'
                          this WILL NOT make device faulty, just set
                          enclosure led to 'FAULTY' status.
    encled enclosure/slot locate - set led indicator to 'locate' status
    encled enclosure/slot off - turn of faulty/locate status
    encled device locate/fault/off will work with sd device (sda, sde)

    encled ALL off
    encled ALL fault
    encled ALL locate - turn all devices to that status (note CAPS ALL)

    examples:
        encled 4:0:1:0/12 - show status for enclosure 4:0:1:0 slot 12
        encled ALL off - disable all indication for all slots in all enclosures
        encled 5:0:24:0/24 fault - set fault indicator for enclosure 5:0:24:0 slot 24
        encled 5:0:24:0/12 locate - set location indicator for enclosure 5:0:24:0 slot 12
    encled sda locate - enable 'locate' for slot with sda block device
    encled /dev/sdbz fault - enable fault indicator slot with sdbz block device

%prep
%setup
%build
%install
install -p -m 755 -D encled %buildroot%_sbindir/encled
install -p -m 755 -D sdled %buildroot%_sbindir/sdled

%files
%_sbindir/encled
%_sbindir/sdled
%doc README

%changelog
* Sun Apr  5 2015 Terechkov Evgenii <evg@altlinux.org> 2015-alt1
- Initial build for ALT Linux Sisyphus
