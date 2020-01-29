%define oname functest

Name:       python3-module-%oname
Version:    0.8.8
Release:    alt3

Summary:    Functional test framework
License:    ASLv2.0
Group:      Development/Python3
Url:        https://pypi.python.org/pypi/functest/

BuildArch:  noarch

Source:     %name-%version.tar
Patch0:     port-on-python3.patch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
Conflicts: python-module-%oname


%description
Functest is a test tool/framework for testing in python.

It focuses on strong debugging, zero boiler plate, setup/teardown module
hierarchies, and distributed result reporting.

%prep
%setup
%patch0 -p2

%build
%python3_build_debug

%install
%python3_install

# There is a file in the package with a name starting with <tt>._</tt>, 
# the file name pattern used by Mac OS X to store resource forks in non-native 
# file systems. Such files are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f

%check
%__python3 setup.py test

%files
%doc PKG-INFO
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests


%changelog
* Wed Jan 29 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.8.8-alt3
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.8-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt2
- Applied python-module-functest-0.8.8-alt1.diff

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt1
- Initial build for Sisyphus

