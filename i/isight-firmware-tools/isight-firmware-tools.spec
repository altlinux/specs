Name: isight-firmware-tools
Version: 1.6
Release: alt1

Summary: Apple Built-In iSight Firmware Tools
License: GPL
Group: System/Kernel and hardware
Url: https://launchpad.net/isight-firmware-tools/main

Packager: Igor Zubkov <icesik@altlinux.org>

Source: %name-%version.tar.gz
Patch0: isight-firmware-tools-1.5.90-alt.patch

# Automatically added by buildreq on Thu Apr 12 2012 (-bi)
# optimized out: elfutils libgpg-error-devel libusb-compat perl-XML-Parser pkg-config python-base
BuildRequires: glib2-devel intltool libgcrypt-devel libusb-compat-devel

%description
Apple Built-In iSight Firmware Tools.

%prep
%setup -q
%patch0 -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name

rm -rf %buildroot%_datadir/doc/isight-firmware-tools/

%files -f %name.lang
%doc AUTHORS ChangeLog HOWTO NEWS README
%_sysconfdir/udev/rules.d/isight.rules
/lib/udev/ift-load
%_bindir/*
%_infodir/*
%_man1dir/*

%changelog
* Thu Apr 12 2012 Igor Zubkov <icesik@altlinux.org> 1.6-alt1
- 1.5.90 -> 1.6
- Fix repocop warning

* Fri Nov 13 2009 Igor Zubkov <icesik@altlinux.org> 1.5.90-alt1
- 1.4.1 -> 1.5.90

* Mon Apr 06 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.4.1-alt1
- 1.4.1 release.
- build with libusb-compat.

* Wed Oct 22 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.2-alt1
- 1.2 release.

* Tue Mar 11 2008 Pavlov Konstantin <thresh@altlinux.org> 1.0.2-alt1
- Initial build for ALT Linux.

