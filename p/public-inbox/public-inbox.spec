Summary: An "archives first" approach to mailing lists

Name: public-inbox
Version: 1.6.0.26.g8080720d
Release: alt1

Group: Networking/Mail
License: AGPL-3.0
URL: https://public-inbox.org

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-perl
BuildRequires: git-core
BuildRequires: pkg-config
BuildRequires: libgit2-devel
BuildRequires: perl-CGI
BuildRequires: perl-Compress-Raw-Zlib
BuildRequires: perl-Crypt-CBC
BuildRequires: perl-DBD-SQLite
BuildRequires: perl-DBIx-DBSchema
BuildRequires: perl-Digest-SHA
BuildRequires: perl-Email-MIME
BuildRequires: perl-Email-MIME-ContentType
BuildRequires: perl-Email-Simple
BuildRequires: perl-Encode
BuildRequires: perl-Encode-CN
BuildRequires: perl-Encode-JP
BuildRequires: perl-Encode-KR
BuildRequires: perl-Encode-TW
BuildRequires: perl-GD-Text
BuildRequires: perl-GraphViz
BuildRequires: perl-HTTP-Date
BuildRequires: perl-HTTP-Message
BuildRequires: perl-HTTP-Tiny
BuildRequires: perl-IO-Compress
BuildRequires: perl-IO-Socket-SSL
BuildRequires: perl-Inline-C
BuildRequires: perl-Mail-IMAPClient
BuildRequires: perl-Mail-SpamAssassin
BuildRequires: perl-Parse-RecDescent
BuildRequires: perl-Plack
BuildRequires: perl-Plack-Middleware-ReverseProxy
BuildRequires: perl-Search-Xapian
BuildRequires: perl-Template-GD
BuildRequires: perl-TimeDate
BuildRequires: perl-URI
BuildRequires: perl-base
BuildRequires: perl-devel
BuildRequires: perl-highlight
BuildRequires: perl-podlators
BuildRequires: xapian-core
BuildRequires: openssl
BuildRequires: sqlite3

%description
public-inbox implements the sharing of an email inbox via git to
complement or replace traditional mailing lists.  Readers may
read via NNTP, Atom feeds or HTML archives.

public-inbox spawned around three main ideas:

* Publicly accessible and archived communication is essential to
  Free Software development.

* Contributing to Free Software projects should not require the
  use of non-Free services or software.

* Graphical user interfaces should not be required for text-based
  communication.  Users may have broken graphics drivers, limited
  eyesight, or be unable to afford modern hardware.

%prep
%setup -q

%build
pushd certs
perl ./create-certs.perl
popd

rm -f -- t/eml.t

%perl_vendor_build

%install
%perl_vendor_install

%make_install \
	DESTDIR=%buildroot \
	PREFIX=%_prefix \
	install-man

rm -f -- %buildroot/%perl_vendor_privlib/PublicInbox/DSKQXS.pm
rm -f -- %buildroot/%perl_vendor_privlib/PublicInbox/KQNotify.pm

mkdir -p "$HOME/.cache/public-inbox/inline-c"

%files
%_bindir/*
%perl_vendor_privlib/*
%_man1dir/*
%_man5dir/*
%_man7dir/*
%_man8dir/*

%changelog
* Thu Oct 15 2020 Alexey Gladkov <legion@altlinux.ru> 1.6.0.26.g8080720d-alt1
- First build for ALTLinux.


