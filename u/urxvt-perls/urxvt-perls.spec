%define _urxvt_perl_dir %_libdir/urxvt/perl

Name: urxvt-perls
Version: 2.2.0.9.git532ccec
Release: alt1

Summary: a small collection of perl extensions for the rxvt-unicode

Group: Terminals
License: GPLv2
Url: https://github.com/muennich/urxvt-perls

Requires: rxvt-unicode

# git://git.altlinux.org/gears/u/urxvt-perls.git
Source: %name-%version-%release.tar

%description
A small collection of perl extensions for the rxvt-unicode terminal emulator.

%prep
%setup -n %name-%version-%release
perl -ne 'print unless /^Installation$/../^keyboard-select$/; print if /^keyboard-select$/; print "\n\n" if eof' -i README.md
perl -ne 'print if /url-select/..eof' deprecated/README.md >> README.md

%install
install -m644 keyboard-select -Dt %buildroot%_urxvt_perl_dir
install -m644 deprecated/* -Dt %buildroot%_urxvt_perl_dir

%files
%doc README.md
%_urxvt_perl_dir/*

%changelog
* Mon Nov 27 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.2.0.9.git532ccec-alt1
- Initial build

