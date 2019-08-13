Name: emacs-with-editor
Version: 2.8.1
Release: alt1

Summary: Use the Emacsclient as the $EDITOR of child processes
License: GPL-3.0-or-later
Group: Editors
Url: https://github.com/magit/with-editor/

# repacked https://github.com/magit/with-editor/archive/v%version.tar.gz
Source: v%version.tar

BuildRequires: emacs-dash
BuildRequires: emacs-nox
BuildRequires: make
BuildRequires: makeinfo
Requires: emacs
Requires: emacs-dash

BuildArch: noarch

%description
This library makes it possible to reliably use the Emacsclient as the $EDITOR
of child processes. It makes sure that they know how to call home. For remote
processes a substitute is provided, which communicates with Emacs on standard
output/input instead of using a socket as the Emacsclient does.

%prep
%setup -n with-editor-%version

%build
make DFLAGS="-L %_emacslispdir" INSTALL_INFO=/sbin/install-info all

%install
install -d %buildroot/%_emacslispdir/
install -m 644 *.el *.elc %buildroot/%_emacslispdir/
install -D -m 644 with-editor.info %buildroot/%_infodir/with-editor.info

%files
%_emacslispdir/*.el
%_emacslispdir/*.elc
%_infodir/with-editor.info.*

%changelog
* Tue Aug 13 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.8.1-alt1
- Initial build for ALT Sisyphus based on openSUSE spec.

