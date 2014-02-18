Name: jreen
Version: 1.1.1
Release: alt1
Epoch: 7

Summary: Free and Opensource Jabber library, written in C++ using cross-platform framework Qt.
Summary(ru_RU.UTF-8): Открытая и свободная Jabber-библиотека, написанная на C++ с использованием кросс-платформенного фреймворка Qt.
License: GPLv2+
Group: System/Libraries

URL: http://qutim.org/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: http://qutim.org/dwnl/44/lib%name-%version.tar.bz2
Patch0: %name-%version-alt-cmake-macros.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libqca2-devel
BuildRequires: libqt4-sql-mysql
BuildRequires: libspeex-devel
BuildRequires: phonon-devel

%description
Jreen - Free and Opensource Jabber library, written in C++ using cross-platform framework Qt. Licensed under the GNU/GPL version 2.

Advantages over other Jabber/XMPP libraries: 
- Easy to extend architecture
- Easy to learn and support
- Very fast

%description -l ru_RU.UTF-8
Jreen - Открытая и свободная Jabber-библиотека, написанная на C++ с использованием кросс-платформенного фреймворка Qt. Распространяется под лицензией GNU/GPL версии 2.

Преимущества перед другими Jabber/XMPP библиотеками: 
- Легко расширяемая архитектура
- Лёгкий в освоении и поддержке
- Очень быстрый

%package -n lib%name
Summary: Free and Opensource Jabber library, written in C++ using cross-platform framework Qt.
Summary(ru_RU.UTF-8): Открытая и свободная Jabber-библиотека, написанная на C++ с использованием кросс-платформенного фреймворка Qt.
Group: System/Libraries

%description -n lib%name
Jreen - Free and Opensource Jabber library, written in C++ using cross-platform framework Qt. Licensed under the GNU/GPL version 2.

Advantages over other Jabber/XMPP libraries: 
- Easy to extend architecture
- Easy to learn and support
- Very fast

%description -l ru_RU.UTF-8 -n lib%name 
Jreen - Открытая и свободная Jabber-библиотека, написанная на C++ с использованием кросс-платформенного фреймворка Qt. Распространяется под лицензией GNU/GPL версии 2.

Преимущества перед другими Jabber/XMPP библиотеками: 
- Легко расширяемая архитектура
- Лёгкий в освоении и поддержке
- Очень быстрый

%package -n lib%name-devel
Summary: Free and Opensource Jabber library, written in C++ using cross-platform framework Qt.
Summary(ru_RU.UTF-8): Открытая и свободная Jabber-библиотека, написанная на C++ с использованием кросс-платформенного фреймворка Qt.
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Jreen - Free and Opensource Jabber library, written in C++ using cross-platform framework Qt. Licensed under the GNU/GPL version 2.

Advantages over other Jabber/XMPP libraries: 
- Easy to extend architecture
- Easy to learn and support
- Very fast

%description -l ru_RU.UTF-8 -n lib%name-devel
Jreen - Открытая и свободная Jabber-библиотека, написанная на C++ с использованием кросс-платформенного фреймворка Qt. Распространяется под лицензией GNU/GPL версии 2.

Преимущества перед другими Jabber/XMPP библиотеками: 
- Легко расширяемая архитектура
- Лёгкий в освоении и поддержке
- Очень быстрый

%prep
%setup -n lib%name-%version
%patch0 -p1

%build
%define lib_suffix %nil
%ifarch x86_64
%define lib_suffix 64
%endif

mkdir -p %_target_platform
pushd %_target_platform
 
cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DLIB_SUFFIX=%lib_suffix \
	-DCMAKE_BUILD_TYPE:STRING=Release
popd

%make_build -C %_target_platform
 
%install
%makeinstall_std -C %_target_platform

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%_pkgconfigdir/lib%name.pc
%dir %_includedir/%name
%_includedir/%name/*.h
%dir %_includedir/%name/experimental
%_includedir/%name/experimental/*.h

%changelog
* Tue Feb 18 2014 Nazarov Denis <nenderus@altlinux.org> 7:1.1.1-alt1
- Version 1.1.1
- Separate package
