%define _unpackaged_files_terminate_build 1
%define oname Fabric

%def_without check

Name: python3-module-%oname
Version: 2.5.0
Release: alt2

Summary: Simple, Pythonic remote execution and deployment.

License: BSD-2-Clause
Group: Development/Python3
Url: https://github.com/fabric/fabric

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro
%if_with check
BuildRequires: python3-module-decorator
BuildRequires: python3-module-invoke
BuildRequires: python3-module-paramiko
BuildRequires: python3-module-six
BuildRequires: python3-module-yaml
%endif

Conflicts: python-module-%oname
%py3_provides %oname


%description
Fabric is a high level Python (2.7, 3.4+) library designed to execute shell
commands remotely over SSH, yielding useful Python objects in return. It builds
on top of Invoke (subprocess command execution and command-line features) and
Paramiko (SSH protocol implementation), extending their APIs to complement one
another and provide additional functionality.


%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%check
%__python3 setup.py test

%files
%doc LICENSE README.rst
%_bindir/fab
%python3_sitelibdir/fabric/
%python3_sitelibdir/*.egg-info

%changelog
* Sun Jul 18 2021 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt2
- cleaup spec, don't pack tests (useless)

* Tue Feb 18 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.5.0-alt1
- Version updated to 2.5.0
- build for python2 disabled.

* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.14.0-alt1
- Updated to upstream version 1.14.0.
- Disabled python-3 build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt1
- automated PyPI update

* Wed Apr 27 2016 Denis Medvedev <nbr@altlinux.org> 1.11.1-alt1
- 1.11.1. Removed changelog.rst from www since new sphinx chokes on that
file.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.10.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1
- Version 1.10.1

* Sun Jul 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt2
- Added module for Python 3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus

