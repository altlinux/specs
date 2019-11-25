%define _unpackaged_files_terminate_build 1
%define oname redmine

Name: python3-module-%oname
Version: 2.2.0
Release: alt2

Summary: Library for communicating with a Redmine project management application.
License: Apache-2.0
Group: Development/Python3
Url: https://python-redmine.com/
# https://github.com/maxtepkeev/python-redmine/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Python-Redmine is a library for communicating with a Redmine project management
application. Redmine exposes some of it's data via REST API for which Python-Redmine
provides a simple but powerful Pythonic API inspired by a well-known Django ORM.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.* LICENSE docs/
%python3_sitelibdir/*


%changelog
* Mon Nov 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt2
- python2 disabled

* Mon Feb 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus
