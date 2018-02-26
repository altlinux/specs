%define Name Bonk
Name: bonk
Version: 0.6
Release: alt4
Summary: %Name lossy/lossless audio coder
Summary(uk_UA.CP1251): %Name аудіо кодер з втратами та без втрат
Summary(ru_RU.CP1251): %Name аудио кодер с потерями и без потерь
License: %gpl2plus
Group: Sound
URL: http://www.logarithmic.net/pfh/%name/
Source: http://www.logarithmic.net/pfh-files/%name/%name-%version.tar
Patch: %name-%version-%release.patch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++

%description
%Name is a high quality audio compression program. It can operate in
either lossless or lossy mode. In lossless mode, the exact original WAV
file can be recovered from the compressed file. In lossy mode, some
information is discarded in the compressed file, yielding a much higher
compression ratio. The information discarded is perceptually
unimportant, and the result should be a *perceptually* lossless
encoding. %Name can compress some types of sounds more than others, so
the actual bit-rate achieved varies.
In lossy mode, it can compress some types of sound to as low as 95 kbps
(a compression ration of 14:1) while maintaining perceptually lossless
CD quality stereo. In general, the compression ratio achieved by %Name
is slightly higher than that achieved using the more common MP3 format,
for equivalent sound quality. In particular it copes with transients
(eg clapping, drum beats) better. Performance on purely tonal sound is
roughly equivalent to MP3.
In lossless mode the compression ratio is typically around 2:1.


%prep
%setup
%patch -p1


%build
%define _optlevel 3
%make_build CXXFLAGS="%optflags"


%install
install -pD -m755 %name %buildroot%_bindir/%name


%files
%doc README
%_bindir/*


%changelog
* Sat Dec 27 2008 Led <led@altlinux.ru> 0.6-alt4
- fixed build with g++ 4.3

* Wed Oct 22 2008 Led <led@altlinux.ru> 0.6-alt3
- cleaned up spec

* Sun Jun 03 2007 Led <led@altlinux.ru> 0.6-alt2
- fixed lapsus in Summary (#11961)
- cleaned up BuildRequires
- fixed License

* Wed Feb 01 2006 Led <led@altlinux.ru> 0.6-alt1
- Initial build
