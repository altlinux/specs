%define oname webplot

Name: python3-module-%oname
Version: 0.8
Release: alt2

Summary: Expose matplotlib figures over http
License: GPLv2
Group: Development/Python3
Url: https://pypi.python.org/pypi/webplot/
# https://github.com/huyng/webplot.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-matplotlib python3-module-flask
BuildRequires: python-tools-2to3

%py3_provides %oname
%py3_requires matplotlib flask


%description
Expose your matplotlib figures over http with 1 line of code.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.8-alt2
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8-alt1.git20150320.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8-alt1.git20150320.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.git20150320
- Initial build for Sisyphus

