%define _unpackaged_files_terminate_build 1
%define oname filedepot
# depends on unmaintained nose
%def_disable check

Name: python3-module-%oname
Version: 0.8.0
Release: alt1
Summary: Toolkit for storing files and attachments in web applications
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/filedepot/

# https://github.com/amol-/depot.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_requires anyascii
%py3_provides %oname

%description
DEPOT is a framework for easily storing and serving files in web
applications on Python2.6+ and Python3.2+.

%prep
%setup

# drop boto-based connector (boto was replaced with boto3)
rm depot/io/awss3.py

%build
%python3_build

%install
%python3_install

%check

%files
%doc *.rst
%python3_sitelibdir/depot/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Wed Mar 09 2022 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.7.1 -> 0.8.0.

* Wed Dec 04 2019 Anton Farygin <rider@altlinux.ru> 0.7.1-alt1
- 0.7.1
- disabled python2 version

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1
- Updated to upstream version 0.5.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt1.git20150209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.3-alt1.git20150209.1
- NMU: Use buildreq for BR.

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20150209
- Initial build for Sisyphus

