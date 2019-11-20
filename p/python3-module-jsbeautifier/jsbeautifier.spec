%define oname jsbeautifier

%def_disable check

Name: python3-module-%oname
Version: 1.5.4
Release: alt2

Summary: JavaScript unobfuscator and beautifier
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/jsbeautifier/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

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

sed -i 's|#!.*/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ \( -name '*.py' -o -name 'js-beautify' \))

%build
%python3_build_debug

%install
%python3_install

%check
py.test-%_python3_version

%files
%doc PKG-INFO
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests


%changelog
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

