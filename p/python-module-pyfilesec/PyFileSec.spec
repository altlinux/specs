Name: python-module-pyfilesec
Version: 0.2.14
Release: alt1
Summary: Working with files that may contain sensitive information
License: GPLv3
Group: Development/Python
Url: https://github.com/jeremygray/pyfilesec
Source: PyFileSec-%version.tar.gz
BuildArch: noarch
%setup_python_module pyfilesec

# Automatically added by buildreq on Thu Jan 16 2014
# optimized out: python-base python-modules python-modules-compiler python-modules-email
BuildRequires: python-devel

%description
pyFileSec provides robust yet easy-to-use tools for working with files
that may contain sensitive information. The aim is to achieve an
"industry standard" level of strong privacy, capable of protecting
confidential information from inspection or accidental disclosure.
Integrity assurance may be useful in archival and provenance
applications.

%prep
%setup -n PyFileSec-%version

%build
%python_build

%install
%python_install

%files
%doc *.rst
%python_sitelibdir_noarch/*

%changelog
* Tue Jan 29 2019 Fr. Br. George <george@altlinux.ru> 0.2.14-alt1
- Autobuild version bump to 0.2.14

* Thu Jan 16 2014 Fr. Br. George <george@altlinux.ru> 0.2.13-alt1
- Initial build for ALT

