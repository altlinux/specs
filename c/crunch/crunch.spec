Name: crunch
Version: 3.6
Release: alt1

Summary: wordlist generator
License: GPL
Group: Security/Networking
Url: http://sourceforge.net/projects/crunch-wordlist/

Source: %name-%version.tar

%description
runch is a wordlist generator where you can specify a standard character set or
a character set you specify. crunch can generate all possible combinations and
permutations.

%prep
%setup -q

%build
%make_build

%install
%make_install install \
    DESTDIR=%buildroot \
    INSTALL_OPTIONS= \
    DOCDIR=%buildroot%_defaultdocdir/%name-%version

%files
%doc COPYING
%_bindir/*
%_datadir/%name
%_man1dir/*

%changelog
* Fri Jun 20 2014 Afanasov Dmitry <ender@altlinux.org> 3.6-alt1
- first build

