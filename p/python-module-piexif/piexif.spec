%define _unpackaged_files_terminate_build 1
%define oname piexif

%def_with python3

Name: python-module-%oname
Version: 1.0.13
Release: alt1.1
Summary: Exif manipulation with pure python script
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/piexif/

# https://github.com/hMatoba/Piexif.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-Pillow
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-Pillow
%endif

%py_provides %oname

%description
This is a renamed project from Pyxif.
To simplify exif manipulations with python. Writing, reading, and more...
Piexif isn't a wrapper. To everywhere with Python.

%if_with python3
%package -n python3-module-%oname
Summary: Exif manipulation with pure python script
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This is a renamed project from Pyxif.
To simplify exif manipulations with python. Writing, reading, and more...
Piexif isn't a wrapper. To everywhere with Python.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst *sample*.py
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *sample*.py
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.13-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.13-alt1
- Updated to upstream version 1.0.13.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.c.git20150128.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.c.git20150128
- Initial build for Sisyphus

