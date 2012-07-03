%def_disable check

Name: archivemail
Version: 0.8.0
Release: alt1.1

Summary: Archive and compress old email
License: GPLv2+
Group: File tools

BuildArch: noarch

Packager: Andrey Rahmatullin <wrar@altlinux.org>

Url: http://archivemail.sourceforge.net/

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: python-modules

%description 
archivemail is a tool written in python(1) for archiving and compressing
old email in mailboxes. By default it will read the mailbox MAILBOX,
moving messages that are older that the specified number of days (180 by
default) to a mbox-format mailbox in the same directory that is
compressed with gzip(1).

archivemail supports reading IMAP, Maildir, MH and mbox-format mailboxes, but
it will always write archive files to mbox-format mailboxes that are compressed
with gzip(1).

%prep
%setup
%patch -p1

%check
./test_archivemail

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
install -p -m755 %name %buildroot%_bindir/%name
install -p -m644 %name.1 %buildroot%_man1dir

%files
%_bindir/*
%_man1dir/*
%doc CHANGELOG FAQ NEWS README TODO test_archivemail examples/

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.0-alt1.1
- Rebuild with Python-2.7

* Wed Aug 11 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.8.0-alt1
- 0.8.0
- re-enable tests (and move them to %%check)

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt2.1
- Rebuilt with python 2.6

* Sat Mar 22 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.7.2-alt2
- disable tests

* Sun Nov 11 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.7.2-alt1
- 0.7.2
- remove manual Requires

* Sun Nov 05 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Wed Aug 23 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Sat Jun 10 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.1-alt0.1
- initial build

