Version: 0.1
Release: alt1
Name: emacs-jdee-addons
License: GPL
Group: Editors
Summary: Various packages for Emacs JDEE
Summary(ru_RU.KOI8-R): Дополнительные пакеты для Emacs JDEE
Requires: emacs-jdee emacs-prog-modes

Source: %name.tar.gz
Source1: emacs-jdee-addons-site-start.el 

BuildArch: noarch

# Automatically added by buildreq on Tue Dec 24 2002
BuildRequires: emacs-jdee emacs-prog-modes

%description
Various packages for Emacs JDEE.

%description -l ru_RU.KOI8-R
Дополнительные пакеты Emacs JDEE

%prep
%setup -n %name

%build
for i in *.el ; do
  emacs -batch --eval "(progn (add-to-list 'load-path \".\") (byte-compile-file \"$i\"))"
done

%install
mkdir -p %buildroot%_emacslispdir/jdee-addons
install -m 644 *.el* %buildroot%_emacslispdir/jdee-addons
%__install -pD -m0644 %SOURCE1 %buildroot%_sysconfdir/emacs/site-start.d/jdee-addons.el

%files
%_emacslispdir/jdee-addons/*.el*
%config(noreplace) %_sysconfdir/emacs/site-start.d/*

%changelog
* Thu May 06 2004 Ott Alex <ott@altlinux.ru> 0.1-alt1
- First build for ALTLinux

