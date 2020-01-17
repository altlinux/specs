%define oname readthedocs-sphinx-ext

Name: python3-module-%oname
Version: 1.0.1
Release: alt1

Summary: This holds code specific for Read the Docs and Sphinx
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/readthedocs-sphinx-ext/
BuildArch: noarch

# https://github.com/rtfd/readthedocs-sphinx-ext.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx

%py3_provides readthedocs_ext


%description
Tooling for a better Read the Docs Sphinx build experience.

%prep
%setup

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
* Fri Jan 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt1
- Version updated to 1.0.1
- porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.3-alt1.git20141102.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.git20141102
- Initial build for Sisyphus

