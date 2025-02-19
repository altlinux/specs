%define oname TurboGears2

Name: python3-module-%oname
Version: 2.5.0
Release: alt1

Summary: Next generation TurboGears

License: MIT
Group: Development/Python
Url: https://pypi.org/project/TurboGears2
Vcs: https://github.com/TurboGears/tg2

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Source: %name-%version.tar

%description
TurboGears is a hybrid web framework able to act both as a Full Stack framework
or as a Microframework. TurboGears helps you get going fast and gets out of your
way when you want it!

TurboGears can be used both as a full stack framework or as a microframework in
single file mode.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.*
%python3_sitelibdir/tg
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Wed Feb 19 2025 Anton Vyatkin <toni@altlinux.org> 2.5.0-alt1
- New version 2.5.0.

* Tue Apr 11 2023 Anton Vyatkin <toni@altlinux.org> 2.4.3-alt2
- Fix requirement

* Mon Nov 29 2021 Anton Farygin <rider@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Wed Dec 04 2019 Anton Farygin <rider@altlinux.ru> 2.4.2-alt1
- 2.4.2
- disabled python2 version

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.3.3-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 2.3.3-alt1.1
- NMU: Use buildreq for BR.

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3-alt1
- Version 2.3.3
- Added module for Python 3

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1
- Version 2.2.0

* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1
- Version 2.0.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.3-alt1.1.1
- Rebuild with Python-2.7

* Sat Aug 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1.1
- Fixed build

* Tue Oct 05 2010 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version (2.0.3) import in git

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1.1
- Rebuilt with python 2.6

* Sun Mar 29 2009 Denis Klimov <zver@altlinux.org> 1.0.8-alt1
- Initial build for ALT Linux

