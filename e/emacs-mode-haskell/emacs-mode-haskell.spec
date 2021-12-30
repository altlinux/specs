Version: 2.1
Release: alt2.1
Name: emacs-mode-haskell
License: GPLv2+
Group: Editors
Url: http://wiki.haskell.org/haskell-mode/
Summary: Haskell mode for Emacs
Summary(ru_RU.UTF-8): Emacs mode для языка программирования Haskell
Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: haskell-mode-%{version}.tar.gz

BuildArch: noarch
Obsoletes: emacs-haskell-mode
Requires: emacs-common

# Automatically added by buildreq on Thu Aug 05 2002
BuildRequires: rpm-build-emacs

%description
Haskell mode for Emacs. This mode provides syntax highliting, indentation
and interaction with haskell interpreters.

%description -l ru_RU.UTF-8
Режим для работы с Haskell из Emacs. Данный режим обеспечивает подсветку
синтаксиса, отступы и взаимодействие с интерпретаторами языка Haskell.

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
	      '(("\\.[hg]s\\(\\|-boot\\)\\'"  . haskell-mode)
		("\\.hi\\(\\|-boot\\)\\'"     . haskell-mode)
		("\\.l[hg]s\\(\\|-boot\\)\\'" . literate-haskell-mode))))
; This could be moved/adapted into a Curry-specific package:
(setq auto-mode-alist
      (append auto-mode-alist
	      '(("\\.curry\\(\\|-boot\\)\\'"  . haskell-mode)
		("\\.lcurry\\(\\|-boot\\)\\'" . literate-haskell-mode))))
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
%doc index.html installation-guide.html fontlock.hs indent.hs
%dir %{_emacslispdir}/haskell-mode/
%{_emacslispdir}/haskell-mode/*.el*
#%config(noreplace) /etc/emacs/site-start.d/haskell-mode.el
%config /etc/emacs/site-start.d/haskell-mode.el

%changelog
* Thu Dec 30 2021 Igor Vlasenko <viy@altlinux.org> 2.1-alt2.1
- NMU: fixed build

* Tue Dec 08 2015 Ivan Zakharyaschev <imz@altlinux.org> 2.1-alt2
- Handle .(hi|[l]hs)-boot files, too;
- and .[l]curry (as a workaround for the absense of a special curry-mode).
- Renamed the package according to ALT's policy for Emacs modes (ALT#30503).

* Mon Feb 27 2006 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1
- new version

* Thu Mar 13 2003 Ott Alex <ott@altlinux.ru> 1.43-alt4
- Fixing startup file

* Sat Feb 08 2003 Ott Alex <ott@altlinux.ru> 1.43-alt3
- fixing spec

* Wed Dec 25 2002 Ott Alex <ott@altlinux.ru> 1.43-alt1
- Initial build
