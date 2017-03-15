Name: pudb
Version: 2017.1.1
Release: alt1
%setup_python_module %name
Summary: A full-screen, console-based Python debugger
License: MIT
Group: Development/Debuggers
Url: http://pypi.python.org/pypi/pudb
Source: %name-%version.tar.gz
BuildArch: noarch
Requires: %packagename

# Automatically added by buildreq on Wed Mar 15 2017
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python3 python3-base
BuildRequires: python-module-setuptools python3-dev python3-module-setuptools

%description
PuDB is a full-screen, console-based visual debugger for Python.

Its goal is to provide all the niceties of modern GUI-based debuggers in
a more lightweight and keyboard-friendly package. PuDB allows you to
debug code right where you write and test it--in a terminal. If you've
worked with the excellent (but nowadays ancient) DOS-based Turbo Pascal
or C tools, PuDB's UI might look familiar.

%package -n pudb3
Group: Development/Debuggers
BuildArch: noarch
Summary: A full-screen, console-based Python3 debugger
Requires: python3-module-%name

%description -n pudb3
PuDB is a full-screen, console-based visual debugger for Python3.

Its goal is to provide all the niceties of modern GUI-based debuggers in
a more lightweight and keyboard-friendly package. PuDB allows you to
debug code right where you write and test it--in a terminal. If you've
worked with the excellent (but nowadays ancient) DOS-based Turbo Pascal
or C tools, PuDB's UI might look familiar.

%package -n %packagename
Group: Development/Python
BuildArch: noarch
Summary: Supplemental python module for %name, %summary
%description -n %packagename
Supplemental python module for %name, %summary

%package -n python3-module-%name
Group: Development/Python
BuildArch: noarch
Summary: Supplemental python3 module for %name, %summary
%description -n python3-module-%name
Supplemental python module for %name, %summary

%prep
%setup

cat > %name.sh <<@@@
#!/bin/sh
python -m pudb.run "\$@"
@@@

sed 's/python/python3/g' %name.sh > %{name}3.sh

%build
%python_build -b build2
%python3_build -b build3

%install
rm -f build && ln -s build2 build
%python_install
rm -f build && ln -s build3 build
%python3_install
install -D -m755 %name.sh %buildroot/%_bindir/%name
install -D -m755 %{name}3.sh %buildroot/%_bindir/%{name}3

%files
%doc README.rst
%_bindir/%name

%files -n pudb3
%doc README.rst
%_bindir/%{name}3

%files -n %packagename
%doc test
%python_sitelibdir_noarch/*

%files -n python3-module-%name
%doc test
%python3_sitelibdir_noarch/*

%changelog
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

