%define modulename mutagenx

Name: python3-module-%modulename
Version: 1.24
Release: alt1.1

Summary: Python module to handle audio metadata
License: GPLv2
Group: Development/Python3

Url: https://pypi.python.org/pypi/mutagenx/
Source: %modulename-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
#BuildPreReq: faad flac liboggz python3-module-eyeD3 vorbis-tools
#BuildPreReq: python3-devel

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base xz
BuildRequires: rpm-build-python3

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

find -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +

%build
%python3_build

%install
%python3_install

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%check
export LC_ALL=en_US.UTF-8
#python3 setup.py test

%files
%doc NEWS *.rst
%python3_sitelibdir/*

%files -n %modulename
%_bindir/*

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.24-alt1.1
- NMU: Use buildreq for BR.

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.24-alt1
- Initial build for Sisyphus

