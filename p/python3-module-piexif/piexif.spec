%define _unpackaged_files_terminate_build 1
%define oname piexif

Name: python3-module-%oname
Version: 1.0.13
Release: alt2

Summary: Exif manipulation with pure python script
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/piexif/
BuildArch: noarch

# https://github.com/hMatoba/Piexif.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Pillow

%py3_provides %oname


%description
This is a renamed project from Pyxif.
To simplify exif manipulations with python. Writing, reading, and more...
Piexif isn't a wrapper. To everywhere with Python.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst *sample*.py
%python3_sitelibdir/*


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.13-alt2
- python2 disabled

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

