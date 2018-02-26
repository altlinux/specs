Name: rpmdiagram
Version: 1.0
Release: alt1

Summary: Draws diagrams of RPM dependencies

Group: File tools
License: GPLv2
Url: http://software.amiga-hardware.com

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://software.amiga-hardware.com/software/%name-%version.tar

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 26 2010 (-bi)
BuildRequires: perl-GraphViz

%description
Draws diagrams of installed RPM dependencies using GraphViz and outputs the
diagram into an image file such as PNG or JPG.

%prep
%setup

%install
mkdir -p %buildroot%_bindir %buildroot%_sysconfdir %buildroot%_datadir/%name
install -pm0755 %name %buildroot%_bindir
install -pm0644 %name.cfg %buildroot%_sysconfdir

%files
%doc examples README COPYING
%_bindir/%name
%config(noreplace) %_sysconfdir/%name.cfg

%changelog
* Tue Oct 26 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus

* Tue May 06 2009 Ian Chapman <packages[AT]amiga-hardware.com> 1.0-1%{?dist}
- Initial release
