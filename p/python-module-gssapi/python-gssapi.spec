%define _unpackaged_files_terminate_build 1
%define mname gssapi

%def_with check

Name: python-module-%mname
Version: 1.6.1
Release: alt1

Summary: Python Bindings for GSSAPI (RFC 2743/2744 and extensions)
License: ISC
Group: Development/Python
# Source-git: https://github.com/pythongssapi/python-gssapi
Url: https://pypi.python.org/pypi/gssapi

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-Cython
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-Cython
BuildRequires: libkrb5-devel >= 1.15

%if_with check
BuildRequires: python-module-nose
BuildRequires: python-module-nose-parameterized
BuildRequires: python-module-six
BuildRequires: python-module-enum34
BuildRequires: python-module-decorator
BuildRequires: python-module-k5test
BuildRequires: python-module-flake8
BuildRequires: python-module-virtualenv
BuildRequires: python-module-future
BuildRequires: python3-module-nose
BuildRequires: python3-module-nose-parameterized
BuildRequires: python3-module-six
BuildRequires: python3-module-decorator
BuildRequires: python3-module-k5test
BuildRequires: python3-module-flake8
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-future
BuildRequires: krb5-kdc >= 1.15
%endif

Requires: libkrb5 >= 1.15
Requires: python-module-six
Requires: python-module-enum34
Requires: python-module-decorator

%description
A set of Python bindings to the GSSAPI C library providing both
a high-level pythonic interfaces and a low-level interfaces
which more closely matches RFC 2743.  Includes support for
RFC 2743, as well as multiple extensions.

%package -n python3-module-%mname
Summary: Python3 Bindings for GSSAPI (RFC 2743/2744 and extensions)
Group: Development/Python3
Requires: libkrb5 >= 1.15
Requires: python3-module-six
Requires: python3-module-decorator

%description -n python3-module-%mname
A set of Python bindings to the GSSAPI C library providing both
a high-level pythonic interfaces and a low-level interfaces
which more closely matches RFC 2743.  Includes support for
RFC 2743, as well as multiple extensions.
This is a Python3 module.

%prep
%setup
%patch -p1

cp -a . ../python3

%build
%add_optflags -fno-strict-aliasing
%python_build_debug
pushd ../python3
%python3_build_debug
popd

%install
%python_install
pushd ../python3
%python3_install
popd

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -vr

%files
%doc LICENSE.txt README.rst
%python_sitelibdir/%mname
%python_sitelibdir/%mname-%version-*.egg-info

%exclude %python_sitelibdir/%mname/tests/

%files -n python3-module-%mname
%doc LICENSE.txt README.rst
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version-*.egg-info

%exclude %python3_sitelibdir/%mname/tests/

%changelog
* Fri Oct 18 2019 Stanislav Levin <slev@altlinux.org> 1.6.1-alt1
- 1.5.1 -> 1.6.1.

* Sat Mar 23 2019 Stanislav Levin <slev@altlinux.org> 1.5.1-alt3
- Fixed errors found by a new flake8 3.7.7.

* Sun Oct 28 2018 Stanislav Levin <slev@altlinux.org> 1.5.1-alt2
- Fixed errors found by a new pycodestyle 2.4.

* Mon Jul 23 2018 Stanislav Levin <slev@altlinux.org> 1.5.1-alt1
- 1.5.0 -> 1.5.1

* Wed Apr 11 2018 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- 1.4.1 -> 1.5.0

* Fri Mar 30 2018 Stanislav Levin <slev@altlinux.org> 1.4.1-alt1
- 1.3.0 -> 1.4.1

* Thu Dec 07 2017 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.2 -> 1.3.0

* Thu Nov 16 2017 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1
- 1.2.0 -> 1.2.2
- Build Python3 package
- Enable tests

* Tue May 10 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Initial build.

