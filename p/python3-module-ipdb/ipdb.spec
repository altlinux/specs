%define _unpackaged_files_terminate_build 1
%define oname ipdb

%def_with check

Name: python3-module-%oname
Version: 0.13.13
Release: alt1
Summary: IPython-enabled pdb
License: BSD 3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/ipdb/

# https://github.com/gotcha/ipdb.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: ipython3

%if_with check
BuildRequires: python3-module-mock
BuildRequires: python3-module-toml
%endif

%description
ipdb exports functions to access the IPython debugger, which features
tab completion, syntax highlighting, better tracebacks, better
introspection with the same interface as the pdb module.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
PYTHONPATH=%buildroot%python3_sitelibdir python3 setup.py test

%files
%doc *.txt *.rst
%_bindir/%{oname}3
%python3_sitelibdir/*

%changelog
* Fri Mar 10 2023 Grigory Ustinov <grenka@altlinux.org> 0.13.13-alt1
- Automatically updated to 0.13.13.

* Mon Dec 19 2022 Grigory Ustinov <grenka@altlinux.org> 0.13.11-alt1
- Automatically updated to 0.13.11.

* Thu May 26 2022 Grigory Ustinov <grenka@altlinux.org> 0.13.9-alt1
- Automatically updated to 0.13.9.

* Thu Jun 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.13.4-alt2
- Updated build dependencies.

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 0.13.4-alt1
- Automatically updated to 0.13.4.

* Thu Sep 03 2020 Grigory Ustinov <grenka@altlinux.org> 0.10.3-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.3-alt1
- Updated to upstream version 0.10.3.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.1-alt1.dev0.git20130919.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.dev0.git20130919
- Initial build for Sisyphus

