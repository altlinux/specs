%def_with docs
Name: python3-module-slixmpp
Version: 1.2.4
Release: alt1
Group: Development/Python3
License: BSD
Url: https://dev.louiz.org/projects/slixmpp
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools gpg

Requires: python3-module-pyasn1-modules

BuildRequires: python3-module-jinja2-tests

%if_with docs
BuildRequires: python3-module-sphinx-sphinx-build-symlink python3-module-sphinx_rtd_theme
%endif

BuildRequires: gpg
Summary: XMPP library for Python 3.4+. It is a fork of SleekXMPP
Source: slixmpp-%version.tar.gz
Buildarch: noarch

%description
Slixmpp's goals is to only rewrite the core of the library (the low level
socket handling, the timers, the events dispatching) in order to remove all
threads.

%prep
%setup -n slixmpp-%version

%build
%python3_build

%if_with docs
python3 setup.py build_sphinx
%endif

%install
%python3_install

%check
python3 setup.py test

%files
%doc README.rst
%if_with docs
%doc build/sphinx/html
%endif
%python3_sitelibdir_noarch/*

%changelog
* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 1.2.4-alt1
- Autobuild version bump to 1.2.4

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 1.2.1-alt1
- Autobuild version bump to 1.2.1

* Wed Jul 20 2016 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Autobuild version bump to 1.1

* Wed Jul 20 2016 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build for ALT

