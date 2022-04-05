%define _unpackaged_files_terminate_build 1
%define oname requests-oauthlib

Name: python3-module-%oname
Version: 1.3.1
Release: alt1

Summary: OAuthlib authentication support for Requests

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/requests-oauthlib

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
This project provides first-class OAuth library support for Requests.

%prep
%setup

#prepare_sphinx .
#ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install
%python3_prune

#export PYTHONPATH=%buildroot%python_sitelibdir
#make -C docs html

%files
%doc *.rst PKG-INFO docs
%python3_sitelibdir/*

%changelog
* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version 1.3.1 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt2
- build python3 package separately

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20140606.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1.git20140606.1
- NMU: Use buildreq for BR.

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20140606
- Initial build for Sisyphus

