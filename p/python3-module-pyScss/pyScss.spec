%define _unpackaged_files_terminate_build 1

%define oname pyScss

%def_with check

Name: python3-module-%oname
Version: 1.3.7
Release: alt3
Summary: pyScss is a compiler for the Sass language
License: MIT
Group: Development/Python
Url: https://pypi.org/project/pyScss/

# https://github.com/Kronuz/pyScss.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: libpcre-devel
BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(PIL)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%py3_provides %oname
%py3_requires PIL

%description
pyScss is a compiler for the Sass language, a superset of CSS3 that adds
programming capabilities and some other syntactic sugar.

%prep
%setup
%patch1 -p1

# fix shebangs
grep -sm1 -rl \
    -e '^#!/usr/bin/env python.*$' | \
xargs sed -s -e '1 s/^#!\/usr\/bin\/env python.*$/#!\/usr\/bin\/python3/'

%build
%add_optflags -I%_includedir/pcre -fno-strict-aliasing
%python3_build_debug

%install
%python3_install
install -p -m644 scss/grammar/*.g \
	%buildroot%python3_sitelibdir/scss/grammar/

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%check
sed -i '/^\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py3: _PYTEST_BIN=%_bindir\/py.test3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/py.test\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test' tox.ini
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vv -r

%files
%doc DESCRIPTION *.rst
%_bindir/less2scss.py3
%_bindir/pyscss.py3
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%dir %python3_sitelibdir/scss
%python3_sitelibdir/scss/*.py
%python3_sitelibdir/scss/__pycache__/
%dir %python3_sitelibdir/scss/grammar
%python3_sitelibdir/scss/grammar/*.py
%python3_sitelibdir/scss/grammar/*.g
%python3_sitelibdir/scss/grammar/_scanner.*.so
%python3_sitelibdir/scss/grammar/__pycache__/
%python3_sitelibdir/scss/extension/

%changelog
* Fri Dec 17 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.7-alt3
- Fixed build with python3.10.

* Wed Aug 05 2020 Stanislav Levin <slev@altlinux.org> 1.3.7-alt2
- Fixed FTBFS(new pytest 6.0.1).

* Thu Apr 30 2020 Stanislav Levin <slev@altlinux.org> 1.3.7-alt1
- 1.3.5 -> 1.3.7.
- Dropped Python2 build.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.5-alt3.qa1
- NMU: applied repocop patch

* Fri Aug 31 2018 Stanislav Levin <slev@altlinux.org> 1.3.5-alt3
- Fix build

* Wed May 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.5-alt2
- Updated build and runtime dependencies.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.5-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.5-alt1
- Updated to upstream release version 1.3.5.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.4-alt1.git20150122.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.4-alt1.git20150122.1
- NMU: Use buildreq for BR.

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20150122
- Initial build for Sisyphus

