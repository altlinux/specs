%define oname sphinxcontrib-ansi
%def_with bootstrap

Name: python-module-%oname
Version: 0.6
Release: alt1.3
Summary: Sphinx extension ansi
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxcontrib-ansi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-sphinx
BuildPreReq: python-module-mock

%if_with bootstrap
%py_provides sphinxcontrib.ansi
%py_requires sphinxcontrib sphinx
%endif

%description
A Sphinx extension, which turns ANSI color sequences in Sphinx documents
into colored HTML output.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%if_without bootstrap
%check
python setup.py test
py.test -vv
%endif

%files
%doc README *.rst doc/*.rst
%python_sitelibdir/*

%changelog
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6-alt1.3
- (NMU) rebuild with all requires

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6-alt1.2
- (NMU) rebuild with python3.6

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Initial build for Sisyphus

