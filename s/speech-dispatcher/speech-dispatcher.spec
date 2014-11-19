
Name: speech-dispatcher
Version: 0.8.1
Release: alt1
License: %gpl2plus
Group: Sound
Summary: A speech output processing service
URL: http://www.freebsoft.org/speechd
Packager: Michael Pozhidaev <msp@altlinux.ru>

BuildRequires(pre): rpm-build-licenses 
BuildRequires: libdotconf-devel >= 0.3
BuildRequires: gcc-c++ glib2-devel glibc-devel-static intltool
BuildRequires:  libXau-devel  libltdl7-devel 
BuildRequires: libalsa-devel libao-devel
BuildRequires: flite-devel  libespeak-devel svox-pico
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-base python3-devel
BuildRequires: libpulseaudio-devel

%add_python3_req_skip speechd_config
%add_python3_req_skip xdg

Source0: %name-%version.tar
Patch1: speech-dispatcher-0.8-alt-flite.patch

%description
Speech Dispatcher is a part of the Free(b)soft project, which is
intended to allow blind and visually impaired people to work with
computer and Internet based on free software.

%package -n libspeechd
Summary: Client library for speech-dispatcher 
Group: System/Libraries

%description -n libspeechd
Applications can use this library to communicate with speech-dispatcher
service and produce speech output.

%package -n libspeechd-devel
Group: Development/C
Summary: Development files to use libspeechd to connect to speech-dispatcher

%description -n libspeechd-devel
Developers can use this library to connect to speech-dispatcher daemon
and produce speech output.

%package output-libao
Group: Sound
Summary: libao output module for speech-dispatcher
Requires: %name = %version-%release

%description output-libao
libao output module for speech-dispatcher

%package output-pulse
Group: Sound
Summary: PulseAudio output module for speech-dispatcher
Requires: %name = %version-%release

%description output-pulse
PulseAudio output module for speech-dispatcher.

%package output-oss
Group: Sound
Summary: OSS output module for speech-dispatcher
Requires: %name = %version-%release

%description output-oss
OSS output module for speech-dispatcher

%package module-flite
Group: Sound
Summary: Flite support for speech-dispatcher
Requires: %name = %version-%release

%description module-flite
Flite support for speech-dispatcher

%package module-festival
Group: Sound
Summary: Festival support for speech-dispatcher
Requires: %name = %version-%release

%description module-festival
Festival support for speech-dispatcher

%package module-pico
Group: Sound
Summary: Pico support for speech-dispatcher
Requires: %name = %version-%release

%description module-pico
Pico support for speech-dispatcher

%package -n python3-module-speechd
Summary: Python client for Speech Dispatcher
Group: Development/Python
BuildArch: noarch

%description -n python3-module-speechd
This python module allows programmsaccess speech-dispatcher service.

%prep
%setup -q 
%patch1 -p1
%build
%autoreconf
%configure --with-espeak \
	   --with-flite  \
           --with-pico \
	   --with-pulse \
	   --with-alsa \
	   --with-libao \
	   --with-oss
%make_build

%install
%make_install DESTDIR='%buildroot' pyexecdir=%python3_sitelibdir_noarch install

%files
%doc ANNOUNCE AUTHORS BUGS ChangeLog doc FAQ NEWS README README.packagers README.style README.translators TODO
%_bindir/*
%config %_sysconfdir/%name
%dir %_libdir/%name
%_libdir/%name/spd_alsa.so
%exclude %_libdir/%name/spd_alsa.*a
%dir %_libdir/%name-modules
%_libdir/%name-modules/sd_dummy
%_libdir/%name-modules/sd_espeak
%_libdir/%name-modules/sd_generic
%_libdir/%name-modules/sd_cicero
# gnome-speech.conf breaks autospawn
%exclude %_sysconfdir/%name/clients/gnome-speech.conf
%_datadir/sounds/%name
%_datadir/%name
%_infodir/*
/usr/share/locale/*/*/*.mo

%files -n libspeechd
%_libdir/libspeechd*.so.*
%exclude %_libdir/libspeechd.*a

%files -n libspeechd-devel
%_includedir/*
%_libdir/libspeechd.so
%_pkgconfigdir/*

%files output-libao
%_libdir/%name/spd_libao.so
%exclude %_libdir/%name/spd_libao.*a

%files output-pulse
%_libdir/%name/spd_pulse.so
%exclude %_libdir/%name/spd_pulse.*a

%files output-oss
%_libdir/%name/spd_oss.so
%exclude %_libdir/%name/spd_oss.*a

%files module-flite
%_libdir/%name-modules/sd_flite

%files module-festival
%_libdir/%name-modules/sd_festival

%files module-pico
%_libdir/%name-modules/sd_pico

%files -n python3-module-speechd
%python3_sitelibdir_noarch/*

%changelog
* Tue Nov 18 2014 Paul Wolneykien <manowar@altlinux.org> 0.8.1-alt1
- Freshed up to v0.8.1 with the help of cronbuild and update-source-functions.

* Wed Jul 03 2013 Paul Wolneykien <manowar@altlinux.org> 0.8-alt2
- Require speech-dispatcher in all modules.
- Exclude the static libs.
- Explicitly configure all of the modules to be packaged.
- Include the default cicero module into the main package.
- Use plain tar sources.
- Cleanup the spec. Strict the pattern for l10n files.
- Build the Python module noarch.
- Add the PulseAudio output module.
- Add msp@ to the cronbuild CC.
- Add cronbuild scripts based on the update-source-functions.
- Exclude clients/gnome-speech.conf which breaks server autospawn.

* Fri May 10 2013 Michael Pozhidaev <msp@altlinux.ru> 0.8-alt1
- New version 0.8 (closes: #28819)
- New subpackages: output-libao, output-oss, module-flite,
  module-festival, module-pico
- python-module-speech subpackage is renamed to python3-module-speechdd

* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.7-alt5.3
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.7-alt5.2.1
- Rebuild with Python-2.7

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.7-alt5.2
- Rebuilt for soname set-versions

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.7-alt5.1
- Rebuilt with python 2.6

* Thu Aug 20 2009 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt5
- 'daemon' term replaced by 'service' one (by mike@ suggestion)

* Mon Aug 17 2009 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt4
- Applied getline patch from sbolshakov@

* Wed Aug 05 2009 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt3
- Applied flite patch (Thanks to sbolshakov@)
- Spec cleanup (removed ldconfig and install_info calls by sbolshakov@)
- Minor fixes

* Mon Sep 15 2008 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt2
- Fixed i586 build

* Sun Sep 07 2008 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt1
- Initial RPM

