%define _unpackaged_files_terminate_build 1
%define mname k5test

Name: python-module-%mname
Version: 0.9.2
Release: alt1%ubt
Summary: Library for setting up self-contained Kerberos 5 environments

Group: Development/Python
License: ISC
# Source git: https://github.com/pythongssapi/k5test.git
Url: https://pypi.python.org/pypi/k5test

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-six
BuildRequires: python-module-setuptools
BuildRequires: python3-module-six
BuildRequires: python3-module-setuptools

BuildArch: noarch

%description
Library for setting up self-contained Kerberos 5 environments, and running
Python unit tests inside those environments. It is based on the file of the
same name found alongside the MIT Kerberos 5 unit tests.

%package -n python3-module-%mname
Summary: Library for setting up self-contained Kerberos 5 environments
Group: Development/Python3

%description -n python3-module-%mname
Library for setting up self-contained Kerberos 5 environments, and running
Python unit tests inside those environments. It is based on the file of the
same name found alongside the MIT Kerberos 5 unit tests.

%prep
%setup
rm -rfv ../python3
cp -a . ../python3

%build
%python_build_debug
pushd ../python3
%python3_build_debug
popd


%install
%python_install
pushd ../python3
%python3_install
popd

%files
%python_sitelibdir/%mname
%python_sitelibdir/%mname-%version-*.egg-info

%files -n python3-module-%mname
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version-*.egg-info

%changelog
* Fri Mar 30 2018 Stanislav Levin <slev@altlinux.org> 0.9.2-alt1%ubt
- 0.9.1 -> 0.9.2

* Mon Nov 20 2017 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1%ubt
- Initial build

