%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define cname TreeSheets

Name: treesheets
Epoch: 1
Version: 3048
Release: alt1

Summary: Free Form Data Organizer
License: Zlib
Group: Office
Url: https://strlen.com/treesheets/
VCS: https://github.com/aardappel/treesheets

Source: %name-%version.tar

Patch: use-packaged-wx.patch

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
%patch -p1
sed -i "s|Categories=.*|Categories=Office;Calendar;Chart;ProjectManagement;Spreadsheet;WordProcessor;|" platform/linux/com.strlen.TreeSheets.desktop

%build
%cmake \
       -Wno-dev \
       -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_INSTALL_PREFIX=%_prefix \
       -DENABLE_LOBSTER=off
%cmake_build

%install
%cmake_install

mkdir -p %buildroot/%_miconsdir
mkdir -p %buildroot/%_niconsdir
cp -v %buildroot/%_datadir/%cname/images/icon16.png %buildroot/%_miconsdir/%{cname}.png
cp -v %buildroot/%_datadir/%cname/images/icon32.png %buildroot/%_niconsdir/%{cname}.png
cp -v %buildroot/%_datadir/doc/TreeSheets/examples/tutorial.cts %buildroot/%_datadir/doc/TreeSheets/examples/tutorial-en.cts

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
%_datadir/metainfo/*%{cname}.metainfo.xml

%changelog
* Sat Mar 28 2026 Nikolay Strelkov <snk@altlinux.org> 1:3048-alt1
- New version 3048.

* Sat Mar 21 2026 Nikolay Strelkov <snk@altlinux.org> 1:3047-alt1
- New version 3047.

* Fri Mar 20 2026 Nikolay Strelkov <snk@altlinux.org> 1:3044-alt1
- New version 3044.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 1:3039-alt1
- New version 3039.

* Wed Mar 04 2026 Nikolay Strelkov <snk@altlinux.org> 1:3021-alt1
- New version 3021.

* Sun Mar 01 2026 Nikolay Strelkov <snk@altlinux.org> 1:3019-alt1
- New version 3019.

* Sat Feb 28 2026 Nikolay Strelkov <snk@altlinux.org> 1:3014-alt1
- New version 3014.

* Wed Feb 25 2026 Nikolay Strelkov <snk@altlinux.org> 1:3005-alt1
- New version 3005.

* Sun Feb 22 2026 Nikolay Strelkov <snk@altlinux.org> 1:3002-alt1
- New version 3002.

* Fri Feb 20 2026 Nikolay Strelkov <snk@altlinux.org> 1:2992-alt1
- New version 2992.

* Tue Feb 17 2026 Nikolay Strelkov <snk@altlinux.org> 1:2991-alt1
- New version 2991.

* Sun Feb 15 2026 Nikolay Strelkov <snk@altlinux.org> 1:2989-alt1
- New version 2989.

* Fri Feb 13 2026 Nikolay Strelkov <snk@altlinux.org> 1:2983-alt1
- New version 2983.

* Sun Feb 08 2026 Nikolay Strelkov <snk@altlinux.org> 1:2975-alt1
- New version 2975.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 1:2967-alt1
- New version 2967.

* Sat Jan 31 2026 Nikolay Strelkov <snk@altlinux.org> 1:2960-alt1
- New version numbering, updated to 2960.
- Enable build on loongarch64 and riscv64.

* Fri Jan 30 2026 Nikolay Strelkov <snk@altlinux.org> 16035416413-alt2
- Exclude loongarch64 and riscv64 arches as not buildable.

* Thu Jul 03 2025 Nikolay Strelkov <snk@altlinux.org> 16035416413-alt1
- Initial build for Sisyphus
