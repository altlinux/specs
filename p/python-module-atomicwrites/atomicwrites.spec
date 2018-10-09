%define _unpackaged_files_terminate_build 1
%define oname atomicwrites

%def_with check

Name: python-module-%oname
Version: 1.2.1
Release: alt1

Summary: Python Atomic file writes on POSIX
License: MIT
Group: Development/Python
# Source-git: https://github.com/untitaker/python-atomicwrites.git
Url: https://pypi.org/project/atomicwrites

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python-module-tox
BuildRequires: python3-module-tox
%endif

BuildArch: noarch

%define long_desc This module provides atomic file writes on POSIX operating  \
systems. It supports:                                                         \
* Race-free assertion that the target file doesn't yet exist                  \
* Simple high-level API that wraps a very flexible class-based API            \
* Consistent error handling across platforms

%description
%long_desc

%package -n python3-module-%oname
Summary: Python3 Atomic file writes on POSIX
Group: Development/Python3

%description -n python3-module-%oname
%long_desc

%prep
%setup
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
export PIP_INDEX_URL=http://host.invalid./

# copy nessecary exec deps
tox --sitepackages -e py%{python_version_nodots python}-test --notest
cp -T %_bindir/py.test .tox/py%{python_version_nodots python}-test/bin/py.test

export PYTHONPATH=build/lib
TOX_TESTENV_PASSENV='PYTHONPATH' tox --sitepackages -e \
py%{python_version_nodots python}-test -v -- -v

pushd ../python3
tox.py3 --sitepackages -e py%{python_version_nodots python3}-test --notest
cp -T %_bindir/py.test3 .tox/py%{python_version_nodots python3}-test/bin/py.test

TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 --sitepackages -e \
py%{python_version_nodots python3}-test -v -- -v
popd

%files
%doc LICENSE README.rst
%python_sitelibdir/atomicwrites/
%python_sitelibdir/atomicwrites-*.egg-info/

%files -n python3-module-%oname
%doc LICENSE README.rst
%python3_sitelibdir/atomicwrites/
%python3_sitelibdir/atomicwrites-*.egg-info/

%changelog
* Tue Oct 09 2018 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.2.0 -> 1.2.1.

* Thu Aug 30 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.5 -> 1.2.0.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 1.1.5-alt1
- Initial build.

