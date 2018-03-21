%define _unpackaged_files_terminate_build 1
%define oname pluggy

%def_with check

Name: python-module-%oname
Version: 0.6.0
Release: alt1%ubt

Summary: Plugin and hook calling mechanisms for python
License: MIT
Group: Development/Python
# Source-git: https://github.com/pytest-dev/pluggy.git
Url: https://pypi.python.org/pypi/pluggy

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-pytest
BuildRequires: python-module-tox
BuildRequires: python-module-virtualenv
BuildRequires: python3-module-pytest
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
%endif

BuildArch: noarch

%description
This is the plugin manager as used by pytest but stripped of pytest
specific details.

%package -n python3-module-%oname
Summary: Plugin and hook calling mechanisms for python
Group: Development/Python3

%description -n python3-module-%oname
This is the plugin manager as used by pytest but stripped of pytest
specific details.

%prep
%setup
# change py.test to python -m pytest
# py.test execute tests out from tox virt env context, but
# python -m pytest within
sed -i '/^\[testenv\]$/ {N; s/\[testenv\]\ncommands=py.test/\[testenv\]\ncommands=python -m pytest/g;h};${x;/./{x;q0};x;q1}' tox.ini
rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
%define python_version_nodots() %(%1 -Esc "import sys; sys.stdout.write('{0.major}{0.minor}'.format(sys.version_info))")

export PIP_INDEX_URL=http://host.invalid./
tox --sitepackages -e py%{python_version_nodots python}-pytestrelease -v

pushd ../python3
tox.py3 --sitepackages -e py%{python_version_nodots python3}-pytestrelease -v
popd

%files
%doc LICENSE *.rst
%python_sitelibdir/*

%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/*

%changelog
* Tue Mar 20 2018 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1%ubt
- 0.3.0 -> 0.6.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.git20150528.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt1.git20150528.2
- Fixed build spec with py.test3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20150528.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150528
- Initial build for Sisyphus

