%define oname RemoteBox
Name: remotebox
Version: 2.4
Release: alt1

Summary: Open Source VirtualBox Client with Remote Management

Group: System/Servers
License: GPL
Url: http://remotebox.knobgoblin.org.uk/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://remotebox.knobgoblin.org.uk/downloads/%oname-%version.tar

BuildArch: noarch

Autoreq: yes,noperl

%add_perl_lib_path %_datadir/%name

# Automatically added by buildreq on Tue Oct 26 2010 (-bi)
BuildRequires: perl-Gtk2 perl-SOAP-Lite

Requires: perl-Gtk2 perl-SOAP-Lite

%description
RemoteBox is a GUI tool which lets you administer guests or virtual
machines running under VirtualBox on a remote server or even the same
local machine. VirtualBox is traditionally a desktop-side virtualisation
solution. The goal of RemoteBox is to provide a GUI that should be
familiar to VirtualBox users whist allowing them to administer a remote
installation of VirtualBox.

%prep
%setup -n %oname-%version
%__subst "s|\(use File::Spec::Win32;\)|#\1|g" share/remotebox/rbox_gui_init.pl

%install
install -D %name %buildroot%_bindir/%name
mkdir -p %buildroot%_datadir/%name/
cp -a share/remotebox/* %buildroot%_datadir/%name/

%__subst "s|\$Bin/share/remotebox|%_datadir/%name|g" %buildroot%_bindir/%name %buildroot/%_datadir/%name/rbox_gui_init.pl


%files
%doc docs
%_bindir/%name
%_datadir/%name/

%changelog
* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt1
- new version 2.4 (with rpmrb script)
- fix requires

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt1
- new version 2.3 (with rpmrb script)

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- new version 2.2 (with rpmrb script)

* Thu Jul 28 2016 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt1
- new version 2.1 (with rpmrb script)

* Tue Oct 26 2010 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- initial build for ALT Linux Sisyphus
