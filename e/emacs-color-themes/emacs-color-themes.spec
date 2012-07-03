# -*- coding: utf-8; mode: rpm-spec -*-

%define pkg_name color-themes

Version: 6.6.0
Release: alt2
Name: emacs-%pkg_name
License: GPL
Group: Editors
Url: https://gna.org/projects/color-theme
Summary: Color themes for GNU Emacs
Requires: emacs-common

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: color-theme-%version.tar.gz
Source1: %pkg_name-emacs.el

Patch0: color-theme_replace-in-string_fix.patch

BuildArch: noarch

# Automatically added by buildreq on Thu Oct 24 2002
BuildRequires: emacs22-X11-athena emacs-devel

%description
Color theme is an Emacs-Lisp package with more than 50 color themes for your use.

All Emacs Lisp code is byte-compiled, install %name-el for sources.

%package el
Summary: The Emacs Lisp sources for bytecode included in %name
Group: Development/Other
Requires: %name = %version-%release

%description el
%name-el contains the Emacs Lisp sources for the bytecode
included in the %name package, that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.

%prep
%setup -q -n color-theme-%version
%patch0 -p1

%install
mkdir -p %buildroot%_emacslispdir/%pkg_name/themes
install -m 644 color-theme.el %buildroot%_emacslispdir/%pkg_name
install -m 644 themes/*.el %buildroot%_emacslispdir/%pkg_name/themes

mkdir -p %buildroot%_emacs_sitestart_dir
install -m 644 %SOURCE1 %buildroot%_emacs_sitestart_dir/%pkg_name.el

%add_lisp_loadpath %buildroot%_emacslispdir/%pkg_name
%add_lisp_loadpath %buildroot%_emacslispdir/%pkg_name/themes
%byte_recompile_lispdir


%files
%doc AUTHORS BUGS README
%dir %_emacslispdir/%pkg_name
%dir %_emacslispdir/%pkg_name/themes
%_emacslispdir/%pkg_name/*.elc
%_emacslispdir/%pkg_name/themes/*.elc
%config(noreplace) %_emacs_sitestart_dir/*

%files el
%_emacslispdir/%pkg_name/*.el
%_emacslispdir/%pkg_name/themes/*.el


%changelog
* Sun Nov 04 2007 Eugene Vlasov <eugvv@altlinux.ru> 6.6.0-alt2
- Used new function color-theme-replace-in-string instead of incorrect
  definition replace-in-string (#13251, used patch from CVS)

* Sun Dec 10 2006 Eugene Vlasov <eugvv@altlinux.ru> 6.6.0-alt1
- Initial build for Sisyphus

