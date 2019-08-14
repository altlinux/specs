Name: emacs-magit-popup
Version: 2.13.0
Release: alt1

Summary: Interface for toggling switches and setting options to invoke a command
License: GPL-3.0-or-later
Group: Editors

Url: https://github.com/magit/magit-popup/

# repacked https://github.com/magit/magit-popup/archive/v%version.tar.gz
Source: v%version.tar

BuildRequires: emacs-nox
BuildRequires: emacs-dash
BuildRequires: git-core
BuildRequires: make
BuildRequires: makeinfo
Requires: emacs
Requires: emacs-dash
Requires: git-core

BuildArch: noarch

%description
This package implements a generic interface for toggling switches and
setting options and then invoking an Emacs command, which does something
with these arguments. The prototypical use is for the command to call an
external process, passing on the arguments as command line arguments. But
this is only one of many possible uses (though the one this library is
optimized for).

%prep
%setup -n magit-popup-%version

%build
make PREFIX=%prefix DESTDIR=%buildroot INSTALL_INFO=/sbin/install-info lispdir=%_emacslispdir LOAD_PATH="-L %_emacslispdir -L ./lisp -L ." all

%install
mkdir -p %buildroot%_emacslispdir
cp -p magit-popup.el* magit-popup-autoloads.el %buildroot%_emacslispdir
mkdir -p %buildroot%_infodir
cp -p magit-popup.info %buildroot%_infodir/

%files
%doc README.md
%doc AUTHORS.md
%_emacslispdir/magit*.el
%_emacslispdir/magit*.elc
%_infodir/magit-popup.info.*

%changelog
* Tue Aug 13 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.13.0-alt1
- Initial build for ALT Sisyphus based on openSUSE spec.

