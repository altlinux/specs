%def_disable passthru
%def_disable static

Name: libcacard
Version: 0.1.2
Release: alt1.1
Summary: Common Access Card (CAC) Emulation
Group: System/Libraries
License: LGPLv2+
Url: http://www.spice-space.org/download

Source: http://www.spice-space.org/download/libcacard/libcacard-%version.tar
Patch: %name-%version-%release.patch
Patch1: %name-0.1.2-alt-DSO.patch
BuildRequires: libnss-devel
%{?_enable_passthru:BuildRequires: libpcsclite-devel}

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
%patch1 -p0

%build
%autoreconf
%configure \
		%{subst_enable passthru} \
		%{subst_enable static}

%make_build

%install
%makeinstall_std

%files
%doc COPYING README
%_libdir/libcacard.so.*

%files devel
%_includedir/cacard
%_pkgconfigdir/*.pc
%_libdir/libcacard.so

%files tools
%_bindir/vscclient

%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.1
- Fixed build

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Wed Jan 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt2
- fix pkg-config file

* Wed Jan 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- initial build for ALT Linux Sisyphus
