%define ver 3.5.0
%define subver 7

Name: nxclient
Version: %ver.%subver
Release: alt3

Summary: NoMachine.com's NX client

License: Proprietary
Group: Networking/Remote access
Url: http://www.nomachine.com

Source0: %name-%ver-%subver.i386.tar
Source1: %name-desktop.tar
Source2: %name-mime.tar
Source10: %name-%ver-%subver.x86_64.tar

Packager: Boris Savelev <boris@altlinux.org>

#BuildRequires: nx = %ver
BuildRequires: nx
BuildRequires: libXft-devel fontconfig-devel libfreetype-devel libcups-devel
BuildRequires: chrpath

Requires: nx = %ver
#BuildRequires: desktop-file-utils

%description
NXClient is a X11/VNC/NXServer client especially tuned for using remote
desktops over low-bandwidth links such as the Internet

%prep
%ifarch %ix86
%setup -b0 -n NX
%else
%setup -b10 -n NX
%endif

tar xf %SOURCE1
tar xf %SOURCE2

%install
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_libdir/%name/bin/
mkdir -p %buildroot%_libdir/%name/lib/
mkdir -p %buildroot%_datadir/%name/

# bin
chrpath -d bin/%name
cp -ap bin/%name %buildroot%_libdir/%name/bin/
cp -ap bin/nxprint %buildroot%_libdir/%name/bin/
for f in esd ssh service ; do 
    ln -s  ../../../bin/nx$f %buildroot%_libdir/%name/bin/nx$f
done
cat >> %buildroot%_libdir/%name/bin/%name.cfg << EOF
<!DOCTYPE NXClientSettings>
<NXClientSettings application="nxclient" version="1.3" >
<group name="General" >
<option key="System NX dir" value="%_libdir/%name" />
</group>
</NXClientSettings>
EOF

ln -s ../..%_libdir/%name/bin/%name %buildroot%_bindir/%name

# lib
# ln -s %_libdir/libXcomp.so.%ver %buildroot%_libdir/%name/lib/libXcomp.so
ln -s ../../libXcomp.so.%ver %buildroot%_libdir/%name/lib/libXcomp.so

# share
cp -ap share/* %buildroot%_datadir/%name
ln -s ../../share/%name %buildroot%_libdir/%name/share

# desktop
mkdir -p %buildroot%_desktopdir/
install -m644 %name-desktop/* %buildroot%_desktopdir/

# mime
mkdir -p %buildroot%_datadir/mimelnk/application/
mkdir -p %buildroot%_datadir/mime/application/
install -m644 %name-mime/*.desktop %buildroot%_datadir/mimelnk/application/
install -m644 %name-mime/*.xml %buildroot%_datadir/mime/application/

# Only one system tuning? (breaks CentOS 5 build)
%if 0
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=RemoteAccess \
	%buildroot%_desktopdir/nxclient-wizard.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=RemoteAccess \
	%buildroot%_desktopdir/nxclient.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=RemoteAccess \
	%buildroot%_desktopdir/nxclient-help.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=RemoteAccess \
	%buildroot%_desktopdir/nxclient-admin.desktop
%endif

%files
%_bindir/%name
%_libdir/%name/
%_datadir/%name/
%_datadir/mime/application/*
%_datadir/mimelnk/application/*
%_desktopdir/*

%changelog
* Wed Dec 21 2011 Michael Shigorin <mike@altlinux.org> 3.5.0.7-alt3
- drop RPATH

* Wed Nov 30 2011 Vitaly Lipatov <lav@altlinux.ru> 3.5.0.7-alt2
- disable desktop-file-install using
- do not require the same version for nx

* Tue Jun 28 2011 Boris Savelev <boris@altlinux.org> 3.5.0.7-alt1
- 3.5.0.7

* Fri Jun 17 2011 Boris Savelev <boris@altlinux.org> 3.5.0.6-alt1
- 3.5.0

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 3.4.0.7-alt4.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for nxclient

* Wed May 04 2011 Vitaly Lipatov <lav@altlinux.ru> 3.4.0.7-alt4
- fix dir creating with dash
- add URL to source tarball (for rpmpub command support)

* Mon Apr 25 2011 Vitaly Lipatov <lav@altlinux.ru> 3.4.0.7-alt3
- cleanup spec, use buildreqs not for ALT only

* Wed Oct 13 2010 Boris Savelev <boris@altlinux.org> 3.4.0.7-alt2
- remove konqueror dep (closes: #24198)

* Wed Mar 10 2010 Boris Savelev <boris@altlinux.org> 3.4.0.7-alt1
- new version

* Tue Oct 06 2009 Boris Savelev <boris@altlinux.org> 3.4.0.5-alt1
- new version

* Thu Feb 26 2009 Boris Savelev <boris@altlinux.org> 3.3.0.6-alt6
- fix link to %%_libdir

* Fri Jan 30 2009 Boris Savelev <boris@altlinux.org> 3.3.0.6-alt5
- add requires to nx = %%ver (fix #18696)

* Mon Jan 19 2009 Boris Savelev <boris@altlinux.org> 3.3.0.6-alt4
- new version

* Sun Jan 18 2009 Michael Shigorin <mike@altlinux.org> 3.3.0.3-alt2.M40.3.1
- updated desktop files with Category entries
  (snooped at http://wiki.zenwalk.org/index.php?title=Nxclient.desktop)
- minor spec cleanup

* Thu Jan 15 2009 Michael Shigorin <mike@altlinux.org> 3.3.0.3-alt2.M40.3
- backport to ALTLinux 4.0 (by rpmbph script)

* Wed Jan 07 2009 Boris Savelev <boris@altlinux.org> 3.3.0.3-alt3
- fix link in %_libdir/%name/lib
- add nxservice symlink

* Mon Jan 05 2009 Boris Savelev <boris@altlinux.org> 3.3.0.3-alt2
- remove alt-specific macroses

* Tue Dec 30 2008 Boris Savelev <boris@altlinux.org> 3.3.0.3-alt1
- initial build

