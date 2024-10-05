%define oname fuse

Name: python3-module-%oname
Version: 1.0.8
Release: alt1

Summary: This is a Python interface to FUSE
License: LGPL-2.1
Group: Development/Python3
URL: https://pypi.org/project/fuse-python
VCS: https://github.com/libfuse/python-fuse

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: libfuse-devel

%description
This is a Python interface to FUSE.

FUSE (Filesystem in USErspace) is a simple interface for userspace
programs to export a virtual filesystem to the linux kernel.  FUSE
also aims to provide a secure method for non privileged users to
create and mount their own filesystem implementations.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc AUTHORS COPYING FAQ README.* example
%python3_sitelibdir/fuse.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/fuse_python-%version.dist-info
%python3_sitelibdir/fuseparts

%changelog
* Fri Aug 23 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.8-alt1
- Automatically updated to 1.0.8.

* Tue Jan 09 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.7-alt1
- Updated to 1.0.7.

* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt1
- Version updated to 1.0.0

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.1-alt1.git20120527.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20120527.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Aug 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20120527
- Initial build for Sisyphus

