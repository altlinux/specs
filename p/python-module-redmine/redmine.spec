%define _unpackaged_files_terminate_build 1

%define oname redmine

Name: python-module-%oname
Version: 2.2.0
Release: alt1

Summary: Library for communicating with a Redmine project management application.
License: Apache-2.0
Group: Development/Python
Url: https://python-redmine.com/
# https://github.com/maxtepkeev/python-redmine/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-module-setuptools
BuildRequires: python-module-requests

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-devel


%description
Python-Redmine is a library for communicating with a Redmine project management
application. Redmine exposes some of it's data via REST API for which Python-Redmine
provides a simple but powerful Pythonic API inspired by a well-known Django ORM.

%package -n python3-module-%oname
Summary: Library for communicating with a Redmine project management application.
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%oname
Python-Redmine is a library for communicating with a Redmine project management
application. Redmine exposes some of it's data via REST API for which Python-Redmine
provides a simple but powerful Pythonic API inspired by a well-known Django ORM.

%prep
%setup

rm -rf ../python3
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

%files
%doc README.* LICENSE docs/
%python_sitelibdir/*

%files -n python3-module-%oname
%doc README.* LICENSE docs/
%python3_sitelibdir/*


%changelog
* Mon Feb 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus
