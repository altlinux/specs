Name: sudoku
Version: 1.0
Release: alt1
Summary: Classic Sudoku game
License: Apache-2.0
Group: Games/Other

Url: https://github.com/ali-begic/sudoku
Vcs: https://github.com/ali-begic/sudoku.git

Source: %name-%version.tar
Patch: %name-%version-fix-install-path.patch

BuildRequires(pre): rpm-macros-qt6
BuildRequires: qt6-base-devel

%description
A classic Sudoku game built with Qt.
It features a modern interface and easy-to-use functionality.

%prep
%setup
%autopatch -p1

%build
%qmake_qt6 src/sudoku.pro
%make_build

%install
%makeinstall INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%{_bindir}/%{name}/

%changelog
* Tue Mar 18 2025 Vitaly Churkin <chur1q@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
