%define _unpackaged_files_terminate_build 1
%define oname pytest-datafiles

Name: python3-module-%oname
Version: 1.0
Release: alt2

Summary: py.test plugin to create a 'tmpdir' containing predefined files/directories
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-datafiles/
BuildArch: noarch

# https://github.com/omarkohl/pytest-datafiles.git
Source0: https://pypi.python.org/packages/22/9b/bc99e1f5abc17d746e41b1fbfb2643268a75189fd7102eff2cd6f2ecc087/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides pytest_datafiles
%py3_requires pytest


%description
py.test plugin to create a tmpdir containing a preconfigured set of
files and/or directories.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.dev0.git20150728.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.dev0.git20150728
- Initial build for Sisyphus

