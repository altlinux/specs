Name: emacs-mew
Version: 6.2.52
Release: alt1
License: GPL
Group: Editors
Url: http://www.mew.org/
Summary: Mew is a mail reader for Emacs

Packager: Alexey Voinov <voins@altlinux.ru>

Requires: emacs-common
Source: %name-%version.tar

# Automatically added by buildreq on Tue Apr 07 2009
BuildRequires: emacs-nox

%description
Mew is a user interface for text messages, multimedia messages (MIME),
news articles and security functionality including PGP, S/MIME, SSH,
and SSL. Also, Mew can work with the recent search services.

Mew is an acronym for "Messaging in the Emacs World". You should spell
it with the first letter capitalized and pronounce it as it is
(i.e. the meow of cats). When the author started programming it, he
chose a cute word from his English dictionary. Thus, Mew.

%package el
Summary: Emacs Lisp source for bytecode included in %name
Group: Development/Other
Requires: %name = %version-%release
BuildArch: noarch

%description el
%name-el contains Emacs Lisp sources for the bytecode
included in the %name package.

You need to install %name-el only if you intend to modify
any of the %name code or see some Lisp examples.

%prep
%setup -q

%build
%configure
make

%install
make install DESTDIR=%buildroot

%files
%_bindir/*
%_man1dir/*
%_infodir/*
%dir %_emacslispdir/mew
%dir %_emacslispdir/mew/etc
%_emacslispdir/mew/*.elc
%_emacslispdir/mew/etc/*

%files el
%_emacslispdir/mew/*.el

%changelog
* Tue Sep 22 2009 Alexey Voinov <voins@altlinux.ru> 6.2.52-alt1
- new version (6.2.52)
- -el subpackage is now noarch

* Fri Apr 10 2009 Alexey Voinov <voins@altlinux.ru> 6.2.51-alt2
- fixed bug with inaccurate using of buffer-auto-save-file-name

* Tue Apr 07 2009 Alexey Voinov <voins@altlinux.ru> 6.2.51-alt1
- initial build for emacs (It was never packaged for GNU Emacs, and
  xemacs-mew looks too old and too XEmacs-specific)

