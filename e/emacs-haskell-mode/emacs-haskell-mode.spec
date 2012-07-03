Version: 2.1
Release: alt1
Name: emacs-haskell-mode
Copyright: GPL
Group: Editors
Url: http://www.haskell.org/haskell-mode/
Summary: Haskell mode for Emacs
Summary(ru_RU.CP1251): Emacs mode дл€ €зыка программировани€ Haskell
Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: haskell-mode-%{version}.tar.gz

BuildArch: noarch
Requires: emacs-common

# Automatically added by buildreq on Thu Aug 05 2002
BuildRequires: emacs-common

%description
Haskell mode for Emacs. This mode provides syntax highliting, indentation
and interaction with haskell interpreters.

%description -l ru_RU.CP1251
–ежим дл€ работы Haskell из Emacs. ƒанный режим обеспечивает подсветку
синтаксиса, отступы и взаимодействие с интерпретаторами €зыка Haskell.

%prep
%setup -n haskell-mode-%{version}

%build
for i in *.el ; do
        emacs -batch --eval "(progn
        (setq load-path (append (list \".\")  load-path))
        (byte-compile-file \"$i\"))"
done

%install
mkdir -p $RPM_BUILD_ROOT%{_emacslispdir}/haskell-mode/
install -m 644 *.el* $RPM_BUILD_ROOT%{_emacslispdir}/haskell-mode/

mkdir -p $RPM_BUILD_ROOT/etc/emacs/site-start.d
cat <<'EOF' >$RPM_BUILD_ROOT/etc/emacs/site-start.d/haskell-mode.el
;; Copyright (C) 2002 Alex Ott
;;
;; Author: ottalex@narod.ru

(setq load-path (append load-path '("/usr/share/emacs/site-lisp/haskell-mode/")))
(setq auto-mode-alist
      (append auto-mode-alist
	      '(("\\.[hg]s\\'"  . haskell-mode)
		("\\.hi\\'"     . haskell-mode)
		("\\.l[hg]s\\'" . literate-haskell-mode))))
(autoload 'haskell-mode "haskell-mode"
  "Major mode for editing Haskell scripts." t)
(autoload 'literate-haskell-mode "haskell-mode"
  "Major mode for editing literate Haskell scripts." t)

; obsolete in 2.1
;(add-hook 'haskell-mode-hook 'turn-on-haskell-font-lock)
(add-hook 'haskell-mode-hook 'turn-on-haskell-decl-scan)
(add-hook 'haskell-mode-hook 'turn-on-haskell-doc-mode)
(add-hook 'haskell-mode-hook 'turn-on-haskell-indent)
(add-hook 'haskell-mode-hook 'turn-on-haskell-simple-indent)
(add-hook 'haskell-mode-hook 'turn-on-haskell-hugs)
EOF
chmod 644 $RPM_BUILD_ROOT/etc/emacs/site-start.d/haskell-mode.el

%files
%defattr(-, root, root)
%doc index.html installation-guide.html fontlock.hs indent.hs
%dir %{_emacslispdir}/haskell-mode/
%{_emacslispdir}/haskell-mode/*.el*
#%config(noreplace) /etc/emacs/site-start.d/haskell-mode.el
%config /etc/emacs/site-start.d/haskell-mode.el

%changelog
* Mon Feb 27 2006 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1
- new version

* Thu Mar 13 2003 Ott Alex <ott@altlinux.ru> 1.43-alt4
- Fixing startup file

* Sat Feb 08 2003 Ott Alex <ott@altlinux.ru> 1.43-alt3
- fixing spec

* Wed Dec 25 2002 Ott Alex <ott@altlinux.ru> 1.43-alt1
- Initial build
