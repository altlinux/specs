%define oname functest
Name: python-module-%oname
Version: 0.8.8
Release: alt2.1
Summary: Functional test framework
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/functest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools
BuildArch: noarch

%py_provides %oname

%description
Functest is a test tool/framework for testing in python.

It focuses on strong debugging, zero boiler plate, setup/teardown module
hierarchies, and distributed result reporting.

%prep
%setup

%build
%python_build_debug

%install
%python_install

# There is a file in the package with a name starting with <tt>._</tt>, 
# the file name pattern used by Mac OS X to store resource forks in non-native 
# file systems. Such files are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f


%check
python setup.py test

%files
%doc PKG-INFO
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/tests

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.8-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt2
- Applied python-module-functest-0.8.8-alt1.diff

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt1
- Initial build for Sisyphus

