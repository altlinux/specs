%define _unpackaged_files_terminate_build 1

%define oname waitress
%def_with check

Name: python3-module-%oname
Version: 2.0.0
Release: alt1

Summary: Waitress WSGI server
License: ZPL-2.1
Group: Development/Python3

Url: https://pypi.org/project/waitress/
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
%endif

Conflicts: python-module-%oname

%description
Waitress is meant to be a production-quality pure-Python WSGI server with
very acceptable performance. It has no dependencies except ones which live
in the Python standard library. It runs on CPython on Unix and Windows under
Python 2.6+ and Python 3.2. It is also known to run on PyPy 1.6.0 on UNIX.
It supports HTTP/1.0 and HTTP/1.1.

For more information, see the "docs" directory of the Waitress package or
visit https://docs.pylonsproject.org/projects/waitress/en/latest/

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr

%files
%doc README.rst CHANGES.txt COPYRIGHT.txt LICENSE.txt
%_bindir/waitress-serve
%python3_sitelibdir/waitress/
%python3_sitelibdir/waitress-%version-py%_python3_version.egg-info/

%changelog
* Wed Apr 14 2021 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.2.1 -> 2.0.0.

* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2.1-alt3
- Build for python2 disabled.

* Mon Feb 25 2019 Stanislav Levin <slev@altlinux.org> 1.2.1-alt2
- Fixed test (test_functional.SleepyThreadTests, closes: #36156).

* Sun Feb 03 2019 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 0.8.10 -> 1.2.1.
- Enabled testing.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.8.10-alt2.dev0.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.10-alt2.dev0.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.8.10-alt2.dev0
- Rebuild with "def_disable check"
- Cleanup buildreq

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.10-alt1.dev0
- Version 0.8.10dev0

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.9-alt1
- Version 0.8.9

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt2.1
- Fixed build

* Wed Mar 06 2013 Aleksey Avdeev <solo@altlinux.ru> 0.8.2-alt2
- Add python{,3}-module-waitress-test subpackages

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1_4
- update to new release by fcimport

* Thu Jan 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1_3
- initial fc import
