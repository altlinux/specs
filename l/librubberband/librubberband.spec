%def_disable static

Name: librubberband
Version: 1.7
Release: alt1

Summary: high quality library for audio time-stretching and pitch-shifting
License: %gpl2plus
Group: System/Libraries
Url: http://www.breakfastquay.com/rubberband/
Packager: Alex Karpov <karpov@altlinux.ru>

Source0: %name-%version.tar

BuildPreReq: rpm-build-licenses
# Automatically added by buildreq on Fri Aug 07 2009
BuildRequires: gcc-c++ ladspa_sdk libfftw3-devel libsamplerate-devel libsndfile-devel libvamp-devel

%description
Rubber Band Library is a high quality software library for audio time-stretching
and pitch-shifting. It permits you to change the tempo and pitch of an audio
recording or stream dynamically and independently of one another.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%package -n rubberband
Summary: An audio time-stretching and pitch-shifting utility program
Group: Sound

%description -n rubberband
An audio time-stretching and pitch-shifting utility program

%package -n vamp-rubberband
Summary: An audio time-stretching and pitch-shifting Vamp plugin
Group: Sound

%description -n vamp-rubberband
An audio time-stretching and pitch-shifting Vamp plugin

%package -n ladspa-rubberband
Summary: An audio time-stretching and pitch-shifting LADSPA plugin
Group: Sound

%description -n ladspa-rubberband
An audio time-stretching and pitch-shifting LADSPA plugin

%prep
%setup

%build
%configure %{subst_enable static} --libdir=%_libdir
%make_build

%install
%makeinstall_std
#mv %buildroot%_prefix/libX %buildroot%_libdir

%files
%_libdir/*.so.*
%doc README.txt

%files devel
%_libdir/*.so
%_includedir/rubberband
%_pkgconfigdir/*.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%files -n rubberband
%_bindir/rubberband

%files -n vamp-rubberband
%_libdir/vamp/vamp-rubberband*

%files -n ladspa-rubberband
%_libdir/ladspa/ladspa-rubberband*
%_datadir/ladspa/rdf/ladspa-rubberband*

%changelog
* Wed Jan 11 2012 Alex Karpov <karpov@altlinux.ru> 1.7-alt1
- new version

* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt1.1
- rebuild (with the help of girar-nmu utility)

* Mon Aug 03 2009 Timur Batyrshin <erthad@altlinux.org> 1.3-alt1
- Initial build for sisyphus

