%define modulename limits
Name: python3-module-%modulename
Version: 1.3
Release: alt1
Summary: Python module to implement rate limiting 
License: MIT
Url: https://limits.readthedocs.io/en/stable/
BuildArch: noarch
Group: Development/Python
Source0: %name-%version.tar
BuildRequires: python3-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-six
%py_provides limits

%description
Python module to implement rate limiting using various strategies and
storage backends such as redis & memcached.

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
* Mon Sep 09 2019 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- first build for ALT


