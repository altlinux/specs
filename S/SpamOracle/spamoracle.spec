Name: SpamOracle
Version: 1.4
Release: alt1

Group: Networking/Mail
Summary: Spam filter
License: GPL2
Url: http://pauillac.inria.fr/~xleroy/software.html#spamoracle
Packager: Evgenii Terechkov <evg@altlinux.ru>
Source: spamoracle-%version.tar.gz
Patch0: spamoracle-%version-russian.patch
BuildRequires: ocaml

%description

  SpamOracle is a tool to help detect and filter away "spam"
  (unsolicited commercial e-mail).  It proceeds by statistical analysis
  of the words that appear in the e-mail, comparing the frequencies of
  words with those found in a user-provided corpus of known spam and
  known legitimate e-mail.  The classification algorithm is based on
  Bayes' formula, and is described in Paul Graham's paper, "A plan for
  spam", http://www.paulgraham.com/spam.html.

Recommends: procmail

%prep
%setup -nspamoracle-%version
%patch0 -p1

%build
make

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir %buildroot%_man5dir
make install BINDIR=%buildroot%_bindir MANDIR=%buildroot%_mandir

%files
%_bindir/spamoracle
%_man1dir/*
%_man5dir/*

%doc README* Changes

%changelog
* Wed Mar  4 2009 Terechkov Evgenii <evg@altlinux.ru> 1.4-alt1
- 1.4
- Spec cleanup
- License tag updated
- Russian patch updated


* Fri Oct 25 2002 Vitaly Lugovsky <vsl@altlinux.ru> 1.2-alt2
- initial release


