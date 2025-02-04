Name: klauslang
Version: 2.6.0
Release: alt1
Summary: Klaus programming language and environment
Summary(ru_RU.UTF-8): Клаус - язык программирования и среда разработки

License: GPL-3.0+
Group: Education
Url: https://gitflic.ru/project/czaerlag/klauslang
Vcs: https://gitflic.ru/project/czaerlag/klauslang.git

ExclusiveArch: x86_64

# https://gitflic.ru/project/czaerlag/klauslang/file/downloadAll?format=tar.bz2&branch=v%version
Source: %name-%version.tar

BuildRequires: fpc >= 3.2.2
BuildRequires: fpc-src
BuildRequires: libgtk+2-devel
BuildRequires: lazarus >= 3.4
BuildRequires: rsync

%description
Klaus is a Russian-based educational programming language,
development environment and a set of training courses
for schoolchildren and students.

%description -l ru_RU.UTF-8
Клаус - язык программирования по-русски, среда разработки
и набор учебных курсов для школьников и студентов.

%package -n %name-teacher
Summary: Klaus training course editor
Summary(ru_RU.UTF-8): Клаус - редактор учебных курсов
Group: Education
Requires: klauslang = %version

%description -n %name-teacher
Klaus training course editor - for teachers and methodologists.
Practicum task soultions source code.

%description -n %name-teacher -l ru_RU.UTF-8
Редактор учебных курсов Клаус - для учителей и методистов.
Исходный код решений задач Практикума.

%prep
%setup

%build
cd ./installer
./compile.sh Linux

%install
cd ./installer
./install.sh %name %buildroot %_libdir %_bindir %_datadir
./install.sh %name-teacher %buildroot %_libdir %_bindir %_datadir
cd ..
ln -sf ../%_lib/%name/amd64/klaus %buildroot%_bindir/klaus
ln -sf ../%_lib/%name/amd64/klaus-ide %buildroot%_bindir/klaus-ide
ln -sf ../%_lib/%name/amd64/klaus-course-edit %buildroot%_bindir/klaus-course-edit

%files -n %name
%_libdir/%name/amd64/klaus
%_libdir/%name/amd64/klaus-ide
%_bindir/klaus
%_bindir/klaus-ide
%_libdir/%name/samples/*
%_libdir/%name/test/*
%_libdir/%name/doc/*
%_libdir/%name/practicum/*.klaus-course
%_libdir/%name/what-s-new.txt
%_desktopdir/klaus-ide.desktop
%_datadir/mime/packages/%name-mime.xml
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_iconsdir/hicolor/scalable/apps/*
%_iconsdir/hicolor/scalable/mimetypes/*
%_iconsdir/hicolor/16x16/mimetypes/*
%_iconsdir/hicolor/32x32/mimetypes/*
%_iconsdir/hicolor/48x48/mimetypes/*

%files -n %name-teacher
%_libdir/%name/amd64/klaus-course-edit
%_bindir/klaus-course-edit
%_libdir/%name/practicum/*.zip
%_desktopdir/klaus-course-edit.desktop
%_datadir/mime/packages/%name-teacher-mime.xml

%changelog
* Sun Feb 02 2025 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- New version.

* Tue Jan 28 2025 Andrey Cherepanov <cas@altlinux.org> 2.5.9-alt1
- Initial build from src.rpm by Konstantin Zakharoff.
