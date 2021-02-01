Name: python-module-parso
Version: 0.5.1
Release: alt2
License: MIT
Summary: A Python3 Parser
Group: Development/Python3
Source: v%version.tar.gz
BuildArch: noarch

# Automatically added by buildreq on Sat Aug 04 2018
BuildRequires: ctags python-module-alabaster python-module-docopt python-module-html5lib python-module-setuptools python-module-sphinxcontrib-websupport time
BuildRequires(pre): rpm-build-python

%description
Parso is a Python parser that supports error recovery and round-trip
parsing for different Python versions (in multiple Python versions).
Parso is also able to list multiple syntax errors in your python file.

Parso has been battle-tested by jedi. It was pulled out of jedi to be
useful for other projects as well.

Parso consists of a small API to parse Python and analyse the syntax tree.

%prep
%setup -n parso-%version

%build
%python_build
make -C docs html

%install
%python_install

%files
%doc docs/_build/html/*
%python_sitelibdir_noarch/*

%changelog
* Mon Feb 01 2021 Fr. Br. George <george@altlinux.ru> 0.5.1-alt2
- Build python2-only version

* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 0.5.1-alt1
- Autobuild version bump to 0.5.1

* Fri Aug 03 2018 Fr. Br. George <george@altlinux.ru> 0.3.1-alt1
- Autobuild version bump to 0.3.1

