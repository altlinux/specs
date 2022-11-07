Name: python3-module-mutagen
Version: 1.46.0
Release: alt1

Summary: Python module to handle audio metadata
License: GPLv2
Group: Development/Python
Url: https://github.com/quodlibet/mutagen.git

Source0: %name-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest) python3(hypothesis)

%description
Mutagen is a Python module to handle audio metadata. It supports FLAC,
M4A, Musepack, MP3, Ogg FLAC, Ogg Speex, Ogg Theora, Ogg Vorbis, True
Audio, and WavPack audio files. All versions of ID3v2 are supported, and
all standard ID3v2.4 frames are parsed. It can read Xing headers to
accurately calculate the bitrate and length of MP3s. ID3 and APEv2 tags
can be edited regardless of audio format. It can also manipulate Ogg
streams on an individual packet/page level.

%package -n mutagen
Summary: Various mutagen (python module to handle audio metadata) binary tools
Group: Sound
Requires: python3-module-mutagen = %version-%release

%description -n mutagen
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
LC_ALL=en_US.UTF-8 \
python3 setup.py test

%files
%python3_sitelibdir/mutagen
%python3_sitelibdir/mutagen-%version.dist-info

%files -n mutagen
%doc COPYING NEWS README.rst
%_bindir/*
%_man1dir/*

%changelog
* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.46.0-alt1
- 1.46.0 released

* Tue Sep 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.45.1-alt1
- 1.45.1 released

* Tue Jul 07 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.44.0-alt1
- 1.44.0 released

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.36-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 22 2016 Anton Midyukov <antohami@altlinux.org> 1.36-alt1
- New version 1.36 (Closes: 32868)

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.24-alt1
- Version 1.24

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.22-alt1
- Version 1.22

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
