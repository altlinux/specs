Name: python-module-mpd
Version: 0.5.5
Release: alt1.1
Summary: A client interface for the Music Player Daemon
Group: Development/Python
License: LGPLv3+
Url: https://travis-ci.org/Mic92/python-mpd2
BuildArch: noarch
Source: v%version.tar.gz
Conflicts: python-module-python-mpd

BuildRequires(pre): rpm-build-python3

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-Pygments python3-module-alabaster python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx_rtd_theme xz
BuildRequires: ctags python-module-alabaster python-module-docutils python-module-html5lib python-module-setuptools python3-module-html5lib python3-module-jinja2-tests python3-module-setuptools python3-module-sphinx rpm-build-python3 time

#BuildRequires: python-module-distribute  python-devel  python-module-setuptools
#BuildRequires: python3-module-distribute python3-devel python3-module-setuptools

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

%package -n python3-module-mpd
Group: Development/Python
Summary: %summary
%description -n python3-module-mpd
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
cp -a . ../python3
%python_build
make -C doc html
cd ../python3
%python3_build
make -C doc SPHINXBUILD=py3_sphinx-build html

%install
%python_install
cd ../python3 && %python3_install

%files
%doc doc/_build/html README.rst
%python_sitelibdir_noarch/*

%files -n python3-module-mpd
%doc ../python3/doc/_build/html README.rst
%python3_sitelibdir_noarch/*

%changelog
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

