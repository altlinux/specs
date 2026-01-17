%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: qlogexplorer
Version: 1.1.2
Release: alt1

Summary: Advanced and fast log explorer with support to JSON files and columns
License: GPL-3.0-only
Group: Text tools
Url: https://github.com/rafaelfassi/qlogexplorer/wiki
VCS: https://github.com/rafaelfassi/qlogexplorer

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)

%description
%summary. Features:

1. Very fast and can handle huge files

The file is not loaded into memory, but indexed by chunks. It allows a
very fast loading, as well as low memory consumption, even when a large
file is opened. QLogExplorer also allows to browser the file and to start
searching even when the file is still being indexed.

2. No locks whatsoever

A monitoring applications shall never interfere with the process that is
generating/managing the logs, therefore the process must be able to
delete, move or compress the log files without getting any denied
operation due the monitoring application is reading it. QLogExplorer
never interferes in the log management process.

3. Supports JSON log files

QLogExplorer completely supports that kind of log format.

4. Templates

Different systems may have different kind of log info, so a template can
be created for each kind of log, having: Columns definition, Highlighters
definition, Predefined search parameters.

5. Advanced search

The search allows multi-parameters where the parameters can be combined
by AND or OR operators. Each parameter can:

* Have the search expression as SubString, Regex or Range.
* Be limited to a specific column.
* Use the negation operator.

%prep
%setup
sed -i "s|Categories=.*|Categories=GTK;Utility;TextTools;FileTools;|" packaging/linux/xdg/applications/qlogexplorer.desktop
sed -i "s|screenshots/||" README.md

%build
%cmake
%cmake_build

%install
%cmake_install

mkdir -pv %buildroot%_datadir
cp -arv packaging/linux/xdg/* %buildroot%_datadir

%files
%doc README.md screenshots/main.png
%_bindir/qlogexplorer
%_desktopdir/qlogexplorer.desktop
%_iconsdir/hicolor/*/apps/qlogexplorer.png
%_iconsdir/hicolor/scalable/apps/qlogexplorer.svg
%_datadir/metainfo/qlogexplorer.appdata.xml

%changelog
* Sat Jan 17 2026 Nikolay Strelkov <snk@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus
