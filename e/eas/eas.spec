%define CVSDATE 20070731
Name: eas
Version: 0.2.2
Release: alt0.6cvs%CVSDATE

Summary: E/AS Automation Solutions
Summary(ru_RU.KOI8-R): EAS - решение для автоматизации бизнеса

License: GPL
Group: Development/Other
Url: http://eas.lrn.ru/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: http://eas.lrn.ru/src/%name-%version.tar.bz2
Source2: %name-service
Patch: %name-%version.patch

%define FCLIPDIR %_libdir/clip
%define VCLIPDIR /var/lib/clip
%define EASDATADIR %VCLIPDIR/%name

# manually removed:
# Automatically added by buildreq on Tue Jan 23 2007
BuildRequires: clip clip-prg docbook-utils libclip-gtk2 libclip-ui libgpm-devel libpam-devel w3c-markup-validator-libs libpth-devel

BuildPreReq: libexpat-devel

%description
E/AS (E/AS Automation Solutions) is open source software system for help
automate business processes in company. E/AS written on CLIP language
(CA-Clipper dialect, compiler can be obtained from ITK.ru) and CLIP tools,
mainly CODB (CLIP Object Database) and COBRA (CLIP Object Broker & Application
Server).

%package -n %name-server
Summary: Server of E/AS
Group: Development/Other

%description -n %name-server
Server daemon of E/AS

%prep
%setup -q
subst 's/\(ch[mo].*\)/\1 || :/g' server/Makefile
subst "s,/usr/lib,%_libdir,g" libeas/Makefile

%build
export CLIPROOT=%FCLIPDIR
%configure --datadir=%_datadir/%name
%make DESTDIR=%buildroot

%install
export CLIPROOT=%FCLIPDIR
%makeinstall_std || %make DESTDIR=%buildroot linuxinstall -C server

cat server/eas.ini.in | \
	sed -e 's|FORMROOT|%_datadir/%name/server|' | \
	sed -e 's|SERVERMODULES|%_datadir/%name/server|' | \
	sed -e 's|\$CLIPROOT|%FCLIPDIR|' > eas.ini
subst "s|%_libdir/clip/cobra/auth/pam-auth|echo OK|" eas.ini

install -D eas.ini %buildroot%_sysconfdir/eas/eas.ini
install -D -m 0755 %SOURCE2 %buildroot%_initrddir/easd
subst "s,/usr/lib,%_libdir,g" %buildroot%_initrddir/easd
install -d %buildroot/var/log/%name

# Menu entry
mkdir -p %buildroot%_desktopdir
cat >%buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Type=Application
Name=E/AS
GenericName=E/AS Enterprise Automation System
Comment=E/AS Enterprise Automation System
Exec=%name
Icon=%name
ServiceTypes=
Categories=Office;Finance;
EOF

%pre
%_sbindir/useradd -r -M easserver -g clip || :

%files
%_bindir/*
%FCLIPDIR/bin/*
%FCLIPDIR/lib/lib*.so
%_libdir/lib%name.so
%_desktopdir/%name.desktop

%files -n %name-server
%dir %_sysconfdir/%name/
%config %_sysconfdir/pam.d/easserver
%config %_sysconfdir/%name/*
%attr (0755, easserver,clip) /var/log/%name
%_initrddir/*
%_datadir/%name

%changelog
* Tue May 03 2011 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt0.6cvs20070731
- Rebuild for set-versioning
- Create system user account for daemon user

* Tue Mar 01 2011 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt0.5cvs20070731
- Fix build in Sisyphus
- Spec cleanup

* Thu Jul 29 2010 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt0.4cvs20070731
- replace menu file by XDG .desktop file
- fix build on x86_64

* Tue Feb 02 2010 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt0.3cvs20070731
- remove deprecated install scripts
- fix clip-prg dependence

* Tue Aug 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt0.2cvs20070731
- rebuild on x86_64

* Tue Jul 31 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt0.1cvs20070731
- new version from CVS
- drop applied patch

* Tue Jan 23 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt0.1cvs20070123
- new version from CVS
- cleanup spec, build with gtk2

* Wed Sep 13 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt0.1
- new version (0.2.1), update buildreq
- welcome to fix this build

* Tue Nov 15 2005 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt0.1v
- new version

* Wed Mar 09 2005 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt0.2v20050207
- first correct build (with clip 1.1.14)

* Sun Feb 13 2005 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt0.1v20050207
- new version (fix cobra packaging)

* Mon Feb 07 2005 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt0.1v20050206
- new version (please check it and send me fixes)

* Mon Dec 06 2004 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt0.1v20041130
- new version (for test purposes only)

* Tue Jul 20 2004 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt0.1v20040715
- if it works for you please tell me how you done it
- new version
- split to server package
- use a macro for ldconfig

* Fri Feb 27 2004 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt0.1v20040226
- first build for Sisyphus
