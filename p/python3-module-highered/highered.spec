%define oname highered

%def_with python3

Name: python3-module-%oname
Version: 0.1.5
Release: alt2

Summary: CRF Edit Distance
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/highered
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-numpy python3-module-pyhacrf

%py3_provides %oname
%py3_requires numpy pyhacrf


%description
Learnable Edit Distance Using PyHacrf.

%prep
%setup

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test -v

%files
%doc PKG-INFO
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.5-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.5-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus

