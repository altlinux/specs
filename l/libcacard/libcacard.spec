%def_enable pcsc
%def_disable static
%def_enable test

Name: libcacard
Version: 2.8.1
Release: alt1
Summary: Common Access Card (CAC) Emulation
Group: System/Libraries
License: LGPLv2.1+
Url: http://www.spice-space.org/download
# https://gitlab.freedesktop.org/spice/libcacard.git
Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(glib-2.0) >= 2.32
BuildRequires: pkgconfig(nss) >= 3.12.8
%{?_enable_pcsc:BuildRequires: pkgconfig(libpcsclite)}
%{?_enable_test:BuildRequires: openssl gnutls-utils nss-utils opensc softhsm}

%description
Common Access Card (CAC) emulation library.

%package devel
Summary: CAC Emulation devel
Group: Development/C
Requires: %name = %version-%release

%description devel
CAC emulation development files.

%prep
%setup
echo "%version" > .tarball-version

%build
%meson \
	%{?_enable_pcsc:-Dpcsc=enabled} \
	%{?_disable_test:-Ddisable_tests=true}

%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc COPYING README.md NEWS
%_libdir/libcacard.so.*

%files devel
%_includedir/cacard
%_pkgconfigdir/*.pc
%_libdir/libcacard.so

%changelog
* Mon Nov 01 2021 Alexey Shabalin <shaba@altlinux.org> 2.8.1-alt1
- new version 2.8.1

* Sat Nov 14 2020 Alexey Shabalin <shaba@altlinux.org> 2.8.0-alt1
- new version 2.8.0

* Fri Aug 02 2019 Alexey Shabalin <shaba@altlinux.org> 2.7.0-alt1
- new version 2.7.0

* Fri Feb 15 2019 Alexey Shabalin <shaba@altlinux.org> 2.6.1-alt2
- really build 2.6.1
- fixed build with autoconf-archive-2019.01.06

* Tue Oct 16 2018 Alexey Shabalin <shaba@altlinux.org> 2.6.1-alt1
- new version 2.6.1

* Sat Aug 18 2018 Alexey Shabalin <shaba@altlinux.org> 2.6.0-alt1
- 2.6.0
- remove vscclient, drop libcacard-tools

* Wed Dec 13 2017 Alexey Shabalin <shaba@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Wed Sep 27 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.5.2-alt2
- Fixes:
  + CVE-2017-6414 Memory leak in the vcard_apdu_new function in card_7816.c

* Thu Dec 17 2015 Alexey Shabalin <shaba@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Wed Jan 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt2
- fix pkg-config file

* Wed Jan 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- initial build for ALT Linux Sisyphus
