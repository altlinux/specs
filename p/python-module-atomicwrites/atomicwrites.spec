%define _unpackaged_files_terminate_build 1
%define oname atomicwrites

%def_with check

Name: python-module-%oname
Version: 1.3.0
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
sed -i '/\[testenv\]/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/py.test3 \{envbindir\}\/py.test\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python}-test,py%{python_version_nodots python3}-test
tox.py3 --sitepackages -p auto -o -v

%files
%doc LICENSE README.rst
%python_sitelibdir/atomicwrites/
%python_sitelibdir/atomicwrites-*.egg-info/

%files -n python3-module-%oname
%doc LICENSE README.rst
%python3_sitelibdir/atomicwrites/
%python3_sitelibdir/atomicwrites-*.egg-info/

%changelog
* Mon Feb 11 2019 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.1 -> 1.3.0.

* Tue Oct 09 2018 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.2.0 -> 1.2.1.

* Thu Aug 30 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.5 -> 1.2.0.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 1.1.5-alt1
- Initial build.

