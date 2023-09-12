%def_with docs
Name: python3-module-slixmpp
Version: 1.7.1
Release: alt2
Group: Development/Python3
License: BSD
Url: https://dev.louiz.org/projects/slixmpp
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools gpg
Patch: 0001-Python3.10-patch.patch
Patch1: 0001-This-hangs.patch

Requires: python3-module-pyasn1-modules
Requires: python3-module-aiodns

%if_with docs
# Automatically added by buildreq on Tue Feb 08 2022
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error mpdecimal pkg-config python3 python3-base python3-dev python3-module-Pygments python3-module-alabaster python3-module-babel python3-module-charset-normalizer python3-module-docutils python3-module-idna python3-module-imagesize python3-module-jinja2 python3-module-markupsafe python3-module-packaging python3-module-pkg_resources python3-module-pyparsing python3-module-pytz python3-module-requests python3-module-sphinx python3-module-urllib3 sh4
BuildRequires: libidn-devel python3-module-Cython python3-module-setuptools python3-module-sphinx-autodoc-typehints python3-module-sphinxcontrib-applehelp python3-module-sphinxcontrib-devhelp python3-module-sphinxcontrib-htmlhelp python3-module-sphinxcontrib-jsmath python3-module-sphinxcontrib-qthelp python3-module-sphinxcontrib-serializinghtml

BuildRequires: python3-module-sphinx-sphinx-build-symlink python3-module-sphinx_rtd_theme
%endif

BuildRequires: gpg
Summary: XMPP library for Python 3.4+. It is a fork of SleekXMPP
Source: slixmpp-slix-%version.tar.gz

%description
Slixmpp's goals is to only rewrite the core of the library (the low level
socket handling, the timers, the events dispatching) in order to remove all
threads.

%prep
%setup -n slixmpp-slix-%version
%patch -p1
%patch1 -p2

%build
%python3_build

%if_with docs
sphinx-build-3 docs html
%endif

%install
%python3_install

%check
python3 setup.py test

%files
%doc README.rst
%if_with docs
%doc html
%endif
%python3_sitelibdir/*

%changelog
* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 1.7.1-alt2
- Fixed FTBFS.

* Tue Feb 08 2022 Fr. Br. George <george@altlinux.ru> 1.7.1-alt1
- Autobuild version bump to 1.7.1

* Thu Jun 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.2-alt2
- drop excessive python3-module-jinja2-tests BR

* Wed Mar 06 2019 Fr. Br. George <george@altlinux.ru> 1.4.2-alt1
- Autobuild version bump to 1.4.2

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 1.3.0-alt1
- Autobuild version bump to 1.3.0

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 1.2.4-alt1
- Autobuild version bump to 1.2.4

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 1.2.1-alt1
- Autobuild version bump to 1.2.1

* Wed Jul 20 2016 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Autobuild version bump to 1.1

* Wed Jul 20 2016 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build for ALT

