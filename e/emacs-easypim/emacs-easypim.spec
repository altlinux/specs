
Name: emacs-easypim
Version: 20110323
Release: alt2
Summary: The simple tool to store personal address book in emacs
Group: Editors
License: GPL
BuildArch: noarch
Packager: Michael Pozhidaev <msp@altlinux.ru>
BuildRequires: emacs-nox emacs-devel
Requires: emacs-base

Source: %name-%version.tar.gz

%description 
%name is the simple tool to store personal address book in
emacs. Information about each person or organization is saved in
separate text file. It allows easy distributed control with git and
simplifies service operations.

%prep
%setup -q
%build
%byte_compile_file elisp/easypim.el

%install
%__install -d -m755 %buildroot%_bindir
%__install -pD -m755 ./shell/* %buildroot%_bindir/

%__install -d %buildroot%_emacslispdir
%__install -pD -m644 elisp/easypim.* %buildroot%_emacslispdir

%__install -d -m755 %buildroot%_sysconfdir/profile.d
%__install -pD -m755 profile.sh %buildroot%_sysconfdir/profile.d/%name.sh

%files
%_bindir/*
%_emacslispdir/*
%_sysconfdir/profile.d/*

%changelog
* Tue Jul 17 2012 Terechkov Evgenii <evg@altlinux.org> 20110323-alt2
- Fix build with emacs24

* Wed Mar 23 2011 Michael Pozhidaev <msp@altlinux.ru> 20110323-alt1
- Initial package

