%define svn r59
Name: neatx
Version: 0.3.1
Release: alt7.%svn.1

Summary: Open Source NX server
Group: Networking/Remote access
License: GPLv2
Url: http://code.google.com/p/neatx/
Packager: Boris Savelev <boris@altlinux.org>
Source: http://neatx.googlecode.com/files/%name-%version.tar.gz
Source1: README.ALT
Requires: nx
Requires: openssl
Requires: netcat
Requires: dbus-tools-gui
Requires: binutils
Requires: Xdialog
Requires: %_bindir/xvt
Requires: python-module-%name = %version-%release
Conflicts: freenx-server
Conflicts: tacix-freenx
BuildPreReq: rpm-build-intro

# Automatically added by buildreq on Wed Jul 08 2009
BuildRequires: python-devel python-module-docutils python-modules-encodings time

%package -n python-module-%name
Summary: Python module for %name
Group: Development/Python
BuildArch: noarch

%description
Neatx is an Open Source NX server, similar to the commercial NX server from NoMachine.

%description -n python-module-%name
Python module for %name

%prep
%setup

%build
%autoreconf
%configure \
	--localstatedir=%_var
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_var/lib/nxserver/home
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_sysconfdir
ln -s ../../%_libdir/%name/nxserver-login-wrapper %buildroot%_bindir/nxserver
install -m644 %SOURCE1 %buildroot%_docdir/%name-%version
install -m644 doc/%name.conf.example %buildroot%_sysconfdir/%name.conf

%pre
%groupadd nx 2> /dev/null ||:
%useradd -g nx -G utmp -d /var/lib/nxserver/home/ -s %_bindir/nxserver \
        -c "NX System User" nx 2> /dev/null ||:
if [ ! -d %_datadir/fonts/misc ] && [ ! -e %_datadir/fonts/misc ] && [ -d %_datadir/fonts/bitmap/misc ]
then
    ln -s %_datadir/fonts/bitmap/misc %_datadir/fonts/misc
fi

%files
%config(noreplace) %_sysconfdir/%name.conf
%_bindir/nxserver
%_libdir/%name
%_datadir/%name
%attr(2770,root,nx) %_var/lib/%name
%attr(2770,root,nx) %_var/lib/%name/sessions
%attr(2750,nx,nx) %_var/lib/nxserver/home
%_docdir/%name-%version

%files -n python-module-%name
%python_sitelibdir_noarch/%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt7.r59.1
- Rebuild with Python-2.7

* Tue Dec 28 2010 Boris Savelev <boris@altlinux.org> 0.3.1-alt7.r59
- fix build (update buildreq)

* Sat Mar 13 2010 Boris Savelev <boris@altlinux.org> 0.3.1-alt6.r59
- build latest from svn
- fix build
- python-module-%name become noarch

* Sun Aug 30 2009 Boris Savelev <boris@altlinux.org> 0.3.1-alt5.r41
- build latest from svn

* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 0.3.1-alt4.r32
- build latest from svn

* Wed Jul 22 2009 Boris Savelev <boris@altlinux.org> 0.3.1-alt3.r21
- build latest from svn

* Thu Jul 09 2009 Boris Savelev <boris@altlinux.org> 0.3.1-alt2
- fix work
- add README.ALT
- replace default config

* Wed Jul 08 2009 Boris Savelev <boris@altlinux.org> 0.3.1-alt1
- initial build for Sisyphus (not tested)

