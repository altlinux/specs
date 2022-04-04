%define oname argcomplete

%def_without check

Name: python3-module-argcomplete
Version: 2.0.0
Release: alt1

Summary: Bash tab completion for argparse

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/argcomplete/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

Obsoletes: python-module-argcomplete
Provides: python-module-argcomplete

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pexpect
BuildRequires: python3-module-tox
BuildRequires: /dev/pts
BuildRequires: tcsh
%endif

%description
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

It makes two assumptions:

* You're using bash or zsh as your shell
* You're using argparse to manage your command line arguments/options

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%if_with check
%check
export LC_ALL=C.UTF-8
export TOX_TESTENV_PASSENV='LC_ALL'
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v
%endif

%files
%doc *.rst
%_bindir/activate-global-python-argcomplete
%_bindir/python-argcomplete-check-easy-install-script
%_bindir/python-argcomplete-tcsh
%_bindir/register-python-argcomplete
%python3_sitelibdir/argcomplete/
%python3_sitelibdir/argcomplete-*.egg-info/

%changelog
* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0 (with rpmrb script)

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.12.3-alt1
- new version 1.12.3 (with rpmrb script)
- drop BR: rpm-build-sphinx

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.12.2-alt1
- new version 1.12.2 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.12.1-alt1
- new version 1.12.1 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.4-alt3
- build python3 package separately, drop tests packing
- disable tests (need rewrite)

* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 1.9.4-alt2
- Dropped BR on python argparse.
- Enabled testing.

* Wed Mar 28 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.9.4-alt1
- Updated version to 1.9.4

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.3-alt1.git20141109.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.3-alt1.git20141109.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1.git20141109.1
- NMU: Use buildreq for BR.

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20141109
- Version 0.8.3

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20141103
- Version 0.8.2
- Enabled testing

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20141005
- Initial build for Sisyphus
