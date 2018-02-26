%define version 0.10.0
%define release alt2
%setup_python_module mpdclient

Name: %packagename
Version: %version
Release: %release.1
Summary: Python client library for mpd (Music Player Daemon)
License: LGPL
Group: Development/Python
Packager: Python Development Team <python at packages.altlinux.org>
BuildArch: noarch

Source0: py-libmpdclient-%version.tar.gz

Url: http://www.musicpd.org/?page=python_module

%description
Python implementation of libmpdclient, much of mpc functionality, and
probably more to come.

%prep
%setup -q -n py-libmpdclient-%version

%build
%__python setup.py build

%install
CFLAGS="%optflags" %__python setup.py \
        install --optimize=2 \
        --root=`pwd`/buildroot \
	--record=INSTALLED_FILES

cp -pr buildroot %buildroot
unset RPM_PYTHON

%files -f INSTALLED_FILES

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10.0-alt2.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.10.0-alt1.1.1
- Rebuilt with python-2.5.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.10.0-alt1.1
- Rebuilt using rpm-build-python-0.29-alt4.

* Sun Apr 02 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.10.0-alt1
- initial build
