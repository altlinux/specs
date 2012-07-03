Name: pudb
Version: 2012.2.1
Release: alt1
%setup_python_module %name
Summary: A full-screen, console-based Python debugger
License: MIT
Group: Development/Debuggers
Url: http://pypi.python.org/pypi/pudb
Source: %name-%version.tar.gz
BuildArch: noarch
Requires: %packagename

# Automatically added by buildreq on Sun May 06 2012
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-email
BuildRequires: python-module-distribute

%description
PuDB is a full-screen, console-based visual debugger for Python.

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

%prep
%setup

cat > %name.sh <<@@@
#!/bin/sh
python -m pudb.run "\$@"
@@@

%build
%python_build

%install
%python_install
install -D -m755 %name.sh %buildroot/%_bindir/%name

%files
%doc README.rst
%_bindir/*

%files -n %packagename
%doc test
%python_sitelibdir_noarch/*

%changelog
* Mon Jun 18 2012 Fr. Br. George <george@altlinux.ru> 2012.2.1-alt1
- Autobuild version bump to 2012.2.1

* Sun May 06 2012 Fr. Br. George <george@altlinux.ru> 2012.1-alt1
- Initial build for ALT

