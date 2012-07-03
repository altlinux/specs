Name: sigil
Version: 0.4
Release: alt1

Summary: Sigil is a free, open source, multi-platform WYSIWYG ebook editor
Summary(ru_RU.UTF-8): Сигиль есть свободный, открытый, многоплатформенный Вицивиговый книгоправщик
License: GPLv3
Group: Editors
Url: http://code.google.com/p/sigil/
Packager: Malo Skryleve <malo@altlinux.org>

Source: %name-%version.tar.bz2

Requires: qt4 >= 4.7 libqt4-xml libqt4-svg libqt4-webkit
BuildPreReq: cmake >= 2.8.0 libqt4-devel >= 4.7
BuildRequires: cmake gcc-c++ libqt4-devel libqt4-svg libqt4-webkit libqt4-xmlpatterns

%description
Sigil is a free, open source, multi-platform WYSIWYG ebook editor.
It is designed to edit books in ePub format. The version of the package
can be found in the ChangeLog.txt file.

%description -l ru_RU.UTF-8
Сигиль есть свободный, открытый, многоплатформенный Вицивиговый
книгоправщик. Он разработан для правки книг в формате ePub. Версия же
набора может быть обретена в файле ChangeLog.txt.

%prep
%setup

%build
mkdir build
cd build
cmake -G "Unix Makefiles" \
	-DCMAKE_INSTALL_PREFIX=%_prefix \
%if %_lib == lib64
        -DLIB_SUFFIX=64 \
%endif
	-DCMAKE_BUILD_TYPE=Release %_builddir/%name-%version \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_BUILD_TYPE="Release" \
	-DCMAKE_SKIP_RPATH=YES

%make_build VERBOSE=1

%install
pushd build
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

%changelog
* Thu Aug 18 2011 Malo Skryleve <malo@altlinux.org> 0.4-alt1
- Imported version sigil 0.4

* Sat Feb 19 2011 Malo Skryleve <malo@altlinux.org> 0.3.4-alt1
- initial build for ALT Linux Sisyphus

