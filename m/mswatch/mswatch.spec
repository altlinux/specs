Name: mswatch
Version: 1.2.0
Release: alt1.svn20120312

Summary: Watch mailstores for changes and initiate mailbox syncs
License: GPLv2+
Group: Networking/Mail
Url: http://mswatch.sourceforge.net/

Source: %name-%version.tar

BuildPreReq: flex gcc-c++ glib2-devel

%description
mswatch is a command line unix program that keeps two mailboxes
synchronized more efficiently and with shorter delays than periodically
synchronizing the two mailboxes.
mswatch watches mailboxes to know when to initiate mailbox syncs. Using
mswatch, your mail synchronization program can be called on demand
instead of through polling, resulting in prompter mail delivery and
lower bandwidth usage and server load.
mswatch is designed to work in conjunction with mailbox synchronization
programs, currently supports watching Linux (2.4+) hosted Maildirs
(including Maildir folders, Maildir++), and is licensed under the GNU
GPL. Future support for additional mailbox formats, especially for mbox,
is planned.

%prep
%setup
%autoreconf

%build
%configure \
	--enable-static
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS ChangeLog INTERFACES NEWS README THANKS TODO generalized mswatchrc.sample

%changelog
* Tue Sep 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.svn20120312
- Version 1.2.0

* Fri Dec 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.1
- Fixed build with glibc 2.16

* Sun Jul 04 2010 Andrey Rahmatullin <wrar@altlinux.org> 1.1.1-alt1
- initial build

