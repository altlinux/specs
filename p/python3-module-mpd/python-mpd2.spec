Name: python3-module-mpd
Version: 0.5.5
Release: alt2
Summary: A client interface for the Music Player Daemon
Group: Development/Python3
License: LGPLv3+
Url: https://travis-ci.org/Mic92/python-mpd2
BuildArch: noarch
Source: v%version.tar.gz
Conflicts: python-module-python-mpd

BuildRequires(pre): rpm-build-python3

BuildRequires: ctags python3-module-jinja2-tests python3-module-sphinx

%description
python-mpd2 is a fork of python-mpd. While 0.4.x was backwards compatible with
python-mpd, starting with 0.5 provides enhanced features which are NOT backward
compatibles with the original python-mpd package. (see PORTING.txt for more
information)

The following features were added:

Python 3 support (but you need at least Python 2.6)
support for the upcoming client-to-client protocol
support for new commands from MPD v0.17 (seekcur, prio, prioid, config, searchadd, searchaddpl)
remove deprecated commands (volume)
explicitly declared MPD commands (which is handy when using for example IPython)
a test suite
API documentation to add new commands (see Future Compatible)
support for Unicode strings in all commands (optionally in python2, default in python3 - see Unicode Handling)
configureable timeouts
support for logging
improved support for sticker
improved support for ranges

%prep
%setup -n python-mpd2-%version

%build
%python3_build
make -C doc SPHINXBUILD=py3_sphinx-build html

%install
%python3_install

%files
%doc doc/_build/html README.rst
%python3_sitelibdir_noarch/*

%changelog
* Thu Jun 03 2021 Grigory Ustinov <grenka@altlinux.org> 0.5.5-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 0.5.5-alt1
- Autobuild version bump to 0.5.5

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.4-alt1.1
- NMU: Use buildreq for BR.

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 0.5.4-alt1
- Autobuild version bump to 0.5.4

* Thu Mar 27 2014 Fr. Br. George <george@altlinux.ru> 0.5.3-alt1
- Autobuild version bump to 0.5.3

* Thu Mar 27 2014 Fr. Br. George <george@altlinux.ru> 0.5.2-alt1
- Initial build from scratch

