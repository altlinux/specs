Name: notmuch
Version: 0.13.2
Release: alt1

Summary: new email reading system called notmuch

Group: Office
License: GPLv3+
Url: http://notmuchmail.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# git clone git://notmuchmail.org/git/notmuch
Source: %name-%version.tar

BuildRequires: gcc-c++ libgmime-devel libtalloc-devel libxapian-devel emacs-devel emacs-nox emacs-gnus

%description
Notmuch is not much of an email program. It doesn't receive messages
(no POP or IMAP suport). It doesn't send messages (no mail composer,
no network code at all). And for what it does do (email search) that
work is provided by an external library, Xapian. So if Notmuch
provides no user interface and Xapian does all the heavy lifting,
then what's left here? Not much.

Notmuch is still in the early stages of development, but it does
include one user interface, (implemented within emacs), which has at
least two users using it for reading all of their incoming mail. If
you've been looking for a fast, global-search and tag-based email
reader to use within emacs, then Notmuch may be exactly what you've
been looking for.

Otherwise, if you're a developer of an existing email program and
would love a good library interface for fast, global search with
support for arbitrary tags, then Notmuch also may be exactly what
you've been looking for.

%package emacs
Group: Office
Summary: Emacs front-end for %name
Requires: %name = %version-%release
BuildArch: noarch

%description emacs
Emacs front-end for %name

%package -n lib%name
Group: System/Libraries
Summary: Shared library for %name

%description -n lib%name
Shared library for %name

%package -n lib%name-devel
Group: Development/C
Summary: Header files for developing programs using lib%name
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the header files needed to develop programs
based on lib%name

%prep
%setup

%build
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
./configure --prefix=%prefix

%make_build V=1

%install
make libdir=%_libdir DESTDIR=%buildroot bash_completion_dir=%_sysconfdir/bash_completion.d install
install -D -m0644 %name.desktop %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_emacs_sitestart_dir
cat >%buildroot%_emacs_sitestart_dir/%name.el <<EOF
; site-start script for Emacs, initializes notmuch
; Evgenii Terechkov, April 2010, <evg@altlinux.ru>

(require 'notmuch)
EOF

%files
%_bindir/%name
%_sysconfdir/bash_completion.d/%name
%_desktopdir/%name.desktop
%_man1dir/%{name}*
%_man5dir/%{name}*
%_man7dir/%{name}*
%doc AUTHORS README NEWS

%files emacs
%_emacs_sitestart_dir/%name.el
%_emacslispdir/*.el*
%_emacslispdir/*%{name}*

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name.h
%_libdir/lib%name.so

%changelog
* Sat Jun 16 2012 Terechkov Evgenii <evg@altlinux.org> 0.13.2-alt1
- 0.13.2

* Fri May 11 2012 Terechkov Evgenii <evg@altlinux.org> 0.12-alt1
- 0.12

* Fri Jan 20 2012 Terechkov Evgenii <evg@altlinux.org> 0.11-alt1
- 0.11
- Completion for notmuch now included in 'zsh' package

* Sat Oct  1 2011 Terechkov Evgenii <evg@altlinux.org> 0.8-alt1
- 0.8

* Mon Jul  4 2011 Terechkov Evgenii <evg@altlinux.org> 0.6-alt1
- 0.6

* Thu Mar 17 2011 Terechkov Evgenii <evg@altlinux.org> 0.5-alt1
- git-20110316 (0.5-110-g7208374)

* Thu Nov  4 2010 Terechkov Evgenii <evg@altlinux.org> 0.4-alt1
- 0.4

* Tue Oct  5 2010 Terechkov Evgenii <evg@altlinux.org> 0.3.1-alt3.git8071c5cd
- git-20101005 (8071c5cd)

* Mon Aug 16 2010 Terechkov Evgenii <evg@altlinux.ru> 0.3.1-alt2.git676d2511
- git-20100816 (676d2511)

* Wed Apr 28 2010 Terechkov Evgenii <evg@altlinux.ru> 0.3.1-alt1
- 0.3.1 bugfix release

* Tue Apr 27 2010 Terechkov Evgenii <evg@altlinux.ru> 0.3-alt1
- 0.3

* Sat Apr 17 2010 Terechkov Evgenii <evg@altlinux.ru> 0.2-alt1
- 0.2

* Tue Apr 13 2010 Terechkov Evgenii <evg@altlinux.ru> 0.1-alt1
- Break to subpackages
- 0.1 (ALT#23302)

* Thu Feb 04 2010 Vitaly Lipatov <lav@altlinux.ru> 0.0.2-alt1
- new build from Jan 24, 2010

* Sun Dec 06 2009 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1
- new build

* Tue Nov 24 2009 Vitaly Lipatov <lav@altlinux.ru> 0.0-alt1
- initial build for ALT Linux Sisyphus

