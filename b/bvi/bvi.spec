Name: bvi
Version: 1.4.0
Release: alt1

Summary: Display-oriented editor for binary files
License: GPLv2+
Group: Editors

Url: https://bvi.sourceforge.net/
Packager: Artem Kurashov <saahriktu@altlinux.org>
Source: %name-%version.tar

BuildRequires: libncurses-devel

%description
The bvi is a display-oriented editor for binary files, based
on the vi text-editor. If you are familiar with vi, just start
the editor and begin to edit! A bmore program is also
included in the package.

%prep
%setup
# Fix the path of the bmore.help file specified in the man page :
sed -i "s@/usr/local/share/bmore.help@%_datadir/%name/bmore.help@" bmore.1

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc README COPYING CREDITS CHANGES
%_bindir/%name
%_bindir/bmore
%_bindir/bvedit
%_bindir/bview
%_datadir/%name/
%_man1dir/*.1*

%changelog
* Fri May 05 2023 Artem Kurashov <saahriktu@altlinux.org> 1.4.0-alt1
- Initial package
