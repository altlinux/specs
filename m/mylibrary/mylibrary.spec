%define _unpackaged_files_terminate_build 1

Name:    mylibrary
Version: 3.2
Release: alt1

Summary: Home librarian
License: GPL-3.0
Group:   Office
Url:     https://github.com/ProfessorNavigator/mylibrary

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gtkmm-4.0)
BuildRequires: pkgconfig(poppler-cpp)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(ddjvuapi)

%description
MyLibrary is a simple program for managing .fb2, .epub, .pdf and .djvu
e-book file collections. It can also work with same formats packed in
zip, 7z, jar, cpio, iso, tar, tar.gz, tar.bz2, tar.xz, rar (see notes)
archives itself or  packed in same types of archives with .fbd files
(epub, djvu and pdf books).
MyLibrary creates own database and does not change files content, names
or location.

%prep
%setup
%patch -p1
chmod -x ru.mail.bobilev_yury.MyLibrary.desktop

%build
%cmake -DCMAKE_BUILD_TYPE=release
%cmake_build

%install
%cmake_install
rm -v %{buildroot}%{_datadir}/MyLibrary/COPYING

%find_lang %name --all-name

%files -f %name.lang
%doc COPYING *.md
%_bindir/%name
%dir %{_datadir}/MyLibrary/
%{_datadir}/MyLibrary/*
%{_datadir}/applications/ru.mail.bobilev_yury.MyLibrary.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Wed Feb 19 2025 Nikolay Strelkov <snk@altlinux.org> 3.2-alt1
- New version 3.2.

* Tue Feb 04 2025 Nikolay Strelkov <snk@altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus
