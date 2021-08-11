%define _unpackaged_files_terminate_build 1

%define oname redmine

Name: python3-module-%oname
Version: 2.3.0
Release: alt1
Summary: Library for communicating with a Redmine project management application.
License: Apache-2.0
Group: Development/Python3
Url: https://python-redmine.com/

BuildArch: noarch

# https://github.com/maxtepkeev/python-redmine/
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
# tests
BuildRequires: python3(coverage)
BuildRequires: python3(nose)
BuildRequires: python3(mock)
BuildRequires: python3(requests)

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

%check
nosetests3 --with-coverage --cover-erase --cover-package=redminelib

%files
%doc README.* LICENSE docs/
%python3_sitelibdir/python_redmine-%version-py*.egg-info
%python3_sitelibdir/redminelib

%changelog
* Wed Aug 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt1
- Updated to upstream version 2.3.0.

* Mon Nov 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt2
- python2 disabled

* Mon Feb 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus
