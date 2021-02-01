Name: python3-module-parso
Version: 0.8.1
Release: alt1
License: MIT
Summary: A Python3 Parser
Group: Development/Python3
Source: v%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# Automatically added by buildreq on Mon Feb 01 2021
# optimized out: ca-trust python-modules python2-base python3 python3-base python3-dev python3-module-Pygments python3-module-alabaster python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-docutils python3-module-idna python3-module-imagesize python3-module-jinja2 python3-module-markupsafe python3-module-openssl python3-module-packaging python3-module-pkg_resources python3-module-pytz python3-module-requests python3-module-sphinx python3-module-urllib3 sh4 xz
BuildRequires: ctags python3-module-setuptools python3-module-sphinxcontrib-applehelp python3-module-sphinxcontrib-devhelp python3-module-sphinxcontrib-htmlhelp python3-module-sphinxcontrib-jsmath python3-module-sphinxcontrib-qthelp python3-module-sphinxcontrib-serializinghtml

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
%python3_build
%make -C docs SPHINXBUILD=py3_sphinx-build html

%install
%python3_install

%files
%doc docs/_build/html/*
%python3_sitelibdir_noarch/*

%changelog
* Mon Feb 01 2021 Fr. Br. George <george@altlinux.ru> 0.8.1-alt1
- Autobuild version bump to 0.8.1

* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 0.5.1-alt1
- Autobuild version bump to 0.5.1

* Fri Aug 03 2018 Fr. Br. George <george@altlinux.ru> 0.3.1-alt1
- Autobuild version bump to 0.3.1

