%define _unpackaged_files_terminate_build 1
%def_with gui

Name: ansifilter
Version: 2.23
Release: alt1
Summary: ANSI terminal escape code converter
Group: Text tools
License: GPL-3.0-only
URL: http://www.andre-simon.de
VCS: https://gitlab.com/saalen/ansifilter

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++
%if_with gui
BuildRequires(pre): rpm-macros-qt6
BuildRequires: qt6-base-devel
%endif

%description
Ansifilter handles text files containing ANSI terminal escape codes.
The command sequences may be stripped or be interpreted to generate
formatted output (HTML, RTF, TeX, LaTeX, BBCode, Pango).

%if_with gui
%package gui
Summary: Qt GUI for %name
Group: Text tools
Requires: %name = %EVR

%description gui
%summary.
%endif

%prep
%setup
%autopatch -p1

%build
%make_build

%if_with gui
pushd src/qt-gui
%qmake_qt6 %name-gui.pro
%make_build
popd
%endif

%install
%makeinstall_std %{?_with_gui:install-gui}

%files
%doc %_docdir/%name
%_bindir/%name
%_man1dir/*.1.*
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%if_with gui
%files gui
%_bindir/%name-gui
%_desktopdir/%name.desktop
%_pixmapsdir/%name.xpm
%endif

%changelog
* Thu Aug 20 2026 Valery Zabrovsky <brow@altlinux.org> 2.23-alt1
- Initial build for ALT Sisyphus.
