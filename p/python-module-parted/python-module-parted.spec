%define _upstream pyparted
Name: python-module-parted
Version: 3.4
Release: alt2.1.1

Summary: Python bindings for libparted

Group: Development/Python
License: GPL v2 or later
URL: https://fedorahosted.org/pyparted/
Packager: Eugene Ostapets <eostapets@altlinux.ru>
Source: %_upstream-%version.tar.gz
Provides: %_upstream


# Automatically added by buildreq on Fri Feb 20 2009
BuildRequires: libparted-devel python-devel
BuildPreReq: python-module-decorator

%description
pyparted is a set of native Python bindings for libparted.  libparted is the
library portion of the GNU parted project.  With pyparted, you can write
applications that interact with disk partition tables and filesystems.

The Python bindings are implemented in two layers.  Since libparted itself
is written in C without any real implementation of objects, a simple 1:1
mapping of externally accessible libparted functions was written.  This
mapping is provided in the _ped Python module.  You can use that module if
you want to, but it's really just meant for the larger parted module.


%prep
%setup -n %_upstream-%version

%build
%autoreconf
%configure
%make_build 

%install
%makeinstall_std

%files
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%python_sitelibdir/parted
%python_sitelibdir/*.so
%exclude %python_sitelibdir/*.la

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4-alt2.1
- Rebuild with Python-2.7

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt2
- Rebuilt for debuginfo

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1
- Version 3.4

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1.1
- Rebuilt with python 2.6

* Tue Mar 03 2009 Eugene Ostapets <eostapets@altlinux.ru> 2.0.4-alt1
- new version

* Thu Feb 26 2009 Eugene Ostapets <eostapets@altlinux.ru> 2.0.2-alt1
- new version 

* Fri Feb 20 2009 Eugene Ostapets <eostapets@altlinux.ru> 2.0.1-alt1
- First build for Sisyphus

