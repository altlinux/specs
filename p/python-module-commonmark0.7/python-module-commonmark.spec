%define  modulename CommonMark

Name:    python-module-commonmark0.7
Version: 0.7.2
Release: alt1

Summary: Python parser for the CommonMark Markdown spec
License: BSD
Group:   Development/Python
URL:     https://github.com/rtfd/CommonMark-py

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python

BuildArch: noarch
Source:  %modulename-%version.tar

%description
Python parser for the CommonMark Markdown spec.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%doc README.rst LICENSE spec.txt docs
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Tue Feb 11 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.7.2-alt1
- initial release

