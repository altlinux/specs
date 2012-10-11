Name: python-module-pyvfs
Version: 0.2.3
Release: alt1
Summary: Simple python VFS library
License: GPLv3+
Group: Development/Python
URL: https://github.com/svinota/pyvfs

BuildArch: noarch
BuildPreReq: python-devel rpm-build-python
Source: %name-%version.tar

%description
PyVFS is a simple VFS library written in Python. It consists of
several layers, allowing to use different low-level protocol
implementations. Now you can choose between 9p (9p2000.u) and
FUSE.

The library can be used to create own servers as well as deploy
bundled applications, e.g. pyvfs.objectfs -- the library, that allows
to represent Python objects as files.

%prep
%setup

%install
%makeinstall python=%{__python} root=%buildroot lib=%{python_sitelibdir}

%files

%{python_sitelibdir}/pyvfs*

%changelog
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
