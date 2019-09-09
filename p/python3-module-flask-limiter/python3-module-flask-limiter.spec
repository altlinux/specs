%define modulename flask_limiter
Name: python3-module-flask-limiter
Version: 1.0.1
Release: alt1
Summary: Python 3 module for rate limiting extension for flask applications
License: MIT
Url: https://flask-limiter.readthedocs.org/
BuildArch: noarch
Group: Development/Python
Source0: %name-%version.tar
BuildRequires: python3-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-six
BuildRequires: python3-module-flask
BuildRequires: python3-module-limits
%py_provides flask_limiter

%description
Flask-Limiter provides rate limiting features to flask routes. It has support
for a configurable backend for storage with current implementations for
in-memory, redis and memcache.

%prep
%setup

%build
sed -i \
    -e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: %version\)\"/" \
    %modulename/_version.py
%python3_build

%install
%python3_install

%files
%doc *.rst LICENSE.txt
%python3_sitelibdir/%modulename
%python3_sitelibdir/*-%version-*.egg-info

%changelog
* Mon Sep 09 2019 Anton Farygin <rider@altlinux.ru> 1.0.1-alt1
- first build for ALT


