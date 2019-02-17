%define _unpackaged_files_terminate_build 1
%define oname lz4

%def_with check

Name: python-module-%oname
Version: 2.1.6
Release: alt1
Summary: LZ4 Bindings for Python
License: BSD
Group: Development/Python
Url: https://pypi.org/project/lz4/

# https://github.com/python-lz4/python-lz4.git
Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python3

BuildRequires: liblz4-devel
BuildRequires: py3c-devel
BuildRequires: python2.7(pkgconfig)
BuildRequires: python2.7(setuptools_scm)
BuildRequires: python3(pkgconfig)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: /proc
BuildRequires: python2.7(future)
BuildRequires: python2.7(psutil)
BuildRequires: python2.7(pytest_cov)
BuildRequires: python3(future)
BuildRequires: python3(psutil)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tox)
%endif

%description
This package provides bindings for the lz4 compression library by Yann
Collet.

%package -n python3-module-%oname
Summary: LZ4 Bindings for Python
Group: Development/Python3

%description -n python3-module-%oname
This package provides bindings for the lz4 compression library by Yann
Collet.

%prep
%setup
# remove bundled libs in favor of system ones
rm -r lz4libs py3c

cp -fR . ../python3

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_install

pushd ../python3
%python3_install
popd

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
sed -i '/\[testenv\]/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/py.test3 \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
%_bindir/tox.py3 --sitepackages -p auto -o -v

%files
%doc *.rst
%python_sitelibdir/lz4-%version-py%_python_version.egg-info/
%python_sitelibdir/lz4/

%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/lz4-%version-py%_python3_version.egg-info/
%python3_sitelibdir/lz4/

%changelog
* Sat Feb 16 2019 Stanislav Levin <slev@altlinux.org> 2.1.6-alt1
- 0.8.2 -> 2.1.6.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.2-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.git20140728.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.git20140728.1
- NMU: Use buildreq for BR.

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20140728
- Initial build for Sisyphus

