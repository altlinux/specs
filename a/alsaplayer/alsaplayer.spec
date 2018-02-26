%def_disable debug
%def_disable profiling
%def_enable nls
%def_with pic

# plugins
# scope
%def_enable opengl
# input
%def_enable mikmod
%def_enable oggvorbis
%def_enable audiofile
%def_enable flac
%def_enable oggflac
%def_enable sndfile
%def_enable mad
%def_enable wav
%def_enable cdda
%def_enable id3tag
# output
%def_enable null
%def_enable jack
%def_enable alsa
%def_enable esd
%def_disable sparc
%def_enable oss
%def_enable nas
%def_disable sgi
# interface
%def_disable gui
%def_enable gtk
%def_enable xosd
%def_enable daemon
%def_enable text
%def_enable systray
# reader
%def_enable file
%def_enable http

%def_with docs
%def_with examples
%def_enable pdf
%def_enable testing

%define icons_sizes 16 22 24 32 48 64 128
#----------------------------------------------------------------------
%define set_enable() %{expand:%%force_enable %{1}} %{expand:%%undefine _disable_%{1}}
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

%{?_enable_gtk:%set_enable gui}

%define svnrev 1333

%define Name Alsaplayer
Name: alsaplayer
%define lname lib%name
Version: 0.99.80
%define prerel %nil
Release: alt11.1
Summary: Advanced Linux Sound Architecture (ALSA) player
Summary(ru_RU.CP1251): Проигрыватель для ALSA
Group: Sound
License: %gpl3plus
URL: http://www.%name.org
# svn co https://alsaplayer.svn.sourceforge.net/svnroot/alsaplayer alsaplayer
%ifdef svnrev
Source0: %url/%name-svn-r%svnrev.tar
%else
Source0: %url/%name-%version%prerel.tar
%endif
Source1: Logo-ombre.png
Patch: %name-svn-r1333-alt.patch
Requires: %name-interface-plugin = %version-%release
Requires: %name-reader-plugin = %version-%release
Requires: %name-in-plugin = %version-%release
Requires: %name-out-plugin = %version-%release
Packager: Led <led@altlinux.ru> 

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++
%{?_with_docs:BuildRequires: doxygen}
%{?_enable_mad:BuildRequires: libmad-devel %{?_enable_id3tag:libid3tag-devel zlib-devel}}
%{?_enable_xosd:BuildRequires: libxosd-devel >= 2}
%{?_enable_oggvorbis:BuildRequires: libvorbis-devel}
%{?_enable_oggflac:BuildRequires: liboggflac-devel libogg-devel}
%{?_enable_opengl:BuildRequires: libGL-devel libGLU-devel}
%{?_enable_nas:BuildRequires: libaudio-devel libXt-devel}
%{?_enable_alsa:BuildRequires: libalsa-devel}
%{?_enable_sgi:BuildRequires: libaudio-devel}
%{?_enable_gtk:BuildRequires: gtk+2-devel >= 2.8.0}
%{?_enable_mikmod:BuildRequires: libmikmod-devel >= 3.1.7}
%{?_enable_audiofile:BuildRequires: libaudiofile-devel >= 0.1.7}
%{?_enable_sndfile:BuildRequires: libsndfile-devel >= 1.0.4}
%{?_enable_esd:BuildRequires: esound-devel >= 0.2.4}
%{?_enable_jack:BuildRequires: jackit-devel >= 0.61.0}
%{?_enable_flac:BuildPreReq: libflac-devel >= 1.0.4  %{?_enable_id3tag:libid3tag-devel zlib-devel}}
%{?_enable_pdf:BuildRequires: tetex-latex >= 2.0 tetex-context tetex-latex-unicode tetex-latex-listings tetex-latex-xcolor}
%{?_enable_gui:BuildRequires: ImageMagick desktop-file-utils}

%description
This package contains %Name is an audio player with wide range of
input, interface, output, and scopes plugins.


%package -n %lname
Summary: Shared library for %Name
Group: System/Libraries

%description -n %lname
This package contains shared library required for %Name to work.


%package full
Summary: Advanced Linux Sound Architecture (ALSA) player with all plugins
Group: Sound
BuildArch: noarch
Requires: %name = %version-%release
Requires: %name-plugins = %version-%release

%description full
This package contains %Name is an audio player with wide range of
input, interface, output, and scopes plugins.


%package plugins
Summary: %Name plugins
Group: System/Libraries
BuildArch: noarch
Requires: %name-plugins-interface = %version-%release
Requires: %name-plugins-reader = %version-%release
Requires: %name-plugins-input = %version-%release
Requires: %name-plugins-output = %version-%release
%{?_enable_gtk:Requires: %name-plugins-scopes = %version-%release}

%description plugins
This package contains plugins for %Name.


%package plugins-common
Summary: %Name plugins common files
Group: System/Libraries
Conflicts: %name-plugins <= 0.99.76-alt1.1.1

%description plugins-common
This package contains plugins common file for %Name.


%package plugins-interface
Summary: %Name interface plugins
Group: System/Libraries
BuildArch: noarch
%{?_enable_daemon:Requires: %name-interface-daemon = %version-%release}
%{?_enable_gtk:Requires: %name-interface-gtk = %version-%release}
%{?_enable_text:Requires: %name-interface-text = %version-%release}
%{?_enable_xosd:Requires: %name-interface-xosd = %version-%release}

%description plugins-interface
This package contains interface plugins for %Name.


%if_enabled gui
%package gui-common
Summary: Common files for %Name GUI interfaces
Group: Sound
BuildArch: noarch
Requires: %name-interface-plugin = %version-%release

%description gui-common
This package contains common files for %Name GUI interfaces.
%endif


%if_enabled daemon
%package interface-daemon
Summary: %Name daemon interface plugin
Group: System/Libraries
Provides: %name-interface-plugin = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description interface-daemon
This package contains daemon interface plugin for %Name.
%endif


%if_enabled gtk
%package interface-gtk
Summary: %Name GTK+ GUI interface plugin
Group: System/Libraries
Provides: %name-interface-plugin = %version-%release
Provides: %name-interface-gui = %version-%release
Provides: %name-interface-gtk2 = %version-%release
Obsoletes: %name-interface-gtk2
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release
Requires: %name-gui-common = %version-%release

%description interface-gtk
This package contains GTK+ GUI interface plugin for %Name.
%endif


%if_enabled text
%package interface-text
Summary: %Name text interface (CLI) plugin
Group: System/Libraries
Provides: %name-interface-plugin = %version-%release
Provides: %name-interface-cli = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description interface-text
This package contains text interface (CLI) plugin for %Name.
%endif


%if_enabled xosd
%package interface-xosd
Summary: %Name XOSD daemon interface plugin
Group: System/Libraries
Provides: %name-interface-plugin = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description interface-xosd
This package contains XOSD daemon interface plugin for %Name.
%endif


%package plugins-reader
Summary: %Name reader plugins
Group: System/Libraries
BuildArch: noarch
%{?_enable_file:Requires: %name-reader-file = %version-%release}
%{?_enable_http:Requires: %name-reader-http = %version-%release}

%description plugins-reader
This package contains reader plugins for %Name.


%if_enabled file
%package reader-file
Summary: %Name file reader plugin
Group: System/Libraries
Provides: %name-reader-plugin = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version

%description reader-file
This package contains file reader plugin for %Name.
%endif


%if_enabled http
%package reader-http
Summary: %Name HTTP reader plugin
Group: System/Libraries
Provides: %name-reader-plugin = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version

%description reader-http
This package contains HTTP reader plugin for %Name.
%endif


%package plugins-input
Summary: %Name input plugins
Group: System/Libraries
BuildArch: noarch
%{?_enable_audiofile:Requires: %name-in-audiofile = %version-%release}
%{?_enable_cdda:Requires: %name-in-cdda = %version-%release}
%{?_enable_flac:Requires: %name-in-flac = %version-%release}
%{?_enable_mad:Requires: %name-in-mad = %version-%release}
%{?_enable_mikmod:Requires: %name-in-mikmod = %version-%release}
%{?_enable_sndfile:Requires: %name-in-sndfile = %version-%release}
%{?_enable_oggvorbis:Requires: %name-in-vorbis = %version-%release}
%{?_enable_wav:Requires: %name-in-wav = %version-%release}

%description plugins-input
This package contains input plugins for %Name.


%if_enabled audiofile
%package in-audiofile
Summary: %Name audiofile input plugin
Group: System/Libraries
Provides: %name-in-plugin = %version-%release
Provides: %name-input-plugin = %version-%release
Provides: %name-input-audiofile = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description in-audiofile
This package contains audiofile input plugin for %Name.
%endif


%if_enabled cdda
%package in-cdda
Summary: %Name CDDA (Audio CD) input plugin
Group: System/Libraries
Provides: %name-in-plugin = %version-%release
Provides: %name-input-plugin = %version-%release
Provides: %name-in-audiocd = %version-%release
Provides: %name-input-cdda = %version-%release
Provides: %name-input-audiocd = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description in-cdda
This package contains CDDA (Audio CD) input plugin for %Name.
%endif


%if_enabled flac
%package in-flac
Summary: %Name FLAC input plugin
Group: System/Libraries
Provides: %name-in-plugin = %version-%release
Provides: %name-input-plugin = %version-%release
Provides: %name-input-flac = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description in-flac
This package contains FLAC input plugin for %Name.
%endif


%if_enabled mad
%package in-mad
Summary: %Name MAD (MP3) input plugin
Group: System/Libraries
Provides: %name-in-plugin = %version-%release
Provides: %name-input-plugin = %version-%release
Provides: %name-in-mp3 = %version-%release
Provides: %name-input-mad = %version-%release
Provides: %name-input-mp3 = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description in-mad
This package contains MAD (MP3) input plugin for %Name.
%endif


%if_enabled mikmod
%package in-mikmod
Summary: %Name Mikmod input plugin
Group: System/Libraries
Provides: %name-in-plugin = %version-%release
Provides: %name-input-plugin = %version-%release
Provides: %name-in-mod = %version-%release
Provides: %name-input-mikmod = %version-%release
Provides: %name-input-mod = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description in-mikmod
This package contains Mikmod input plugin for %Name.
%endif


%if_enabled sndfile
%package in-sndfile
Summary: %Name sndfile input plugin
Group: System/Libraries
Provides: %name-in-plugin = %version-%release
Provides: %name-input-plugin = %version-%release
Provides: %name-input-sndfile = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description in-sndfile
This package contains sndfile input plugin for %Name.
%endif


%if_enabled oggvorbis
%package in-vorbis
Summary: %Name OGG Vorbis input plugin
Group: System/Libraries
Provides: %name-in-plugin = %version-%release
Provides: %name-input-plugin = %version-%release
Provides: %name-in-oggvorbis = %version-%release
Provides: %name-input-vorbis = %version-%release
Provides: %name-input-oggvorbis = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description in-vorbis
This package contains OGG Vorbis input plugin for %Name.
%endif


%if_enabled wav
%package in-wav
Summary: %Name WAV input plugin
Group: System/Libraries
Provides: %name-in-plugin = %version-%release
Provides: %name-input-plugin = %version-%release
Provides: %name-input-wav = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description in-wav
This package contains WAV input plugin for %Name.
%endif


%package plugins-output
Summary: %Name output plugins
Group: System/Libraries
BuildArch: noarch
%{?_enable_alsa:Requires: %name-out-alsa = %version-%release}
%{?_enable_esd:Requires: %name-out-esound = %version-%release}
%{?_enable_jack:Requires: %name-out-jack = %version-%release}
%{?_enable_nas:Requires: %name-out-nas = %version-%release}
%{?_enable_null:Requires: %name-out-null = %version-%release}
%{?_enable_oss:Requires: %name-out-oss = %version-%release}

%description plugins-output
This package contains output plugins for %Name.


%if_enabled alsa
%package out-alsa
Summary: %Name ALSA output plugin
Group: System/Libraries
Provides: %name-out-plugin = %version-%release
Provides: %name-output-plugin = %version-%release
Provides: %name-output-alsa = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description out-alsa
This package contains ALSA output plugin for %Name.
%endif


%if_enabled esd
%package out-esound
Summary: %Name ESounD output plugin
Group: System/Libraries
Provides: %name-out-plugin = %version-%release
Provides: %name-output-plugin = %version-%release
Provides: %name-output-esound = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description out-esound
This package contains ESounD output plugin for %Name.
%endif


%if_enabled jack
%package out-jack
Summary: %Name JACK output plugin
Group: System/Libraries
Provides: %name-out-plugin = %version-%release
Provides: %name-output-plugin = %version-%release
Provides: %name-output-jack = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description out-jack
This package contains JACK output plugin for %Name.
%endif


%if_enabled nas
%package out-nas
Summary: %Name NAS output plugin
Group: System/Libraries
Provides: %name-out-plugin = %version-%release
Provides: %name-output-plugin = %version-%release
Provides: %name-output-nas = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description out-nas
This package contains NAS output plugin for %Name.
%endif


%if_enabled null
%package out-null
Summary: %Name NULL output plugin
Group: System/Libraries
Provides: %name-out-plugin = %version-%release
Provides: %name-output-plugin = %version-%release
Provides: %name-output-null = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description out-null
This package contains NULL output plugin for %Name.
%endif


%if_enabled oss
%package out-oss
Summary: %Name OSS output plugin
Group: System/Libraries
Provides: %name-out-plugin = %version-%release
Provides: %name-output-plugin = %version-%release
Provides: %name-output-oss = %version-%release
Requires: %lname = %version-%release
Requires: %name = %version-%release
Requires: %name-plugins-common = %version-%release

%description out-oss
This package contains OSS output plugin for %Name.
%endif


%if_enabled gtk
%package scopes
Summary: %Name visualisation plugins
Group: System/Libraries
Requires: %lname = %version-%release
Requires: %name = %version-%release
Provides: %name-plugins-scopes2 = %version-%release
Provides: %name-plugins-scopes = %version-%release
Provides: %name-plugins-vis = %version-%release
Obsoletes: %name-scopes2
Obsoletes: %name-vis-plugin

%description scopes
This package contains visualisation plugins for %Name.
%endif


%package -n %lname-devel
Summary: Development files for %Name
Group: Development/C++
Requires: %lname = %version-%release

%description -n %lname-devel
This package contains header files and libraries needed to develop
plugins for %Name.


%package -n %lname-devel-doc
Summary: Development documentation for %Name
Group: Development/Documentation
BuildArch: noarch

%description -n %lname-devel-doc
This package contains development documentation for %Name.


%prep
%ifdef svnrev
%setup -n %name-svn-r%svnrev
%else
%setup -n %name-%version%prerel
%endif
%{?_enable_gui:install -D -m 0644 %SOURCE1 ./icons/%name.png}
%patch -p1


%build
./bootstrap
%configure \
    %{subst_enable debug} \
    %{subst_enable profiling} \
    %{subst_enable nls} \
    %{subst_with pic} \
    %{subst_enable opengl} \
    %{subst_enable mikmod} \
    %{subst_enable oggvorbis} \
    %{subst_enable audiofile} \
    %{subst_enable sndfile} \
    %{subst_enable mad} \
    %{subst_enable id3tag} \
    %{subst_enable wav} \
    %{subst_enable null} \
    %{subst_enable cdda} \
    %{subst_enable flac} \
    %{subst_enable oggflac} \
    %{subst_enable jack} \
    %{subst_enable alsa} \
    %{subst_enable esd} \
    %{subst_enable sparc} \
    %{subst_enable oss} \
    %{subst_enable sgi} \
    %{subst_enable_to gtk gtk2} \
    %{subst_enable systray} \
    %{subst_enable xosd} \
    %{subst_enable text} \
    %{subst_enable file} \
    %{subst_enable http} \
    %{subst_enable daemon} \
    %{subst_enable nas} \
%if_disabled testing
    --disable-glibtest \
    --disable-libmikmodtest \
    --disable-oggtest \
    --disable-vorbistest \
    --disable-audiofiletest \
    --disable-esdtest
%endif

%make_build
%{?_with_docs:%{?_enable_pdf:make -C docs/reference/latex}}

%if_enabled gui
for s in %icons_sizes; do
    convert -resize ${s}x$s -depth 8 icons/{%name,%{name}_$s}.png
done
%endif


%install
%make_install DESTDIR=%buildroot DOC_DIR=%_docdir/%lname-devel-%version install

%{?_enable_gtk:ln -sf libgtk2_interface.so %buildroot%_libdir/%name/interface/libgtk_interface.so}
%if_without docs
install -d -m 0755 %buildroot%_docdir/%lname-devel-%version
%else
mv %buildroot%_docdir/%lname-devel-%version{/reference,}/html
%{?_enable_pdf:install -m 0644 docs/reference/latex/*.pdf %buildroot%_docdir/%lname-devel-%version/}
%if_with examples
install -d -m 0755 %buildroot%_docdir/%lname-devel-%version/examples
install -m 0644 examples/{README.*,*.c} %buildroot%_docdir/%lname-devel-%version/examples/
%endif
%endif
install -m 0644 docs/*.txt %buildroot%_docdir/%lname-devel-%version/
bzip2 --best --keep --force ChangeLog
rm -f %buildroot%_libdir/%name/*/*.la
%if_enabled gui
for s in %icons_sizes; do
    install -D -m 0644 {icons/%{name}_$s,%buildroot%_iconsdir/hicolor/${s}x$s/apps/%name}.png
done
%endif
%find_lang %name
subst '/^[^%%]/s|^.*/\([[:lower:]][[:lower:]]_[[:upper:]][[:upper:]]\)/.*$|%%lang(\1) &|' %name.lang


%files
%doc AUTHORS ChangeLog.* README TODO
%_bindir/*
%_man1dir/*


%files -n %lname
%_libdir/*.so.*


%files full


%files plugins


%files plugins-common
%dir %_libdir/%name
%dir %_libdir/%name/input
%dir %_libdir/%name/interface
%dir %_libdir/%name/output
%dir %_libdir/%name/reader


%files plugins-interface


%if_enabled daemon
%files interface-daemon
%_libdir/%name/interface/libdaemon_interface.so
%endif


%if_enabled gui
%files gui-common
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%endif


%if_enabled gtk
%files interface-gtk -f %name.lang
%_libdir/%name/interface/libgtk2_interface.so
%_libdir/%name/interface/libgtk_interface.so
%endif


%if_enabled text
%files interface-text
%_libdir/%name/interface/libtext_interface.so
%endif


%if_enabled xosd
%files interface-xosd
%_libdir/%name/interface/libxosd_interface.so
%endif


%files plugins-reader


%if_enabled file
%files reader-file
%_libdir/%name/reader/libfile.so
%endif


%if_enabled http
%files reader-http
%_libdir/%name/reader/libhttp.so
%endif


%files plugins-input


%if_enabled audiofile
%files in-audiofile
%_libdir/%name/input/libaf.so
%endif


%if_enabled cdda
%files in-cdda
%_libdir/%name/input/libcdda.so
%endif


%if_enabled flac
%files in-flac
%_libdir/%name/input/libflac_in.so
%endif


%if_enabled mad
%files in-mad
%_libdir/%name/input/libmad_in.so
%endif


%if_enabled mikmod
%files in-mikmod
%_libdir/%name/input/libmod.so
%endif


%if_enabled sndfile
%files in-sndfile
%_libdir/%name/input/libsndfile_in.so
%endif


%if_enabled oggvorbis
%files in-vorbis
%_libdir/%name/input/libvorbis_in.so
%endif


%if_enabled wav
%files in-wav
%_libdir/%name/input/libwav.so
%endif


%files plugins-output


%if_enabled alsa
%files out-alsa
%_libdir/%name/output/libalsa_out.so
%endif


%if_enabled esd
%files out-esound
%_libdir/%name/output/libesound_out.so
%endif


%if_enabled jack
%files out-jack
%_libdir/%name/output/libjack_out.so
%endif


%if_enabled nas
%files out-nas
%_libdir/%name/output/libnas_out.so
%endif


%if_enabled null
%files out-null
%_libdir/%name/output/libnull_out.so
%endif


%if_enabled oss
%files out-oss
%_libdir/%name/output/liboss_out.so
%endif


%if_enabled gtk
%files scopes
%dir %_libdir/%name/scopes2
%_libdir/%name/scopes2/*
%endif


%files -n %lname-devel
%dir %_docdir/%lname-devel-%version
%_docdir/%lname-devel-%version/*.txt
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*


%if_with docs
%files -n %lname-devel-doc
%dir %_docdir/%lname-devel-%version
%_docdir/%lname-devel-%version/html
%{?_enable_pdf:%_docdir/%lname-devel-%version/*.pdf}
%{?_with_examples:%_docdir/%lname-devel-%version/examples}
%endif


%changelog
* Tue Apr 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.80-alt11.1
- Fixed build

* Tue Aug 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.99.80-alt11
- build fixed

* Thu Feb 19 2009 Led <led@altlinux.ru> 0.99.80-alt10
- removed ExcludeArch

* Wed Jan 14 2009 Led <led@altlinux.ru> 0.99.80-alt9
- fixed spec

* Sat Dec 27 2008 Led <led@altlinux.ru> 0.99.80-alt8
- cleaned up spec

* Fri Aug 08 2008 Led <led@altlinux.ru> 0.99.80-alt7
- fixed %name.desktop

* Sat Jun 07 2008 Led <led@altlinux.ru> 0.99.80-alt6
- removed unnecessary Conflicts (#15935)
  (thanx to Anton V. Boyarshinov)

* Tue May 13 2008 Led <led@altlinux.ru> 0.99.80-alt5
- updated BuildRequires

* Fri Apr 04 2008 Led <led@altlinux.ru> 0.99.80-alt4
- updated from SVN (revision 1333):
  + updated %name.1
- fixes desktop-mime-entry

* Sun Mar 02 2008 Led <led@altlinux.ru> 0.99.80-alt3
- updated from SVN (revision 1332):
  + Added initial systray icon function in gtk2

* Sun Mar 02 2008 Led <led@altlinux.ru> 0.99.80-alt2
- updated icons

* Tue Nov 06 2007 Led <led@altlinux.ru> 0.99.80-alt1
- 0.9.80 release
- updated %name-0.99.80-configure.patch

* Wed Oct 10 2007 Led <led@altlinux.ru> 0.99.80-alt0.11
- 0.99.80-rc4

* Sun Oct 07 2007 Led <led@altlinux.ru> 0.99.80-alt0.10
- 0.99.80-rc3
- fixed License
- updated %name-0.99.80-rc3-configure.patch

* Sun Jul 15 2007 Led <led@altlinux.ru> 0.99.80-alt0.9
- 0.99.80-rc2
- Changed License

* Tue Jun 26 2007 Led <led@altlinux.ru> 0.99.80-alt0.8
- SVN snapshot (revision 1239)
- updated uk.po

* Mon Jun 25 2007 Led <led@altlinux.ru> 0.99.80-alt0.7
- cleaned up spec
- fixed License

* Mon Jun 25 2007 Led <led@altlinux.ru> 0.99.80-alt0.6
- SVN snapshot (revision 1232)
- added %name-full virtual package
- added required Obsoletes/Conflicts
- updated %name-svn-r1232-configure.patch

* Sun Jun 24 2007 Led <led@altlinux.ru> 0.99.80-alt0.5
- SVN snapshot (revision 1229)
- added %name.uk.po

* Sat Jun 23 2007 Led <led@altlinux.ru> 0.99.80-alt0.4
- SVN snapshot (revision 1224)
- removed %name-svn-r1201-flac.patch (fixed in upstream)
- no gtk+ 1.x intrface, used gtk+ 2.x instead (%name-interface-gtk
  package)
- fixed BuildRequires

* Thu Jun 14 2007 Led <led@altlinux.ru> 0.99.80-alt0.3
- SVN snapshot (revision 1201)
- updated %name-svn-r1201-configure.patch
- updated %name-svn-r1201-flac.patch
- replaced %%__autoreconf with ./bootstrap

* Thu Jun 07 2007 Led <led@altlinux.ru> 0.99.80-alt0.2
- fixed %name.desktop

* Wed Jun 06 2007 Led <led@altlinux.ru> 0.99.80-alt0.1
- 0.99.80-rc1

* Sun May 27 2007 Led <led@altlinux.ru> 0.99.79-alt0.3
- 0.99.79
- cleaned up spec
- removed %name-0.99.76+flac-1.1.3.patch
- added %name-0.99.79-flac.patch

* Fri Mar 16 2007 Led <led@altlinux.ru> 0.99.77-alt1
- 0.99.77
- updated %name-0.99.77-configure.patch
- added %name-interface-gtk2 package
- fixed spec

* Wed Mar 07 2007 Led <led@altlinux.ru> 0.99.76-alt3
- rebuild with libFLAC.so.8

* Mon Jan 22 2007 Led <led@altlinux.ru> 0.99.76-alt2
- remade spec
- added %name-0.99.76-configure.patch
- added %name-0.99.76+flac-1.1.3.patch

* Tue Feb 22 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.99.76-alt1.1.1
- Rebuilt with libflac-1.1.2-alt1

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.99.76-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Dec 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.99.76-alt1
- 0.99.76
- do not package .la files.
- fix TEXTREL bug.

* Wed Apr 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.99.75-alt1
- 0.99.75

* Sun Mar 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.99.74-alt1
- 0.99.74

* Tue Dec 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.99.73-alt1
- new version.
- lib%name, -devel and plugins subpackages.
- enabled flac support.
- descriptions, menus improved.

* Tue Oct 29 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.99.72-alt1
- 0.99.72
- unusual jack support disabled.
- broken flac support disabled.

* Tue Jun 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.99.71-alt1
- 0.99.71

* Thu May 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.99.70-alt1
- 0.99.70
- flac input plugin
- buildrequres updated

* Sun Apr 21 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.99.59-alt2
- rebuilt with jack, buildrequres updated.

* Tue Apr 09 2002 Rider <rider@altlinux.ru> 0.99.59-alt1
- 0.99.59

* Tue Mar 19 2002 Rider <rider@altlinux.ru> 0.99.57-alt1
- 0.99.57

* Sun Feb 10 2002 Rider <rider@altlinux.ru> 0.99.53-alt0.1
- 0.99.53

* Fri Oct 12 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.99.51-alt0.1-cvs
- Compile from CVS version

* Mon Sep 24 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.99.50-alt2
- Some fixes

* Mon Sep 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.99.50-alt1
- 0.99.50

* Mon Aug 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.99.36-alt1
- 0.99.36

* Tue Aug 21 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.99.35-alt1
- 0.99.35

* Thu Aug 16 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.99.34-alt1
- 0.99.34

* Tue Jan 16 2001 Dmitry V. Levin <ldv@fandra.org> 0.99.33-ipl0.1mdk
- 0.99.33-pre2.
- RE adaptions.

* Thu Dec  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.32-12mdk
- Recompile with alsa-0.5.10.

* Tue Nov 28 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.32-11mdk
- Add icons.

* Sat Nov 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.32-10mdk
- fix gcc2.96 compilation.

* Thu Oct 24 2000 David BAUDENS <baudens@mandrakesoft.com> 0.99.32-9mdk
- EcludeArch: ppc

* Thu Aug 24 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99.32-8mdk
- remove some debugging messages

* Thu Aug 24 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99.32-7mdk
- build against latest alsa-lib
- fix requires

* Sun Aug 13 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.99.32-6mdk
- disabled the use of makeinstall macro in order to have the libraries installed
  in the correct place (reported by Anton Graham <darkimage@bigfoot.com>)
- cleaner specfile
- more menu dir macros

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.99.32-5mdk
- automatically added BuildRequires

* Mon Jul 17 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99.32-4mdk
- fix macros

* Tue Jun 27 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.32-3mdk
- macroszifications.
- build against latest alsa-lib
- Use macros for update-menus.

* Mon Jun 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99.32-2mdk
- build against latest alsa-lib
- add url

* Thu Jun 08 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99.32-1mdk
- new release

* Fri May 19 2000 Francis Galiegue <fg@mandrakesoft.com> 0.99.31-2mdk

- ExcludeArch: alpha sparc sparc64

* Sun Apr 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.31-1mdk
- Add menu entry.
- Fix Requires.
- Fix titi sucks.
- Build again latest alsa-lib and libmikmod.

* Thu Apr 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.99.31-2mdk
- fixed group

* Thu Mar 09 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>
- update to 99.31
- compiled against alsa-lib-0.5.5

* Tue Aug 24 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- initial spec
