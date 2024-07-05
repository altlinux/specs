%define _unpackaged_files_terminate_build 1

Name:    asbru-cm
Version: 6.4.0
Release: alt1

Summary: Asbru Connection Manager is a user interface that helps organizing remote terminal sessions and automating repetitive tasks.
License: GPL-3.0
Group:   Networking/Remote access
Url:     https://github.com/asbru-cm/asbru-cm

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: asbru-cm-manpage-name.patch

BuildArch: noarch

BuildRequires(pre): perl-devel
BuildRequires(pre): rpm-build-gir
BuildRequires: perl(Crypt/Blowfish.pm)
BuildRequires: perl(Crypt/CBC.pm)
BuildRequires: perl(Crypt/Rijndael.pm)
BuildRequires: perl(Encode.pm)
BuildRequires: perl(Expect.pm)
BuildRequires: perl(Gtk3.pm)
BuildRequires: perl(Gtk3/SimpleList.pm)
BuildRequires: perl(Net/ARP.pm)
BuildRequires: perl(Net/Ping.pm)
BuildRequires: perl(OSSP/uuid.pm)
BuildRequires: perl(Socket6.pm)
BuildRequires: perl(YAML.pm)

BuildRequires: typelib(Gtk) = 3.0
BuildRequires: typelib(Vte) = 2.91
BuildRequires: typelib(Wnck) = 3.0

%add_perl_lib_path %_datadir/%name/lib
%add_perl_lib_path %_datadir/%name/lib/ex
%add_perl_lib_path %_datadir/%name/lib/edit
%add_findreq_skiplist %_datadir/%name/%name
%add_findreq_skiplist %_datadir/%name/lib/*.pm
%add_findreq_skiplist %_datadir/%name/lib/asbru_conn
%add_findreq_skiplist %_datadir/%name/utils/*.pl

Requires: perl(Crypt/Blowfish.pm)
Requires: perl(Crypt/CBC.pm)
Requires: perl(Crypt/Rijndael.pm)
Requires: perl(Encode.pm)
Requires: perl(Expect.pm)
Requires: perl(Gtk3.pm)
Requires: perl(Gtk3/SimpleList.pm)
Requires: perl(Net/ARP.pm)
Requires: perl(Net/Ping.pm)
Requires: perl(OSSP/uuid.pm)
Requires: perl(Socket6.pm)
Requires: perl(YAML.pm)

%description
%summary

%prep
%setup
%autopatch -p1

%build

%install
install -Dpm 0755 asbru-cm %buildroot%_bindir/%name
install -Dpm 0644 res/asbru-cm.desktop %buildroot%_desktopdir/%name.desktop
install -Dpm 0644 res/asbru-cm.1 %buildroot%_man1dir/%name.1
install -Dpm 0644 res/asbru_bash_completion %buildroot%_datadir/bash-completion/completions/%name

install -Dpm 0644 res/asbru-logo-24.png %buildroot%_iconsdir/hicolor/24x24/apps/%name.png
install -Dpm 0644 res/asbru-logo-64.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -Dpm 0644 res/asbru-logo-256.png %buildroot%_iconsdir/hicolor/256x256/apps/%name.png
install -Dpm 0644 res/asbru-logo.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

install -Dpm 0644 res/*.{png,pl,glade,svg} -t %buildroot%_datadir/%name/res/
mkdir -p %buildroot%_datadir/%name/{res/themes,utils}
cp -a res/themes/* %buildroot%_datadir/%name/res/themes
cp -a utils/*.pl %buildroot%_datadir/%name/utils

mkdir %buildroot%_datadir/%name/lib
cp -a lib/* %buildroot%_datadir/%name/lib

mv %buildroot%_bindir/%name %buildroot%_datadir/%name/%name
ln -s ../share/%name/%name %buildroot%_bindir/%name

%files
%doc README.md
%_bindir/%{name}*
%_man1dir/%{name}*
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_datadir/bash-completion/completions/*

%changelog
* Thu Jul 04 2024 Andrey Cherepanov <cas@altlinux.org> 6.4.0-alt1
- Initial build for Sisyphus.
