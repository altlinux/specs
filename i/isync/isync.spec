Name: isync
Version: 1.0.4
Release: alt1.1

Summary: Utility to synchronize IMAP mailboxes with local maildir folders
License: GPLv2+
Group: Networking/Mail
Url: http://isync.sourceforge.net/

Packager: Andrey Rahmatullin <wrar@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: libdb4-devel libssl-devel

%add_findreq_skiplist %_bindir/get-cert

%description
isync is a command line utility which synchronizes mailboxes; currently
Maildir and IMAP4 mailboxes are supported.
New messages, message deletions and flag changes can be propagated both ways.
It is useful for working in disconnected mode, such as on a laptop or with a
non-permanent internet collection (dIMAP).

%prep
%setup
%patch -p1
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
* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Mon Jul 05 2010 Andrey Rahmatullin <wrar@altlinux.org> 1.0.4-alt1
- initial build

