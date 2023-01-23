%define _unpackaged_files_terminate_build 1
%define pkgname requests

%def_with check

Name: python3-module-%pkgname
Version: 2.28.2
Release: alt1

Summary: HTTP library, written in Python, for human beings
License: Apache-2.0
Group: Development/Python3

Url: https://pypi.org/project/requests/
VCS: https://github.com/psf/requests
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# direct dependencies
BuildRequires: python3(charset_normalizer)
BuildRequires: python3(idna)
BuildRequires: python3(urllib3)

# extra
BuildRequires: python3(PySocks)
BuildRequires: python3(chardet)

BuildRequires: python3(trustme)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-mock)
BuildRequires: python3(pytest-httpbin)
%endif

%py3_requires charset_normalizer

%description
Requests allows you to send HTTP/1.1 requests extremely easily. There's no need
to manually add query strings to your URLs, or to form-encode your POST data.
Keep-alive and HTTP connection pooling are 100%% automatic, thanks to urllib3.

%prep
%setup
%autopatch -p1

# Unbundle the certificate bundle from mozilla.
rm -rf requests/cacert.pem

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests

%files
%doc AUTHORS.rst HISTORY.md README.md
%python3_sitelibdir/%pkgname/
%python3_sitelibdir/%{pyproject_distinfo %pkgname}/

%changelog
* Mon Jan 23 2023 Stanislav Levin <slev@altlinux.org> 2.28.2-alt1
- 2.28.1 -> 2.28.2.

* Mon Jul 25 2022 Stanislav Levin <slev@altlinux.org> 2.28.1-alt1
- 2.28.1

* Tue Feb 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.27.1-alt1
- 2.27.1

* Tue Oct 05 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.26.0-alt2
- add explicit charset_normalizer req

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.26.0-alt1
- 2.26.0

* Thu Mar 4 2021 Vladimir Didenko <cow@altlinux.org> 2.25.1-alt2
- fix build with idna >= 3.0

* Fri Feb 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.25.1-alt1
- 2.25.1

* Sat Dec 12 2020 Alexey Shabalin <shaba@altlinux.org> 2.25.0-alt2
- fix for chardet >= 4.0.0

* Mon Nov 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.25.0-alt1
- 2.25.0

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.24.0-alt1
- 2.24.0

* Thu Mar 19 2020 Alexey Shabalin <shaba@altlinux.org> 2.23.0-alt1
- 2.23.0
- build as python3 module

* Sat Oct 05 2019 Anton Farygin <rider@altlinux.ru> 2.22.0-alt1
- 2.22.0

* Mon Dec 24 2018 Alexey Shabalin <shaba@altlinux.org> 2.21.0-alt1
- 2.21.0

* Fri Jul 06 2018 Dmitry V. Levin <ldv@altlinux.org> 2.19.1-alt1
- Emergency NMU: 2.18.4 -> 2.19.1.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.18.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Sep 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.4-alt1
- New version

* Wed Sep 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.12.4-alt5
- Do not remove bundled chardet and urllib3 libraries

* Mon Feb 27 2017 Michael Shigorin <mike@altlinux.org> 2.12.4-alt4
- BOOTSTRAP: introduce check knob (*off* by default),
  put (unused) BR: python-module-httpbin under it

* Mon Jan 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.12.4-alt3
- removed bundled idna

* Mon Jan 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.12.4-alt2
- updated urllib3 patches

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.12.4-alt1
- automated PyPI update

* Fri May 6 2016 Vladimir Didenko <cow@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 2.9.1-alt1
- 2.9.1

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.7.0-alt1.git20150719.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.7.0-alt1.git20150719.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.7.0-alt1.git20150719.1
- NMU: Use buildreq for BR.

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.git20150719
- Version 2.7.0

* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1.git20150316
- Version 2.6.0

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.git20150204
- New snapshot

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.git20150109
- New snapshot

* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.git20141223
- Version 2.5.1

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.git20141216
- Version 2.5.0

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt2.git20141107
- New snapshot

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt2.git20141101
- I took it

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1.git20141101
- Version 2.4.3 (ALT #30439)

* Tue Jul 22 2014 Lenar Shakirov <snejok@altlinux.ru> 2.3.0-alt1
- New version (based on Fedora - 2.3.0-2.fc21.src)
- Unbundle urllib3 and chardet packages (use system modules)

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.12.1-alt1.1
- Rebuild with Python-3.3

* Fri May 18 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1-alt1
- initial
