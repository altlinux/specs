%define _unpackaged_files_terminate_build 1

%define cname TreeSheets

Name: treesheets
Version: 16035416413
Release: alt1

Summary: Free Form Data Organizer
License: Zlib
Group: Office
Url: https://strlen.com/treesheets/
VCS: https://github.com/aardappel/treesheets

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libwxBase3.2-devel

%description
TreeSheets is a "hierarchical spreadsheet" that is a great replacement
for spreadsheets, mind mappers, outliners, PIMs, text editors and small
databases.

Suitable for any kind of data organization, such as todo lists,
calendars, project management, brainstorming, organizing ideas,
planning, requirements gathering, presentation of information, etc.

It's like a spreadsheet, immediately familiar, but much more suitable
for complex data because it's hierarchical. It's like a mind mapper,
but more organized and compact. It's like an outliner, but in more than
one dimension. It's like a text editor, but with structure.

%prep
%setup
sed -i "s|Categories=.*|Categories=Office;Calendar;Chart;ProjectManagement;Spreadsheet;WordProcessor;|" platform/linux/com.strlen.TreeSheets.desktop

%build
%cmake \
       -Wno-dev \
       -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_INSTALL_PREFIX=%_prefix \
       -DGIT_WXWIDGETS_SUBMODULES=OFF \
       -DTREESHEETS_WITH_STATIC_WXWIDGETS=OFF
%cmake_build

%install
%cmake_install

mkdir -p %buildroot/%_miconsdir
mkdir -p %buildroot/%_niconsdir
cp -v %buildroot/%_datadir/%cname/images/icon16.png %buildroot/%_miconsdir/%{cname}.png
cp -v %buildroot/%_datadir/%cname/images/icon32.png %buildroot/%_niconsdir/%{cname}.png

%find_lang %name --all-name

%files -f %{name}.lang
%doc README.md TODO.txt ZLIB_LICENSE.txt
%_bindir/%cname
%_desktopdir/*%{cname}.desktop
%_miconsdir/%{cname}*.*
%_niconsdir/%{cname}*.*
%_iconsdir/hicolor/scalable/apps/*%{cname}.svg
%dir %_datadir/%cname
%_datadir/%cname/*
%dir %_datadir/doc/%cname
%_datadir/doc/%cname/*
%_datadir/mime/packages/*%{cname}.xml

%changelog
* Thu Jul 03 2025 Nikolay Strelkov <snk@altlinux.org> 16035416413-alt1
- Initial build for Sisyphus
