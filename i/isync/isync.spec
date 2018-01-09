Name: isync
Version: 1.3.0
Release: alt1

Summary: Utility to synchronize IMAP mailboxes with local maildir folders
License: GPLv2+
Group: Networking/Mail
Url: http://isync.sourceforge.net/
Packager: Kirill Maslinsky <kirill@altlinux.org>

Source: %name-%version.tar

BuildPreReq: libdb6.1-devel libssl-devel libsocket-devel

%add_findreq_skiplist %_bindir/get-cert

%description
isync is a command line utility which synchronizes mailboxes; currently
Maildir and IMAP4 mailboxes are supported.
New messages, message deletions and flag changes can be propagated both ways.
It is useful for working in disconnected mode, such as on a laptop or with a
non-permanent internet collection (dIMAP).

%prep
%setup
touch ChangeLog
%autoreconf

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS NEWS README TODO src/mbsyncrc.sample src/compat/isyncrc.sample

%changelog
* Tue Jan 09 2018 Kirill Maslinsky <kirill@altlinux.org> 1.3.0-alt1
- version up

* Tue Aug 02 2016 Lenar Shakirov <snejok@altlinux.ru> 1.2.1-alt1
- New version

* Wed Sep 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2.git20140712
- Built with libdb6.1 instead of libdb4.8

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20140712
- Version 1.1.2

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.4-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Mon Jul 05 2010 Andrey Rahmatullin <wrar@altlinux.org> 1.0.4-alt1
- initial build

