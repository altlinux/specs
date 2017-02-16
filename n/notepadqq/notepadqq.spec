Summary:	A Linux clone of Notepad++
Name:		notepadqq
Version:	1.0.1
Release:	alt1
License:	GPLv3
Group:		Editors
URL:		http://notepadqq.altervista.org/wp/
Source0:	%name-%version.tar
Source1:	codemirror.tar

BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-webkit-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-svg-devel

Requires:       qt5-translations

%description
Notepadqq is a Notepad++-like editor for the Linux desktop.

%prep
%setup -q
tar xf %SOURCE1
mkdir -p src/editor/libs/codemirror/mode/m4

# (tpg) fix libdir
sed -i -e "s/lib/%{_lib}/g" src/ui/ui.pro

%build
%configure --qmake=qmake-qt5 --lrelease=lrelease-qt5
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

# (tpg) bug #1136
ln -sf %_libdir/notepadqq/notepadqq-bin %buildroot%_bindir/notepadqq-bin

%files
%doc README.md CONTRIBUTORS.md
%_bindir/notepadqq*
%_libdir/notepadqq/notepadqq-bin
%_datadir/applications/notepadqq.desktop
%_iconsdir/hicolor/*/apps/notepadqq.*g
%_datadir/notepadqq

%changelog
* Thu Feb 16 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- new version 1.0.1

* Fri Oct 07 2016 Andrey Cherepanov <cas@altlinux.org> 0.53.0-alt1
- New vesion

* Sun May 29 2016 Andrey Cherepanov <cas@altlinux.org> 0.51.0-alt1
- New version

* Sat Feb 27 2016 Andrey Cherepanov <cas@altlinux.org> 0.50.6-alt1
- New version

* Sat Feb 27 2016 Andrey Cherepanov <cas@altlinux.org> 0.50.4-alt1
- Initial build to Sisyphus (thanks OpenMandriva for spec)

* Thu Dec 17 2015 Crispin Boylan <crisb@mandriva.org> 0.50.4-1
- (93178b5) 0.50.4


