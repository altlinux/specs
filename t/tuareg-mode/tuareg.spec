Name: tuareg-mode
Version: 1.45.6
Release: alt1

Group: Development/Other
Summary: Emacs mode for Objective Caml
License: GPL
Url: http://www-rocq.inria.fr/~acohen/tuareg/index.html.en
Source:  tuareg-mode-%version.tar.bz2
BuildArch: noarch
Packager: Ilya Mashkin <oddity@altlinux.ru>

%description

 Tuareg is an alternative [X]Emacs mode for Objective Caml.

%prep
%setup

%build

%install
%define _compress_method skip

mkdir -p $RPM_BUILD_ROOT/etc/emacs/site-start.d/
mkdir -p $RPM_BUILD_ROOT/usr/share/emacs/site-lisp/tuareg/

cat <<EOF >$RPM_BUILD_ROOT/etc/emacs/site-start.d/tuareg.el
(setq load-path (cons "/usr/share/emacs/site-lisp/tuareg" load-path))

(setq auto-mode-alist (cons '("\\\\.ml\\\\w?" . tuareg-mode) auto-mode-alist))
(autoload 'tuareg-mode "tuareg" "Major mode for editing Caml code" t)
(autoload 'camldebug "camldebug" "Run the Caml debugger" t)

(if (and (boundp 'window-system) window-system)
    (if (string-match "XEmacs" emacs-version)
        (require 'sym-lock)
      (require 'font-lock)))

EOF

cp tuareg.el sym-lock.el camldebug.el $RPM_BUILD_ROOT/usr/share/emacs/site-lisp/tuareg/

%files
/etc/emacs/site-start.d/tuareg.el
/usr/share/emacs/site-lisp/tuareg/*

%doc README custom-tuareg.el

%changelog
* Wed Oct 22 2008 Ilya Mashkin <oddity@altlinux.ru> 1.45.6-alt1
- 1.45.6

* Fri Nov 26 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.43.0-alt1
- new version

* Sun Dec 01 2002 Vitaly Lugovsky <vsl@altlinux.ru> 1.40.4-alt1
- new version

* Thu Oct 24 2002 Vitaly Lugovsky <vsl@altlinux.ru> 1.40.3-alt1
- new version

* Sun Aug 18 2002 Vitaly Lugovsky <vsl@altlinux.ru> 1.40.2-alt1
- new version

* Tue Jun 25 2002 Vitaly Lugovsky <vsl@altlinux.ru> 1.38.9-alt2
- paths fixed

* Mon Jun 24 2002 Vitaly Lugovsky <vsl@altlinux.ru>
- First RPM release

