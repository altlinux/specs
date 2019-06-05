%define _unpackaged_files_terminate_build 1
%define oname pluggy

%def_with check

Name: python-module-%oname
Version: 0.12.0
Release: alt1

Summary: Plugin and hook calling mechanisms for python
License: MIT
Group: Development/Python
# Source-git: https://github.com/pytest-dev/pluggy.git
Url: https://pypi.python.org/pypi/pluggy

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python2.7(setuptools_scm)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python2.7(importlib_metadata)
BuildRequires: python2.7(pytest)
BuildRequires: python3(importlib_metadata)
BuildRequires: python3(tox)
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

# there is a file with name CHANGELOG.rst, not CHANGELOG
# a wrong reference leads to broken install via pip
sed -i '/^include CHANGELOG$/{s/$/.rst/}' MANIFEST.in
rm -rf ../python3
cp -a . ../python3

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python_build

pushd ../python3
%python3_build
popd

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_install

pushd ../python3
%python3_install
popd

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
sed -i '/\[testenv\]/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/py.test3 \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini
tox.py3 --sitepackages -p auto -o -v -r


%files
%doc LICENSE CHANGELOG.rst README.rst
%python_sitelibdir/pluggy/
%python_sitelibdir/pluggy-*.egg-info/

%files -n python3-module-%oname
%doc LICENSE CHANGELOG.rst README.rst
%python3_sitelibdir/pluggy/
%python3_sitelibdir/pluggy-*.egg-info/

%changelog
* Thu Jun 06 2019 Stanislav Levin <slev@altlinux.org> 0.12.0-alt1
- 0.11.0 -> 0.12.0.

* Wed May 08 2019 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1
- 0.9.0 -> 0.11.0.

* Sun Mar 17 2019 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- 0.8.1 -> 0.9.0.

* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1
- 0.8.0 -> 0.8.1.

* Sat Oct 20 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.7.1 -> 0.8.0.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1
- 0.6.0 -> 0.7.1.

* Tue Mar 20 2018 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
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

