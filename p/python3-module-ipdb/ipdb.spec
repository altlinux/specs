%define _unpackaged_files_terminate_build 1
%define oname ipdb

Name: python3-module-%oname
Version: 0.10.3
Release: alt2
Summary: IPython-enabled pdb
License: GPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/ipdb/

# https://github.com/gotcha/ipdb.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: ipython3
BuildRequires: python3-module-pathlib2

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

