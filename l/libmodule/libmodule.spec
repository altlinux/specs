%define abiversion 5

Name: libmodule
Version: 5.0.1
Release: alt1

Summary: A simple and elegant implementation of the C actor library
Summary(ru_RU.UTF-8): Простая и элегантная реализация библиотеки C акторов

License: MIT
Group: Development/C
Url: https://github.com/FedeDP/libmodule

# Source-url: https://github.com/FedeDP/libmodule/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires(pre): rpm-macros-cmake

%description
Libmodule offers a small and simple implementation of the C actor library
that allows developers to easily and elegantly create modular C projects.
A module is an Actor that can also listen for socket events.

%description -l ru_RU.UTF-8
Libmodule предлагает небольшую и простую реализацию библиотеки акторов C,
которая позволяет разработчикам легко и элегантно создавать модульные
проекты C. Module - это Актор, который может прослушивать события сокета.


%package -n %name%abiversion
Summary: A simple and elegant implementation of the C actor library
Summary(ru_RU.UTF-8): Простая и элегантная реализация библиотеки C акторов
Group: System/Libraries

%description -n %name%abiversion
Libmodule offers a small and simple implementation of the C actor library
that allows developers to easily and elegantly create modular C projects.
A module is an Actor that can also listen for socket events.

%description -n %name%abiversion -l ru_RU.UTF-8
Libmodule предлагает небольшую и простую реализацию библиотеки акторов C,
которая позволяет разработчикам легко и элегантно создавать модульные
проекты C. Module - это Актор, который может прослушивать события сокета.


%package devel
Summary: Development files for the %name of the C library
Summary(ru_RU.UTF-8): Файлы разработки для %name библиотеки C
Group: Development/C
Requires: %name%abiversion = %EVR

%description devel
Header files for developing actors of the C-library %name.

%description devel -l ru_RU.UTF-8
Заголовочные файлы для разработки акторов C-библиотеки %name.


%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

# This license is included in the general license package and does not require separate packaging.
rm -I %buildroot%_datadir/licenses/%name/LICENSE

%files -n %name%abiversion
%doc README.md
%_libdir/%name.so.%abiversion
%_libdir/%name.so.%abiversion.*

%files devel
%_includedir/module/*
%_libdir/%name.so
%_datadir/pkgconfig/%name.pc

%changelog
* Fri Sep 16 2022 Evgeny Chuck <koi@altlinux.org> 5.0.1-alt1
- new version (5.0.1) with rpmgs script
- initial build for ALT Linux Sisyphus
