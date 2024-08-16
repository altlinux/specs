%define _unpackaged_files_terminate_build  0

Name: mu
Version: 1.10.9
Release: alt1
Summary: Set of utilities to deal with Maildirs
Group: Networking/Mail
License: GPL-3.0
Url: https://github.com/djcb/mu
Source0: https://github.com/djcb/%name/releases/download/v%version/%name-%version.tar

# Automatically added by buildreq on Wed Dec 20 2023
# optimized out: cmake cmake-modules emacs-common glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-locales libgio-devel libgpg-error libp11-kit libsasl2-3 libstdc++-devel libtree-sitter ninja-build perl perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl perl-parent pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-paste python3-module-setuptools sh5 tzdata xz
BuildRequires: ccmake emacs-athena emacs-el gcc-c++ git-core libgmime3.0-devel libssl-devel libxapian-devel libxforms-demos lua5.4 makeinfo meson python3-module-mpl_toolkits python3-module-tqdm python3-module-zope

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
%meson
%meson_build

%install
%meson_install
rm -f %buildroot/usr/share/doc/mu/NEWS.org
rm -f %buildroot/usr/share/doc/mu/mu4e-about.org

%check
%__meson_test

%files
%_bindir/%name
%_man1dir/%{name}*.1.*
%_man5dir/%{name}*.5.*
%_man7dir/%{name}*.7.*
%_infodir/*
/usr/share/emacs/site-lisp/mu4e/*.el
/usr/share/emacs/site-lisp/mu4e/*.elc
%doc AUTHORS COPYING ChangeLog NEWS* README* mu4e/mu4e-about.org

%changelog
* Fri Aug 16 2024 Ivan A. Melnikov <iv@altlinux.org> 1.10.9-alt1
- 1.10.9
- Reduce BuildRequires to fix FTBFS
- Add %%check section

* Wed Dec 20 2023 Denis Smirnov <mithraen@altlinux.ru> 1.10.7-alt1
- 1.10.7

* Wed Dec 19 2018 Terechkov Evgenii <evg@altlinux.org> 1.0-alt1
- Initial buid for ALT Linux Sisyphus
