%define _unpackaged_files_terminate_build 1

%define oname contextlib2
%def_with check

Name: python-module-%oname
Version: 0.5.5
Release: alt1

Summary: Backports and enhancements for the contextlib module

Group: Development/Python
License: LGPLv2+
Url: https://pypi.org/project/contextlib2/

# Source-git: https://github.com/jazzband/contextlib2.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python-module-coverage
BuildRequires: python-module-unittest2
BuildRequires: python3-module-coverage
BuildRequires: python3-module-tox
%endif

%description
contextlib2 is a backport of the standard library's contextlib
module to earlier Python versions.

It also serves as a real world proving ground for possible
future enhancements to the standard library version.

%package -n python3-module-%oname
Summary: Backports and enhancements for the contextlib module
Group: Development/Python3

%description -n python3-module-%oname
contextlib2 is a backport of the standard library's contextlib
module to earlier Python versions.

It also serves as a real world proving ground for possible
future enhancements to the standard library version.

%prep
%setup

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
sed -i '/\[testenv\]/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/coverage3 \{envbindir\}\/coverage\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/coverage' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%python_sitelibdir/contextlib2.py*
%python_sitelibdir/contextlib2-*.egg-info/

%files -n python3-module-%oname
%python3_sitelibdir/contextlib2.py
%python3_sitelibdir/__pycache__/contextlib2.cpython-*.py*
%python3_sitelibdir/contextlib2-*.egg-info/

%changelog
* Mon Jan 28 2019 Stanislav Levin <slev@altlinux.org> 0.5.5-alt1
- 0.4.0 -> 0.5.5.

* Fri Feb 03 2017 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1.1.1.1.1.1
- BOOTSTRAP: avoid python-module-mwlib -> gevent -> greenlet (!e2k)

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.1.1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1.1.1
- NMU: Use buildreq for BR.

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.1
- Added module for Python 3

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus
