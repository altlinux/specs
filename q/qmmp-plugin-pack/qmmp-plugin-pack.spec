%define		branch 0.6
%define		svn svn2810

Version:	%branch.0
Name:		qmmp-plugin-pack
Release:	alt1.%svn
Summary:	Plugin pack is a set of extra plugins for Qmmp.
Summary(ru_RU.UTF8): Набор дополнительных модулей для Qmmp.
Summary(uk_UA.UTF8): Набір додаткових модулів для Qmmp.
License:	GPLv2
Group:		Sound
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://qmmp.ylsoftware.com/plugins_en.php
Source0:	%name-%version-svn.tar.bz2


BuildRequires:	cmake >= 2.4.8 gcc-c++ libmpg123-devel libqmmp-devel >= 0.6.0 libtag-devel >= 1.6 yasm

%description
Plugin pack is a set of extra plugins for Qmmp.

Plugins List
 - MPG123 - MPEG v1/2 layer1/2/3 decoder using of libmpg123 library
 - FFap - enhanced Monkey's Audio (APE) decoder (24-bit samples and embedded cue support)
 - Qmmp Simple Ui (QSUi) - simple user interface based on standard widgets set

%description -l ru_RU.UTF8
Набор дополнительных модулей для Qmmp.

Список модулей
 - MPG123 - декодер MPEG v1/2 layer1/2/3 с использованием библиотеки libmpg123
 - FFap - улучшенный декодер Monkey's Audio (APE) (поддержка 24-х бит и встроенного cue)
 - Qmmp Simple Ui (QSUi) - простой пользовательский интерфейс с использованием стандартных элементов

%description -l uk_UA.UTF8
Набір додаткових модулів для Qmmp.

Перелік модулів
 - MPG123 - декодер MPEG v1/2 layer1/2/3 з використанням бібліотеки libmpg123
 - FFap - покращений декодер Monkey's Audio (APE) (підтримка 24-х біт та вбудованого cue)
 - Qmmp Simple Ui (QSUi) - простий інтерфейс користувача з використанням стандартних елементів

%package -n %name-in-mpg123
Summary: MPG123 - MPEG v1/2 layer1/2/3 decoder using of libmpg123 library
Summary(ru_RU.UTF8): MPG123 - декодер MPEG v1/2 layer1/2/3 с использованием библиотеки libmpg123
Summary(uk_UA.UTF8): MPG123 - декодер MPEG v1/2 layer1/2/3 з використанням бібліотеки libmpg123
Group: Sound
Requires: qmmp >= %version-%release

%description -n %name-in-mpg123
MPG123 - MPEG v1/2 layer1/2/3 decoder using of libmpg123 library for Qmmp.

%description -l ru_RU.UTF8 -n %name-in-mpg123
MPG123 - декодер MPEG v1/2 layer1/2/3 с использованием библиотеки libmpg123 для Qmmp.

%description -l uk_UA.UTF8 -n %name-in-mpg123
MPG123 - декодер MPEG v1/2 layer1/2/3 з використанням бібліотеки libmpg123 для Qmmp.

%package -n %name-in-ffap
Summary: FFap - enhanced Monkey's Audio (APE) decoder (24-bit samples and embedded cue support)
Summary(ru_RU.UTF8): FFap - улучшенный декодер Monkey's Audio (APE) (поддержка 24-х бит и встроенного cue)
Summary(uk_UA.UTF8): FFap - покращений декодер Monkey's Audio (APE) (підтримка 24-х біт та вбудованого cue)
Group: Sound
Requires: qmmp >= %version-%release

%description -n %name-in-ffap
FFap - enhanced Monkey's Audio (APE) decoder (24-bit samples and embedded cue support) for Qmmp.

%description -l ru_RU.UTF8 -n %name-in-ffap
FFap - улучшенный декодер Monkey's Audio (APE) (поддержка 24-х бит и встроенного cue) для Qmmp.

%description -l uk_UA.UTF8 -n %name-in-ffap
FFap - покращений декодер Monkey's Audio (APE) (підтримка 24-х біт та вбудованого cue) для Qmmp.

%package -n %name-qsui
Summary: Qmmp Simple Ui - simple user interface based on standard widgets set
Summary(ru_RU.UTF8): Qmmp Simple Ui - простой пользовательский интерфейс с использованием стандартных элементов
Summary(uk_UA.UTF8): Qmmp Simple Ui - простий інтерфейс користувача з використанням стандартних елементів
Group: Sound
Requires: qmmp >= %version-%release

%description -n %name-qsui
Qmmp Simple Ui - simple user interface based on standard widgets set for Qmmp.

%description -l ru_RU.UTF8 -n %name-qsui
Qmmp Simple Ui - простой пользовательский интерфейс с использованием стандартных элементов для Qmmp.

%description -l uk_UA.UTF8 -n %name-qsui
Qmmp Simple Ui - простий інтерфейс користувача з використанням стандартних елементів для Qmmp.

%prep
%setup -q -n %name-%version-svn

%build
# # with CMake
# #cmake \
# #	-DCMAKE_INSTALL_PREFIX=%prefix \
# #	-DCMAKE_CXX_FLAGS:STRING="%optflags -fPIC" \
# #	-DCMAKE_C_FLAGS:STRING="%optflags -fPIC" \
# #	-DLIB_DIR:STRING=%_lib

# # with QMake
export PATH=$PATH:%_qt4dir/bin
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" LIB_DIR=/%_lib %name.pro
%make_build VERBOSE=1

%install
# # with CMake
# #%make DESTDIR=%buildroot install

# # with QMake
%make INSTALL_ROOT=%buildroot%prefix install

%files -n %name-in-mpg123
%_libdir/qmmp/Input/libmpg123.so

%files -n %name-in-ffap
%_libdir/qmmp/Input/libffap.so

%files -n %name-qsui
%_libdir/qmmp/Ui/libqsui.so

%changelog
* Mon Jul 16 2012 Motsyo Gennadi <drool@altlinux.ru> 0.6.0-alt1.svn2810
- initial build for ALT Linux
