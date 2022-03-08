Name:		psensor
Version:	1.2.1
Release:	alt1

Summary:	A Graphical Temperature Monitor
License:	GPLv2
Group:		System/Kernel and hardware

Url:		http://wpitchoune.net/blog/psensor/

# Source-git: https://gitlab.com/jeanfi/psensor
Source0:	%name-%version.tar

Patch1:		0001-fix-compilation-with-microhttpd-since-version-0.9.71.patch

BuildRequires: libsensors-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libgtk+3-devel
BuildRequires: libudisks2-devel
BuildRequires: libatasmart-devel
BuildRequires: libnotify-devel
BuildRequires: libappindicator-gtk3-devel
BuildRequires: libcurl-devel
BuildRequires: libjson-c-devel
BuildRequires: nvidia-settings-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: libgtop2-devel
BuildRequires: help2man
BuildRequires: asciidoctor
BuildRequires: cppcheck

Requires:	lm_sensors hddtemp

%description
Psensor is a graphical hardware temperature monitor for Linux.
It can monitor:
* the temperature of the motherboard and CPU sensors (using lm-sensors).
* the temperature of the NVidia GPUs (using XNVCtrl).
* the temperature of ATI/AMD GPUs (not enabled in Ubuntu PPAs or official
  distribution repositories, see the instructions for enabling its support).
* the temperature of the Hard Disk Drives (using hddtemp or libatasmart).
* the rotation speed of the fans (using lm-sensors).
* the CPU usage (since 0.6.2.10 and using Gtop2).

%prep
%setup -q
%patch1 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing -Wno-error=incompatible-pointer-types -Wno-misleading-indentation"
%autoreconf
%configure
%__make -j1

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_datadir/applications/%name.desktop
%_datadir/glib-2.0/schemas/psensor.gschema.xml
%_man1dir/%{name}*.1.*
%_datadir/%name
%_datadir/icons/*/*/*/%{name}*
%doc %_datadir/doc/*
%_bindir/%{name}*
%exclude %_docdir/%name/COPYING
%exclude %_datadir/icons/ubuntu*

%changelog
* Sun Oct 03 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.2.1-alt1
- Initial build in Sisyphus (thanks Fedora for the spec)

