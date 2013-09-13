Name: bpython
Version: 0.12
Release: alt1

Summary: bpython is a fancy interface to the Python interpreter for Unix-like operating systems.
License: MIT
Group: Development/Python
Url: http://bpython-interpreter.org/
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Fri Sep 13 2013 (-bi)
# optimized out: python-base python-devel python-module-BeautifulSoup python-module-Pygments python-module-SQLAlchemy python-module-distribute python-module-docutils python-module-genshi python-module-html5lib python-module-jinja2 python-module-jinja2-tests python-module-lxml python-module-protobuf python-module-pytz python-module-simplejson python-module-whoosh python-modules python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-xml
BuildRequires: python-module-babel python-module-mock python-module-sphinx python-module-urwid


BuildRequires: python-module-setuptools python-module-setuptools-tests

%description
bpython is a fancy interface to the Python interpreter for
Unix-like operating systems.

It has the following features:
 - In-line syntax highlighting.
 - Readline-like autocomplete with suggestions displayed as you type.
 - Expected parameter list for any Python function.
 - "Rewind" function to pop the last line of code from memory and
   re-evaluate.
 - Send the code you've entered off to a pastebin.
 - Save the code you've entered to a file.
 - Auto-indentation

%package gtk
Group: Development/Python
Summary: GTK front-end for bpython.
Requires: %name = %version-%release

%description gtk
GTK front-end for bpython

%package urwid
Group: Development/Python
Summary: Urwid front-end for bpython.
Requires: %name = %version-%release

%description urwid
Urwid front-end for bpython

%prep
%setup -q
%patch -p1

%build
%python_build

%install
%python_install
mv %buildroot%python_sitelibdir/%name/urwid.py %buildroot%python_sitelibdir/%name/urwid_.py

%check
python setup.py test

%files
%_bindir/%{name}
%exclude %_bindir/%{name}-gtk
%exclude %_bindir/%{name}-urwid
%python_sitelibdir/%name/
%exclude %python_sitelibdir/%name/gtk_.py
%exclude %python_sitelibdir/%name/urwid_.py
%exclude %python_sitelibdir/%name/test
%python_sitelibdir/bpdb/
%python_sitelibdir/%name-%version-py%_python_version.egg-info
%_desktopdir/%name.desktop
%_man1dir/*
%_man5dir/*

%files urwid
%_bindir/%{name}-urwid
%python_sitelibdir/%name/urwid_.py

%files gtk
%_bindir/%{name}-gtk
%python_sitelibdir/%name/gtk_.py

%changelog
* Fri Sep 13 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.12-alt1
- New version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.7.1-alt1.1
- Rebuild with Python-2.7

* Tue Aug 24 2010 Alexey Morsov <swi@altlinux.ru> 0.9.7.1-alt1
- new version

* Sat Jan 23 2010 Alexey Morsov <swi@altlinux.ru> 0.9.6.2-alt2
- fix python requires
- fix requires

* Tue Jan 19 2010 Alexey Morsov <swi@altlinux.ru> 0.9.6.2-alt1
- initial build


