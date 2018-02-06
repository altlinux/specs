%define oname zc-zookeeper-static

%define zkver 3.4.6

Name: python-module-%oname
Version: 3.4.4.1
Release: alt1.git20120925.1
Summary: ZooKeeper Python bindings
License: Apache
Group: Development/Python
Url: https://pypi.python.org/pypi/zc-zookeeper-static/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/python-zk/zc-zookeeper-static.git
Source: %name-%version.tar
#Source1: http://apache.osuosl.org/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: doxygen graphviz cppunit-devel gcc-c++

%py_provides zookeeper

%description
This is a self-contained distribution of the ZooKeeper Python bindings.
It should build on any unix-like system by just running the setup.py
script or using an install tool like pip, easy_install or buildout.

%prep
%setup

%build
python get_source_files.py $PWD/zookeeper-%zkver.tar.gz
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.4.4.1-alt1.git20120925.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.4.1-alt1.git20120925
- Initial build for Sisyphus

