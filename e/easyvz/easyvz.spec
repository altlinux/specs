Name: easyvz
Version: 0.1
Release: alt3.1.qa1.1.1

Summary: EasyVZ is a graphical frontend for OpenVZ.

License: GPL
Group: System/Configuration/Other

URL: http://binarykarma.com
Packager: Slava Dubrovskiy <dubrsl@altlinux.org>
Source0: http://heanet.dl.sourceforge.net/sourceforge/easyvz/%name-%version.tar.gz
Source1: %name.init
Source2: %name.png
Source3: %name.desktop
Patch0: %name-%version-daemon-alt.patch

Requires: python-module-pygtk-libglade

%define dirvz ezvz
%define daemoname easyvzd

%description
EasyVZ is a graphical frontend for OpenVZ. It lets you create, delete and
manage VPSs or VEs.

Please be warned that EasyVZ is still pre-alpha software. That pretty much
means there are still hell lot of bugs and nothing is guarunteed.

%package server
License: GPL
Group: System/Configuration/Other
Summary: EasyVZ-server is a server for menage OpenVZ.
Requires: vzctl procps
%description server
EasyVZ-server is a server for menage OpenVZ.

WARNING!!!: In the current version of the software, there is no authentication,
anyone who can run the client can manage the server. Please exercise caution.


%prep
%setup -q -n %dirvz

find %_builddir/%dirvz -type d -name .svn -print0 | xargs -r0 rm -fr
find %_builddir/%dirvz -type f -print0 | xargs -r0 %__subst "s|/vz/private|/var/lib/vz/private|g"
find %_builddir/%dirvz -type f -print0 | xargs -r0 %__subst "s|/vz/template|/var/lib/vz/template|g"

%patch0 -p1

%__subst "s|/usr/bin/env python|/usr/bin/python|g" backend/server.py
%__subst "s|/usr/bin/env python|/usr/bin/python|g" gui/ezvz.py
%__subst "s|Cpu|CPU|g" backend/ezvzlib.py

%build

%install
%__mkdir_p %buildroot%python_sitelibdir/%name/
%__mkdir_p %buildroot%python_sitelibdir/%name-server/
%__mkdir_p %buildroot%_sysconfdir
%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot%_sbindir
%__mkdir_p %buildroot%_initrddir
%__mkdir_p %buildroot%_desktopdir
%__mkdir_p %buildroot%_niconsdir

%__cp -fR gui/* %buildroot%python_sitelibdir/%name/
%__cp -fR backend/* %buildroot%python_sitelibdir/%name-server/
%__cp -f %name.conf %buildroot%_sysconfdir/%name.conf
%__cp -f %SOURCE1 %buildroot%_initrddir/%daemoname
%__cp -f %SOURCE2 %buildroot%_niconsdir/%name.png
%__cp -f %SOURCE3 %buildroot%_desktopdir/%name.desktop

%__cat << EOF > %buildroot%_bindir/%name
#!/bin/sh
d=\`pwd\`
cd %python_sitelibdir/%name
%__python ezvz.py
cd \$d
EOF

%__cat << EOF > %buildroot%_sbindir/%daemoname
#!/bin/sh
exec %python_sitelibdir/%name-server/server.py \$*
EOF

%post server
%post_service %daemoname
echo WARNING!!!: In the current version of the software, there is no authentication,
echo anyone who can run the client can manage the server. Please exercise caution.

%preun server
%preun_service %daemoname

%files
%doc COPYING INSTALL README
%attr(0755,root,root) %_bindir/*
%python_sitelibdir/%name
%attr(0755,root,root) %python_sitelibdir/%name/ezvz.py
%_desktopdir/*
%_niconsdir/*

%files server
%config(noreplace) %_sysconfdir/%name.conf
%python_sitelibdir/%name-server
%attr(0755,root,root) %python_sitelibdir/%name-server/server.py
%attr(0755,root,root) %_sbindir/*
%attr(0755,root,root) %_initrddir/%daemoname

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt3.1.qa1.1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3.1.qa1.1
- Rebuilt with python 2.6

* Thu Nov 12 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.1-alt3.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for easyvz
  * pixmap-in-deprecated-location for easyvz
  * postclean-05-filetriggers for spec file

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt3.1
- Rebuilt with python-2.5.

* Wed May 16 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1-alt3
- Change in requires top to procps

* Tue May 15 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1-alt2
- Fix #11770
- Add top in requires

* Wed Mar 07 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1-alt1
- Fix URL
- Add IP options in config
- Add %%config(noreplace) for %_sysconfdir/%name.conf

* Thu Feb 08 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1-alt0
- First alpha build for Sisyphus. All works, but...;-)
