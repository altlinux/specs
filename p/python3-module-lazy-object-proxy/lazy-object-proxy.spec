%define _unpackaged_files_terminate_build 1
%define oname lazy-object-proxy

%def_with check

Name: python3-module-%oname
Version: 1.6.0
Release: alt2

Summary: A fast and thorough lazy object proxy
License: BSD
Group: Development/Python3
# Source-git: https://github.com/ionelmc/python-lazy-object-proxy.git
Url: https://pypi.org/project/lazy-object-proxy/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_benchmark)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

%py3_provides lazy-object-proxy

Conflicts: python-module-lazy_object_proxy
Obsoletes: python-module-lazy_object_proxy

%description
This Python module is based on wrapt's ObjectProxy with one big change: it
calls a function the first time the proxy object is used, while
wrapt.ObjectProxy just forwards the method calls to the target object.

%prep
%setup
%autopatch -p1

%build
%add_optflags -fno-strict-aliasing
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export PIP_NO_BUILD_ISOLATION=no
export TOXENV=py%{python_version_nodots python3}-cover
tox.py3 --sitepackages -vvr --no-deps --console-scripts -s false

%files
%doc AUTHORS.rst README.rst CHANGELOG.rst
%dir %python3_sitelibdir/lazy_object_proxy
%python3_sitelibdir/lazy_object_proxy/*.py
%python3_sitelibdir/lazy_object_proxy/__pycache__/
%python3_sitelibdir/lazy_object_proxy/cext.cpython-*.so
%python3_sitelibdir/lazy_object_proxy-%version-py%_python3_version.egg-info/

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt2
- Added conflict to old package.

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1
- 1.5.1 -> 1.6.0.

* Mon Sep 07 2020 Stanislav Levin <slev@altlinux.org> 1.5.1-alt1
- 1.4.2 -> 1.5.1.

* Wed Oct 16 2019 Stanislav Levin <slev@altlinux.org> 1.4.2-alt1
- 1.4.1 -> 1.4.2.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 1.4.1-alt2
- Fixed testing against Pytest 5.

* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 1.4.1-alt1
- 1.3.1 -> 1.4.1.

* Mon Sep 03 2018 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- Initial build.
