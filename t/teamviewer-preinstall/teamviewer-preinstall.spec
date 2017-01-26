Name: teamviewer-preinstall
Version: 11.0
Release: alt2

Summary: TeamViewer pre-installation scripts
Group: Networking/WWW
License: Public domain
Url: http://www.teamviewer.com

Source: %name-%version.tar

ExclusiveArch: %ix86

BuildRequires: libexpat
BuildRequires: libalsa zlib
BuildRequires: libSM libXext libXtst
BuildRequires: libXdamage libXfixes libXrender
BuildRequires: libXinerama libXrandr
BuildRequires: libfreetype libfontconfig
BuildRequires: libdbus libjpeg libpng12

Requires: bash >= 3.0
Requires: expat >= 1.95

%install
mkdir -p %buildroot%_libdir/%name
for lib in \
    libSM.so.6 \
    libXdamage.so.1 \
    libXext.so.6 \
    libXfixes.so.3 \
    libXinerama.so.1 \
    libXrandr.so.2 \
    libXrender.so.1 \
    libXtst.so.6 \
    libasound.so.2 \
    libdbus-1.so.3 \
    libexpat.so.1 \
    libfontconfig.so.1 \
    libfreetype.so.6 \
    libgcc_s.so.1 \
    libjpeg.so.62 \
    libnss_db.so.2 \
    libpng12.so.0 \
    libz.so.1
do 
    ln -s "$(ls {,/usr}/lib/$lib 2>/dev/null)" %buildroot%_libdir/%name/$lib || echo "ABSENT LIBRARY $lib"
done

%description
TeamViewer pre-installation scripts.
See http://www.teamviewer.com

Check with teamviewer_11.0.57095.i686.rpm

%files
%_libdir/%name

%changelog
* Thu Jan 26 2017 Andrey Cherepanov <cas@altlinux.org> 11.0-alt2
- Add glibc-nss to requirements

* Mon Jul 11 2016 Andrey Cherepanov <cas@altlinux.org> 11.0-alt1
- Adapt for new Arepo: package symlinks to 32-bit kibraries

* Fri Mar 16 2012 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- build only for i586 (use arepo for i586-teamviewer-preinstall)

* Thu Mar 01 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt3
- fix requires for both x86_64 and i586

* Mon Jan 23 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt2
- initial build for ALT Linux Sisyphus
