%define rtai 0
%set_verify_elf_method unresolved=relaxed
Name: linuxcnc
Version: 2.7.5
Release: alt1

Summary: LinuxCNC controls CNC machines
Summary(ru_RU.UTF-8): Программа управления ЧПУ станков
License: GPLv2+ and LGPLv2
Group: Engineering
#Url: linuxcnc.org/
Url: https://github.com/LinuxCNC/linuxcnc

Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar
Patch1: fix_install-alt.patch
BuildPreReq: gcc-c++ imake libGL-devel libGLU-devel libXaw-devel libXinerama-devel libXmu-devel libXt-devel libncurses-devel libreadline-devel pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(libgnomeprintui-2.2) pkgconfig(libmodbus) pkgconfig(libudev) pkgconfig(libusb-1.0) python-devel tcl-devel tk-devel xorg-cf-files kmod bwidget tcl-img tclx python-modules-tkinter python-module-lxml boost-python-devel ImageMagick-tools xsltproc groff procps psmisc graphviz dblatex docbook-xsl netcat texlive-lang-cyrillic texlive-lang-french texlive-lang-spanish texlive-lang-german asciidoc-a2x source-highlight ghostscript-utils

Requires: python-module-%name = %version
Requires: tcl-%name = %version
Requires: %name-doc = %version
Requires: %name-data = %version
Requires: lib%name = %version

%description
LinuxCNC is software that runs on Linux, on most standard PCs, that can
interpret G-code and run a CNC machine. It was originally developed on a
milling machine, but support was added for lathes and many other types of
machine. It can be used with mills, lathes, plasma cutters, routers, robots,
and so on. 

%description -l ru_RU.UTF-8
LinuxCNC это программа, которая работает на ОС Linux на большинстве стандартных
ПК, которые могут интерпретировать G-код и запустить станок с ЧПУ. Изначально он
был разработан для фрезерного станка, но поддержка была добавлена и для токарных
станков и многих других типов машин. Он может быть использован с токарными
станками, станками плазменной резки, маршрутизаторами, роботами, и так далее.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Development files for %name

%package data
Summary: Data files for %name
Buildarch: noarch
Group: Engineering

%description data
Data files for %name

%package -n lib%name
Summary: Library for %name
Group: Engineering

%description -n lib%name
Library for %name

%package doc
Summary: Documementation for %name
Buildarch: noarch
Group: Documentation

%description doc
Documementation for %name

%package doc-fr
Summary: French documementation for %name
Buildarch: noarch
Group: Documentation
Requires: %name-doc = %version

%description doc-fr
French documementation for %name

%package doc-es
Summary: Spanish documementation for %name
Buildarch: noarch
Group: Documentation
Requires: %name-doc = %version

%description doc-es
Spanish documementation for %name

%package -n tcl-%name
Summary: Tcl files for %name
Group: Development/Tcl
Provides: tcl(Hal) tcl(Linuxcnc) tcl(Ngcgui)
%description -n tcl-%name
Tcl files for %name

%package -n python-module-%name
Summary: Python modules for %name
Group: Development/Python
Provides: python2.7(emccanon) python2.7(interpreter)
#%%add_findreq_skiplist %python_sitelibdir/*.so
#%%add_findprov_skiplist %python_sitelibdir/*.so

%description -n python-module-%name
Python modules for %name

%prep
%setup -n %name-%version
%patch1 -p1

%build
pushd src
%autoreconf
%configure --enable-build-documentation=pdf \
           --enable-non-distributable=yes\
           %if %rtai==1
           --with-realtime=/patch/to/rtai
           %else
           --with-realtime=uspace
           %endif
           
%make_build
popd

%install
pushd src
%makeinstall_std SITEPY=%python_sitelibdir
popd

%if %rtai==1
    mv %buildroot%_sysconfdir/init.d/* %buildroot%_initdir
%else
    rm -fR %buildroot%_sysconfdir/init.d/*
%endif

install -d -m755 %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc.desktop %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc-latency.desktop %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc-pncconf.desktop %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc-stepconf.desktop %buildroot%_desktopdir

#fix desktop categories
sed 's/X-CNC/Development;Engineering/' -i %buildroot%_desktopdir/*

### == desktop file documentation
cat>%buildroot%_desktopdir/%name-documentation.desktop<<END
[Desktop Entry]
Name=LinuxCNC Documentation
Name[ru_RU]= Документация LinuxCNC 
Comment=LinuxCNC Documentation
Comment[ru_RU]=Документация LinuxCNC
Exec=%_bindir/xdg-open %_docdir/%name
Icon=linuxcncicon
Terminal=false
Type=Application
Categories=Development;Engineering;
END

#install rules
install -d -m755 %buildroot%_udevrulesdir
cp debian/extras/lib/udev/rules.d/* %buildroot%_udevrulesdir

for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps
	convert linuxcncicon.png -resize $x'x'$x \
	        %buildroot%_iconsdir/hicolor/$x'x'$x/apps/linuxcncicon.png
done
%find_lang %name
%find_lang gmoccapy

%files -f %name.lang 
%_bindir/*
%_libexecdir/%name
%_sysconfdir/%name
%if_with %rtai
%_initdir/realtime
%endif
%_udevrulesdir/*.rules
%_desktopdir/*.desktop
%exclude %_desktopdir/%name-documentation.desktop
%_sysconfdir/X11/app-defaults/*
%_datadir/axis/tcl
%_datadir/%name/hallib
%_datadir/%name/ncfiles

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/*.a

%files data -f gmoccapy.lang
%_datadir/%name
%exclude %_datadir/%name/hallib
%exclude %_datadir/%name/ncfiles
%dir %_datadir/axis
%_datadir/axis/images
%_datadir/glade3
%_datadir/gmoccapy
%_datadir/gscreen
%_datadir/gtksourceview-2.0/*
%_liconsdir/*
%_niconsdir/*
%_miconsdir/*
%_mandir/man?/*

%files doc
%_desktopdir/%name-documentation.desktop
%dir %_docdir/%name
%_docdir/%name/*
%exclude %_docdir/%name/*_??.pdf

%files doc-fr
%_docdir/%name/*_fr.pdf

%files doc-es
%_docdir/%name/*_es.pdf

%files -n python-module-%name
%python_sitelibdir/*

%files -n tcl-%name
%dir %_libexecdir/tcltk/
%_libexecdir/tcltk/%name

%files devel
%_includedir/%name
%_libdir/*.so

%changelog
* Fri Jul 22 2016 Anton Midyukov <antohami@altlinux.org> 2.7.5-alt1
- New version 2.7.5
- Fix repocop warning.

* Thu May 12 2016 Anton Midyukov <antohami@altlinux.org> 2.7.4-alt1.20160506.1
- Initial build for Alt Linux Sisyphus.
