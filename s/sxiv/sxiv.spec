Name: sxiv
Version: 1.32
Release: alt1

Summary: Simple X Image Viewer
License: GPLv2
Group: Graphics
Url: https://github.com/muennich/sxiv

Packager: %packager
Source: %name-%version.tar

# Automatically added by buildreq on Sun Mar 22 2015
# optimized out: imlib2 libX11-devel libcloog-isl4 xorg-xproto-devel
BuildRequires: imlib2-devel libexif-devel libgif-devel

%add_findreq_skiplist %_datadir/%name/exec/key-handler

%description
sxiv is an alternative to feh and qiv. Its only dependencies
besides xlib are imlib2, libexif and giflib. The primary goal
for writing sxiv is to create an image viewer, which only has
the most basic features required for fast image viewing.
It has vi key bindings and works nicely with tiling window managers.
Its code base should be kept small and clean to make it easy
for you to dig into it and customize it for your needs.

%description -l ru_RU.UTF-8
sxiv - это альтернатива просмотрщика изображений fex и qiv.
Он зависит лишь от xlib, imlib2, libexif и giflib. Основная
задача, которую решал автор sxiv - написание лёгкой программы
изображений, которая умеет лишь самое необходимое для быстрого
просмотра изображений. sxiv поддерживает клавиатурные соглашения
vi и прекрасно работает с мозаичными оконными менеджерами
(i3, awesome и т.д.). Автор sxiv старался писать исходные
тексты программы так, чтобы их было легко читать и модифицировать.

%prep
%setup -q

%build
%make

%install
%make PREFIX=%buildroot/usr install 

# Раскладываем документацию.
%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir/
install -pm644 {README.md,LICENSE} %buildroot%docdir/

%files
%_bindir/sxiv
%dir %_datadir/%name/
%dir %_datadir/%name/exec
%_datadir/%name/exec/image-info
%_datadir/%name/exec/key-handler
%_man1dir/*
%dir %docdir
%doc %docdir/*

%changelog
* Tue Dec 22 2015 Andrey Bergman <vkni@altlinux.org> 1.32-alt1
- Version update.

* Tue Mar 31 2015 Andrey Bergman <vkni@altlinux.org> 1.31-alt1.2
- Added skiplist.

* Sun Mar 22 2015 Andrey Bergman <vkni@altlinux.org> 1.31-alt1.1
- Added missed directories ownership.

* Sun Mar 22 2015 Andrey Bergman <vkni@altlinux.org> 1.31-alt1
- Initial version for Sisyphus.

