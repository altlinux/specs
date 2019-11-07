%define oname mpltools

%def_disable check

Name: python3-module-%oname
Version: 0.2.0
Release: alt3

Summary: Tools for Matplotlib
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/mpltools/
# https://github.com/tonysyu/mpltools.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-matplotlib 
BuildPreReq: python3-module-pygobject3
BuildPreReq: python3-module-pycairo python3-module-mock
BuildPreReq: python3-module-nose python3-module-pytz

%py3_provides %oname
%py3_requires matplotlib configobj future gi cairo


%description
As the name implies, mpltools provides tools for working with
matplotlib. For the most part, these tools are only loosely-connected in
functionality, so the best way to get started is to look at the example
gallery: http://tonysyu.github.com/mpltools/auto_examples/index.html .

%prep
%setup

%build
%python3_build_debug

sed -i 's|#!.*/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%install
%python3_install

%check
export PYTHONPATH=$PWD
python3 setup.py test
python3 examples/plot_all_styles.py

%files
%doc *.rst examples/*.py
%python3_sitelibdir/*


%changelog
* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt3
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt2.git20150224.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt2.git20150224.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 0.2.0-alt2.git20150224
- turn off docs generation and tests

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150224
- Initial build for Sisyphus

