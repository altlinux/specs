%define _unpackaged_files_terminate_build 1
%define oname categorical-distance

Name: python3-module-%oname
Version: 1.9
Release: alt2

Summary: Compare categorical variables
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/categorical-distance/
BuildArch: noarch

# https://github.com/datamade/categorical-distance.git
Source0: https://pypi.python.org/packages/48/5c/fc965dba19378a75936ab27fb44f4e8d4ffe14eff27daf51ced701f423b2/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-numpy python3-module-nose
BuildRequires: python-tools-2to3

%py3_provides categorical
%py3_requires numpy


%description
Compare two categorical variables.

%prep
%setup -q -n %{oname}-%{version}

## py2 -> py3
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')
##

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
nosetests3 -vv

%files
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.9-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.9-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5-alt1.git20150304.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20150304
- Version 1.5
- Added module for Python 3

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.git20141205
- Fixed build

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20141205
- Initial build for Sisyphus

