Name: mswatch
Version: 1.1.1
Release: alt1

Summary: Watch mailstores for changes and initiate mailbox syncs
License: GPLv2+
Group: Networking/Mail
Url: http://mswatch.sourceforge.net/

Packager: Andrey Rahmatullin <wrar@altlinux.org>

Source: %name-%version.tar
Patch0: %name-1.1.1-link-fix.patch

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
%patch0 -p2
%autoreconf

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS ChangeLog INTERFACES NEWS README TODO generalized mswatchrc.sample

%changelog
* Sun Jul 04 2010 Andrey Rahmatullin <wrar@altlinux.org> 1.1.1-alt1
- initial build

