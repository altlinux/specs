%define modname pyvfs

Name: python3-module-%modname
Version: 0.2.10
Release: alt2

Summary: Simple python VFS library
License: GPLv3+
Group: Development/Python3
URL: https://github.com/svinota/pyvfs
BuildArch: noarch

Source: pyvfs-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-objects.inv python3-module-sphinx

Requires: python3-module-py9p >= 1.0.6-alt1


%description
PyVFS is a simple VFS library written in Python. It consists of
several layers, allowing to use different low-level protocol
implementations. Now you can choose between 9p (9p2000.u) and
FUSE.

The library can be used to create own servers as well as deploy
bundled applications, e.g. pyvfs.objectfs -- the library, that allows
to represent Python objects as files.

%prep
%setup -n pyvfs-%version

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
make force-version
%python3_build

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html
mkdir man
cp -fR docs/_build/html/* man/

%install
%python3_install

%files
%doc README* LICENSE man/
%python3_sitelibdir/*


%changelog
* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.10-alt2
- build for python2 disabled

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
