Name: scanbuttond
Version: 0.2.3
Release: alt4

Summary: Scanner Button tools to SANE

Group: System/Libraries
License: GPL
Url: http://scanbuttond.sf.net

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version.tar
Source1: scanbuttond.init
Source2: initscanner.sh
Source3: buttonpressed.sh
Source4: scanbuttond.conf
Patch0: scanbuttond-0.2.3.diff

# Automatically added by buildreq on Sat Jan 06 2007
BuildRequires: gcc-c++ libusb-compat-devel

%description
Modern scanners usually have several front panel buttons which are intended to
trigger certain actions like copying, faxing or mailing the scanned document.
This daemon monitors the scanner's buttons and runs a shell script whenever one
of these buttons has been pressed. Because it is accessing the scanner directly
via libusb, there should be no conflicts with SANE or other scanner drivers:
scanbuttond simply won't touch the scanner hardware while you are using SANE.

See http://www.linux.com/print.pl?sid=06/12/18/1937227 for examples.

%prep
%setup -q
%patch0 -p1

%build
%autoreconf
%configure --libdir=%_libdir/%name
%make_build

%install
%makeinstall_std

rm -rf %buildroot%_libdir/%name/*.{la,so}
rm -rf %buildroot%_sysconfdir/scanbuttond/*.sh

mkdir -p -m 755 %buildroot{%_initdir/,%_sysconfdir/sysconfig/}
install -c -m 755 %SOURCE1 %buildroot%_initdir/%name
install -m 755 %SOURCE2 %buildroot%_sysconfdir/%name/
install -m 755 %SOURCE3 %buildroot%_sysconfdir/%name/
install -m 644 %SOURCE4 %buildroot%_sysconfdir/sysconfig/%name

%files
%doc README AUTHORS ChangeLog
%_bindir/%name
%_libdir/%name/
%_initdir/%name
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/meta.conf
%_sysconfdir/%name/*.sh
%config(noreplace) %_sysconfdir/sysconfig/%name

%changelog
* Sat Oct 29 2011 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt4
- remove evolution, gimp deps (ALT bug #26516)

* Tue Apr 28 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt3
- fix build, remove ldconfig from post/postun script

* Mon Jan 28 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt2
- add config in sysconfig
- fix Canon LIDE25 problem (set -r 1000000 option)

* Sat Dec 29 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt1
- add autoreconf due new autotools

* Sat Jan 06 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt0.1
- initial build for ALT Linux Sisyphus

* Mon Oct 16 2006 Parag Nemade <panemade@gmail.com>- 0.2.3-9
- Got CVS tagging problem as usual to me
- so increasing release number

* Mon Oct 16 2006 Parag Nemade <panemade@gmail.com>- 0.2.3-8
- corrected scanbuttond.init which i hacked from lisa daemon

* Thu Oct 12 2006 Parag Nemade <panemade@gmail.com>- 0.2.3-7
- missing directory ownership Fixed

* Wed Oct 11 2006 Parag Nemade <panemade@gmail.com>- 0.2.3-6
- Move libscanbtnd*so to %%{_libdir}/scanbuttond.
- Let the app dlopen *.so.1 instead of *.so.

* Tue Oct 10 2006 Parag Nemade <panemade@gmail.com>- 0.2.3-5
- wrong preun call for ldconfig fix to postun

* Tue Oct 05 2006 Parag Nemade <panemade@gmail.com>- 0.2.3-4
- Some SPEC file Fixes

* Tue Oct 03 2006 Parag Nemade <panemade@gmail.com>- 0.2.3-3
- Chmod'd Source1-3 644, to avoid rpmlint error on SRPM
- Fixed error that installs Source1 *in* %%{_initrddir}/scannerbuttond/
- Renamed Source1 to scanbuttond.init

* Tue Oct 03 2006 Parag Nemade <panemade@gmail.com>- 0.2.3-2
- Initial Release
