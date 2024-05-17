%define _unpackaged_files_terminate_build 1

%define oname ptpython

Name: python3-module-%oname
Version: 3.0.26
Release: alt1
Summary: Python REPL build on top of prompt_toolkit
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/ptpython
VCS: https://github.com/jonathanslenders/ptpython

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-prompt_toolkit python3-module-setuptools python3-module-wheel
BuildRequires: python3(pygments)

Provides: %oname = %version.%release
Provides: %{oname}3 = %version.%release
Obsoletes: %{oname}3 < %version.%release

%py3_requires  jedi

%description
ptpython is an advanced Python REPL built on top of the prompt_toolkit
library.

%package ipython
Group: Development/Python3
Summary: IPython addon for ptpython
Provides: %oname-ipython = %version.%release

%description ipython
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE
%doc CHANGELOG *.rst
%doc examples
%_bindir/*
%exclude %_bindir/*ipython*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-*dist-info
%exclude %python3_sitelibdir/%oname/*ipython*

%files ipython
%_bindir/*ipython*
%python3_sitelibdir/%oname/*ipython*

%changelog
* Fri May 17 2024 Grigory Ustinov <grenka@altlinux.org> 3.0.26-alt1
- Build new version.

* Mon Jan 29 2024 Grigory Ustinov <grenka@altlinux.org> 3.0.25-alt1
- NMU: Build new version.

* Tue Sep 12 2023 Fr. Br. George <george@altlinux.org> 3.0.23-alt1
- Autobuild version bump to 3.0.23

* Wed Jan 19 2022 Fr. Br. George <george@altlinux.ru> 3.0.20-alt1
- Autobuild version bump to 3.0.20
- Separate IPython add-on

* Tue Sep 15 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.5-alt1
- Updated to upstream version 3.0.5.

* Wed Apr 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.41-alt3
- Build for python2 disabled.

* Fri Apr 19 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.41-alt2
- Fixed build with python-3.7.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.41-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.41-alt1
- Updated to upstream version 0.41.

* Thu Aug 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.38-alt1
- Updated to upstream version 0.38.

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.20-alt1.git20150808.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20-alt1.git20150808
- Initial build for Sisyphus

