Name: sigil
Version: 0.6.1
Release: alt1

Summary: Sigil is a free, open source, multi-platform WYSIWYG ebook editor
Summary(ru_RU.UTF-8): Сигиль есть свободный, открытый, многоплатформенный Вицивиговый книгоправщик
License: GPLv3
Group: Editors
Url: http://code.google.com/p/sigil/

Source: %name-%version.tar.bz2

BuildPreReq: rpm-macros-cmake
BuildRequires: cmake >= 2.8.0 libqt4-devel >= 4.8 gcc-c++ libFlightCrew-devel  zlib-devel libhunspell-devel libpcre-devel
BuildRequires:  boost-devel boost-filesystem-devel boost-program_options-devel boost-datetime-devel boost-regex-devel boost-thread-devel boost-system-devel
%description
Sigil is a free, open source, multi-platform WYSIWYG ebook editor.
It is designed to edit books in ePub format. The version of the package
can be found in the ChangeLog.txt file.

%description -l ru_RU.UTF-8
Сигиль есть свободный, открытый, многоплатформенный Вицивиговый
книгоправщик. Он разработан для правки книг в формате ePub. Версия же
набора может быть обретена в файле ChangeLog.txt.

%prep
%setup -q

%build
%cmake
cd BUILD
%make_build

%install
pushd BUILD
%makeinstall_std
popd
%find_lang %name
mkdir -p %buildroot%_liconsdir
mv %buildroot%_pixmapsdir/*.png %buildroot%_liconsdir/

%files
%doc INSTALL.txt README.txt ChangeLog.txt
%_bindir/*
%_desktopdir/*.desktop
%_liconsdir/*.png
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Mon Dec 03 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.1-alt1
- new version

* Thu Aug 18 2011 Malo Skryleve <malo@altlinux.org> 0.4-alt1
- Imported version sigil 0.4

* Sat Feb 19 2011 Malo Skryleve <malo@altlinux.org> 0.3.4-alt1
- initial build for ALT Linux Sisyphus

