# TODO: build here
Name: openproj
Version: 1.2
Release: alt1.qa1

License: GPL
Group: Office
Url: http://openproj.org/

Summary: A Java based project manager

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/openproj/%name-%version.tar.bz2

Requires: java >= 1.6.0-4

BuildPreReq: desktop-file-utils

%description
OpenProj is a free, open source desktop alternative to Microsoft Project.
If you are managing a group project we recommend Project-ON-Demand.
If you want a free replacement to commercial desktop software, then
OpenProj is perfect.

%prep
%setup -q
%__subst "s|^OPENPROJ_HOME0.*|OPENPROJ_HOME0=%_libdir/%name|g" openproj.sh

%install
export DONT_STRIP=1

mkdir -p %buildroot/%_bindir/
mkdir -p %buildroot/%_libdir/%name/
cp -af * %buildroot/%_libdir/%name/
mv %buildroot/%_libdir/%name/openproj.sh %buildroot/%_bindir/%name

mkdir -p %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Open Project
Comment=Java based project manager
Exec=%_bindir/%name
Icon=taskmanagement_section.png
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Office;Development;ProjectManagement;
EOF

%files
%_bindir/%name
%_libdir/%name/
%_desktopdir/%name.desktop

%changelog
* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.2-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for openproj
  * desktop-mime-entry for openproj
  * postun_ldconfig for openproj
  * postclean-05-filetriggers for spec file

* Sat Jun 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- new version 1.2 (with rpmrb script)
- fix bindir/openproj owner

* Thu Nov 08 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt2
- cleanup spec, do not use wrap script for running
- strip version from lib dir

* Mon Oct 29 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt1
- initial build for ALT Linux Sisyphus (thanks Mandriva for spec)

* Tue Oct 02 2007 Texstar <texstar@gmail.com> 0.9.6-1pclos2007
- import into pclos 2007
