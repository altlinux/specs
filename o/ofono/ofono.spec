%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define _udevrulesdir /lib/udev/rules.d

%def_with check

Name: ofono
Version: 2.19
Release: alt1

Summary: Mobile telephony stack
License: GPL-2.0
Group: Communications
Url: https://git.kernel.org/pub/scm/network/ofono/ofono.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(ell)

%description
oFono is a stack for mobile telephony devices on Linux. oFono supports
speaking to telephony devices through specific drivers, or with generic
AT commands.

oFono also includes a low-level plug-in API for integrating with other
telephony stacks, cellular modems and storage back-ends. The plug-in API
functionality is modeled on public standards, in particular 3GPP TS
27.007 "AT command set for User Equipment (UE)."

This package includes the core daemon.

%package devel
Summary: Development files for oFono
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description devel
oFono is a stack for mobile telephony devices on Linux. oFono supports
speaking to telephony devices through specific drivers, or with generic
AT commands.

oFono also includes a low-level plug-in API for integrating with other
telephony stacks, cellular modems and storage back-ends. The plug-in API
functionality is modeled on public standards, in particular 3GPP TS
27.007 "AT command set for User Equipment (UE)."

This package includes the header files for building oFono plugins.

%prep
%setup

%build
if [ ! -f configure ]; then
./bootstrap
fi
%configure \
           --prefix=%_prefix \
           --sysconfdir=%_sysconfdir \
           --localstatedir=%_var \
           --sbindir=%_sbindir \
           --enable-external-ell \
           --enable-test \
           --enable-tools \
           --enable-dundee \
           --with-systemdunitdir=%_unitdir
%make_build

%install
%makeinstall_std

install -D -m 0644 plugins/ofono.rules %buildroot%_udevrulesdir/97-ofono.rules
install -D -m 0644 plugins/ofono-speedup.rules %buildroot%_udevrulesdir/97-ofono-speedup.rules

%check
%make_build -j1 check

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_sysconfdir/dbus-1/system.d/dundee.conf
%_sysconfdir/dbus-1/system.d/ofono.conf
%dir %_sysconfdir/ofono
%_sysconfdir/ofono/phonesim.conf
%_unitdir/dundee.service
%_unitdir/ofono.service
%_udevrulesdir/97-ofono.rules
%_udevrulesdir/97-ofono-speedup.rules
%_sbindir/dundee
%_sbindir/ofonod
%_man8dir/ofonod.8.*
%dir %_datadir/ofono
%_datadir/ofono/provision.db

%files devel
%doc HACKING examples
%dir %_includedir/ofono
%_includedir/ofono/*
%dir %_libdir/ofono
%_libdir/ofono/*
%_pkgconfigdir/ofono.pc

%changelog
* Sun Nov 23 2025 Nikolay Strelkov <snk@altlinux.org> 2.19-alt1
- New version 2.19.

* Sun Nov 09 2025 Nikolay Strelkov <snk@altlinux.org> 2.18-alt1
- New version 2.18.

* Mon Jul 14 2025 Nikolay Strelkov <snk@altlinux.org> 2.17-alt1
- Initial build for Sisyphus
