Name:		cpu-g
Version:	0.9.0
Release:	alt1

License:	GPLv3
Group:		System/Kernel and hardware
Summary:	CPU-G is an application that shows useful information about your hardware
Url:		http://sourceforge.net/projects/cpug/

Source0:	%name-%version.tar.gz
Patch0:		cpu-g-patch.patch

BuildArch: noarch

Requires: python-module-pygtk-libglade

%description
CPU-G is an application that shows useful information about your hardware.
It collects and displays information about your CPU, RAM, Motherboard, some
general information about your system and more.

%prep
%setup -n %name-%version
%patch0

%install
%__mkdir -p %buildroot/%_datadir/{%name,applications,pixmaps}
%__mkdir -p %buildroot/%_datadir/%name/data/logos
%__mkdir -p $RPM_BUILD_ROOT/%_bindir

%__install -m 755 %name %buildroot/%_datadir/%name
%__install -m 644 %name.glade %buildroot/%_datadir/%name
%__install -m 644 data/*.png %buildroot/%_datadir/%name/data
%__install -m 644 data/logos/* %buildroot/%_datadir/%name/data/logos
%__install -m 644 data/%name.png %buildroot/%_datadir/pixmaps
%__install -m 644 data/%name.desktop %buildroot/%_desktopdir
ln -s %_datadir/%name/%name $RPM_BUILD_ROOT%_bindir/%name

%files
%dir %_datadir/%name
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_datadir/pixmaps/%name.png
%doc COPYING
%doc README
%doc doc/cpu-g.1

%changelog
* Thu Mar 31 2016 Motsyo Gennadi <drool@altlinux.ru> 0.9.0-alt1
- initial build for ALT Linux
