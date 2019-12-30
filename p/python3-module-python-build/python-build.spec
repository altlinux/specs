%define oname python-build

Name: python3-module-%oname
Version: 0.2.1
Release: alt2

Summary: Tool to download and build python based upon pyenv
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-build/
BuildArch: noarch

# https://github.com/crdoconnor/python-build.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides python_build


%description
BuildPython is a python library to download and build a version of
python into a specified directory.

It can substitute for virtualenv.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%filter_from_requires /^python-base/d

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*


%changelog
* Mon Dec 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.1-alt2
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.1-alt1.git20150708.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20150708.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1.git20150708.1
- NMU: Use buildreq for BR.

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150708
- Initial build for Sisyphus

