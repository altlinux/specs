
Name: emacs-removable-media
Version: 20110427
Release: alt0.1
Summary: The simple tool for emacs users to mount removable devices
Group: Editors
License: GPL
BuildArch: noarch
Packager: Michael Pozhidaev <msp@altlinux.ru>
BuildRequires: emacs23 emacs-devel
Requires: emacs-base emacs-elib

Source: %name-%version.tar.gz
Source1: site-start.el

%description 
%name is the simple tool for emacs users to mount removable devices.

%prep
%setup -q
%build
%byte_compile_file elisp/removable-media.el

%install
%__install -d -m755 %buildroot%_bindir
%__install -pD -m755 ./shell/* %buildroot%_bindir/

%__install -d %buildroot%_emacslispdir
%__install -pD -m644 elisp/removable-media.* %buildroot%_emacslispdir

%__install -d %buildroot%_emacs_sitestart_dir
%__install -pD -m 644 %SOURCE1 %buildroot%_emacs_sitestart_dir/removable-media.el

%files
%_bindir/*
%_emacslispdir/*
%_emacs_sitestart_dir/*

%changelog
* Wed Apr 27 2011 Michael Pozhidaev <msp@altlinux.ru> 20110427-alt0.1
- Added site-start script with autoloac declarations

* Thu Apr 14 2011 Michael Pozhidaev <msp@altlinux.ru> 20110414-alt0.1
- Fixed bug with invalid regexp format

* Fri Apr 08 2011 Michael Pozhidaev <msp@altlinux.ru> 20110408-alt0.1
- Initial package

