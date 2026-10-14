Name: massdns
Version: 1.1.0
Release: alt2

Summary: High-performance DNS stub resolver for bulk lookups

License: GPL-3.0
Group: Networking/DNS
Url: https://github.com/blechschmidt/massdns

ExcludeArch: %ix86

# Source-url: https://github.com/blechschmidt/massdns/archive/v%version.tar.gz
Source: %name-%version.tar

%description
MassDNS is a simple high-performance DNS stub resolver targeting those
who seek to resolve a massive amount of domain names in the order of
millions or even billions. Without special binding, MassDNS is capable
of resolving over 350,000 names per second using publicly available
resolvers.

%prep
%setup

%build
# upstream takes the version from git describe, absent in the tarball
%make_build CFLAGS="%optflags" PROJECT_FLAGS='-DMASSDNS_REVISION=\"v%version\"'

%install
install -Dm755 bin/massdns %buildroot%_bindir/massdns
install -Dm644 doc/massdns.1 %buildroot%_man1dir/massdns.1

%files
%doc README.md LICENSE
%_bindir/massdns
%_man1dir/massdns.1*

%changelog
* Tue Oct 13 2026 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- set the version shown by massdns --version (closes: #58649)

* Thu Feb 12 2026 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Sisyphus
