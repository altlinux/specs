%define oname tkform

Name: python3-module-%oname
Version: 0.9
Release: alt2

Summary: A tkinter form-based GUI that wraps python scripts
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/tkform/
BuildArch: noarch

# https://github.com/boscoh/tkform.git
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-modules-tkinter

%py3_provides %oname


%description
tkform wraps an elegant form-based GUI around Python scripts using only
standard Python.

%prep
%setup
%patch0 -p1

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.md *.png tkform_ex*
%python3_sitelibdir/*


%changelog
* Wed Jan 29 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.9-alt2
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9-alt1.git20150220.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.git20150220
- Initial build for Sisyphus

