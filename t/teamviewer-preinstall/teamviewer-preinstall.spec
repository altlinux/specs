Name: teamviewer-preinstall
Version: 0.2
Release: alt1

Summary: Team viewer pre-installation scripts

Group: Networking/WWW
License: Public domain
Url: http://www.teamviewer.com

Source: %name-%version.tar

ExclusiveArch:  %{ix86}

#Requires: libc.so.6 libnss_nis.so.2
Requires: glibc-core glibc-nss

#Requires: libasound.so.2 libz.so.1
Requires: libalsa zlib

#Requires: libSM.so.6 libXext.so.6 libXtst.so.6
Requires: libSM libXext libXtst

#Requires: libXdamage.so.1 libXfixes.so.3 libXrender.so.1
Requires: libXdamage libXfixes libXrender

#Requires: libfreetype.so.6
Requires: libfreetype

# required by teamviewer_linux package
Provides: glibc(x86-32) = 2.11, alsa-lib(x86-32), zlib(x86-32)
Provides: libSM(x86-32), libXext(x86-32), libXtst(x86-32)
Provides: libXdamage(x86-32), libXfixes(x86-32), libXrender(x86-32)
Provides: freetype(x86-32)

%description
TeamViewer pre-installation scripts.
See http://www.teamviewer.com

%files

%changelog
* Fri Mar 16 2012 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- build only for i586 (use arepo for i586-teamviewer-preinstall)

* Thu Mar 01 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt3
- fix requires for both x86_64 and i586

* Mon Jan 23 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt2
- initial build for ALT Linux Sisyphus
