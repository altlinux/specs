%define oname sphinx_readable_theme

Name: python3-module-%oname
Version: 1.3.0
Release: alt2

Summary: Sphinx Readable Theme
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/sphinx-readable-theme/
BuildArch: noarch

# https://github.com/ignacysokolowski/sphinx-readable-theme.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_provides %oname


%description
A clean and readable Sphinx theme with focus on autodoc - documentation
from docstrings.

Inspired by flask-sphinx-themes.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
export LC_ALL=en_US.UTF-8
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst docs/source/*.rst docs/source/example.py
%python3_sitelibdir/*


%changelog
* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3.0-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.git20150327.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.git20150327.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20150327
- Initial build for Sisyphus

