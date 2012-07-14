%define winemonodir %_datadir/wine/mono

Name: wine-mono
Version: 0.0.4
Release: alt1

Summary: Windows build of Mono to run .NET applications via Wine

License: MPL
Group: Office
Url: http://wiki.winehq.org/Mono

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source: http://prdownloads.sf.net/projects/wine/files/Wine%%20Mono/%version/wine-mono-%version.msi
Source: http://downloads.sourceforge.net/wine/wine-mono-%version.msi

BuildArch: noarch

%description
Mono is an open-source and cross-platform implementation of the .NET
Framework. Wine can use a Windows build of Mono to run .NET applications.
For Wine releases 1.5.3 and later, the Wine Mono package is recommended.

%install
mkdir -p %buildroot%winemonodir
install -m 644 %SOURCE0 %buildroot%winemonodir

%files
%dir %_datadir/wine/
%dir %winemonodir/
%winemonodir/%name-%version.msi

%changelog
* Sat Jul 14 2012 Vitaly Lipatov <lav@altlinux.ru> 0.0.4-alt1
- initial build for ALT Linux Sisyphus (0.0.4 use since wine 1.5.6)

