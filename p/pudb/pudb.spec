Name: pudb
Version: 2024.1
Release: alt1

Summary: A full-screen, console-based Python debugger
License: MIT
Group: Development/Debuggers
Url: http://pypi.python.org/pypi/pudb
BuildArch: noarch

Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
Requires: python3(pygments) python3(%name) python3(jedi)
Provides: %{name}3 = %version.%release

# Automatically added by buildreq on Thu Jun 20 2024
# optimized out: bash5 libgpg-error python3 python3-base python3-dev python3-module-automat python3-module-cffi python3-module-pkg_resources python3-module-py3dephell python3-module-pytest python3-module-setuptools sh5
BuildRequires: python3-module-Cython python3-module-pyproject-installer python3-module-pytest-mock python3-module-trio python3-module-wheel python3-module-urwid

%description
PuDB is a full-screen, console-based visual debugger for Python.

Its goal is to provide all the niceties of modern GUI-based debuggers in
a more lightweight and keyboard-friendly package. PuDB allows you to
debug code right where you write and test it--in a terminal. If you've
worked with the excellent (but nowadays ancient) DOS-based Turbo Pascal
or C tools, PuDB's UI might look familiar.

%package -n python3-module-%name
Summary: Supplemental python3 module for %name, %summary
Group: Development/Python3
BuildArch: noarch
Requires: python3(urwid_readline)

%description -n python3-module-%name
Supplemental python module for %name, %summary

%package -n python3-module-%name-ipython
Summary: IPython plugin for %name
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%name-ipython
IPython plugin for %name

%prep
%setup

%build
%pyproject_build

%check
python3 -m pytest

%install
%pyproject_install

%files
%doc README.rst
%_bindir/*

%files -n python3-module-%name
%doc examples manual-tests
%python3_sitelibdir_noarch/*
%exclude %python3_sitelibdir_noarch/%name/ipython*

%files -n python3-module-%name-ipython
%python3_sitelibdir_noarch/%name/ipython*

%changelog
* Thu Jun 20 2024 Fr. Br. George <george@altlinux.org> 2024.1-alt1
- Autobuild version bump to 2024.1

* Tue Aug 16 2022 Fr. Br. George <george@altlinux.org> 2022.1.2-alt1
- Autobuild version bump to 2022.1.2
- Introduce tests

* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 2022.1.1-alt1
- Autobuild version bump to 2022.1.1

* Fri Feb 11 2022 Fr. Br. George <george@altlinux.ru> 2022.1-alt1
- Autobuild version bump to 2022.1
- Separate IPython plugin

* Mon Feb 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 2019.2-alt2
- Build for python2 disabled.

* Mon Nov 25 2019 Fr. Br. George <george@altlinux.ru> 2019.2-alt1
- Autobuild version bump to 2019.2

* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 2019.1-alt1
- Autobuild version bump to 2019.1

* Mon Sep 18 2017 Fr. Br. George <george@altlinux.ru> 2017.1.4-alt1
- Autobuild version bump to 2017.1.4

* Fri Aug 25 2017 Fr. Br. George <george@altlinux.ru> 2017.1.3-alt1
- Autobuild version bump to 2017.1.3

* Fri May 19 2017 Fr. Br. George <george@altlinux.ru> 2017.1.2-alt1
- Autobuild version bump to 2017.1.2

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 2017.1.1-alt1
- Autobuild version bump to 2017.1.1
- Introduce PuDB3

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 2016.2-alt1
- Autobuild version bump to 2016.2

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 2015.4.1-alt1
- Autobuild version bump to 2015.4.1

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 2015.3-alt1
- Autobuild version bump to 2015.3

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 2015.2-alt1
- Autobuild version bump to 2015.2

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 2015.1-alt1
- Autobuild version bump to 2015.1

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 2014.1-alt1
- Autobuild version bump to 2014.1

* Mon Feb 24 2014 Fr. Br. George <george@altlinux.ru> 2013.5.1-alt1
- Autobuild version bump to 2013.5.1

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 2013.3.6-alt1
- Autobuild version bump to 2013.3.6

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 2013.3.5-alt1
- Autobuild version bump to 2013.3.5

* Mon Jun 10 2013 Fr. Br. George <george@altlinux.ru> 2013.2-alt1
- Autobuild version bump to 2013.2

* Mon Apr 01 2013 Fr. Br. George <george@altlinux.ru> 2013.1-alt1
- Autobuild version bump to 2013.1

* Tue Aug 21 2012 Fr. Br. George <george@altlinux.ru> 2012.3-alt1
- Autobuild version bump to 2012.3

* Mon Jun 18 2012 Fr. Br. George <george@altlinux.ru> 2012.2.1-alt1
- Autobuild version bump to 2012.2.1

* Sun May 06 2012 Fr. Br. George <george@altlinux.ru> 2012.1-alt1
- Initial build for ALT

