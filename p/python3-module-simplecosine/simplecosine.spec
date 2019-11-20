%define _unpackaged_files_terminate_build 1
%define oname simplecosine

Name: python3-module-%oname
Version: 1.1
Release: alt2

Summary: Simple cosine distance
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/simplecosine/
BuildArch: noarch

Source0: https://pypi.python.org/packages/20/af/fc538611b39e3fa884054051d65b10325ac5fc55e4f946a8b443950f52ba/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-numpy

%py3_provides %oname
%py3_requires numpy

%description
Simple cosine distance.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%python3_sitelibdir/*


%changelog
* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

