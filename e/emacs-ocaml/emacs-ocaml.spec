Version: 3.05
Release: alt1
Name: emacs-ocaml
Copyright: GPL
Group: Editors
Packager: Alexander Borovsky <partizan@altlinux.ru>
Url: http://caml.inria.fr/
Summary: OCaml mode for Emacs
Summary(ru_RU.CP1251): Режим OCaml для Emacs

Source: emacs-ocaml.tar.bz2

BuildArch: noarch

BuildRequires: emacs-common
Requires: emacs-common


%description
Mode to programming on Objective Caml for Emacs

%description -l ru_RU.CP1251
Режим для программирования на Objective Caml для Emacs

%prep
%setup -n emacs

%build

%install
%__mkdir_p %buildroot%_bindir
make install install-ocamltags BINDIR=%buildroot%_bindir EMACSDIR=%buildroot%_datadir/emacs/site-lisp

install -d $RPM_BUILD_ROOT%_sysconfdir/emacs/site-start.d
cat <<EOF >$RPM_BUILD_ROOT%_sysconfdir/emacs/site-start.d/ocaml.el
(require 'caml-font)
(autoload 'caml-mode "caml" "Caml editing mode" t)
(add-to-list 'auto-mode-alist '("\\\\.ml[iylp]?$" . caml-mode))
(autoload 'run-caml "inf-caml" "Run an inferior Caml process." t)
(autoload 'camldebug "camldebug" "Run the Caml debugger." t)

EOF

%clean

%files
%defattr(-, root, root)
%_bindir/*
%doc README
%{_emacslispdir}/*
%config(noreplace) /etc/emacs/site-start.d/ocaml.el

%changelog
* Sat Nov 20 2004 Alexander Borovsky <partizan@altlinux.ru> 3.05-alt1
-  First build for ALTLinux
