%def_enable pcsc
%def_disable static

Name: libcacard
Version: 2.5.3
Release: alt1%ubt
Summary: Common Access Card (CAC) Emulation
Group: System/Libraries
License: LGPLv2.1+
Url: http://www.spice-space.org/download
# git://anongit.freedesktop.org/spice/libcacard
Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: pkgconfig(glib-2.0) >= 2.22 pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(nss) >= 3.12.8
%{?_enable_pcsc:BuildRequires: pkgconfig(libpcsclite)}

%description
Common Access Card (CAC) emulation library.

%package tools
Summary: CAC Emulation tools
Group: Development/Other
Requires: %name = %version-%release

%description tools
CAC emulation tools.

%package devel
Summary: CAC Emulation devel
Group: Development/C
Requires: %name = %version-%release

%description devel
CAC emulation development files.

%prep
%setup
%patch -p1
echo "%version" > .tarball-version

%build
%autoreconf
%configure \
		%{subst_enable pcsc} \
		%{subst_enable static}

%make_build

%install
%makeinstall_std

%files
%doc COPYING README.md NEWS
%_libdir/libcacard.so.*

%files devel
%_includedir/cacard
%_pkgconfigdir/*.pc
%_libdir/libcacard.so

%files tools
%_bindir/vscclient

%changelog
* Wed Dec 13 2017 Alexey Shabalin <shaba@altlinux.ru> 2.5.3-alt1%ubt
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
