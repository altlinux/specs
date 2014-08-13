%define oname fuse

Summary: This is a Python interface to FUSE
Name: python3-module-%oname
Version: 0.2.1
Release: alt1.git20120527
Url: http://sourceforge.net/projects/fuse/
# git://git.code.sf.net/p/fuse/fuse-python
Source0: python-%oname.tar
License: LGPL
Group: Development/Python3

BuildRequires(pre): rpm-build-python3
BuildPreReq: libfuse-devel python3-devel python-tools-2to3

%description
This is a Python interface to FUSE.

FUSE (Filesystem in USErspace) is a simple interface for userspace
programs to export a virtual filesystem to the linux kernel.  FUSE
also aims to provide a secure method for non privileged users to
create and mount their own filesystem implementations.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc AUTHORS COPYING FAQ README.* example
%python3_sitelibdir/*

%changelog
* Wed Aug 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20120527
- Initial build for Sisyphus

