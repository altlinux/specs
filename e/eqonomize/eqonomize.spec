%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: eqonomize
Version: 1.5.11
Release: alt1

Summary: personal accounting software for the small household economy
License: GPL-2.0-or-later
Group: Graphical desktop/KDE
Url: https://github.com/Eqonomize/Eqonomize

Source: %name-%version.tar

BuildRequires: qt6-base-devel
BuildRequires: /usr/bin/lrelease-qt6

%description
Eqonomize! is a personal accounting software for KDE, with focus on efficiency
and ease of use for the small household economy. It provides a complete
solution, with bookkeeping by double entry and support for scheduled recurring
transactions, security investments, and budgeting. It gives a clear overview
of past and present transactions, and development of incomes and expenses,
with descriptive tables and charts, as well as an approximation of future
account values.

%package doc
Summary: documentation for the Eqonomize! accounting software
Group: Documentation
BuildArch: noarch

%description doc
Eqonomize! is a personal accounting software for KDE, with focus on efficiency
and ease of use for the small household economy.

This package contains the Eqonomize! Handbook.

%prep
%setup

%build
lrelease-qt6 Eqonomize.pro
qmake-qt6 \
          PREFIX=%_prefix \
          CONFIG+=nostrip \
          QMAKE_CXXFLAGS="%optflags" \
          Eqonomize.pro

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%find_lang %name --with-qt

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README.md
%_bindir/eqonomize
%_desktopdir/eqonomize.desktop
%dir %_datadir/eqonomize
%_datadir/eqonomize/currencies.xml
%dir %_datadir/eqonomize/translations
%_iconsdir/hicolor/*/*/*
%_man1dir/eqonomize.1.*
%_datadir/mime/packages/eqonomize.xml

%files doc
%doc budget.eqz eqz_file_format
%dir %_datadir/doc/eqonomize
%dir %_datadir/doc/eqonomize/html
%dir %_datadir/doc/eqonomize/html/C
%_datadir/doc/eqonomize/html/C/*

%changelog
* Sat Nov 29 2025 Nikolay Strelkov <snk@altlinux.org> 1.5.11-alt1
- Initial build for Sisyphus
