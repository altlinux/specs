%define codemirror_ver 5.3.0

Summary:	A Linux clone of Notepad++
Name:		notepadqq
Version:	0.50.6
Release:	alt1
License:	GPLv3
Group:		Editors
URL:		http://notepadqq.altervista.org/wp/
Source0:	https://github.com/notepadqq/notepadqq/archive/%{name}-%{version}.tar.gz
Source1:	https://github.com/notepadqq/CodeMirror/archive/CodeMirror-%{codemirror_ver}.tar.gz

Patch:		%name-alt-no-qtchooser.patch

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
%setup -q -a 1
%patch -p2

# (tpg) install CodeMirror
mv -f CodeMirror-%{codemirror_ver}/* src/editor/libs/codemirror
mkdir -p src/editor/libs/codemirror/mode/m4

# (tpg) fix libdir
sed -i -e "s/lib/%{_lib}/g" src/ui/ui.pro

%build
%qmake_qt5 PREFIX=%_prefix *.pro
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
* Sat Feb 27 2016 Andrey Cherepanov <cas@altlinux.org> 0.50.6-alt1
- New version

* Sat Feb 27 2016 Andrey Cherepanov <cas@altlinux.org> 0.50.4-alt1
- Initial build to Sisyphus (thanks OpenMandriva for spec)

* Thu Dec 17 2015 Crispin Boylan <crisb@mandriva.org> 0.50.4-1
- (93178b5) 0.50.4


