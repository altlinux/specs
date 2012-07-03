Version: 2.0
%define slimedir %_emacslispdir/slime
Release: alt1.qa1
Name: emacs-slime
License: GPL
Group: Editors
Summary: Superior Lisp Interaction Mode for Emacs
Requires: emacs-common 
Url: http://common-lisp.net/project/slime

Source: slime.tar.bz2
Source1: slime-start-script.el

BuildRequires: emacs-common

%description
slime -- Superior Lisp Interaction Mode for Emacs, provides minor mode for
Emacs, makes programming in Common Lisp more comfortable. This mode provides more
features, than standard inferor mode and ILISP. It ca\ould be used as add-on to 
this modes.

%package el
Summary: The Emacs Lisp sources for bytecode included in %name
Group: Development/Other
Requires: %name = %version-%release

%description el
%name-el contains the Emacs Lisp sources for the bytecode
included  in the %name package, that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.


%prep
%setup -n slime

%build
for i in *.el ; do
	emacs -batch --eval "(progn
	(setq load-path (append (list \".\")  load-path))
	(byte-compile-file \"$i\"))"
done

cd doc
make contributors.texi
make slime.info

%install
mkdir -p %buildroot/%slimedir
install -m 644 *.el* %buildroot/%slimedir/
install -m 644 *.lisp %buildroot/%slimedir/
mkdir -p %buildroot/%_sysconfdir/emacs/site-start.d
install -m 644 %SOURCE1 %buildroot/%_sysconfdir/emacs/site-start.d/slime.el
mkdir -p %buildroot/%_infodir
install -m 644 doc/*.info %buildroot/%_infodir/

%files
%doc README NEWS HACKING ChangeLog
%_emacslispdir/slime/*.elc
%_emacslispdir/slime/*.lisp
%_infodir/*
%_sysconfdir/emacs/site-start.d/*

%files el
%_emacslispdir/slime/*.el

%changelog
* Wed Dec 02 2009 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for emacs-slime
  * postclean-05-filetriggers for spec file

* Sun Dec 02 2007 Alexey Voinov <voins@altlinux.ru> 2.0-alt1
- version updated (2.0)
- url updated
- site-start script rewritten
- el subpackage created


* Tue May 04 2004 Ott Alex <ott@altlinux.ru> 0.99-alt1.20040430
- Initial build for ALTLinux

