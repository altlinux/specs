%define _unpackaged_files_terminate_build 1
%define oname http-checks

Name: python3-module-%oname
Version: 0.2.1
Release: alt1

Summary: Test a couple of hundred urls in seconds

License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/http-checks/

# Source-url: %__pypi_url %oname
Source: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro >= 2.2.4

BuildRequires: python3-module-yaml python3-module-requests
BuildRequires: python3-module-gevent python3-module-BeautifulSoup4
BuildRequires: python3(json) python3(jsonpath_rw)

%py3_provides httpchecks
%py3_requires yaml gevent bs4

%description
http-checks is an application that can test a couple of hundred urls in
seconds.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%check
export PATH=$PATH:%buildroot%_bindir

python3 setup.py test
export PYTHONPATH=$PWD
#http-checks.py3 -c check_sample.yml

%files
%doc PKG-INFO
%_bindir/*
%python3_sitelibdir/*


%changelog
* Wed Apr 21 2021 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- NMU: new version 0.2.1 (with rpmrb script)

* Wed Oct 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt2
- disable python2, enable python3

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1.1.qa1
- NMU: applied repocop patch

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt1
- Updated to upstream version 0.2.0.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt1
- automated PyPI update

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.7-alt1.git20150106
- Version 0.1.7

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.git20141127
- Version 0.1.6

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20141126
- Initial build for Sisyphus

