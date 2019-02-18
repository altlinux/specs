%define _unpackaged_files_terminate_build 1
%define modname daemon

%def_with check

Name: python-module-%modname
Version: 2.2.3
Release: alt1

Summary: Library to implement a well-behaved Unix daemon process
License: Apache-2.0 / GPLv3
Group: Development/Python
Url: https://pypi.org/project/python-daemon/
Packager: Python Development Team <python@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python2.7(json)
BuildRequires: python2.7(docutils)
BuildRequires: python3(docutils)

%if_with check
BuildRequires: python3(lockfile)
BuildRequires: python3(mock)
BuildRequires: python3(testscenarios)
BuildRequires: python3(tox)
%endif

%description
A well-behaved Unix daemon process is tricky to get right, but the required
steps are much the same for every daemon program. A DaemonContext instance
holds the behaviour and configured process environment for the program; use the
instance as a context manager to enter a daemon state.

%package -n python3-module-%modname
Summary: Library to implement a well-behaved Unix daemon process
Group: Development/Python3

%description -n python3-module-%modname
A well-behaved Unix daemon process is tricky to get right, but the required
steps are much the same for every daemon program. A DaemonContext instance
holds the behaviour and configured process environment for the program; use the
instance as a context manager to enter a daemon state.

%prep
%setup
%patch -p1

rm -rf ../python3
cp -fR . ../python3

%build
# workaround https://pagure.io/python-daemon/issue/31
python setup.py egg_info
%python_build

pushd ../python3
python3 setup.py egg_info
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
# skip for now PEP517/PEP518
rm pyproject.toml
# relax requirements
sed -i '/deps = -r{toxinidir}\/pip-requirements\/test\.txt/d' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
%_bindir/tox.py3 --sitepackages -p auto -o -v -- -ra

%files
%doc ChangeLog LICENSE.* README doc/*
%python_sitelibdir/%modname/
%python_sitelibdir/python_daemon-%version-py%_python_version.egg-info/

%files -n python3-module-%modname
%doc ChangeLog LICENSE.* README doc/*
%python3_sitelibdir/%modname/
%python3_sitelibdir/python_daemon-%version-py%_python3_version.egg-info/


%changelog
* Mon Feb 18 2019 Stanislav Levin <slev@altlinux.org> 2.2.3-alt1
- 2.1.2 -> 2.2.3.
- Enable testing.
- Fixed build against setuptools 40.7.0+.

* Wed Mar 21 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.1.2-alt1
- Version 2.1.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.5-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.5-alt2
- NMU: added python-modules-json and python-module-setuptools to BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.5-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 19 2015 Terechkov Evgenii <evg@altlinux.org> 2.0.5-alt1
- Update to 2.0.5

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.5-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.5-alt2.1
- Rebuild with Python-2.7

* Fri Aug 13 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.5.5-alt2
- pidlockfile.py: add checking for stale {pid,lock}file

* Sun Apr 04 2010 Denis Klimov <zver@altlinux.org> 1.5.5-alt1
- Initial build for ALT Linux
