%define _unpackaged_files_terminate_build 1
%define mname requests-gssapi

%def_with check

Name: python-module-%mname
Version: 1.0.0
Release: alt1%ubt

Summary: A GSSAPI/SPNEGO authentication handler for python-requests
License: ISC
Group: Development/Python
# Source-git: https://github.com/pythongssapi/requests-gssapi.git
Url: https://pypi.org/project/requests-gssapi

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-requests
BuildRequires: python-module-gssapi
BuildRequires: python-module-mock
BuildRequires: python3-module-requests
BuildRequires: python3-module-gssapi
BuildRequires: python3-module-mock
%endif

BuildArch: noarch

%define _overview						     \
Requests is an HTTP library, written in Python, for human beings.    \
This library adds optional GSSAPI authentication support and	     \
supports mutual authentication.					     \
								     \
It provides a fully backward-compatible shim for the old 	     \
python-requests-kerberos library. A more powerful interface is 	     \
provided by the HTTPSPNEGOAuth component, but this is of course not  \
guaranteed to be compatible.					     

%description %_overview

%package -n python3-module-%mname
Summary: A GSSAPI/SPNEGO authentication handler for python-requests
Group: Development/Python3

%description -n python3-module-%mname
%_overview

%prep
%setup

cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
python setup.py test

pushd ../python3
python3 setup.py test
popd

%files
%doc AUTHORS LICENSE *.rst
%python_sitelibdir/*

%files -n python3-module-%mname
%doc AUTHORS LICENSE *.rst
%python3_sitelibdir/*

%changelog
* Fri May 04 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1%ubt
- Initial build
