%define wxbranch 3.1
%define wxversion %version-gtk2
%define wxrelease %(echo %wxversion |sed 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')
%define wxrelease_nodot %(echo %wxrelease |sed 's/\\.//g')
%define mfl WX_RELEASE=%wxrelease WX_RELEASE_NODOT=%wxrelease_nodot WX_VERSION=%wxversion

Name: wxGTK3.1-gtk2
Version: 3.1.0
Release: alt2.20160229

Summary: The GTK+ port of the wxWidgets library
License: wxWidgets License
Group: System/Libraries
Url: http://wxwidgets.org

Packager: Anton Midyukov <antohami@altlinux.org>

# https://github.com/wxWidgets/wxWidgets.git
Source: %name-%version.tar
Source2: ld_shared_wrapper.pl
Patch1: wxGTK3.0-disable-ABI-checking.patch
Patch2: wxGTK3.1-gtk2-fix-config.patch

# Automatically added by buildreq on Wed Dec 10 2008
BuildRequires: gcc-c++ libGL-devel libSDL-devel libSM-devel
BuildRequires: libXinerama-devel libesd-devel libexpat-devel
BuildRequires: libjpeg-devel libtiff-devel libgtk+2-devel

BuildPreReq: xorg-xextproto-devel xorg-inputproto-devel libXtst-devel
BuildPreReq: rpm-build-java libXxf86vm-devel libbfd-devel
BuildPreReq: libstdc++-devel gstreamer-devel gst-plugins-devel
BuildPreReq: libGConf-devel gst-plugins-devel libpng-devel
BuildPreReq: libnotify-devel libwebkitgtk2-devel libmspack-devel

%description
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs
(GTK+, Motif/LessTif, MS Windows, Mac) from the same source code.

This is a GTK+ port.

%package -n lib%name
Summary: The GTK+ port of the wxWidgets library
Group: System/Libraries

%description -n lib%name
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs
(GTK+, Motif/LessTif, MS Windows, Mac) from the same source code.

This is a GTK+ port.

%package -n lib%name-devel
Summary: Development files for wxGTK library
Group: Development/C++
Requires: lib%name = %version-%release
Requires: python-module-PyDSTool
%add_python_req_skip utils
Conflicts: libwxGTK2.9-devel
Conflicts: libwxGTK3.0-devel
Conflicts: libwxGTK3.1-devel
Conflicts: wxGTK-devel
Conflicts: libwxGTK-devel

%description -n lib%name-devel
Header files for wxGTK, the GTK+ port of the wxWidgets library.

%prep
%setup
%patch1 -p1
%patch2 -p1
%__subst "s,bakefile/presets,bakefile/presets-\$(WX_RELEASE),g" Makefile.in

rm -fR src/{expat,jpeg,tiff,zlib,png}

%build
CONF_FLAG="--enable-shared --without-debug_flag --without-debug_info"

./autogen.sh
sed 's/WX_RELEASE=.*/WX_RELEASE=%wxrelease/' -i configure
sed 's/WX_VERSION=.*/WX_VERSION=%wxversion/' -i configure
sed "s/WX_VERSION_TAG=.*/WX_VERSION_TAG=`echo WX\${lib_unicode_suffix}\${WX_LIB_FLAVOUR}_%(echo %wxrelease |sed 's/-.*//') | tr '[[a-z]]' '[[A-Z]]'`/" -i configure
GST_CFLAGS="$(pkg-config --cflags gstreamer-0.10)"
export LIBS="-lX11"
DEFS="-DUNICODE=1 -DwxUSE_UNICODE=1 -DwxDEBUG_LEVEL=0"
%add_optflags -fno-strict-aliasing $GST_CFLAGS $DEFS
%configure $CONF_FLAG \
	--with-sdl \
	--enable-unicode \
	--enable-optimise \
	--with-regex=yes \
	--disable-rpath \
	--without-subdirs \
	--without-odbc \
	--with-opengl \
	--disable-joystick \
	--enable-plugins \
	--enable-precomp-headers=yes \
	--enable-sound \
	--enable-soname \
	--enable-mediactrl \
	--enable-stc \
	--enable-gui \
	--with-xresources \
	--without-gnomeprint \
	--enable-graphics_ctx \
	--enable-utf8=yes \
	--enable-utf8only=no \
	--enable-nanox \
	--enable-intl \
	--enable-xlocale \
	--enable-config \
	--enable-protocols \
	--enable-ftp \
	--enable-http \
	--enable-stl \
	--enable-std_containers \
	--enable-std_iostreams \
	--enable-std_string \
	--enable-std_string_conv_in_wxstring \
	--enable-fileproto \
	--enable-sockets \
	--enable-ipv6 \
	--enable-dataobj \
	--enable-ipc \
	--enable-baseevtloop \
	--enable-epollloop \
	--enable-selectloop \
	--enable-any \
	--enable-arcstream \
	--enable-base64 \
	--enable-backtrace \
	--enable-catch_segvs \
	--enable-cmdline \
	--enable-datetime \
	--enable-debugreport \
	--enable-dynamicloader \
	--enable-exceptions \
	--enable-ffile \
	--enable-file \
	--enable-filehistory \
	--enable-filesystem \
	--enable-fontenum \
	--enable-fontmap \
	--enable-fs_archive \
	--enable-fs_inet \
	--enable-fsvolume \
	--enable-fswatcher \
	--enable-geometry \
	--enable-log \
	--enable-longlong \
	--enable-mimetype \
	--enable-printfposparam \
	--enable-snglinst \
	--enable-stdpaths \
	--enable-stopwatch \
	--enable-streams \
	--enable-sysoptions \
	--enable-tarstream \
	--enable-textbuf \
	--enable-textfile \
	--enable-timer \
	--enable-variant \
	--enable-zipstream \
	--enable-url \
	--enable-protocol \
	--enable-protocol-http \
	--enable-protocol-ftp \
	--enable-protocol-file \
	--enable-threads \
	--enable-docview \
	--enable-help \
	--enable-html \
	--enable-htmlhelp \
	--enable-xrc \
	--enable-aui \
	--enable-propgrid \
	--enable-ribbon \
	--enable-constraints \
	--enable-loggui \
	--enable-logwin \
	--enable-logdialog \
	--enable-mdi \
	--enable-mdidoc \
	--enable-richtext \
	--enable-postscript \
	--enable-printarch \
	--enable-svg \
	--enable-webview \
	--enable-clipboard \
	--enable-dnd \
	--enable-markup \
	--enable-accel \
	--enable-animatectrl \
	--enable-bannerwindow \
	--enable-artstd \
	--enable-arttango \
	--enable-bmpbutton \
	--enable-bmpcombobox \
	--enable-button \
	--enable-calendar \
	--enable-caret \
	--enable-checkbox \
	--enable-checklst \
	--enable-choice \
	--enable-choicebook \
	--enable-collpane \
	--enable-colourpicker \
	--enable-combobox \
	--enable-comboctrl \
	--enable-commandlinkbutton \
	--enable-dataviewctrl \
	--enable-datepick \
	--enable-detect_sm \
	--enable-dirpicker \
	--enable-display \
	--enable-editablebox \
	--enable-filectrl \
	--enable-filepicker \
	--enable-fontpicker \
	--enable-gauge \
	--enable-grid \
	--enable-headerctrl \
	--enable-hyperlink \
	--enable-imaglist \
	--enable-infobar \
	--enable-listbook \
	--enable-listbox \
	--enable-listctrl \
	--enable-notebook \
	--enable-notifmsg \
	--enable-odcombobox \
	--enable-popupwin \
	--enable-prefseditor \
	--enable-radiobox \
	--enable-radiobtn \
	--enable-richmsgdlg \
	--enable-richtooltip \
	--enable-rearrangectrl \
	--enable-sash \
	--enable-scrollbar \
	--enable-searchctrl \
	--enable-slider \
	--enable-spinbtn \
	--enable-spinctrl \
	--enable-splitter \
	--enable-statbmp \
	--enable-statbox \
	--enable-statline \
	--enable-stattext \
	--enable-statusbar \
	--enable-taskbaricon \
	--enable-tbarnative \
	--enable-textctrl \
	--enable-timepick \
	--enable-tipwindow \
	--enable-togglebtn \
	--enable-toolbar \
	--enable-toolbook \
	--enable-treebook \
	--enable-treectrl \
	--enable-treelist \
	--enable-commondlg \
	--enable-aboutdlg \
	--enable-choicedlg \
	--enable-coldlg \
	--enable-filedlg \
	--enable-finddlg \
	--enable-fontdlg \
	--enable-dirdlg \
	--enable-msgdlg \
	--enable-numberdlg \
	--enable-splash \
	--enable-textdlg \
	--enable-tipdlg \
	--enable-progressdlg \
	--enable-wizarddlg \
	--enable-menus \
	--enable-miniframe \
	--enable-tooltips \
	--enable-splines \
	--enable-mousewheel \
	--enable-validators \
	--enable-busyinfo \
	--enable-hotkey \
	--enable-metafiles \
	--enable-dragimage \
	--enable-uiactionsim \
	--enable-dctransform \
	--enable-webviewwebkit \
	--enable-palette \
	--enable-image \
	--enable-gif \
	--enable-pcx \
	--enable-tga \
	--enable-iff \
	--enable-pnm \
	--enable-xpm \
	--enable-ico_cur \
	--enable-autoidman \
	--with-themes=all \
	--with-gtk=2 \
	--with-libpng \
	--with-libjpeg \
	--with-libtiff \
	--with-libjbig \
	--with-liblzma \
	--with-libxpm \
	--with-libmspack \
	--with-libnotify \
	--with-sdl \
	--with-zlib \
	--with-expat \
	--with-x \
	--enable-compat28

%make SHARED_LD_CXX='perl %SOURCE2 $(CXX) -shared -fPIC -g -o' %mfl

#fixed patch to include_cppflags
#sed 's/${includedir}\/wx-3.1/${includedir}\/wx-3.1-gtk2/' -i \
#    lib/wx/config/gtk2-unicode-3.1

%install
%makeinstall_std %mfl

wx_config_filename=$(basename %buildroot%_libdir/wx/config/*-unicode-[0-9]*)
ln -sf ../..%_libdir/wx/config/$wx_config_filename %buildroot%_bindir/wx-config

cp -fR include/wx/private %buildroot%_includedir/wx-%wxrelease/wx/
cp -fR include/wx/unix/private %buildroot%_includedir/wx-%wxrelease/wx/unix/

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%dir %_libdir/wx
%dir %_libdir/wx/config
%_libdir/wx/config/gtk2-unicode-%wxrelease
%dir %_libdir/wx/include
%dir %_libdir/wx/include/gtk2-unicode-%wxrelease
%_libdir/wx/include/gtk2-unicode-%wxrelease/wx
%doc docs/*
%dir %_datadir/bakefile
%_datadir/bakefile/*
%_bindir/*
%dir %_libdir/wx/%wxversion
%_libdir/wx/%wxversion/*.so
%_datadir/aclocal/*.m4
%_includedir/wx-%wxrelease
%_libdir/*.so

%changelog
* Mon Jan 30 2017 Anton Midyukov <antohami@altlinux.org> 3.1.0-alt2.20160229
- Rebuilt with gcc6

* Tue May 31 2016 Anton Midyukov <antohami@altlinux.org> 3.1.0-alt1.20160229
- Initial build for Alt Linux Sisyphus (Closes: 31762). Thanks Aleksey Borisenkov.
