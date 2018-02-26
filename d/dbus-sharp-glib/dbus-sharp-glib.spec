
Summary: C# bindings for D-Bus glib main loop integration
Name: dbus-sharp-glib
Version: 0.5.0
Release: alt1
Url: http://mono.github.com/dbus-sharp/
Packager: Mono Maintainers Team <mono@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch
License: MIT
Group: Development/Other

BuildPreReq: /proc
BuildRequires: mono-mcs mono-devel
BuildRequires: dbus-sharp-devel >= 0.7.0

%description
C# bindings for D-Bus glib main loop integration

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
%_monodir/dbus-sharp-glib-1.0
%_monogacdir/dbus-sharp-glib

%files devel
%_pkgconfigdir/dbus-sharp-glib-1.0.pc

%changelog
* Mon Feb 20 2012 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- initial build for ALT Linux Sisyphus
