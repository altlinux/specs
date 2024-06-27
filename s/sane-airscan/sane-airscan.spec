%define _unpackaged_files_terminate_build 1
%def_with check

Name: sane-airscan
Version: 0.99.29
Release: alt2

Summary: This package contains SANE backend for AirScan (eSCL) and WSD document scanners

License: GPLv2
Group: Graphics
Url: https://github.com/alexpevzner/sane-airscan
#Git: https://github.com/alexpevzner/sane-airscan.git

Source: %name-%version.tar

Patch0: %name-%version-%release.patch

BuildRequires: libavahi-glib-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libsane-devel
BuildRequires: libxml2-devel
BuildRequires: libgnutls-devel
BuildRequires: libtiff-devel

%description
Similar to how most modern network printers support "driverless" printing, using
the universal vendor-neutral printing protocol, many modern network scanners and
MFPs support "driverless" scanning.

Driverless scanning comes in two flavors:

    Apple AirScan or AirPrint scanning (official protocol name is eSCL)
    Microsoft WSD, or WS-Scan (term WSD means "Web Services for Devices)

This backend implements both protocols, choosing automatically between them. It
was successfully tested with many devices from Brother, Canon, Kyocera, Lexmark,
Epson, HP, Ricoh, Samsung and Xerox both in WSD and eSCL modes.

For eSCL devices, Apple maintains a comprehensive list of compatible devices,
but please note, this list contains not only scanners and MFP, but pure printers
as well.

This backend doesn't require to install and doesn't conflict with
vendor-provided proprietary software like ScanGear from Canon, HPLIP from HP and
so on.

%prep
%setup
%patch0 -p1
%ifarch %e2k
# as of lcc 1.27.14
sed -i 's/-Werror/-Wno-error/g' Makefile
%endif

%build
%make_build

%install
%makeinstall_std STRIP=''

%check
%make_build check

%files
%_bindir/*
%config(noreplace) %_sysconfdir/sane.d/*.conf
%config(noreplace) %_sysconfdir/sane.d/dll.d/*
%_libdir/sane/libsane-airscan.so.*
%_man1dir/*.1.xz
%_man5dir/*.5.xz

%changelog
* Thu Jun 27 2024 Michael Shigorin <mike@altlinux.org> 0.99.29-alt2
- E2K: lcc 1.27 ftbfs workaround (ilyakurdyukov@)

* Fri Mar 01 2024 Nikolai Kostrigin <nickel@altlinux.org> 0.99.29-alt1
- new version

* Sat Feb 17 2024 Nikolai Kostrigin <nickel@altlinux.org> 0.99.28-alt1
- new version

* Wed Jan 31 2024 Nikolai Kostrigin <nickel@altlinux.org> 0.99.27-alt2.git3a6fd942
- 0.99.27 plus latest upstream fixes and features
  + fix FTBFS when building against libxml2
  + new models support tested and fixed
- spec: do not use meson for build
  + refer to https://github.com/alexpevzner/sane-airscan/issues/49#issuecomment-657639351
  + remove meson from BR:
- spec: add libtiff-devel to BR: according to upstream codebase changes

* Fri Oct 29 2021 Nikolai Kostrigin <nickel@altlinux.org> 0.99.27-alt1
- new version

* Fri Apr 16 2021 Nikolai Kostrigin <nickel@altlinux.org> 0.99.26-alt1
- new version
  + ready to be built with GCC11
  + contains workaround for some EPSON devices firmware bugs

* Tue Apr 13 2021 Nikolai Kostrigin <nickel@altlinux.org> 0.99.25-alt1
- new version
  + supports automated tests
  + supports blacklisting of unneeded devices discovered on the net
- spec: add check section

* Mon Feb 08 2021 Nikolai Kostrigin <nickel@altlinux.org> 0.99.24-alt1
- new version

* Sat Jan 16 2021 Nikolai Kostrigin <nickel@altlinux.org> 0.99.23-alt1
- new version

* Tue Nov 24 2020 Nikolai Kostrigin <nickel@altlinux.org> 0.99.21-alt1
- new version

* Mon Aug 31 2020 Nikolai Kostrigin <nickel@altlinux.org> 0.99.15-alt1
- new version
  + spec: add libgnutls-devel to and remove libsoup-devel from BR:
  + spec: switch off strip option to provide debuginfo package

* Fri Jul 10 2020 Nikolai Kostrigin <nickel@altlinux.org> 0.99.8-alt1.20200709.git8bba080
- initial build for Sisyphus

