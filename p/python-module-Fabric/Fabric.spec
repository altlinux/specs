%define _unpackaged_files_terminate_build 1
%define oname Fabric

%def_without python3

Name: python-module-%oname
Version: 1.14.0
Release: alt1
Summary: A simple, Pythonic tool for remote execution and deployment
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://github.com/fabric/fabric

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-alabaster python-module-html5lib python-module-objects.inv python-module-paramiko
BuildRequires: python-module-releases
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%endif

%py_provides %oname
%py_requires paramiko

%description
Fabric is a Python (2.5-2.7) library and command-line tool for
streamlining the use of SSH for application deployment or systems
administration tasks.

It provides a basic suite of operations for executing local or remote
shell commands (normally or via sudo) and uploading/downloading files,
as well as auxiliary functionality such as prompting the running user
for input, or aborting execution.

%if_with python3
%package -n python3-module-%oname
Summary: A simple, Pythonic tool for remote execution and deployment
Group: Development/Python3
%py3_requires paramiko

%description -n python3-module-%oname
Fabric is a Python (2.5-2.7) library and command-line tool for
streamlining the use of SSH for application deployment or systems
administration tasks.

It provides a basic suite of operations for executing local or remote
shell commands (normally or via sudo) and uploading/downloading files,
as well as auxiliary functionality such as prompting the running user
for input, or aborting execution.
%endif

%package docs
Summary: Documentationr for Fabric
Group: Development/Documentation

%description docs
Fabric is a Python (2.5-2.7) library and command-line tool for
streamlining the use of SSH for application deployment or systems
administration tasks.

It provides a basic suite of operations for executing local or remote
shell commands (normally or via sudo) and uploading/downloading files,
as well as auxiliary functionality such as prompting the running user
for input, or aborting execution.

This package contains documentationr for Fabric.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx sites
ln -s ../objects.inv sites/docs/
ln -s ../objects.inv sites/www/

%build
%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -n -w '{}' +
%python3_build_debug
popd
%endif

pushd sites/docs
sphinx-build -b html -E . docs
popd
pushd sites/www
sphinx-build -b html -E . www
popd

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/fab %buildroot%_bindir/fab.py3
%endif

%python_install

%files
%doc LICENSE AUTHORS README.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%files docs
%doc sites/docs/docs
%doc sites/www/www

%if_with python3
%files -n python3-module-%oname
%doc LICENSE AUTHORS README.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.14.0-alt1
- Updated to upstream version 1.14.0.
- Disabled python-3 build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt1
- automated PyPI update

* Wed Apr 27 2016 Denis Medvedev <nbr@altlinux.org> 1.11.1-alt1
- 1.11.1. Removed changelog.rst from www since new sphinx chokes on that
file.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.10.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1
- Version 1.10.1

* Sun Jul 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt2
- Added module for Python 3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus

