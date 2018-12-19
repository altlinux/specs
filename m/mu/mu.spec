%define _unpackaged_files_terminate_build  0

Name: mu
Version: 1.0
Release: alt1
Summary: Set of utilities to deal with Maildirs
Group: Networking/Mail
License: GPL-3.0
Url: https://github.com/djcb/mu
Source0: https://github.com/djcb/%name/releases/download/v%version/%name-%version.tar

BuildRequires: libxapian-devel libgmime-devel gcc-c++

%description
 mu is a set of utilities to deal with Maildirs, specifically,
 indexing and searching.
  - mu index - recursively scans a collection of email messages, and
    stores information found in a database.
  - mu find - searches for messages based on some search criteria.
  - mu mkmdir - creates a new Maildir.
 .
 mu uses libgmime2 to parse the message, and Xapian to store the message data.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/%{name}*.1.*
%_man5dir/%{name}*.5.*
%_man7dir/%{name}*.7.*
%doc AUTHORS COPYING ChangeLog NEWS* TODO HACKING README*

%changelog
* Wed Dec 19 2018 Terechkov Evgenii <evg@altlinux.org> 1.0-alt1
- Initial buid for ALT Linux Sisyphus
