%define _unpackaged_files_terminate_build 1
%define oname lazy-object-proxy

%def_with check

Name: python3-module-%oname
Version: 1.5.1
Release: alt1

Summary: A fast and thorough lazy object proxy
License: BSD
Group: Development/Python3
# Source-git: https://github.com/ionelmc/python-lazy-object-proxy.git
Url: https://pypi.org/project/lazy-object-proxy/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_benchmark)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tox)
%endif

%py3_provides lazy-object-proxy

%description
This Python module is based on wrapt's ObjectProxy with one big change: it
calls a function the first time the proxy object is used, while
wrapt.ObjectProxy just forwards the method calls to the target object.

%prep
%setup

# adjust deps
grep -qsF 'pytest-travis-fold' tox.ini || exit 1
grep -qsF 'Django' tox.ini || exit 1
grep -qsF 'objproxies' tox.ini || exit 1
sed -i \
-e '/pytest-travis-fold/d' \
-e '/Django/d' \
-e '/objproxies/d' \
tox.ini

%build
%add_optflags -fno-strict-aliasing
%python3_build

%install
%python3_install

%check
sed -i -e '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/pytest\
    sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' \
-e '/setenv =/a\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/py.test3' \
tox.ini
export PIP_NO_INDEX=YES
export PIP_NO_BUILD_ISOLATION=no
export TOXENV=py%{python_version_nodots python3}-cover
tox.py3 --sitepackages -vvr

%files
%doc AUTHORS.rst README.rst CHANGELOG.rst
%dir %python3_sitelibdir/lazy_object_proxy
%python3_sitelibdir/lazy_object_proxy/*.py
%python3_sitelibdir/lazy_object_proxy/__pycache__/
%python3_sitelibdir/lazy_object_proxy/cext.cpython-*.so
%python3_sitelibdir/lazy_object_proxy-%version-py%_python3_version.egg-info/

%changelog
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
