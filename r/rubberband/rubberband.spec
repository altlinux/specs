Name: rubberband
Version: 4.0.0
Release: alt1

Summary: High quality library for audio time-stretching and pitch-shifting
License: GPL-2.0-or-later
Group: Sound
Url: http://www.breakfastquay.com/rubberband/

Vcs: https://github.com/breakfastquay/rubberband.git
Source: %name-%version.tar

BuildRequires: gcc-c++ meson
BuildRequires: ladspa_sdk libfftw3-devel libsamplerate-devel libsndfile-devel libvamp-devel lv2-devel

%package -n librubberband3
Summary: High quality library for audio time-stretching and pitch-shifting
Group: System/Libraries

%package -n librubberband-devel
Summary: Headers for %name
Group: Development/C

%package -n ladspa-rubberband
Summary: An audio time-stretching and pitch-shifting LADSPA plugin
Group: Sound

%package -n lv2-rubberband
Summary: An audio time-stretching and pitch-shifting LV2 plugin
Group: Sound

%package -n vamp-rubberband
Summary: An audio time-stretching and pitch-shifting Vamp plugin
Group: Sound

%define desc \
Rubber Band Library is a high quality software library for audio time-stretching\
and pitch-shifting. It permits you to change the tempo and pitch of an audio\
recording or stream dynamically and independently of one another.

%description %desc

%description -n librubberband3 %desc

%description -n librubberband-devel %desc
Headers for building software that uses %name

%description -n ladspa-rubberband
An audio time-stretching and pitch-shifting LADSPA plugin

%description -n lv2-rubberband
An audio time-stretching and pitch-shifting LV2 plugin

%description -n vamp-rubberband
An audio time-stretching and pitch-shifting Vamp plugin

%prep
%setup

%build
%meson -Dfft=fftw -Dresampler=libsamplerate -Ddefault_library=shared
%meson_build

%install
%meson_install

%files
%_bindir/rubberband*

%files -n librubberband3
%doc README* CHANGELOG
%_libdir/*.so.*

%files -n librubberband-devel
%_includedir/rubberband
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n ladspa-rubberband
%_libdir/ladspa/ladspa-rubberband*
%_datadir/ladspa/rdf/ladspa-rubberband*

%files -n lv2-rubberband
%_libdir/lv2/rubberband.lv2

%files -n vamp-rubberband
%_libdir/vamp/vamp-rubberband*

%changelog
* Thu Nov 28 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 4.0.0-alt1
- 4.0.0 released

* Mon Aug 28 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.3.0-alt1
- 3.3.0 released

* Mon Jun 19 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.2.1-alt1
- 3.2.1 released

* Mon Dec 05 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.2-alt1
- 3.1.2 released

* Mon Oct 03 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.0-alt1
- 3.1.0 released

* Fri Sep 23 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.0-alt1
- 3.0.0 released

* Thu Sep 23 2021 Igor Vlasenko <viy@altlinux.org> 1.9.2-alt1
- new version
- switched to the official git

* Thu Sep 23 2021 Igor Vlasenko <viy@altlinux.org> 1.8.1-alt2.hg20140905.1
- NMU: fixed build with LTO

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.8.1-alt1.hg20140905.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1.hg20140905
- Version 1.8.1

* Wed Jan 11 2012 Alex Karpov <karpov@altlinux.ru> 1.7-alt1
- new version

* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3-alt1.1
- rebuild (with the help of girar-nmu utility)

* Mon Aug 03 2009 Timur Batyrshin <erthad@altlinux.org> 1.3-alt1
- Initial build for sisyphus
