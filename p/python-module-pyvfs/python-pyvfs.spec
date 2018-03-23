%define modname pyvfs
%define buildroot %_topdir/BUILDROOT

Name: python-module-%modname
Version: 0.2.10
Release: alt1

Summary: Simple python VFS library
License: GPLv3+
Group: Development/Python
URL: https://github.com/svinota/pyvfs
BuildArch: noarch

Source: pyvfs-%version.tar

BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-objects.inv
BuildRequires: python-module-setuptools
BuildRequires: python-devel

Requires: python-module-py9p >= 1.0.6-alt1

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-devel


%description
PyVFS is a simple VFS library written in Python. It consists of
several layers, allowing to use different low-level protocol
implementations. Now you can choose between 9p (9p2000.u) and
FUSE.

The library can be used to create own servers as well as deploy
bundled applications, e.g. pyvfs.objectfs -- the library, that allows
to represent Python objects as files.

%package -n python3-module-%modname
Summary: Simple python VFS library
Group: Development/Python

%description -n python3-module-%modname
PyVFS is a simple VFS library written in Python. It consists of
several layers, allowing to use different low-level protocol
implementations. Now you can choose between 9p (9p2000.u) and
FUSE.

The library can be used to create own servers as well as deploy
bundled applications, e.g. pyvfs.objectfs -- the library, that allows
to represent Python objects as files.

%prep
%setup -n pyvfs-%version

rm -rf ../python3
cp -fR . ../python3

%prepare_sphinx .
ln -s ../objects.inv docs/
  
%build
make force-version
%python_build

pushd ../python3
make force-version
%python3_build
popd


export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html
mkdir man
cp -fR docs/_build/html/* man/

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README* LICENSE man/
%python_sitelibdir/*

%files -n python3-module-%modname
%doc README* LICENSE man/
%python3_sitelibdir/*

%changelog
* Fri Mar 23 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.10-alt1
- Version 0.2.10

* Fri Nov 30 2012 Peter V. Saveliev <peet@altlinux.org> 0.2.8-alt1
- directory listing fix for v9fs
- version sync with py9p

* Sun Nov  4 2012 Peter V. Saveliev <peet@altlinux.org> 0.2.7-alt2
- dependencies update

* Fri Oct 26 2012 Peter V. Saveliev <peet@altlinux.org> 0.2.7-alt1
- authentication options support

* Mon Oct 22 2012 Peter V. Saveliev <peet@altlinux.org> 0.2.6-alt2
- urgent fixes for new cycle detection
- support unicode strings as keys in dictionaries
- fix function calls

* Mon Oct 22 2012 Peter V. Saveliev <peet@altlinux.org> 0.2.6-alt1
- symlink support

* Fri Oct 19 2012 Peter V. Saveliev <peet@altlinux.org> 0.2.5-alt1
- new cycle detection mechanism for objectfs
- transaction-like cleanup for Inode class

* Tue Oct 16 2012 Peter V. Saveliev <peet@altlinux.org> 0.2.4-alt2
- import path fixes
- urgent fixes for function calls

* Mon Oct 15 2012 Peter V. Saveliev <peet@altlinux.org> 0.2.4-alt1
- Function exports added
- Method calls (by FS read/write) implemented

* Fri Oct 12 2012 Peter V. Saveliev <peet@altlinux.org> 0.2.3-alt2
- add README and LICENSE
- use targz for distribution archive
- unify gear and bdist archive layout

* Thu Oct 11 2012 Peter V. Saveliev <peet@altlinux.org> 0.2.3-alt1
- functions as files (containing disassembled code)
- writeable attribute files
- pyvfs.objectfs: disable autostart with OBJECTFS_AUTOSTART
- pyvfs.objectfs: new argument "functions" for the decorator
- pyvfs.objectfs: new argument "basedir" for the decorator

* Sat Oct  6 2012 Peter V. Saveliev <peet@altlinux.org> 0.2.2-alt1
- Read-write FUSE support
- pyvfs.utils.Server as a dedicated user interface to start FS
- pyvfs.objectfs: new argument "weakref" for the decorator
- pyvfs.objectfs: new argument "basedir" for the decorator

* Thu Oct  4 2012 Peter V. Saveliev <peet@altlinux.org> 0.2.1-alt1
- FUSE support

* Tue Oct  2 2012 Peter V. Saveliev <peet@altlinux.org> 0.1.1-alt1
- initial build
