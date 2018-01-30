%def_with docs
%def_without static
%set_verify_elf_method unresolved=relaxed
Name: linuxcnc
Version: 2.7.12
Release: alt1

Summary: LinuxCNC controls CNC machines
Summary(ru_RU.UTF-8): Программа управления ЧПУ станков
License: GPLv2+ and LGPLv2
Group: Engineering
Url: https://github.com/LinuxCNC/linuxcnc

Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar
Patch: fix_build_with_libmodbus3.1.4.patch
Patch1: fix-dir-path.patch
Buildrequires(pre): rpm-build-tcl rpm-build-python
# Automatically added by buildreq on Thu Feb 02 2017
# optimized out: ImageMagick-tools asciidoc boost-python-headers dblatex docbook-dtds fontconfig fontconfig-devel fonts-type1-urw ghostscript-classic glib2-devel groff-base libGL-devel libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel libart_lgpl-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgnomecanvas-devel libgnomeprint-devel libgpg-error libgtk+2-devel libncurses-devel libpango-devel libstdc++-devel libtinfo-devel libwayland-client libwayland-server libxml2-devel perl pkg-config python-base python-devel python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python-modules-xml sysvinit-utils tcl tcl-devel tex-common texlive-base texlive-base-bin texlive-bibtex-extra texlive-common texlive-fonts-recommended texlive-generic-recommended texlive-latex-base texlive-latex-extra texlive-latex-recommended texlive-pictures texlive-xetex tk xml-common xorg-xproto-devel xsltproc zlib-devel
BuildRequires: boost-devel-headers boost-python-devel bwidget gcc-c++ libstdc++-devel imake kmod libGLU-devel libXaw-devel libXinerama-devel libgnomeprintui-devel libmodbus-devel libreadline-devel libudev-devel libusb-devel python-modules-tkinter python-modules-unittest tcl-img tclx time tk-devel xorg-cf-files
BuildRequires: pkgconfig(pygtk-2.0)
BuildRequires: intltool
%if_with docs
BuildPreReq: asciidoc-a2x ghostscript-common ghostscript-utils source-highlight graphviz groff-ps
%endif
BuildPreReq: desktop-file-utils ImageMagick-tools 

%if_with docs
Requires: %name-doc = %version
%endif

Requires: %name-data = %version
Requires: lib%name = %version
%py_requires gtk.glade
%add_tcl_req_skip Hal
%add_tcl_req_skip Linuxcnc
%add_tcl_req_skip Ngcgui
%add_python_req_skip emccanon
%add_python_req_skip interpreter

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

%package -n liblinuxcnc-devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description -n liblinuxcnc-devel
Development files for %name

%package -n liblinuxcnc-devel-static
Summary: Static version of linuxcnc libraries
Group: Development/C++
Requires: %name-devel = %version-%release

%description -n liblinuxcnc-devel-static
Static version of linuxcnc libraries

%package data
Summary: Data files for %name
Buildarch: noarch
Group: Engineering
Conflicts: linuxcnc-doc < 2.7.12

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

%prep
%setup
%patch -p1
%patch1 -p1

#fix make install
sed 's/ -o root//g' -i src/Makefile

%build
pushd src
%autoreconf
%configure  --enable-non-distributable=yes \
            --with-realtime=uspace \
            %if_with docs
            --enable-build-documentation=pdf \
            %endif

%make_build
popd

%install
pushd src
%makeinstall_std
popd

install -d -m755 %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc.desktop %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc-latency.desktop %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc-pncconf.desktop %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc-stepconf.desktop %buildroot%_desktopdir

#fix desktop Name
pushd %buildroot%_desktopdir
sed 's/Name=/Name=LinuxCNC /g' -i linuxcnc-pncconf.desktop \
    linuxcnc-stepconf.desktop linuxcnc-latency.desktop
popd

#fix desktop categories
desktop-file-install --dir %buildroot%_desktopdir \
        --remove-key=Version \
        --remove-category=X-CNC \
        --add-category=Development \
        --add-category=Engineering \
        %buildroot%_desktopdir/*.desktop

### == desktop file documentation
cat>%buildroot%_desktopdir/%name-documentation.desktop<<END
[Desktop Entry]
Name=LinuxCNC Documentation
Name[ru_RU]= LinuxCNC Документация 
Exec=%_bindir/xdg-open %_docdir/%name
Icon=linuxcncicon
Terminal=false
Type=Application
Categories=Development;Engineering;
END

#install rules
mkdir -p %buildroot%_udevrulesdir
cp debian/extras/lib/udev/rules.d/* %buildroot%_udevrulesdir

# convert and install icon files
for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps
    convert linuxcncicon.png -resize $x'x'$x \
            %buildroot%_iconsdir/hicolor/$x'x'$x/apps/linuxcncicon.png
done

#fix uncompressed manual pages
pushd %buildroot%_mandir
xz `find -name *.?`
popd

%find_lang %name gmoccapy --output=%name.lang

%files
%_bindir/*
%_libexecdir/%name
%_sysconfdir/%name
%_initdir/realtime
%_udevrulesdir/*.rules
%_desktopdir/*.desktop
%_sysconfdir/X11/app-defaults/*
%_datadir/axis
%exclude %_datadir/axis/images
%_datadir/%name/hallib
%_datadir/%name/ncfiles
%dir %_libexecdir/tcltk
%_libexecdir/tcltk/%name
%python_sitelibdir/*

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/*.a

%files -n lib%name-devel
%_includedir/%name
%_libdir/*.so

%if_with static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files data -f %name.lang
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
%_docdir/%name
%if_with docs
%exclude %_docdir/%name/*.pdf
%endif

%if_with docs
%files doc
%_docdir/%name/*.pdf
%exclude %_docdir/%name/*_??.pdf

%files doc-fr
%_docdir/%name/*_fr.pdf

%files doc-es
%_docdir/%name/*_es.pdf
%endif

%changelog
* Tue Jan 30 2018 Anton Midyukov <antohami@altlinux.org> 2.7.12-alt1
- new version 2.7.12
- Fix pathdir

* Wed Aug 30 2017 Anton Midyukov <antohami@altlinux.org> 2.7.11-alt1
- New version 2.7.11
- Added missing requires 

* Sun Jul 30 2017 Anton Midyukov <antohami@altlinux.org> 2.7.10-alt2
- Fix desktop categories.

* Tue Jul 25 2017 Anton Midyukov <antohami@altlinux.org> 2.7.10-alt1
- new version 2.7.10

* Sun Jun 11 2017 Anton Midyukov <antohami@altlinux.org> 2.7.9-alt1
- New version 2.7.9
- Remove fix_build_for_i586.patch

* Fri Mar 24 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.7.8-alt1.qa1
- Rebuilt against Tcl/Tk 8.6

* Sat Feb 04 2017 Anton Midyukov <antohami@altlinux.org> 2.7.8-alt1
- New version 2.7.8
- Fix build with libmodbus3.1.4
- Fix build for i586
- Remove subpackage python-module-linuxcnc and tcl-linuxcnc

* Fri Jul 22 2016 Anton Midyukov <antohami@altlinux.org> 2.7.5-alt1
- New version 2.7.5
- Fix repocop warning.

* Thu May 12 2016 Anton Midyukov <antohami@altlinux.org> 2.7.4-alt1.20160506.1
- Initial build for Alt Linux Sisyphus.
