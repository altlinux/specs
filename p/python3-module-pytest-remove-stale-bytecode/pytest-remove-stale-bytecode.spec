%define _unpackaged_files_terminate_build 1
%define oname pytest-remove-stale-bytecode

Name: python3-module-%oname
Version: 2.1
Release: alt2

Summary: py.test plugin to remove stale byte code files
License: ZPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-remove-stale-bytecode
BuildArch: noarch

Source0: https://pypi.python.org/packages/3d/29/8389e329a55beb7b752d94fc28e9acaf6c3e6791f17cec86736a47853294/%{oname}-%{version}.zip

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest unzip


%description
This plugin removes all stale bytecode files before running tests. This
makes sure that removed python files are no longer visible for the test
runner as their bytecode file (*.pyc, *.pyo) is removed as well.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt *.rst
%python3_sitelibdir/*


%changelog
* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

