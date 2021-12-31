Version: 3.3
Release: alt1
Name: emacs-pov-mode
License: GPLv2+
Group: Editors
Url: http://www.acc.umu.se/~woormie/povray/
Vcs: https://github.com/emacsmirror/pov-mode
Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Summary: Emacs mode for editing POVRAY files
Summary(ru_RU.UTF-8): Режим Emac для редактирования файлов POVRAY
Requires: emacs-common emacsen-startscripts

Source: %name-%version.tar
# from http://imagico.de/imenu/index.php
# for 2.10. deprecated for now?
Source1: pov-im.el
Source2: emacs-pov-start-script.el

BuildArch: noarch

# Automatically added by buildreq on Tue Dec 24 2002
BuildRequires: rpm-build-emacs

%description
Emacs mode for editing POVRAY files

%description -l ru_RU.UTF-8
Режим Emac для редактирования файлов POVRAY

%prep
%setup -q

%build
cp %SOURCE1 .
for i in *.el ; do
	emacs -batch --eval "(progn
	(setq load-path (append (list \".\")  load-path))
	(byte-compile-file \"$i\"))"
done

%install
%define povdir %_emacslispdir/pov-mode
mkdir -p %buildroot%povdir/
install -m 644 *.el* %buildroot%povdir/
install -m 644 *.xpm %buildroot%povdir/
cp -R InsertMenu %buildroot%povdir/
mkdir -p %buildroot%_emacs_sitestart_dir
install -m 644 %SOURCE2 %buildroot%_emacs_sitestart_dir/pov.el

install -D -m 644 pov-mode.info %buildroot%_infodir/pov-mode.info

%files
%doc README
%_infodir/*.info*
%povdir
%_emacs_sitestart_dir/*

%changelog
* Sat Jan 01 2022 Igor Vlasenko <viy@altlinux.org> 3.3-alt1
- new version

* Wed Jan 11 2006 Igor Vlasenko <viy@altlinux.ru> 2.10-alt2
- updated url; now maintained by Emacs Maintainers Team

* Tue Oct 28 2003 Ott Alex <ott@altlinux.ru> 2.10-alt1
- Initial build

