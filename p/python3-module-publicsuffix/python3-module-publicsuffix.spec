%define modulename publicsuffix
Name: python3-module-%modulename
Version: 1.1.0
Release: alt1
Summary: Python module to get a domain suffix using the Public Suffix List
License: BSD-Like
Url: https://pypi.org/project/publicsuffix/
BuildArch: noarch
Group: Development/Python
# http://www.tablix.org/~avian/git/publicsuffix.git
Source0: %name-%version.tar
BuildRequires: python3-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
This Python module allows you to get the public suffix of a domain name using
the Public Suffix List from http://publicsuffix.org.

A public suffix is one under which Internet users can directly register names.
Some examples of public suffixes are .com, .co.uk and pvt.k12.wy.us. Accurately
knowing the public suffix of a domain is useful when handling web browser
cookies, highlighting the most important part of a domain name in a user
interface or sorting URLs by web site.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc ChangeLog LICENSE README.rst
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-*.egg-info

%changelog
* Thu Sep 05 2019 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- first build for ALT

