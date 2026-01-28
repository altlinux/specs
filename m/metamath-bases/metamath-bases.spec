%define SYMBVERSION 2025.10.05
Name:           metamath-bases
Version:        2026.01.26
Release:        alt1
License:        CC0-1.0
Summary:        A collection of rigorously verified Metamath databases

Source:         set.mm-develop-%version.tar.gz
Source1:        symbols-main-%SYMBVERSION.tar.gz
VCS:            https://github.com/metamath/set.mm
URL:            https://us.metamath.org/
Group:          Sciences/Mathematics

ExclusiveArch:  %ix86 x86_64
BuildArch:      noarch
# Automatically added by buildreq on Tue Jan 27 2026
# optimized out: bash5 libgpg-error python3 python3-base sh5
BuildRequires: metamath

BuildRequires:  metamath

%description
Metamath is a computer language and associated computer program for
archiving, verifying, and studying mathematical proofs.

This is a collection of rigorously verified Metamath databases that
specify mathematical axioms and formal proofs of theorems derived from
those axioms.

%prep
%setup -n set.mm-develop -b1
ln ../symbols-main/symbols/* .

%build
metamath 'read set.mm' 'markup mmset.raw.html mmset.html /ALT /CSS' quit
metamath 'read iset.mm' 'markup mmil.raw.html mmil.html /ALT /CSS' quit
cp mmbiblio.raw.html mmbiblio.html

%install
mkdir -p %buildroot%_datadir/metamath
install -m 644 *.mm* *discouraged %buildroot%_datadir/metamath/

%check
scripts/verify --top_date_skip --extra 'write bibliography mmbiblio.html' set.mm
scripts/verify --top_date_skip iset.mm

%files
%doc *.html *.md *.txt *.gif
%_datadir/metamath/*

%changelog
* Tue Jan 27 2026 Fr. Br. George <george@altlinux.org> 2026.01.26-alt1
- Initial build for ALT
