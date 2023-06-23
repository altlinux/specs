%define _upstream pyparted
%define oname parted

Name: python3-module-%oname
Version: 3.13.0
Release: alt1

Summary: Python bindings for libparted

Group: Development/Python3
License: GPL-2.0-or-later
URL: https://pypi.org/project/pyparted
VCS: https://github.com/dcantrell/pyparted

Source: %name-%version.tar

Provides: %_upstream

BuildRequires: libparted-devel
BuildRequires(pre): rpm-build-python3

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
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build

%install
%python3_install

%files
%doc AUTHORS NEWS README.md TODO
%python3_sitelibdir/parted
%python3_sitelibdir/*.so
%python3_sitelibdir/*.egg-info

%changelog
* Fri Jun 23 2023 Grigory Ustinov <grenka@altlinux.org> 3.13.0-alt1
- Automatically updated to 3.13.0.

* Tue May 24 2022 Grigory Ustinov <grenka@altlinux.org> 3.12.0-alt1
- Automatically updated to 3.12.0.

* Wed Jan 27 2021 Grigory Ustinov <grenka@altlinux.org> 3.11.7-alt1
- Automatically updated to 3.11.7.
- Drop python2 support.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.1-alt1
- Updated to upstream version 3.11.1.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.10.0-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.10.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.0-alt1
- Version 3.10.0 (ALT #30392)
- Added module for Python 3

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

