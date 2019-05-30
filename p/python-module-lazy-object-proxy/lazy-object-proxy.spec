%define _unpackaged_files_terminate_build 1
%define oname lazy-object-proxy

%def_with check

Name: python-module-%oname
Version: 1.4.1
Release: alt1

Summary: A fast and thorough lazy object proxy
License: BSD
Group: Development/Python
# Source-git: https://github.com/ionelmc/python-lazy-object-proxy.git
Url: https://pypi.org/project/lazy-object-proxy/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python2.7(setuptools_scm)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python2.7(pytest)
BuildRequires: python2.7(pytest_benchmark)
BuildRequires: python2.7(pytest_cov)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_benchmark)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tox)
%endif

%description
This Python module is based on wrapt's ObjectProxy with one big change: it
calls a function the first time the proxy object is used, while
wrapt.ObjectProxy just forwards the method calls to the target object.

%package -n python3-module-%oname
Summary: A fast and thorough lazy object proxy
Group: Development/Python3

%description -n python3-module-%oname
This Python3 module is based on wrapt's ObjectProxy with one big change: it
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

# make use of -fno-strict-aliasing inside tox
grep -qsF 'SETUPPY_CFLAGS=-coverage' tox.ini || exit 1
sed -i 's/SETUPPY_CFLAGS=-coverage/& -fno-strict-aliasing/g' tox.ini

rm -rf ../python3
cp -a . ../python3

%build
%add_optflags -fno-strict-aliasing
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
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    cp %_bindir\/py.test3 \{envbindir\}\/pytest\
    sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python}-cover,\
py%{python_version_nodots python3}-cover
tox.py3 --sitepackages -p auto -o -rv

%files
%doc AUTHORS.rst README.rst CHANGELOG.rst
%dir %python_sitelibdir/lazy_object_proxy
%python_sitelibdir/lazy_object_proxy/*.py
%python_sitelibdir/lazy_object_proxy/*.py[co]
%python_sitelibdir/lazy_object_proxy/cext.so
%python_sitelibdir/lazy_object_proxy-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%doc AUTHORS.rst README.rst CHANGELOG.rst
%dir %python3_sitelibdir/lazy_object_proxy
%python3_sitelibdir/lazy_object_proxy/*.py
%python3_sitelibdir/lazy_object_proxy/__pycache__/
%python3_sitelibdir/lazy_object_proxy/cext.cpython-*.so
%python3_sitelibdir/lazy_object_proxy-%version-py%_python3_version.egg-info/

%changelog
* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 1.4.1-alt1
- 1.3.1 -> 1.4.1.

* Mon Sep 03 2018 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- Initial build.
