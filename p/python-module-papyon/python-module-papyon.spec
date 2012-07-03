%define _name papyon

Name: python-module-%_name
Version: 0.5.6
Release: alt1

Summary: Python libraries for MSN Messenger network
Group: Development/Python
License: GPLv2+
Url: http://www.freedesktop.org/wiki/Software/papyon
Source: http://www.freedesktop.org/software/%_name/releases/%_name-%version.tar.gz
Patch: %_name-0.5.6-farstream.patch

BuildArch: noarch

Obsoletes: python-module-pymsn
Provides: python-module-pymsn
%py_provides logger
%py_requires logging

BuildPreReq: rpm-build-python python-devel
BuildRequires: python-module-pygobject-devel

# Automatically added by buildreq on Thu Nov 19 2009
BuildRequires: libuuid python-module-OpenSSL python-module-PyXML python-modules-email python-modules-logging python-module-Crypto

%description
Papyon is the library behind the msn connection manager for telepathy.
Papyon uses the glib mainloop to process the network events in an
asynchronous manner

%setup_python_module %_name

%prep
%setup -q -n %_name-%version
%patch -p1 -b .farstream

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*
%doc COPYING NEWS AUTHORS

%changelog
* Sat Mar 10 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.6-alt1
- 0.5.6
- adapted for farstream (fc patch)

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.5-alt1.1
- Rebuild with Python-2.7

* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Fri Dec 17 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Sat May 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.8-alt1
- 0.4.8

* Mon May 24 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.7-alt1
- 0.4.7

* Fri Apr 09 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.6-alt1
- 0.4.6

* Sun Mar 14 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.5-alt1
- 0.4.5

* Wed Jan 20 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4

* Thu Nov 19 2009 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- first build for Sisyphus

