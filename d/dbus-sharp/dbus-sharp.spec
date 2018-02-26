
Summary: C# bindings for D-Bus
Name: dbus-sharp
Version: 0.7.0
Release: alt1

Url: http://mono.github.com/dbus-sharp/

Source: %name-%version.tar
Patch: %name-%version-%release.patch
License: MIT
Group: Development/Other

Packager: Mono Maintainers Team <mono@packages.altlinux.org>

BuildPreReq: /proc
BuildRequires: mono-mcs mono-devel

%description
D-Bus mono bindings for use with mono programs.

%package devel
Summary: Development files for D-Bus Sharp
Group: Development/Other
Requires: %name = %version-%release

%description devel
Development files for D-Bus Sharp development.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING README
%_monodir/dbus-sharp-1.0
%_monogacdir/dbus-sharp

%files devel
%_pkgconfigdir/dbus-sharp-1.0.pc

%changelog
* Mon Feb 20 2012 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- initial build for ALT Linux Sisyphus
