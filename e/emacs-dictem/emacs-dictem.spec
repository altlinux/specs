Name: emacs-dictem
Version: 1.0.4
Release: alt1

Summary: Dictionary (RFC 2229) client for Emacs
License: GPL-2.0-or-later
Group: Editors
Url: https://sourceforge.net/projects/dictem/

# https://github.com/cheusov/dictem
Source: dictem-%version.tar

BuildArch: noarch
Requires: dict
BuildRequires: emacs-nox

%description
DictEm is a Dictionary protocol client for GNU Emacs.

It uses a console dict client (http://sf.net/projects/dict) and
implements all functions of the client part of DICT protocol
(RFC-2229, www.dict.org), i.e. looking up words and definitions,
obtaining information about available strategies, provided databases,
information about DICT server etc.

%prep
%setup -n dictem-%version

%build
for n in *.el; do
	emacs -batch --eval "
		(progn
		 (setq load-path (append (list \".\") load-path))
		 (byte-compile-file \"$n\")
		)"
done

%install
mkdir -p %buildroot%_emacslispdir
install -pm644 *.el{,c} %buildroot%_emacslispdir/

%files
%_emacslispdir/*.el
%_emacslispdir/*.elc
%doc AUTHORS README NEWS

%changelog
* Sat Aug 25 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0.4-alt1
- 0.0.2 -> 1.0.4.

* Wed Dec 01 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.0.2-alt1
- New version

* Wed Jul 07 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.0.1-alt1
- First build for ALT project
