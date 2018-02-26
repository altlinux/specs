Version: 2.10
Release: alt2
Name: emacs-pov-mode
License: GPL
Group: Editors
Url: http://www.acc.umu.se/~woormie/povray/
Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Summary: Emacs mode for editing POVRAY files 
Summary(ru_RU.KOI8-R): Режим Emac для редактирования файлов POVRAY
Requires: emacs-common emacsen-startscripts 

Source: pov-mode.%version.tgz
Source1: pov-im.el
Source2: emacs-pov-start-script.el

BuildArch: noarch

# Automatically added by buildreq on Tue Dec 24 2002
BuildRequires: emacs-common 

%description
Emacs mode for editing POVRAY files 

%description -l ru_RU.KOI8-R
Режим Emac для редактирования файлов POVRAY

%prep
%setup -c %name-%version -a 0

%build
cp %SOURCE1 .
for i in *.el ; do
	emacs -batch --eval "(progn
	(setq load-path (append (list \".\")  load-path))
	(byte-compile-file \"$i\"))"
done

%install
mkdir -p %buildroot%_emacslispdir/
install -m 644 *.el* %buildroot%_emacslispdir/
install -m 644 *.xpm %buildroot%_emacslispdir/
cp -R InsertMenu %buildroot%_emacslispdir/
mkdir -p %buildroot/%_sysconfdir/emacs/site-start.d
install -m 644 %SOURCE2 %buildroot/%_sysconfdir/emacs/site-start.d/pov.el

%files
%doc 
%_emacslispdir/*.el*
%_sysconfdir/emacs/site-start.d/*

%changelog
* Wed Jan 11 2006 Igor Vlasenko <viy@altlinux.ru> 2.10-alt2
- updated url; now maintained by Emacs Maintainers Team

* Tue Oct 28 2003 Ott Alex <ott@altlinux.ru> 2.10-alt1
- Initial build

