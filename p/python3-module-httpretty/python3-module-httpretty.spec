%define  modulename httpretty

Name:    python3-module-%modulename
Version: 1.0.3
Release: alt1

Summary: HTTP client mocking tool for Python - inspired by Fakeweb for Ruby
License: MIT
Group:   Development/Python3
URL:     https://github.com/gabrielfalcao/HTTPretty

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Thu Dec 03 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.3-alt1
- Splite python3 module from python-module-httpretty package
