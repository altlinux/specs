Name: pydb
Version: 1.25

Release: alt1.1.1

Summary: pydb is an expanded version of the Python debugger

Url: http://bashdb.sourceforge.net/pydb
License: GPL
Group: Development/Python

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source: http://dl.sf.net/bashdb/%name-%version.tar.bz2
Source: http://prdownloads.sourceforge.net/sourceforge/bashdb/%name-%version.tar.bz2
#Patch: %name.patch

# Automatically added by buildreq on Sun Jul 30 2006
BuildRequires: emacs-common fontconfig python-devel python-modules python-modules-encodings

%description
Extended Python Debugger is a more complete debugger for Python
than the stock pdb.py debugger. It supports a "restart" command,
non-interactive POSIX-like line tracing, command options, disassembly
of instructions, and stack traces that give better information for exec
statements. Stepping/nexting skips over method/function "defs". It tries
to follow gdb's command set unless there is good reason not to.

%prep
%setup -q
#patch

%build
%configure
%make

%install
%makeinstall_std
ln -sf ../../%python_sitelibdir/%name/%name.py %buildroot/%_bindir/%name

%files
%doc README THANKS NEWS TODO
%_bindir/%name
%python_sitelibdir/%name/
%_datadir/emacs/site-lisp/
%_man1dir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.25-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.25-alt1.1
- Rebuilt with python 2.6

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 1.25-alt1
- new version 1.25 (with rpmrb script)

* Sat Nov 18 2006 Vitaly Lipatov <lav@altlinux.ru> 1.19-alt0.1
- new version 1.19 (with rpmrb script)

* Sun Jul 30 2006 Vitaly Lipatov <lav@altlinux.ru> 1.17-alt0.1
- initial build for ALT Linux Sisyphus
