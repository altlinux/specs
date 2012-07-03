%define version 0.1.1
%define release alt6

%define oname notify-python

%setup_python_module notify

Name: %packagename
Version: %version
Release: %release.1
Packager: Python Development Team <python@packages.altlinux.org>

Summary: Python bindings for libnotify
License: LGPL
Group: System/Libraries
Url: http://www.galago-project.org/
Source0: http://www.galago-project.org/files/releases/source/%oname/%oname-%version.tar.bz2
Patch0: notify-python-0.1.1-fix-GTK-symbols.patch
# http://pkgs.fedoraproject.org/gitweb/?p=notify-python.git;a=blob_plain;f=libnotify07.patch
Patch1: libnotify07.patch

Obsoletes: notify-python
Provides: notify-python = %version-%release

# Automatically added by buildreq on Mon Jul 09 2007
BuildRequires: gcc-c++ libnotify-devel python-module-pygtk-devel

%description
Python bindings for libnotify.

%prep
%setup -n %oname-%version
%patch0 -p1
%patch1 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%files
%python_sitelibdir/*
%_datadir/pygtk/2.0/defs/pynotify.defs
%_pkgconfigdir/notify-python.pc

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt6.1
- Rebuild with Python-2.7

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt6
- Fixed build (thnx shaba@)

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt5
- Rebuilt for debuginfo

* Wed Jan 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt4
- Fixed init.py so that it is able to load the needed GTK2 symbols from
  pygtk by Tom "spot" Callaway <tcallawa@redhat.com> (ALT #24883)

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt3.1.1
- Rebuilt with python 2.6

* Fri Feb 01 2008 Grigory Batalov <bga@altlinux.ru> 0.1.1-alt3.1
- Rebuilt with python-2.5.

* Tue Jan 22 2008 Grigory Batalov <bga@altlinux.ru> 0.1.1-alt3
- Use python_sitelibdir macro while packaging.

* Fri Sep 28 2007 Igor Zubkov <icesik@altlinux.org> 0.1.1-alt2
- rename package from notify-python to python-module-notify (closes #12410)

* Mon Jul 09 2007 Igor Zubkov <icesik@altlinux.org> 0.1.1-alt1
- build for Sisyphus

