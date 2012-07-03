Name: seabios
Version: 1.7.0
Release: alt1
Summary: Open-source legacy BIOS implementation

Group: Emulators
License: LGPLv3
Url: http://www.coreboot.org/SeaBIOS

Source: %name-%version.tar

BuildRequires: python-base

%description
SeaBIOS is an open-source legacy BIOS implementation which can be used as
a coreboot payload. It implements the standard BIOS calling interfaces
that a typical x86 proprietary BIOS implements.

%prep
%setup -q

# Makefile changes version to include date and buildhost
%__subst 's,VERSION=%version.*,VERSION=%version,g' Makefile

%build
export CFLAGS="$RPM_OPT_FLAGS"
%make

%install
mkdir -p %buildroot%_libexecdir/%name
install -m 0644 out/bios.bin %buildroot%_libexecdir/%name

%files
%doc COPYING COPYING.LESSER README TODO
%dir %_libexecdir/%name
%_libexecdir/%name/bios.bin

%changelog
* Tue May 22 2012 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Mon Mar 12 2012 Alexey Shabalin <shaba@altlinux.ru> 1.6.3.2-alt1
- 1.6.3.2

* Fri Dec 02 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.3.1-alt1
- 1.6.3.1

* Thu Oct 13 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Thu Aug 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1.git8e3014
- upstream git snapshot 8e301472e324b6d6496d8b4ffc66863e99d7a505

* Fri Feb 04 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.1.3-alt1
- 0.6.1.3

* Fri Dec 24 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.1.2-alt1
- initial build for ALT Linux Sisyphus
