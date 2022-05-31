%define _unpackaged_files_terminate_build 1

%define oname django-storages

%def_with check

Name: python3-module-%oname
Version: 1.12.3
Release: alt1

Summary: Support for many storage backends in Django
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/jschneier/django-storages.git
BuildArch: noarch

# VCS:https://github.com/jschneier/django-storages.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_django)
BuildRequires: python3-module-django
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-django-tests
%endif

%add_python3_req_skip azure.core.exceptions azure.storage.blob dropbox.exceptions
%add_python3_req_skip dropbox.files paramiko

%description
django-storages is a project to provide a variety of storage
backends in a single library.

This library is usually compatible with the currently supported
versions of Django. Check the Trove classifiers in setup.py to be sure.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install --install-lib=%python3_sitelibdir

%check
python3 -m pytest tests/test_utils.py tests/test_ftp.py --ds=tests.settings

%files
%doc *.rst LICENSE AUTHORS
%python3_sitelibdir/*


%changelog
* Mon May 30 2022 Dmitry Lyalyaev <fruktime@altlinux.org> 1.12.3-alt1
- Initial build for ALT Linux
