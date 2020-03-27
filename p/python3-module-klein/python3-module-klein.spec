%define  modulename klein

Name:    python3-module-%modulename
Version: 19.6.0
Release: alt2

Summary: werkzeug + twisted.web
License: MIT
Group:   Development/Python3
URL:     https://github.com/twisted/klein

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3-module-incremental

BuildArch: noarch

Source:  %modulename-%version.tar

Patch1: 0001-typing-is-not-needed-since-Python-3.5-as-it-s-built-in.patch

%description
Klein is a micro-framework for developing production-ready web services with
Python. It is "micro" in that it has an incredibly small API similar to Bottle
and Flask. It is not "micro" in that it depends on things outside the standard
library. This is primarily because it is built on widely used and well tested
components like Werkzeug and Twisted.

%prep
%setup -n %modulename-%version
%patch1 -p1

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc README.rst

%changelog
* Thu Mar 26 2020 Mikhail Gordeev <obirvalger@altlinux.org> 19.6.0-alt2
- Fix requires to typing in setup.py

* Tue Mar 24 2020 Mikhail Gordeev <obirvalger@altlinux.org> 19.6.0-alt1
- Initial build for Sisyphus
