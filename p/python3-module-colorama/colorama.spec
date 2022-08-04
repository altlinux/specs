%define oname colorama

%def_with check

Name: python3-module-%oname
Version: 0.4.5
Release: alt1

Summary: Simple cross-platform colored terminal text in Python

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/colorama

# https://github.com/tartley/colorama
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
%endif

%py3_provides %oname

%description
Makes ANSI escape character sequences for producing colored terminal
text and cursor positioning work under MS Windows.

ANSI escape character sequences have long been used to produce colored
terminal text and cursor positioning on Unix and Macs. Colorama makes
this work on Windows, too, by wrapping stdout, stripping ANSI sequences
it finds (which otherwise show up as gobbledygook in your output), and
converting them into the appropriate win32 calls to modify the state of
the terminal. On other platforms, Colorama does nothing.

Colorama also provides some shortcuts to help generate ANSI sequences
but works fine in conjunction with any other ANSI sequence generation
library, such as Termcolor.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test-3

%files
%doc *.rst demos
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Thu Aug 04 2022 Grigory Ustinov <grenka@altlinux.org> 0.4.5-alt1
- Automatically updated to 0.4.5.

* Thu Jul 22 2021 Grigory Ustinov <grenka@altlinux.org> 0.4.4-alt2
- Drop python2 support.

* Wed Nov 18 2020 Grigory Ustinov <grenka@altlinux.org> 0.4.4-alt1
- Automatically updated to 0.4.4.

* Thu Dec 19 2019 Grigory Ustinov <grenka@altlinux.org> 0.4.3-alt1
- Build new version 0.4.3.

* Tue Jul 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.4.1-alt1
- Build new version (Closes: #37069).

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.9-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.9-alt1
- Updated to upstream version 0.3.9.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.7-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.3-alt1.git20150709.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1.git20150709
- Version 0.3.3

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20141101
- Initial build for Sisyphus
