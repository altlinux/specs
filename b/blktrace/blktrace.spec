Name: blktrace
Version: 1.0.5
Release: alt1

Summary: Block IO tracer
License: GPL
Group: System/Kernel and hardware

Url: http://git.kernel.dk/?p=blktrace.git
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sat Jun 14 2008
BuildRequires: libaio-devel texlive-latex-recommended

%description
%name can show detailed info about what is happening on a block
device io queue. This is valuable for diagnosing and fixing
performance or application problems relating to block layer io.

Authors:
--------
    Jens Axboe <axboe/kernel.dk>

%prep
%setup

%build
make CFLAGS="%optflags" all docs

%install
make \
	dest=%buildroot \
	prefix=%buildroot%prefix \
	mandir=%buildroot%_mandir \
	install

%files
%doc README doc/*.pdf
%_bindir/*
%_man1dir/*
%_man8dir/*

%changelog
* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 1.0.5-alt1
- 1.0.5

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt1.1
- Rebuild with Python-2.7

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 1.0.3-alt1
- 1.0.3

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.1
- Rebuilt with python 2.6

* Fri Oct 30 2009 Michael Shigorin <mike@altlinux.org> 1.0.1-alt1
- 1.0.1
- reworked gear repo style

* Sat Jun 14 2008 Michael Shigorin <mike@altlinux.org> 0.99.3-alt1
- built for ALT Linux (based on btrace.spec in source repo)
  + commit 84a26fcd9adebd1537bf2c4eee69d1ca23ccbc5f
    (seems working while last release is a bit dated)
- spec fixup/cleanup
- buildreq

* Mon Oct 10 2005 - axboe@suse.de
- Initial version
