Name: i3
Version: 4.21.1
Release: alt1

Summary: I3 window manager
License: BSD-like
Group: Graphical desktop/Other

URL: http://i3wm.org/
Source: %name-%version.tar
Source1: alt.i3.config
Source2: i3-logo.png

Packager: %packager

# It requires dmenu for launching programs (Ctrl-d keybinding)
Requires: dmenu

# Automatically added by buildreq on Tue Mar 03 2015
BuildRequires: libev-devel libpango-devel libpcre2-devel libstartup-notification-devel libxcbutil-cursor-devel libxcbutil-devel libxcbutil-icccm-devel libxcbutil-keysyms-devel libxkbcommon-x11-devel libyajl-devel libxcbutil-xrm-devel xmlto asciidoc meson ninja-build

# Добавлено вручную - автоматика, увы, не находит.
BuildRequires: perl-Pod-Parser perl-AnyEvent-I3

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

%build

mkdir build
cd build
meson --buildtype release -Ddocs=True -Dmans=True --prefix /usr ..
ninja

# Сжимаем страницы руководств
cd ../man
bzip -9 *.1

%install

mkdir -p %buildroot%_bindir

cd build
meson install --destdir %buildroot
cd ..

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
%define docdir %_docdir/%name

# Устанавливаем страницы руководств.
mkdir -p %buildroot%_man1dir
install -pm644 man/i3*.1.bz2 %buildroot%_man1dir/

# Копируем альтернативную конфигурацию в каталог документации.
install -pm644 -D %SOURCE1 %buildroot%docdir/

%files

%doc %docdir
%%config %i3dir/
%_bindir/*
%_man1dir/*
%config /etc/X11/wmsession.d/13i3
%_niconsdir/i3.png
%_datadir/xsessions/i3.desktop

%files devel
%_includedir/*

%changelog
* Sun Nov 06 2022 Andrey Bergman <vkni@altlinux.org> 4.21.1-alt1
- Version update

* Fri Oct 14 2022 Andrey Bergman <vkni@altlinux.org> 4.21-alt1
- Version update

* Sun Feb 06 2022 Andrey Bergman <vkni@altlinux.org> 4.20.1-alt1
- Version update

* Sat Feb 05 2022 Andrey Bergman <vkni@altlinux.org> 4.19-alt2
- Correct buildreq.

* Wed Nov 18 2020 Andrey Bergman <vkni@altlinux.org> 4.19-alt1
- Version update

* Wed Sep 30 2020 Andrey Bergman <vkni@altlinux.org> 4.18.2-alt1
- Version update

* Sun Jun 07 2020 Andrey Bergman <vkni@altlinux.org> 4.18.1-alt1
- Version update

* Sat Sep 21 2019 Andrey Bergman <vkni@altlinux.org> 4.17.1-alt2
- Add desktop file to xsessions.

* Wed Sep 04 2019 Andrey Bergman <vkni@altlinux.org> 4.17.1-alt1
- Version update

* Sun Aug 04 2019 Andrey Bergman <vkni@altlinux.org> 4.17-alt1
- Version update

* Sat Feb 02 2019 Andrey Bergman <vkni@altlinux.org> 4.16.1-alt1
- Version update

* Wed Nov 07 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.16-alt2
- fixed packaging on armh

* Mon Nov 05 2018 Andrey Bergman <vkni@altlinux.org> 4.16-alt1
- Version update

* Fri Mar 30 2018 Andrey Bergman <vkni@altlinux.org> 4.15-alt1
- Version update

* Fri Oct 13 2017 Andrey Bergman <vkni@altlinux.org> 4.14.1-alt1
- Version update

* Mon Dec 12 2016 Andrey Bergman <vkni@altlinux.org> 4.13-alt1
- Version update

* Sun Mar 06 2016 Andrey Bergman <vkni@altlinux.org> 4.12-alt1
- Version update

* Fri Oct 09 2015 Andrey Bergman <vkni@altlinux.org> 4.11-alt1
- Version update

* Thu Sep 10 2015 Andrey Bergman <vkni@altlinux.org> 4.10.4-alt1
- Version update

* Fri Aug 07 2015 Andrey Bergman <vkni@altlinux.org> 4.10.3-alt1
- Version update

* Fri Apr 17 2015 Andrey Bergman <vkni@altlinux.org> 4.10.2-alt1
- Version update

* Tue Mar 31 2015 Andrey Bergman <vkni@altlinux.org> 4.10.1-alt1
- Version update

* Sun Mar 22 2015 Andrey Bergman <vkni@altlinux.org> 4.9.1-alt1
- Version update

* Tue Mar 03 2015 Andrey Bergman <vkni@altlinux.org> 4.9-alt1
- Version update

* Mon Jun 16 2014 Andrey Bergman <vkni@altlinux.org> 4.8-alt1
- Version update

* Mon Jan 27 2014 Andrey Bergman <vkni@altlinux.org> 4.7.2-alt1
- Version update

* Sat Dec 28 2013 Andrey Bergman <vkni@altlinux.org> 4.7-alt1.1
- Added perl-Pod-Parser buildreq.

* Sat Dec 28 2013 Andrey Bergman <vkni@altlinux.org> 4.7-alt1
- Version update

* Tue Aug 27 2013 Andrey Bergman <vkni@altlinux.org> 4.6-alt1
- Version update

* Fri Apr 12 2013 Andrey Bergman <vkni@altlinux.org> 4.5.1-alt2
- Added dmenu to Requires

* Fri Apr 12 2013 Andrey Bergman <vkni@altlinux.org> 4.5.1-alt1
- Version update

* Fri Jan 18 2013 Andrey Bergman <vkni@altlinux.org> 4.4-alt3
- Added perl-Pod-Parser buildreq.

* Sat Dec 22 2012 Andrey Bergman <vkni@altlinux.org> 4.4-alt2
- Removed patch for .desktop file.

* Sat Dec 22 2012 Andrey Bergman <vkni@altlinux.org> 4.4-alt1
- Version update

* Sat Sep 29 2012 Andrey Bergman <vkni@altlinux.org> 4.3-alt1
- Version update

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

