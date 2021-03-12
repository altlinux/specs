%define modname smartypants

Name: python3-module-%modname
Version: 2.0.1
Release: alt1

Summary: Python with the SmartyPants
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/%modname

Vcs: https://github.com/leohemsted/smartypants.py.git
Source: %modname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
Python module to translate plain ASCII punctuation characters into
"smart" typographic punctuation HTML entities.

%modname is a Python fork of SmartyPants (http://daringfireball.net/projects/smartypants/)

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%files
%_bindir/smartypants
%python3_sitelibdir_noarch/*
%doc README*

%changelog
* Fri Mar 12 2021 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- first build for Sisyphus (v2.0.1-4-gc46d26c)




