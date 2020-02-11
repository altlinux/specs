%define oname recommonmark

Name: python-module-%oname
Version: 0.6.0
Release: alt1

Summary: A markdown parser for docutils
License: MIT
Group: Development/Python
Url: https://github.com/rtfd/recommonmark
BuildArch: noarch

Source0: %name-%version.tar
Patch0: fix-import.patch

BuildRequires(pre): rpm-build-python

%description
A docutils-compatibility bridge to CommonMark.
This allows you to write CommonMark inside of Docutils & Sphinx projects.

%prep
%setup
%patch0 -p1

%build
%python_build

%install
%python_install --optimize=2

%files
%doc README.md
%_bindir/*
%python_sitelibdir/*

%changelog
* Tue Feb 11 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- initial release

