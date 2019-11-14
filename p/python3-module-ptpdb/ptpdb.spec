%define oname ptpdb

Name: python3-module-%oname
Version: 0.17
Release: alt2

Summary: Python debugger (pdb) build on top of prompt_toolkit
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/ptpdb
# https://github.com/jonathanslenders/ptpdb.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: ptpython3 python3-module-prompt_toolkit

%py3_provides %oname
%py3_requires ptpython prompt_toolkit


%description
(Still experimental) PDB replacement, build on top of prompt_toolkit and
ptpython.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc *.rst examples
%python3_sitelibdir/*


%changelog
* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.17-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.17-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.17-alt1
- Updated to upstream version 0.17.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt1.git20150808.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20150808
- Initial build for Sisyphus

