%define oname pymsnt
Name: jabber-pymsnt
Version: 0.11.3
Release: alt1.1.1

Summary: MSN transport for XMPP servers
License: GPL
Group: System/Servers
Url: http://delx.net.au/projects/pymsnt/
Packager: Boris Savelev <boris@altlinux.org>

Requires(post): jabber-common

Provides: jabber-msn-t
Obsoletes: jabber-msn-t

BuildArch: noarch

BuildPreReq: rpm-build-compat jabber-common

# needed by component script
Requires: xmllint python-module-twisted-words

Source0: http://delx.net.au/projects/pymsnt/tarballs/%oname-%version.tar.bz2
Source1: pymsnt.init
Source2: pymsnt.adapter
Patch0: pymsnt-config.patch

%description
%oname is a MSN transport for Jabber servers.
This package contains only `xmlfiles' backend.

%prep
%setup -q -n %oname-%version
%patch0 -p0

%install
mkdir -p %buildroot%_var/run/pymsnt %buildroot%_spooldir/pymsnt
install -pm0755 -D PyMSNt.py %buildroot%_datadir/pymsnt/PyMSNt.py
cp -ap src %buildroot%_datadir/pymsnt/
cp -ap data %buildroot%_datadir/pymsnt/
install -pm 0755 -D %SOURCE1 %buildroot%_initdir/%name
install -pm 0755 -D %SOURCE2 %buildroot%_jabber_component_dir/pymsnt
install -pm 0640 -D config-example.xml %buildroot%_sysconfdir/pymsnt.xml

%pre
/usr/sbin/groupadd -r -f _pymsnt &>/dev/null ||:
/usr/sbin/useradd -r -g _pymsnt -d /dev/null -s /dev/null \
		-c "MSN Jabber transport" -M -n _pymsnt &>/dev/null ||:

%post
%post_service %name
%_jabber_config

%preun
%preun_service %name

%files
%doc docs/developer.html docs/server.html docs/style.css docs/user.html
%attr(0640,root,_pymsnt) %config(noreplace) %_sysconfdir/pymsnt.xml
%_initdir/%name
%_datadir/pymsnt/
%_jabber_component_dir/pymsnt/
%attr(0770,root,_pymsnt) %dir %_spooldir/pymsnt
%attr(0770,root,_pymsnt) %dir %_var/run/pymsnt

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.3-alt1.1.1
- Rebuild with Python-2.7

* Wed Dec 02 2008 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3-alt1.1
- Rebuilt with python 2.6

* Wed Mar 4 2008 Boris Savelev <boris@altlinux.org> 0.11.3-alt1
- initial build
