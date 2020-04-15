# %%define _unpackaged_files_terminate_build 1

%define oname ptpython

Name: %{oname}3
Version: 0.41
Release: alt3

Summary: Python REPL build on top of prompt_toolkit
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/ptpython/

BuildArch: noarch

# https://github.com/jonathanslenders/ptpython.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-prompt_toolkit

%py3_requires  IPython jedi

%description
ptpython is an advanced Python REPL built on top of the prompt_toolkit
library.

%prep
%setup
%patch1 -p1

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 tests/run_tests.py -v

%files
%doc CHANGELOG *.rst
%_bindir/*3
%python3_sitelibdir/*

%changelog
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

