
Name: emacs-rbook
Version: 1.3.5
Release: alt2

License: Public domain
Group: Accessibility
Summary: The emacs plugin to read text files with Text-to-Speech engine (ru_tts)

BuildArch: noarch
Requires: emacs-common ru_tts sox lame
BuildRequires: emacs-devel emacs-nox
Url: ftp://ftp.rakurs.spb.ru/pub/Goga/projects/rbook
Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: rbook-%version.tar.bz2
Patch1: rbook-1.3.5-alt-path.patch
Patch2: rbook-1.3.5-alt-init.patch

%description
This package allow you to listen large text files with Text-to-Speech engine. It 
uses ru_tts speech synthesizer and supports Russian language.
Currently, mp3 files generation does not work properly.

%prep
%setup -q -n rbook-%version
%patch1 -p1
%patch2 -p1

%build
%byte_compile_file rbook.el

%install

%__install -pD -m 755 speak %buildroot/%_bindir/rbook-speak
%__install -pD -m 755 mp3 %buildroot/%_bindir/rbook-mp3
%__install -pD -m 755 play %buildroot/%_bindir/rbook-play

%__install -pD -m 644 rbook.el %buildroot/%_emacslispdir/rbook.el
%__install -pD -m 644 rbook.elc %buildroot/%_emacslispdir/rbook.elc

%__install -pD -m 644 rbook-init.el %buildroot/%_emacs_sitestart_dir/rbook.el

%__install -pD -m 644 task-done.au %buildroot/%_datadir/%name/task-done.au
%__install -pD -m 644 progress.au %buildroot/%_datadir/%name/progress.au

%files
%config(noreplace) %_emacs_sitestart_dir/*
%_bindir/*
%_emacslispdir/*
%_datadir/%name
%doc ChangeLog README.txt

%changelog
* Tue Jul 17 2012 Terechkov Evgenii <evg@altlinux.org> 1.3.5-alt2
- Fix build with emacs24

* Tue Sep 20 2011 Michael Pozhidaev <msp@altlinux.ru> 1.3.5-alt1
- New version

* Wed Jul 30 2008 Michael Pozhidaev <msp@altlinux.ru> 1.3-alt1
- Initial RPM
