%define oname pyalsa

Name: python-module-pyalsa
Version: 1.0.22
Release: alt1.1.1

Summary: Wrapper for accessing the ALSA API from Python
License: GPL
Group: Development/Python

Url: http://bigasterisk.com
Source: %url/post/%oname-%version.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Fri Oct 22 2010
BuildRequires: libalsa-devel python-devel

%define _python_egg_info %python_sitelibdir/%oname-%version-py%__python_version.egg-info
%setup_python_module %oname

%description
This package contains wrappers for accessing the ALSA API from Python.
It is currently fairly complete for PCM devices and Mixer access.
MIDI sequencer support is low on our priority list, but volunteers
are welcome.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%oname/
%_python_egg_info

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.22-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.22-alt1.1
- Rebuild with Python-2.7

* Fri Oct 22 2010 Michael Shigorin <mike@altlinux.org> 1.0.22-alt1
- built for ALT Linux
  + new alsa-tools want this
  + 1.1 won't build with our precious python-module-Pyrex, hm
