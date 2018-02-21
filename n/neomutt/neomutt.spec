Name: neomutt
Version: 20180221
Release: alt1

%define docdir %_docdir/%name-%version
%undefine _configure_gettext

Summary: A version of Mutt with added features

License: GPLv2+ and Public Domain
Group: Networking/Mail
Url: https://www.neomutt.org/

# https://github.com/neomutt/neomutt.git
Source: %name-%version-%release.tar

BuildRequires: docbook-style-xsl xsltproc tcl elinks
BuildRequires: liblua5-devel libnotmuch-devel libdb4.8-devel
BuildRequires: libgpgme-devel libncursesw-devel libssl-devel libsasl2-devel libidn-devel

Requires: mailcap

%description
Neomutt is a small but very powerful text based program for reading
and sending electronic mail under unix operating systems, including
support for color terminals, MIME, OpenPGP, and a threaded sorting
mode.

%prep
%setup -n %name-%version-%release

%build
%configure \
                --disable-nls \
		--docdir=%docdir \
                --with-ui=ncurses  \
		--gpgme \
		--notmuch \
		--lua \
		--bdb \
		--ssl \
		--sasl

%make_build

%install
%makeinstall_std

%files
%config(noreplace) %_sysconfdir/neomuttrc
%_bindir/neomutt
%_mandir/man?/*
%_libexecdir/neomutt*
%docdir

%changelog
* Wed Feb 21 2018 Vitaly Chikunov <vt at altlinux.org> 20180221-alt1
- initial build for ALT Linux Sisyphus
