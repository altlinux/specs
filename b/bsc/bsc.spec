Name:		bsc
Version:	4.1.0
Release:	alt1

Summary:	BeeSoft Commander
License:	GPLv2
Group:		File tools
URL:		http://www.beesoft.org/
Packager:       Andrey Cherepanov <cas@altlinux.org>

Source0:	%{name}_%{version}_src.tar.gz
Source1:	%name.desktop
Patch:		%name.diff

BuildRequires:	gcc-c++, libqt4-devel

%description
Beesoft Commander is a two-panel file manager (like Norton Commander)
for Linux. He are using a Qt GUI-library.

User have possibility to use followed operations:
 * can change access rights to file(s) or directory (recursive too),
 * can view or edit files contents,
 * copy, move, delete, rename and pack file(s),
 * copy, move, delete, rename and pack directiories (recursive),
 * can change time stamp for files,
 * and many more...

%prep
%setup -q -n %{name}
cp %SOURCE1 .
%patch -p 0

%build
qmake-qt4
make 

%install
%makeinstall INSTALL_ROOT=%{buildroot}

%files
%doc licence.txt
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/BeesoftCommander.png

%changelog
* Mon Feb 07 2011 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1
- Initial build in Sisyphus
