%define module_name bundle

Name: python3-module-%module_name
Version: 1.1.2
Release: alt3

Summary: Manages installed Bundle packages
License: BSD License
Group: Development/Python3
URL: https://github.com/ask/bundle.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Manages installed Bundle packages

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py.*')

%build
%python_build

%install
%python3_install

%if "%_target_libdir_noarch" != "%_libdir"
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc AUTHORS Changelog LICENSE README.rst TODO
%python3_sitelibdir/bundle*


%changelog
* Mon Nov 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.2-alt3
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.2-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.2-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2
- Added module for Python 3

* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.2-alt1
- build for ALT
