Name: SpamOracle
Version: 1.6
Release: alt1.1

Group: Networking/Mail
Summary: Spam filter
License: GPL2
Url: https://github.com/xavierleroy/spamoracle
Packager: Evgenii Terechkov <evg@altlinux.ru>
Source: spamoracle-%version.tar
Patch1: spamoracle-alt-bytecode-build.patch

BuildRequires(pre): rpm-build-ocaml >= 1.6.1
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
%autopatch -p1

%build
make \
%ifnarch %ocaml_native_arch
    NATIVE=false
%endif
    %nil

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir %buildroot%_man5dir
make install BINDIR=%buildroot%_bindir MANDIR=%buildroot%_mandir LANGUAGES="-DFRENCH -DRUSSIAN -DGERMAN"

%files
%_bindir/spamoracle
%_man1dir/*
%_man5dir/*

%doc README* Changes

%changelog
* Wed Feb 28 2024 Ivan A. Melnikov <iv@altlinux.org> 1.6-alt1.1
- NMU: fix build w/o ocamlopt

* Wed Feb 26 2020 Anton Farygin <rider@altlinux.ru> 1.6-alt1
- 1.6
- cleanup spec

* Mon Jul  2 2018 Terechkov Evgenii <evg@altlinux.org> 1.4-alt2
- 0fc9993
- Update URL tag

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Mar  4 2009 Terechkov Evgenii <evg@altlinux.ru> 1.4-alt1
- 1.4
- Spec cleanup
- License tag updated
- Russian patch updated


* Fri Oct 25 2002 Vitaly Lugovsky <vsl@altlinux.ru> 1.2-alt2
- initial release


