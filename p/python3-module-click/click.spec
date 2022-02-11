%define _unpackaged_files_terminate_build 1
%define pypi_name click

%def_with check

Name: python3-module-%pypi_name
Version: 8.0.3
Release: alt1

Summary: Composable command line interface toolkit

License: BSD
Group: Development/Python
Url: https://pypi.org/project/click/

# Source-git: https://github.com/pallets/click.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

%description
Click is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary.  It's the "Command
Line Interface Creation Kit".  It's highly configurable but comes with
sensible defaults out of the box.

It aims to make the process of writing command line tools quick and fun
while also preventing any frustration caused by the inability to
implement an intended CLI API.

%prep
%setup
%autopatch -p1
rm -vf src/click/_winconsole.py

%build
%python3_build

%install
%python3_install
rm -rfv %buildroot%python3_sitelibdir/click/tests/

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false

%files
%doc README.* LICENSE.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version-py%_python3_version.egg-info/

%changelog
* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 8.0.3-alt1
- 7.1.2 -> 8.0.3.

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 7.1.2-alt2
- NMU: don't pack tests, but pack click.testing

* Fri Jul 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.1.2-alt1
- 7.1.2 released

* Mon Jul 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 7.0-alt1
- Version updated to 7.0

* Tue Apr 23 2019 Michael Shigorin <mike@altlinux.org> 6.7-alt1.1.1
- introduce doc knob (on by default)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 6.7-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 6.7-alt1
- new version 6.7 (with rpmrb script)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.0-alt1.dev.git20150808.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 5.0-alt1.dev.git20150808.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt1.dev.git20150808
- New snapshot

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt1.dev.git20150725
- Version 5.0-dev

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.dev.git20141014
- Initial build for Sisyphus

