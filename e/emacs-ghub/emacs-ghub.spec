Name: emacs-ghub
Version: 2.0.1
Release: alt1

Summary: Minuscule client libraries for the APIs of various Git forges
License: GPL-3.0-or-later
Group: Editors
Url: https://github.com/magit/ghub/

# repacked https://github.com/magit/ghub/releases/v%version.tar.gz
Source: v%version.tar

BuildRequires: emacs-dash
BuildRequires: emacs-nox
BuildRequires: make
BuildRequires: makeinfo
Requires: emacs
Requires: emacs-dash

BuildArch: noarch

%define _magit_make make PREFIX=%prefix DESTDIR=%buildroot lispdir=%_emacslispdir LOAD_PATH="-L %_emacslispdir -L ./lisp -L ."

%description
Ghub provides basic support for using the APIs of various Git forges from
Emacs packages. Originally it only supported the Github REST API, but now it
also supports the Github GraphQL API as well as the REST APIs of Gitlab,
Gitea, Gogs and Bitbucket.

%prep
%setup -n ghub-%version

%build
%_magit_make all INSTALL_INFO=/sbin/install-info

%install
mkdir -p %buildroot/%_emacslispdir
%__cp ghub.el* %buildroot/%_emacslispdir
%__cp ghub-autoloads.el* %buildroot/%_emacslispdir
%__cp glab.el* %buildroot/%_emacslispdir

%files
%doc README.md
%_emacslispdir/ghub.el*
%_emacslispdir/glab.el*
%_emacslispdir/ghub-autoloads.el

%changelog
* Tue Aug 13 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.0.1-alt1
- Initial build for ALT Sisyphus based on openSUSE spec.
