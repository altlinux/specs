%define oname functools32

%def_without check

Name:       python3-module-%oname
Version:    3.2.3.2
Release:    alt2

Summary:    Backport of the functools module from Python 3.2.3 for use on 2.7 and PyPy
License:    PSF
Group:      Development/Python3
Url:        https://pypi.python.org/pypi/functools32/

BuildArch:  noarch

#           https://github.com/MiCHiLU/python-functools32.git
Source:     %name-%version.tar
Patch0:     port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
This is a backport of the functools standard library module from Python
3.2.3 for use on Python 2.7 and PyPy. It includes new features lru_cache
(Least-recently-used cache decorator).

%prep
%setup
%patch0 -p1

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 test_functools32.py -v

%files
%doc ChangeLog *.rst
%python3_sitelibdir/*


%changelog
* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.2.3.2-alt2
- Porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.2.3.2-alt1.git20150711.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.3.2-alt1.git20150711
- Initial build for Sisyphus

