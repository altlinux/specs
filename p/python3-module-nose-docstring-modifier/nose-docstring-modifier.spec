%define oname nose-docstring-modifier

Name: python3-module-%oname
Version: 0.0.6
Release: alt2

Summary: Add attributes next to the original docstring
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/nose-docstring-modifier/
BuildArch: noarch

# https://github.com/taykey/nose-docstring.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python-tools-2to3

%py3_provides nose_docstring_modifier


%description
This plugin enables you to modify docstring of tests based on their
attributes.

%prep
%setup

ln -s README.rst README.md

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.6-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.6-alt1.git20141126.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.6-alt1.git20141126.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20141126
- Version 0.0.6

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20141124
- Version 0.0.5

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20141106
- Version 0.0.4

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20141105
- Initial build for Sisyphus

