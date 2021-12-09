%define _unpackaged_files_terminate_build 1

Name: cardpeek
Version: 0.8.4
Release: alt1

Summary: Cardpeek is a tool to read the contents of ISO7816 smart cards.
License: GPL-3.0
Group: System/Configuration/Hardware

Url: https://github.com/L1L1/cardpeek
#Git: https://github.com/L1L1/cardpeek.git
Source: %name-%version.tar

BuildRequires: make
BuildRequires: glib2-devel
Buildrequires: libgtk+3-devel
BuildRequires: libpcsclite-devel
BuildRequires: liblua5.3-devel
BuildRequires: libcurl-devel
BuildRequires: libssl-devel
BuildRequires: libreadline-devel

Requires: pcsc-lite-ccid

%description
Cardpeek is a Linux/Windows/Mac OS X tool to read the contents of ISO7816 smart
cards. It features a GTK GUI to represent card data in a tree view, and is
extendable with a scripting language (LUA).

The goal of this project is to allow smart card owners to be better informed
about what type of personal information is stored in these devices.

The tool currently reads the contents of:

- EMV Pin and Chip cards, including NFC ones
- Navigo (Paris), MOBIB (Belgium), RavKav (Israel) and other public transport
cards of the Calypso family - screenshot
- The French health card "Vitale 2"
- Electronic/Biometric passports in BAC security mode
- GSM SIM cards (but not USIM data)
- The Belgian eID card
- Driver tachograph cards
- OpenPGP cards (beta)

It can also read the following cards with limited interpretation of data:

- Some Mifare cards (such as the Thalys card)
- Moneo, the French electronic purse

%prep
%setup

%build
autoreconf --install
./configure --prefix=%_prefix
%make_build

%install
%makeinstall_std

# will pick it up later with doc script
rm -rf %buildroot/%_datadir/doc/%name/%{name}_ref.en.pdf

%files
%doc AUTHORS COPYING NEWS README doc/cardpeek_ref.en.pdf
%_bindir/%name
%_datadir/appdata/%name.appdata.xml
%_datadir/applications/%name.desktop
%_iconsdir/hicolor/48x48/apps/%name-logo.png
%_man1dir/%name.1.xz

%changelog
* Wed Dec 08 2021 Nikolai Kostrigin <nickel@altlinux.org> 0.8.4-alt1
- initial build for Sisyphus
