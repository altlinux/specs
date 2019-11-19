%define oname progress

Name: python3-module-%oname
Version: 1.2
Release: alt2

Summary: Easy to use progress bars
License: ISC
Group: Development/Python3
Url: https://pypi.python.org/pypi/progress
# https://github.com/verigak/progress.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
Easy progress reporting for Python.

There are 6 progress bars to choose from:
* Bar
* ChargingBar
* FillingSquaresBar
* FillingCirclesBar
* IncrementalBar
* ShadyBar

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v
%__python3 test_progress.py -v

%files
%doc LICENSE *.rst
%python3_sitelibdir/*


%changelog
* Tue Nov 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2-alt2
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2-alt1.git20131128.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt1.git20131128.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20131128
- Initial build for Sisyphus

