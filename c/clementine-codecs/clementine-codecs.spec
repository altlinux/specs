Name: clementine-codecs
Version: 1.2.3
Release: alt1

Summary: Meta package with user friendly names for GStreamer codecs
License: %gpl2plus
Group: Sound

Url: http://code.google.com/p/clementine-player
Packager: Vladimir Didenko <cow@altlinux.org>
BuildArch: noarch

BuildPreReq: rpm-build-licenses


%description
A set of virtual packages that provide user friendly names for
Gstreamer codecs


%package -n %name-aac
Summary: AAC support for clementine
Group: Sound

Requires: gst-plugins-bad

%description -n %name-aac
This package provides AAC support for clementine


%package -n %name-alac
Summary: Apple Lossless support for clementine
Group: Sound

Requires: gst-plugins-good gst-ffmpeg

%description -n %name-alac
This package provides Apple Lossless support for clementine


%package -n %name-ape
Summary: Monkey Audio support for clementine
Group: Sound

Requires: gst-plugins-good gst-ffmpeg

%description -n %name-ape
This package provides Monkey Audio support for clementine


%package -n %name-flac
Summary: FLAC support for clementine
Group: Sound

Requires: gst-plugins-good

%description -n %name-flac
This package provides FLAC support for clementine


%package -n %name-mp3
Summary: MP3 support for clementine
Group: Sound

Requires: gst-plugins-ugly

%description -n %name-mp3
This package provides mp3 support for clementine


%package -n %name-ogg
Summary: Ogg Vorbis support for clementine
Group: Sound

Requires: gst-plugins-base

%description -n %name-ogg
This package provides Ogg Vorbis support for clementine


%package -n %name-wav
Summary: Waveform Audio File Format support for clementine
Group: Sound

Requires: gst-plugins-ugly gst-ffmpeg

%description -n %name-wav
This package provides Waveform Audio File Format support for clementine


%package -n %name-wma
Summary: Windows Media Audio support for clementine
Group: Sound

Requires: gst-plugins-ugly gst-ffmpeg

%description -n %name-wma
This package provides Windows Media Audio support for clementine


%package -n %name-full
Summary: A full set of clementine codecs
Group: Sound

Requires: %name-aac = %version-%release
Requires: %name-alac = %version-%release
Requires: %name-ape = %version-%release
Requires: %name-flac = %version-%release
Requires: %name-mp3 = %version-%release
Requires: %name-ogg = %version-%release
Requires: %name-wav = %version-%release
Requires: %name-wma = %version-%release

%description -n %name-full
This package provides full set of clementine codecs


%prep

%files -n %name-aac
%files -n %name-alac
%files -n %name-ape
%files -n %name-flac
%files -n %name-mp3
%files -n %name-ogg
%files -n %name-wav
%files -n %name-wma
%files -n %name-full

%changelog
* Wed Feb 25 2015 Vladimir Didenko <cow@altlinux.org> 1.2.3-alt1
- Initial build (closes: #30819)
