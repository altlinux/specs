Summary: C# bindings for D-Bus
Name:    dbus-sharp
Version: 0.8.1
Release: alt1

Url: https://github.com/mono/dbus-sharp

Source:  %name-%version.tar
License: MIT
Group:   Development/Other

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

%build
%autoreconf
%configure --libdir=%_libexecdir
%make

%install
%makeinstall_std pkgconfigdir=%_pkgconfigdir

%files
%doc AUTHORS COPYING README
%_monodir/dbus-sharp-2.0
%_monogacdir/dbus-sharp

%files devel
%_pkgconfigdir/dbus-sharp-2.0.pc

%changelog
* Thu Jun 09 2016 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt1
- new version 0.8.1

* Mon Feb 20 2012 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- initial build for ALT Linux Sisyphus
