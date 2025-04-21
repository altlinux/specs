%define oname jsbeautifier

%def_with check

Name: python3-module-%oname
Version: 1.15.4
Release: alt1

Summary: JavaScript unobfuscator and beautifier
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jsbeautifier
VCS: https://github.com/beautifier/js-beautify
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-six
%endif

%py3_provides %oname


%description
Beautify, unpack or deobfuscate JavaScript. Handles popular online
obfuscators.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Beautify, unpack or deobfuscate JavaScript. Handles popular online
obfuscators.

This package contains tests for %oname.

%prep
%setup

%build
cd python
mv setup-js.py setup.py
%pyproject_build

%install
cd python
%pyproject_install

%check
cd python
%pyproject_run_pytest

%files
%_bindir/js-beautify
%python3_sitelibdir_noarch/%oname
%python3_sitelibdir_noarch/%oname-%version.dist-info
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests

%changelog
* Mon Apr 21 2025 Grigory Ustinov <grenka@altlinux.org> 1.15.4-alt1
- Build new version (Closes: #53911).
- Build with check.

* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.5.4-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.5.4-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.4-alt1.1
- NMU: Use buildreq for BR.

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.4-alt1
- Initial build for Sisyphus

