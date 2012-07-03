Name: i3
Version: 4.2
Release: alt1.3

Summary: I3 window manager
License: BSD-like
Group: Graphical desktop/Other

URL: http://i3wm.org/
Source: %name-%version.tar
Source1: alt.i3.config
Source2: i3-logo.png
Patch: %name-alt-desktop.patch

Packager: %packager

# Automatically added by buildreq on Sat Apr 14 2012
BuildRequires: asciidoc-a2x flex libXcursor-devel libev-devel libpcre-devel libstartup-notification-devel libxcbutil-devel libyajl-devel

%package devel
Summary: Development file for IPC interface of i3 window manager
Summary(ru_RU.UTF-8): Заголовочный файл для программ, использующих IPC интерфейс менеджера окон i3
Group: Development/C
Requires: %name = %version-%release glibc-devel

%description
i3 is a tiling window manager, completely written from scratch. It is
UTF-8 clean, supports more flexible layouts than column-based approach
used by other window managers, implements different modes, like vim.
The IPC interface for other programs is supported. This interface
can be more lightweight than 9P filesystem used in wmii.
Last but not least, i3 uses xcb as far as possible for speed and code
clearness.

%description -l ru_RU.UTF-8
i3 - это мозаичный менеджер окон, написанный с учётом большого
опыта использования и модификации wmii. i3 полностью поддерживает
кодировку UTF-8. Он позволяет значительно более гибко располагать
окна, нежели колоночные оконные менеджеры; реализует IPC интерфейс
для подключения других программ; использует xcb для ясности
кода и быстродействия.

%description devel
This package includes file that is required for creating C programs
that can interact with i3 window manager via it's IPC.

%description -l ru_RU.UTF-8 devel
Этот пакет содержит заголовочный файл в котором описан интерфейс
для взаимодействия с менеджером окон i3 из программ на C.


%prep
%setup -n %name-%version
%patch0 -p1

%build
%make

# Сжимаем страницы руководств
cd man
bzip -9 *.1

%install
make DESTDIR=%buildroot install

#%%ifarch x86_64
#install -d %buildroot%_libdir
#mv %buildroot%_libexecdir/*.so %buildroot%_libdir/
#%%endif

%define i3dir /etc/i3

# Копируем пиктограмму с сайта i3.
install -pm644 -D %SOURCE2 %buildroot%_niconsdir/i3.png

# Добавляем запись в WMsession.d
mkdir -p %buildroot/etc/X11/wmsession.d
cat >%buildroot/etc/X11/wmsession.d/13i3 <<EOF
NAME=i3
ICON=%_niconsdir/i3.png
DESC=%summary
EXEC=%_bindir/i3
SCRIPT:
exec %_bindir/i3
EOF

# Файл .desktop для менеджера окон не нужен, потому, что запускать оконный менеджер
# из меню другого оконного менеджера несколько странно.
# install -pm644 -D %name.xsession.desktop %buildroot%_desktopdir/%name.desktop

# Раскладываем документацию по каталогам.
# Всё, за исключением *.dia и Makefile.
%define docdir %_docdir/%name-%version

mkdir -p %buildroot%docdir/{html,refcard}
install -pm644 docs/*.html %buildroot%docdir/html/
install -pm644 docs/*.png %buildroot%docdir/html/
install -pm644 docs/{debugging,hacking-howto,ipc,multi-monitor,testsuite,userguide,wsbar} %buildroot%docdir
install -pm644 docs/refcard.* %buildroot%docdir/refcard

# Устанавливаем страницы руководств.
mkdir -p %buildroot%_man1dir
install -pm644 man/i3*.1.bz2 %buildroot%_man1dir/

# Копируем альтернативную конфигурацию в каталог документации.
install -pm644 -D %SOURCE1 %buildroot%docdir/

%files

%%doc %docdir
%%config %i3dir/
%_bindir/*
%_man1dir/*
%config /etc/X11/wmsession.d/13i3
%_niconsdir/i3.png

%files devel
%_includedir/*

%changelog
* Wed May 23 2012 Andrey Bergman <vkni@altlinux.org> 4.2-alt1.3
- Removed useless .desktop file.

* Tue May 15 2012 Andrey Bergman <vkni@altlinux.org> 4.2-alt1.2
- Corrected desktop file.

* Fri Apr 27 2012 Andrey Bergman <vkni@altlinux.org> 4.2-alt1.1
- Corrected name of desktop file.

* Fri Apr 27 2012 Andrey Bergman <vkni@altlinux.org> 4.2-alt1
- Version update.

* Sat Apr 14 2012 Andrey Bergman <vkni@altlinux.org> 4.1.2-alt1.3
- Added devel package.

* Sat Apr 14 2012 Andrey Bergman <vkni@altlinux.org> 4.1.2-alt1.2
- Added icon.

* Sat Apr 14 2012 Andrey Bergman <vkni@altlinux.org> 4.1.2-alt1.1
- Added alternative configuration file.

* Sat Apr 14 2012 Andrey Bergman <vkni@altlinux.org> 4.1.2-alt1
- Initial release for Sisyphus.

