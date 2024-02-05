Name: x16-rom
Version: r46
Release: alt1
Summary: Commander X16 BASIC/KERNAL/DOS/GEOS ROM
Group: Development/Tools
License: BSD2
Url: https://github.com/commanderx16/x16-rom
Packager: Artyom Bystrov <arbars@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar
Source2: github-pandoc.css

BuildRequires: gcc
BuildRequires: make
BuildRequires: cc65-devel
BuildRequires: python3-dev
BuildRequires: lzsa
BuildRequires: pandoc

%description
This is the Commander X16 ROM containing BASIC,
KERNAL, DOS and GEOS. BASIC and KERNAL are
derived from the Commodore 64 versions.
GEOS is derived from the C64/C128 version.

%prep
%setup

%build
pandoc \
    --from gfm \
    --to html -c github-pandoc.css \
    --standalone \
    --metadata pagetitle="X16 KERNAL/BASIC/DOS ROM" README.md \
    --output KERNAL-BASIC.html

make RELEASE_VERSION=46

%install
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_docdir/%name
install -p -m 0775 build/x16/rom.bin %buildroot%_datadir/%name/%name.bin
install -p -m 0775 build/x16/*.sym %buildroot%_datadir/%name
install -Dm644 KERNAL-BASIC.html %buildroot%_docdir/%name/KERNAL-BASIC.html
install -Dm644 %SOURCE2 %buildroot%_docdir/%name/github-pandoc.css

%files
%doc README.md
%_datadir/%name/%name.bin
%_datadir/%name/*.sym
%_docdir/%name/KERNAL-BASIC.html
%_docdir/%name/github-pandoc.css

%changelog
* Mon Feb  5 2024 Artyom Bystrov <arbars@altlinux.org> r46-alt1
- Update to new version

* Wed Aug 11 2021 Artyom Bystrov <arbars@altlinux.org> r38-alt4
- update sources to "master" branch

* Fri Aug 06 2021 Artyom Bystrov <arbars@altlinux.org> r38-alt3
- add noarch

* Fri Aug 06 2021 Artyom Bystrov <arbars@altlinux.org> r38-alt2
- Delete unneeded Requires 

* Sat Jan 09 2021 Artyom Bystrov <arbars@altlinux.org> r38-alt1
- initial build for ALT Sisyphus
