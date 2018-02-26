Name: bpython
Version: 0.9.7.1
Release: alt1.1

Summary: bpython is a fancy interface to the Python interpreter for Unix-like operating systems.
License: MIT
Group: Development/Python
Url: http://bpython-interpreter.org/
BuildArch: noarch

Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar

Buildrequires: python-devel >= 2.5
Requires: python >= 2.5 python-module-Pygments

%description
bpython is a fancy interface to the Python interpreter for
Unix-like operating systems (I hear it works fine on OS X).
It is released under the MIT License. It has the following features:

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
Requires: bpython python-module-pygtk

%description gtk
GTK front-end for bpython

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --optimize=2 --record=INSTALLED_FILES


%files
%_bindir/%name
%python_sitelibdir/%name/
%python_sitelibdir/%name-%version-py%__python_version.egg-info
%python_sitelibdir/bpdb/
%_desktopdir/%name.desktop
%_man1dir/*
%_man5dir/*

%files gtk
%_bindir/%{name}-gtk

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.7.1-alt1.1
- Rebuild with Python-2.7

* Tue Aug 24 2010 Alexey Morsov <swi@altlinux.ru> 0.9.7.1-alt1
- new version

* Sat Jan 23 2010 Alexey Morsov <swi@altlinux.ru> 0.9.6.2-alt2
- fix python requires
- fix requires 

* Tue Jan 19 2010 Alexey Morsov <swi@altlinux.ru> 0.9.6.2-alt1
- initial build


