%define gobuild go build

Name: aerc
Version: 0.16.0
Release: alt1
Summary: Email client for your terminal

License: MIT
Group: File tools
Url: https://git.sr.ht/~rjarry/aerc

# Source-url:         https://git.sr.ht/~rjarry/aerc/archive/%version.tar.gz#/%name-%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires: scdoc
BuildRequires: desktop-file-utils
BuildRequires: gnupg
BuildRequires: libnotmuch-devel
BuildRequires: rpm-build-python3

BuildRequires(pre): rpm-macros-golang
ExclusiveArch: %go_arches

BuildRequires: golang >= 1.7

Requires: notmuch

%description
Aerc is an email client that runs in your terminal. It's highly
efficient and extensible, perfect for the discerning hacker.

%prep
%setup -a1

# Disable building of aerc that we handle manually in the SPEC and
# preserve mtimes
sed -e 's|install: $(DOCS) aerc wrap|install: $(DOCS)|' \
    -e 's|install -m|install -pm|' \
    -i Makefile

# From go.mod replace statements:
# replace golang.org/x/crypto => github.com/ProtonMail/go-crypto v0.0.0-20200420072808-71bec3603bf3
# replace github.com/zenhack/go.notmuch => github.com/brunnre8/go.notmuch v0.0.0-20201126061756-caa2daf7093c
#__subst "s|golang.org/x/crypto|github.com/ProtonMail/go-crypto|" $(find . -name "*.go" -type f)
#__subst "s|github.com/zenhack/go.notmuch|github.com/brunnre8/go.notmuch|" $(find . -name "*.go" -type f)

%build
export GOFLAGS=-mod=vendor
make wrap colorize CC=gcc
export BUILDTAGS=notmuch
export LDFLAGS="-X main.Version=%version \
                -X main.Prefix=%prefix \
                -X main.Flags=$(echo -- $(GOFLAGS) | base64 | tr -d '\r\n') \
                -X git.sr.ht/~rjarry/aerc/config.shareDir=%_datadir \
                -X git.sr.ht/~rjarry/aerc/config.libexecDir=%_libexecdir"
%gobuild -o aerc git.sr.ht/~rjarry/aerc

%install
export PREFIX=%prefix
%makeinstall_std
desktop-file-validate %buildroot/%_desktopdir/aerc.desktop

%files
%doc LICENSE
%doc doc README.md
%_bindir/aerc
%_bindir/carddav-query
%_datadir/aerc/
%_desktopdir/aerc.desktop
/usr/libexec/aerc/
%_man1dir/carddav-query.*
%_man1dir/aerc-*.1.*
%_man1dir/aerc.1*
%_man5dir/aerc-*.5.*
%_man7dir/aerc-*.7.*

%changelog
* Tue Nov 07 2023 Vitaly Lipatov <lav@altlinux.ru> 0.16.0-alt1
- new version 0.16.0 (with rpmrb script)

* Wed Aug 02 2023 Vitaly Lipatov <lav@altlinux.ru> 0.15.2-alt1
- initial build for ALT
