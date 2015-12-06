Name: pcb
Version: 20140316
Release: alt1

Summary: PCB
License: GPL
Group: Development/Other
Url: http://ftp.geda-project.org/pcb/pcb-20140316/

Packager: barssc <barssc@altlinux.ru>

Source0: %name-%version.tar.gz

BuildRequires: gcc-c++ libX11-devel flex gtk+2 libgd2-devel libgd2 libdbus-devel libdbus libdbus-glib libdbus-glib-devel tk intltool libGL-devel libGLU-devel libgtkglext-devel
BuildRequires: libgtk+2-devel libgtk+2 libjpeg libjpeg-devel gd2-utils libpng-devel zlib-devel libXpm-devel libfreetype-devel perl-XML-Parser desktop-file-utils
Requires: dbus-tools-gui
Requires(post,postun): shared-mime-info >= 0.15-alt2

%description
PCB is a CAD (computer aided design) program for the physical
design of printed circuit boards. Schematic drawed in gEDA transfer to PCB with gsch2pcb command.
Narrowly, the transfer procces, editing and PNG/PS/GERBER generation described in documentation in pcb-doc package.

%description -l ru_RU.UTF-8
PCB - это САПР, предназначенный для создания печатных плат. Схема начерченная в программе gEDA переносится
в PCB с помощью программы gsch2pcb, входящей в состав gEDA. Подробно процесс переноса, дальнейшего редактирования и
получения PNG/PS/GERBER-файлов для отправки на производство описан в документации, входящей в пакет pcb-doc.

%package -n %name-doc
Summary: Documentation for PCB
Summary(ru_RU.UTF-8): Документация для PCB
License: GPL
Group: Development/Other
Requires: %name = %version-%release
BuildArch: noarch

%description -n %name-doc
This documentation narrates about PCB programm and pcb creation flow witn gEda and PCB.

%description -l ru_RU.UTF-8 -n %name-doc
Эта документация рассказывает о программе PCB и правильной последовательности создания печатных плат с помощью пакетов gEDA и PCB.

%package -n %name-examples
Summary: Examples for PCB
Summary(ru_RU.UTF-8): Примеры для PCB
License: GPL
Group: Development/Other
Requires: %name = %version-%release
BuildArch: noarch

%description -n %name-examples
Example of pcb created in PCB.

%description -l ru_RU.UTF-8 -n %name-examples
Пример разработанной в PCB печатной платы.

%package -n %name-library
Summary: Component library for PCB
Summary(ru_RU.UTF-8): Библиотеки компонентов для PCB
License: GPL
Group: Development/Other
Requires: %name = %version-%release
BuildArch: noarch

%description -n %name-library
Component library for PCB. Contains basic set of thru-hole and SMD components.
For example: TSSOP, SO, SOIC, MSOP, TQFP, LQFP and etc.

%description -l ru_RU.UTF-8 -n %name-library
Библиотека компонентов для PCB. Собержит базовый набор выводных и безвыводных компонентов.
В том числе: TSSOP, SO, SOIC, MSOP, TQFP, LQFP и т.д.

%set_verify_elf_method textrel=relaxed, unresolved=relaxed

%prep
%setup -q

%build
%configure	\
    --enable-doc \
    --enable-dbus \
    --disable-toporouter \
    --with-gui=gtk

%make_build

%install
%make DESTDIR=%buildroot install

%files -n %name
%_bindir/*
%_datadir/pcb/tools/*
%_datadir/pcb/*.sh
%_datadir/pcb/qfp-ui
%_datadir/pcb/qfp.dat
%_datadir/pcb/pcb-menu.res
%_datadir/pcb/gpcb-menu.res
%_datadir/pcb/default_font
%_datadir/icons/hicolor/16x16/mimetypes/*
%_datadir/icons/hicolor/22x22/mimetypes/*
%_datadir/icons/hicolor/24x24/mimetypes/*
%_datadir/icons/hicolor/32x32/mimetypes/*
%_datadir/icons/hicolor/48x48/mimetypes/*
%_datadir/icons/hicolor/48x48/apps/*
%_datadir/icons/hicolor/scalable/mimetypes/*
%_datadir/icons/hicolor/scalable/apps/*
%_datadir/mimelnk/application/*
%_datadir/mime/application/*
%_datadir/mime/packages/pcb.xml
%_datadir/locale/ru/*
%_datadir/gEDA/scheme/gnet-pcbfwd.scm
%_man1dir/*
%doc %_datadir/info/pcb*
%_desktopdir/pcb.desktop

%files -n %name-examples
%_datadir/doc/pcb/examples/*
%_datadir/doc/pcb/tutorial/*

%files -n %name-library
%_datadir/pcb/m4/*
%_datadir/pcb/newlib/*
%_datadir/pcb/pcblib-newlib/*
%_datadir/pcb/pcblib
%_datadir/pcb/pcblib.contents


%files -n %name-doc
%doc %_datadir/doc/%name/*html*
%doc %_datadir/doc/%name/*.png
%doc %_datadir/doc/%name/*.pdf


%changelog
* Sun Dec 6 2015 barssc <barssc@altlinux.ru> 20140316-alt1
- New version 20140316.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 20081128-alt4.1
- NMU: added BR: texinfo
- WARN: look orphaned: modern pcb has version 2014-03-17

* Wed Apr 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20081128-alt4
- fix build

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 20081128-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for pcb
  * postclean-05-filetriggers for spec file

* Sun Jun 28 2009 Alexander Gvozdev <gab@altlinux.ru> 20081128-alt3
- M4 component library moved in separate package.

* Wed Jun 17 2009 Alexander Gvozdev <gab@altlinux.ru> 20081128-alt2
- Remove conflicts with shared-mime-info (bug 20484).

* Sat Dec 6 2008 Alexander Gvozdev <gab@altlinux.ru> 20081128-alt1
- Checkout up to 20081128.

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 20080202-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for pcb

* Sat Feb 9 2008 Alexander Gvozdev <gab@altlinux.ru> 20080202-alt1
- Checkout up to 20080202.

* Thu Jan 3 2008 Alexander Gvozdev <gab@altlinux.ru> 20070912-alt1
- Detalize packet descriptions.

* Mon Mar 5 2007 Alexander Gvozdev <gab@altlinux.ru> 20070912-alt0
- Initial build
