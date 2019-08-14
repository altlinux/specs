%define oname magit

Name: emacs-magit
Version: 2.90.1
Release: alt1

Summary: Git interaction mode for emacs

License: GPL-3.0-or-later
Group: Development/Other
Url: https://github.com/magit/magit

# repacked https://github.com/magit/magit/releases/download/%version/magit-%version.tar.gz
Source: %oname-%version.tar
Source1: %oname.el

BuildRequires: emacs-devel emacs-dash emacs-ghub emacs-magit-popup emacs-with-editor makeinfo
Requires: emacs-dash emacs-ghub emacs-magit-popup emacs-with-editor
BuildArch: noarch

%description
Magit is an interface to the version control system Git, implemented as an
Emacs package. Magit aspires to be a complete Git porcelain. While we cannot
(yet) claim that Magit wraps and improves upon each and every Git command,
it is complete enough to allow even experienced Git users to perform almost
all of their daily version control tasks directly from within Emacs.

%prep
%setup -q -n magit-%version

%build
make PREFIX=%_prefix DESTDIR=%buildroot INSTALL_INFO=/sbin/install-info lispdir=%_emacslispdir LOAD_PATH="-L %_emacslispdir -L ./lisp -L ." -C lisp magit-version.el
make PREFIX=%_prefix DESTDIR=%buildroot INSTALL_INFO=/sbin/install-info lispdir=%_emacslispdir LOAD_PATH="-L %_emacslispdir -L ./lisp -L ."

%install
make install DESTDIR=%buildroot PREFIX=%_prefix
install -p %SOURCE1 -D %buildroot%_emacs_sitestart_dir/%oname.el

%files
%doc README.md
%doc Documentation/AUTHORS.md
%config(noreplace) %_emacs_sitestart_dir/%oname.el
%_emacslispdir/magit/magit*.el
%_emacslispdir/magit/magit*.elc
%_emacslispdir/magit/git-commit.el
%_emacslispdir/magit/git-commit.elc
%_emacslispdir/magit/git-rebase.el
%_emacslispdir/magit/git-rebase.elc
%_infodir/magit.info.*

%changelog
* Mon Jul 29 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.90.1-alt1
- Initial build for ALT Sisyphus.

