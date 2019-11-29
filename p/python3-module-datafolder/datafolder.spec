%define _unpackaged_files_terminate_build 1
%define oname datafolder

Name: python3-module-%oname
Version: 0.3.6
Release: alt2

Summary: Install and access data files (conf, json, sqlite3, ...) in an easy way
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/datafolder/
BuildArch: noarch

# https://github.com/xlcnd/datafolder.git
Source0: https://pypi.python.org/packages/ec/8b/cc0f6bc805e9fe56a401306126d500498d619e5b96f4d4830f62fa3a48e0/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose

%py3_provides %oname
%py3_requires setuptools


%description
datafolder is a small python library that makes it very easy to install
the data files of your package and access them later.

If you want to install some data files (conf, sqlite, csv, ...) to a
place like the user's home directory and find it difficult with
setuptools, then here is some help.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
nosetests3 -v

%files
%doc CHANGES.txt *.rst
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.6-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.5-alt1.git20150225.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.git20150225
- Version 0.3.5

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150210
- Version 0.2.1

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150208
- Initial build for Sisyphus

