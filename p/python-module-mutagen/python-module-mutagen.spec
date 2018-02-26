%define modulename mutagen

Name: python-module-%modulename
Version: 1.20
Release: alt1.1

Summary: Python module to handle audio metadata
License: GPLv2
Group: Development/Python

Packager: Andrey Rahmatullin <wrar@altlinux.org>

Url: http://code.google.com/p/mutagen/
Source: %modulename-%version.tar
BuildArch: noarch

%setup_python_module %modulename

BuildPreReq: faad flac liboggz python-module-eyeD3 vorbis-tools

%description
Mutagen is a Python module to handle audio metadata. It supports FLAC,
M4A, Musepack, MP3, Ogg FLAC, Ogg Speex, Ogg Theora, Ogg Vorbis, True
Audio, and WavPack audio files. All versions of ID3v2 are supported, and
all standard ID3v2.4 frames are parsed. It can read Xing headers to
accurately calculate the bitrate and length of MP3s. ID3 and APEv2 tags
can be edited regardless of audio format. It can also manipulate Ogg
streams on an individual packet/page level.

This module is built for python %_python_version

%package -n %modulename
Summary: Various mutagen (python module to handle audio metadata) binary tools
Group: Sound

%description -n %modulename
%summary

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%check
python setup.py test

%files
%doc API-NOTES NEWS README TODO TUTORIAL
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%files -n %modulename
%_bindir/*
%_man1dir/*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.20-alt1.1
- Rebuild with Python-2.7

* Tue Aug 24 2010 Andrey Rahmatullin <wrar@altlinux.org> 1.20-alt1
- 1.20
- package docs
- clarify License:
- run tests

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.18-alt1.1
- Rebuilt with python 2.6

* Fri Nov 06 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.18-alt1
- 1.18
- Package additional tools to separate package

* Sun Mar 18 2007 Mikhail Yakshin <greycat@altlinux.org> 1.10.1-alt1
- Initial build for ALT Linux
