%define _unpackaged_files_terminate_build 1
%define oname nosepipe

Name: python3-module-%oname
Version: 0.9
Release: alt2

Summary: Plugin for the nose testing framework for running tests in a subprocess
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/nosepipe/
# https://github.com/dmccombs/nosepipe.git
BuildArch: noarch

# Source-url: https://pypi.io/packages/source/n/%oname/%oname-%version.tar.gz
Source: %name-%version.tar


BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-nose python3-module-django-nose

%py3_provides %oname


%description
Plugin for the nose testing framework for running tests in a subprocess.

Use nosetests --with-process-isolation to enable the plugin. When
enabled, each test is run in a separate process.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9-alt2
- disable python2

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- new version 0.9 (with rpmrb script)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt1.git20150720.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20150720
- Version 0.7

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.git20150224
- Version 0.6

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20141114
- Initial build for Sisyphus

