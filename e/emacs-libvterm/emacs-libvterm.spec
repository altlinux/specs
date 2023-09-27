Name: emacs-libvterm
Version: 0.0.20230210
Release: alt1

Summary: Libvterm-based terminal emulator for Emacs
License: GPLv3
Group: Terminals
Url: https://github.com/akermu/emacs-libvterm

Source: %name-%version.tar

BuildRequires: /usr/bin/emacs
BuildRequires: cmake libvterm-devel

%description
Fully-fledged terminal emulator inside GNU Emacs based on libvterm.
As a result of using compiled code (instead of elisp), emacs-libvterm is fully
capable, fast, and it can seamlessly handle large outputs.

%define emacsversion %(emacs -q --batch --eval '(princ (format "%s.%s" emacs-major-version emacs-minor-version))')
%define modulepath %_libdir/emacs/%emacsversion/site-lisp

%prep
%setup

%build
%cmake
%cmake_build

%install
install -pm0644 -D vterm-module.so %buildroot%modulepath/vterm/vterm-module.so
install -pm0644 vterm.el %buildroot%modulepath/vterm

%global _customdocdir %_defaultdocdir/%name

%files
%doc README* etc/*
%modulepath/vterm

%changelog
* Mon Sep 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20230210-alt1
- initial
