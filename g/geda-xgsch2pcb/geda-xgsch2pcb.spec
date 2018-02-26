Name: geda-xgsch2pcb
Version: 0.1.2
Release: alt1.3.1

Summary: xgsch2pcb
License: GPL
Group: Development/Other
Url: http://geda.seul.org/

Packager: Alexander Gvozdev <gab@altlinux.ru>

Source0: %name-%version.tar.gz

BuildRequires: python python-module-pygtk python-module-pygobject python-module-dbus perl-XML-Parser desktop-file-utils
####%%%%Requires: dbus-tools-gui

%description
Graphic wrapper for gsch2pcb. This is a easy way to forward notation and syncronization from schematic to pcb.

%description -l ru_RU.UTF-8
Графический враппер для программы gsch2pcb. Облегчает поцесс синхронизации принципиальной схемы с разводкой печатной платы.


%set_verify_elf_method textrel=relaxed, unresolved=relaxed

%prep
%setup -q

##%patch0 -p1

%build
%undefine __libtoolize
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files -n %name
%_bindir/*
%_libdir/%name/*.pyc
%_libdir/%name/*.pyo
%_libdir/%name/*.py
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/48x48/apps/geda-xgsch2pcb.png
%_datadir/icons/hicolor/scalable/apps/geda-xgsch2pcb.svg

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt1.3.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.3
- Rebuilt with python 2.6

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1.2.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for geda-xgsch2pcb
 * update_menus for geda-xgsch2pcb

* Wed Feb 20 2008 Alexander Gvozdev <gab@altlinux.ru> 0.1.2-alt1.2
- Remove unneeded file "mimeinfo.cache"

* Sat Jan 12 2008 Alexander Gvozdev <gab@altlinux.ru> 0.1.2-alt1
- New version in upstream

* Sat Jan 5 2008 Alexander Gvozdev <gab@altlinux.ru> 0.1.1-alt1
- Initial build

