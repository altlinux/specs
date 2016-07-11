Name: jreen
Version: 1.2.1
Release: alt1
Epoch: 7

Summary: Free and Opensource Jabber library, written in C++ using cross-platform framework Qt.
Summary(ru_RU.UTF-8): Открытая и свободная Jabber-библиотека, написанная на C++ с использованием кросс-платформенного фреймворка Qt.
License: GPLv2+
Group: System/Libraries

URL: http://qutim.org/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://codeload.github.com/euroelessar/%name/tar.gz/v%version
Source: %name-%version.tar.gz
Patch0: %name-%version-qt56-alt.patch

BuildRequires: cmake
BuildRequires: libgsasl-devel
BuildRequires: libqt4-webkit-devel
BuildRequires: libspeex-devel
BuildRequires: phonon-devel
BuildRequires: qt4-designer
BuildRequires: qt5-base-devel

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

%package -n lib%name-qt5
Summary: Free and Opensource Jabber library, written in C++ using cross-platform framework Qt.
Summary(ru_RU.UTF-8): Открытая и свободная Jabber-библиотека, написанная на C++ с использованием кросс-платформенного фреймворка Qt.
Group: System/Libraries

%description -n lib%name-qt5
Jreen - Free and Opensource Jabber library, written in C++ using cross-platform framework Qt. Licensed under the GNU/GPL version 2.

Advantages over other Jabber/XMPP libraries: 
- Easy to extend architecture
- Easy to learn and support
- Very fast

%description -l ru_RU.UTF-8 -n lib%name-qt5
Jreen - Открытая и свободная Jabber-библиотека, написанная на C++ с использованием кросс-платформенного фреймворка Qt. Распространяется под лицензией GNU/GPL версии 2.

Преимущества перед другими Jabber/XMPP библиотеками: 
- Легко расширяемая архитектура
- Лёгкий в освоении и поддержке
- Очень быстрый

%package -n lib%name-qt5-devel
Summary: Free and Opensource Jabber library, written in C++ using cross-platform framework Qt.
Summary(ru_RU.UTF-8): Открытая и свободная Jabber-библиотека, написанная на C++ с использованием кросс-платформенного фреймворка Qt.
Group: Development/C++
Requires: lib%name-qt5 = %version-%release

%description -n lib%name-qt5-devel
Jreen - Free and Opensource Jabber library, written in C++ using cross-platform framework Qt. Licensed under the GNU/GPL version 2.

Advantages over other Jabber/XMPP libraries: 
- Easy to extend architecture
- Easy to learn and support
- Very fast

%description -l ru_RU.UTF-8 -n lib%name-qt5-devel
Jreen - Открытая и свободная Jabber-библиотека, написанная на C++ с использованием кросс-платформенного фреймворка Qt. Распространяется под лицензией GNU/GPL версии 2.

Преимущества перед другими Jabber/XMPP библиотеками: 
- Легко расширяемая архитектура
- Лёгкий в освоении и поддержке
- Очень быстрый

%prep
%setup
%patch0 -p1

%build
# Build Qt4 version
mkdir -p %_target_platform-qt4
pushd %_target_platform-qt4
 
cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DGSASL_INCLUDE_DIRS:PATH=%_includedir \
	-DJREEN_FORCE_QT4:BOOL=TRUE \
	-Wno-dev
popd

%make_build -C %_target_platform-qt4

# Build Qt5 version
mkdir -p %_target_platform-qt5
pushd %_target_platform-qt5
 
cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DGSASL_INCLUDE_DIRS:PATH=%_includedir \
	-Wno-dev
popd

%make_build -C %_target_platform-qt5
 
%install
# Install Qt4 version
%makeinstall_std -C %_target_platform-qt4

# Install Qt5 version
%makeinstall_std -C %_target_platform-qt5

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%_pkgconfigdir/lib%name.pc
%dir %_includedir/%name-qt4
%dir %_includedir/%name-qt4/%name
%_includedir/%name-qt4/%name/*.h
%dir %_includedir/%name-qt4/%name/experimental
%_includedir/%name-qt4/%name/experimental/*.h

%files -n lib%name-qt5
%_libdir/lib%name-qt5.so.*

%files -n lib%name-qt5-devel
%_libdir/lib%name-qt5.so
%_pkgconfigdir/lib%name-qt5.pc
%dir %_includedir/%name-qt5
%dir %_includedir/%name-qt5/%name
%_includedir/%name-qt5/%name/*.h
%dir %_includedir/%name-qt5/%name/experimental
%_includedir/%name-qt5/%name/experimental/*.h

%changelog
* Mon Jul 11 2016 Nazarov Denis <nenderus@altlinux.org> 7:1.2.1-alt1
- Version 1.2.1

* Thu Sep 18 2014 Nazarov Denis <nenderus@altlinux.org> 7:1.2.0-alt1
- Version 1.2.0
- Add Qt5 version

* Sun Feb 23 2014 Nazarov Denis <nenderus@altlinux.org> 7:1.1.1-alt0.M70P.1
- Build for branch p7

* Thu Feb 20 2014 Nazarov Denis <nenderus@altlinux.org> 7:1.1.1-alt0.M70T.1
- Build for branch t7

* Tue Feb 18 2014 Nazarov Denis <nenderus@altlinux.org> 7:1.1.1-alt1
- Version 1.1.1
- Separate package
