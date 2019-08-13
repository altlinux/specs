Name: manpageeditor
Version: 0.1.3
Release: alt1

Summary: Manpages editor
Summary(ru_RU.UTF-8): Редактор man-страниц

License: GPLv3
Group: Development/Tools
Url: https://github.com/KeithDHedger/ManPageEditor

Packager: Grigory Ustinov <grenka@altlinux.org>

Source: %name-%version.tar

# Automatically added by buildreq on Mon Aug 12 2019
# optimized out: fontconfig fontconfig-devel glib2-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libpango-devel libstdc++-devel pkg-config python-base python-modules python3 python3-base
BuildRequires: gcc-c++ groff-base libxcb-devel libgtksourceview-devel unzip libaspell-devel aspell aspell-en

%description
Create, edit, import, preview man-pages.

%description -l ru_RU.UTF-8
Создание, редактирование, импорт и предпросмотр man-страниц.

%prep
%setup

%build
%configure --enable-aspell
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog INSTALL README BUGS-ETC
%_bindir/*
%_datadir/ManPageEditor
%_datadir/applications/ManPageEditor.desktop
%_datadir/icons/hicolor/256x256/apps/ManPageEditor.png
%_datadir/pixmaps/ManPageEditor.png
%_man1dir/*

%changelog
* Tue Aug 13 2019 Grigory Ustinov <grenka@altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus (Closes: #37100).
