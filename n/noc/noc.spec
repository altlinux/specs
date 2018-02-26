
Name: noc
Version: 0.7.0
Release: alt4

Summary: NOC Project is an Operation Support System (OSS)
Group: Networking/Other
License: BSD-like
Url: http://nocproject.org
BuildArch: noarch
Source: %name-%version.tar
Source2: %name.init
Source3: %name-README.ALT.UTF8
Source4: %name.sysconfig
Patch: %name-%version-%release.patch

%define nocdir %_datadir/%name
%add_findreq_skiplist %nocdir/main/templates/*

Requires: mercurial telnet openssh-clients rsync tar gzip smi-tools bind-utils gnupg postgresql make fping mongo
Requires: python-module-psycopg2 python-module-coverage python-module-webob python-module-webtest
Requires: python-module-django-tagging >= 0.3.1
Requires: python-module-protobuf >= 2.3.0
Requires: python-module-django >= 1.3
Requires: python-module-django-dbbackend-psycopg2 >= 1.2.1
Requires: python-module-Crypto python-module-gmpy
Requires: python-module-creole
Requires: python-module-pymongo
Requires: python-module-netifaces
Requires: python-module-cjson

# Automatically added by buildreq on Wed Apr 21 2010
BuildRequires: python-devel

%description
NOC Project is an Operation Support System (OSS) for the Telco, Service provider and Enterprise Network Operation Centers (NOC).
Areas covered by NOC:
    * Fault Management
    * Performance Management
    * Service Activation/Provisioning
    * Knowledge Base
    * Multi-VRF Address space management
    * Virtual Circuits management (VLAN, DLCI, etc)
    * Configuration Management
    * DNS provisioning
    * Peering management, RPSL and BGP filters generator, integrated looking glass
    * Reporting

%prep
%setup -q
%patch -p1

#delete contrib
rm -rf contrib
sed -i '/^contrib/d' MANIFEST MANIFEST-ACTIVATOR

%__subst 's,../../../../contrib/bin/sphinx-build,sphinx-build,' share/docs/en/nocbook/Makefile

# delete MacOS files
find -type f -name "._*" -print -exec rm -rf {} \;

find -type f -print0 |
	xargs -r0 grep -FZl \/opt\/noc -- |
	xargs -r0 %__subst -p 's,/opt/noc,%nocdir,g' --

# change default paths in configs
%__subst "s,/var/repo,%_localstatedir/%name/repo," etc/noc.defaults
%__subst "s,/var/backup,%_localstatedir/%name/backup," etc/noc.defaults
%__subst "s,/usr/local/bin/hg,/usr/bin/hg," etc/noc.defaults
%__subst "s,/usr/local/bin/pg_dump,/usr/bin/pg_dump," etc/noc.defaults
%__subst "s,/usr/bin/tar,/bin/tar," etc/noc.defaults
%__subst "s,/usr/bin/gzip,/bin/gzip," etc/noc.defaults
%__subst "s,pidfile  = /var/log/,pidfile  = /var/run/," etc/*.defaults

%build
%python_build

%install
%python_install

# dirs:
mkdir -p %buildroot%_localstatedir/%name/{local,repo/config,backup,static/doc,.ssh}
mkdir -p %buildroot{%_logdir/%name,%_var/run/%name,%_sysconfdir/sysconfig,%_initdir}

# configs:
install -m 640 %SOURCE4 %buildroot%_sysconfdir/sysconfig/%name
install -m 755 %SOURCE2 -D %buildroot%_initdir/%name
for d in etc/*.defaults; do
    conf=`echo $d|sed 's/.defaults$/.conf/'`
    if [ ! -f $conf ]; then
        cp $d $conf
    fi
done
cp etc/*.conf %buildroot%nocdir/etc/

# ln -s %nocdir/etc %buildroot%_sysconfdir/%name

pushd %buildroot%nocdir
    ln -s %_localstatedir/%name/local local
    ln -s %_localstatedir/%name/static/doc static/doc
popd

pushd %buildroot%_sysconfdir
    ln -s %nocdir/etc %name
popd

# cleanup
rm -rf %buildroot%nocdir/share/{linux,sunos,FreeBSD}

# don't need post-install script
rm -rf %buildroot%nocdir/scripts/post-install

# Install Attention README
install -m 0644 %SOURCE3 README.ALT.UTF8

%pre
%_sbindir/groupadd -r -f noc >/dev/null 2>&1 || :
%_sbindir/useradd -M -r -d %_localstatedir/%name -s /bin/false -c "NOC User" -g noc noc >/dev/null 2>&1 || :

%post
%post_service noc

%preun
%preun_service noc

%files
%doc README.ALT.UTF8 AUTHORS LICENSE LICENSE.RU INSTALL README
%dir %nocdir
%nocdir/*
%attr(750,noc,noc) %dir %nocdir/etc
%attr(750,noc,noc) %dir %nocdir/etc/ssh
%attr(640,noc,noc) %config %nocdir/etc/*.defaults
%attr(640,noc,noc) %config(noreplace) %nocdir/etc/*.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%_sysconfdir/%name
%config(noreplace) %_initdir/%name

%attr(0700,noc,noc) %dir %_localstatedir/%name/.ssh
%attr(0770,noc,noc) %dir %_localstatedir/%name/local
%attr(0770,noc,noc) %dir %_localstatedir/%name/repo
%attr(0770,noc,noc) %dir %_localstatedir/%name/repo/config
%attr(0770,noc,noc) %dir %_localstatedir/%name/backup
%attr(0755,noc,noc) %dir %_localstatedir/%name/static
%attr(0775,noc,noc) %dir %_localstatedir/%name/static/doc
%attr(0775,noc,noc) %dir %_logdir/%name
%attr(0775,noc,noc) %dir %_var/run/%name

%changelog
* Wed Jun 20 2012 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt4
- 0.7(4)

* Thu May 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt3.1
- Removed requires python-module-django-dbbackend-psycopg

* Wed Apr 18 2012 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt3
- 0.7(3)

* Wed Feb 01 2012 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt2
- 0.7(2)

* Tue Nov 22 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- 0.7(1)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.4-alt1.1
- Rebuild with Python-2.7

* Tue May 17 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Wed Apr 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Fri Mar 04 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Tue Feb 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.1-alt1.hg20110208
- snapshot 20110208
- add requires python-module-django-dbbackend-psycopg (closes: #25028)
- fix package dir /var/lib/noc/static/doc (closes: #25029)

* Mon Dec 20 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6-alt1
- 0.6
- fix DB backup with django-1.2
- drop contrib dir in scripts

* Fri Dec 03 2010 Alexey Shabalin <shaba@altlinux.ru> 0.5.1-alt2
- use system sphinx-build

* Thu Dec 02 2010 Alexey Shabalin <shaba@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Thu Oct 07 2010 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt3
- add --displayname noc to init

* Thu Sep 23 2010 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt2
- update webserver instalation url in README.ALT.UTF8
- add requires to python-module-django-dbbackend-psycopg2

* Mon Sep 20 2010 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt1
- 0.5a

* Tue Apr 27 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4-alt2
- change home dir for user noc to %_localstatedir/%name
- mkdir .ssh in home dir
- update Requires
- fix permissions %_localstatedir/%name and %nocdir/etc
- add README.ALT.UTF8

* Wed Apr 21 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4-alt1
- 0.4

* Mon Mar 01 2010 Alexey Shabalin <shaba@altlinux.ru> 0.3.2-alt1
- initial build

