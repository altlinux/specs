Name: uaputl
Version: 1.12
Release: alt1

Summary: Issuing commands to the wireless driver for setting up AP parameters
License: GPLv2
Group: System/Kernel and hardware
URL: http://www.plugcomputer.org/plugwiki/index.php/Setting_GuruPlug_to_be_a_WiFi_Access_Point

Packager: Paul Wolneykien <manowar@altlinux.ru>

Source: %name-%version.tar
Patch0: autotools.patch
Patch1: remove-exe-suffix.patch
Patch2: cleanup-source.patch

%description
A userspace utility to be used for issuing commands to the wireless
driver for setting up AP parameters.
Run /sbin/uaputl --help to have a look at the available options.

The /sbin/uapevent can be used to monitor the AP state and events.

%define uapdir uap

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure --with-confsubdir=%uapdir
%make_build

%install
%makeinstall sbindir=%buildroot/sbin

%files
%doc INSTALL README COPYING AUTHORS NEWS ChangeLog
/sbin/*
%dir %_sysconfdir/%uapdir
%_sysconfdir/%uapdir/*.conf

%changelog
* Tue Jun 21 2011 Paul Wolneykien <manowar@altlinux.ru> 1.12-alt1
- Use the uaputl reported version as the package version.
- Add the uapevent program.

* Tue Jun 21 2011 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt1
- Initial version for ALTLinux
