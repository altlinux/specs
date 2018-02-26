Name: xpybind
Version: 0.8.0
Release: alt2.1

Summary: bind X11 Window System key sequences to Python functions
License: GPL
Group: Graphical desktop/Other
URL: http://xpybind.sourceforge.net
Packager: Maxim Bodyansky <maximbo@altlinux.ru>

Source0: %name-%version.tar.gz

Patch0: %name-fix.patch

# Automatically added by buildreq on Sun Aug 07 2005
BuildRequires: python-base python-devel python-modules-encodings xorg-xproto-devel libX11-devel

%description
A user daemon for globally binding emacs-like keyboard key sequences in X
to callable objects in Python that can do anything from launching programs,
killing processes, edit xpybind's own configuration, and anything that can 
be programmed from Python.


%prep
%setup -q
%patch0 -p1
subst s!python2\.3!python%__python_version! src/Makefile src/xpybind.c


%build
%make_build


%install
%__install -D -m755 src/xpybind %buildroot%_bindir/xpybind
%__install -D -m644 src/xpybind.py %buildroot%python_sitelibdir/xpybind.py
%__install -D -m644 man/xpybind.1 %buildroot%_man1dir/xpybind.1
%__install -D -m644 man/xpybind.5 %buildroot%_man5dir/xpybind.5


%files
%doc README AUTHORS NEWS examples/dot.xpybind.complex
%_bindir/*
%_man1dir/*
%_man5dir/*
%python_sitelibdir/*


%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.0-alt2.1
- Rebuild with Python-2.7

* Wed Apr 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.0-alt2
- fix build

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.1.2
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.8.0-alt1.1.1
- Rebuilt with python-2.5.

* Sat Nov 05 2005 Maxim Bodyansky <maximbo@altlinux.ru> 0.8.0-alt1.1
- Fixed segfaults when running with Python 2.4

* Thu Aug 11 2005 Maxim Bodyansky <maximbo@altlinux.ru> 0.8.0-alt1
- Initial build for ALT Linux.
