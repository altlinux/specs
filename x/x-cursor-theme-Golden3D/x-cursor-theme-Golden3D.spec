%define themename Golden
%define themename3d %{themename}3D
%define contentnum 5507

Name: x-cursor-theme-%themename3d
Version: 0.8
Release: alt1

Summary: Animated 3D cursors for XFree86
Summary(ru_RU.CP1251): Анимированные 3D-курсоры для XFree86

License: LGPL
Group: System/XFree86
BuildArch: noarch

Url: http://kde-look.org/content/show.php?content=%contentnum
Source: %contentnum-%themename-XCursors-3D-%version.tar.bz2

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

%description
This package contains animated 3D cursors for XFree86. There are (in
separate packages) blue, silver and golden versions of these cursors.

%description -l ru_RU.CP1251
Этот пакет содержит анимированные 3D-курсоры для XFree86. Существуют
(в разных пакетах) голубой, золотой и серебряный варианты этих курсоров.

%prep
%setup -q -n %themename-XCursors-3D-%version

%build
%__mv Gold %themename3d
%__subst 's,Gold,%themename3d,' default/index.theme

%install
%__install -d %buildroot%_iconsdir/
%__cp -a %themename3d/ %buildroot%_iconsdir/

%files
%_iconsdir/%themename3d
%doc README default/index.theme

%changelog
* Sun Aug 08 2004 Andrey Rahmatullin <wrar@altlinux.ru> 0.8-alt1
- initial build