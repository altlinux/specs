%define version 0.6.6.2
%define release alt2
%setup_python_module coherence

Name: coherence
Version: %version
Release: %release.1

Summary: An UPnP/DLNA MediaServer
Packager: Alexey Shabalin <shaba at altlinux.ru>
License: MIT
Group: System/Servers
URL: http://coherence-project.org
Buildarch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Source2: coherence.init

Requires: %packagename = %version-%release
BuildPreReq: rpm-build-python rpm-build-gnome

BuildRequires: python-module-Axiom python-module-Crypto python-module-Cython python-module-Nevow python-module-Epsilon
BuildRequires: python-module-Pyrex python-module-configobj python-module-feedparser python-module-louie
BuildRequires: python-module-twisted-core python-module-twisted-web python-module-gdata python-module-pyinotify
BuildRequires: python-devel python-module-setuptools

%description
Coherence is a framework written in Python enabling applications to participate
in digital living networks, such as the UPnP universe.

This is an UPnP/DLNA MediaServer

%package applet
Summary: Start/stop applet for Coherence MediaServer
Group: Development/Python
Requires: %name = %version-%release

%description applet
Start/stop applet for Coherence MediaServer

%package -n %packagename
Summary: Python framework to participate in digital living networks
Group: Development/Python

%description -n %packagename
Coherence is a framework written in Python enabling applications to participate
in digital living networks, such as the UPnP universe.

%prep
%setup -q
#find coherence -type f -exec \
#   sed -i 's/coherence.extern.louie as louie/louie/' {} \;
#rm -rf coherence/extern/{louie,uuid}
rm -rf coherence/extern/uuid

%patch -p1

%build
%python_build

%install
%python_install

mkdir -p \
	%buildroot%_initdir \
	%buildroot%_sysconfdir/%name \
	%buildroot%_iconsdir/%name \
	%buildroot%_niconsdir \
	%buildroot%_datadir/dbus-1/services

install -m 755 %SOURCE2 %buildroot%_initdir/%name
install -m 644 docs/coherence.conf.example %buildroot%_sysconfdir/%name/%name.conf
install -m 644 misc/org.Coherence.service %buildroot%_datadir/dbus-1/services/

install -m644 "misc/Desktop-Applet/tango-system-file-manager.png" %buildroot%_iconsdir/%name/
install -m644 "misc/Desktop-Applet/tango-system-file-manager-32x32.png" %buildroot%_niconsdir/


%files
%doc LICENCE README docs/*
%_bindir/%name
%_initdir/%name
%_datadir/dbus-1/services/*.service
%config(noreplace) %_sysconfdir/%name/%name.conf

%files applet
%_bindir/applet-coherence
%_iconsdir/%name/*
%_niconsdir/*

%files -n %packagename
%python_sitelibdir/*.egg-info
%python_sitelibdir/%modulename
# We don't want this in the package
%exclude %python_sitelibdir/misc/

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.6.2-alt2.1
- Rebuild with Python-2.7

* Fri Mar 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.6.2-alt2
- drop python-module-pygoogle from BuildRequires

* Fri Jan 15 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.6.2-alt1
- 0.6.6.2

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt2.1
- Rebuilt with python 2.6

* Mon Oct 26 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.4-alt2
- package external svn module from https://code.fluendo.com/flumotion/svn/flumotion/trunk/flumotion/extern/log
- update buildreq

* Fri Jun 05 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.4-alt1
- 0.6.4
- adapt spec for build from git.alt

* Sun Apr 19 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1
- 0.6.2
- don't install plugins

* Sat Jan 03 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- first build for Sisyphus


