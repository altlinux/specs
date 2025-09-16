%define winemonodir %_datadir/wine/mono

Name: wine-mono-10.2.0
Version: 10.2.0
Release: alt1

Summary: Windows build of Mono to run .NET applications via Wine

License: GPL AND LGPL2.1 AND MPL-2.0
Group: Office
Url: http://wiki.winehq.org/Mono

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://dl.winehq.org/wine/wine-mono/%version/wine-mono-%version-x86.tar.xz
Source: %name-%version.tar

BuildArch: noarch

AutoReq: no
AutoProv: no

Provides: wine-mono = %version
Obsoletes: wine-mono <= 7.4.0-alt1

%description
Mono is an open-source and cross-platform implementation of the .NET
Framework. Wine can use a Windows build of Mono to run .NET applications.

%prep
%setup
# fix python2 print
%__subst 's|^print \(.*\)|print (\1)|' lib/mono/lldb/mono.py

%install
mkdir -p %buildroot%winemonodir/%name/
cp -a * %buildroot%winemonodir/%name/

%files
%dir %_datadir/wine/
%dir %winemonodir/
%winemonodir/%name/

%changelog
* Thu Sep 11 2025 Vitaly Lipatov <lav@altlinux.ru> 10.2.0-alt1
- new version (10.2.0) with rpmgs script
