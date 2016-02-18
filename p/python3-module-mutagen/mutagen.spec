%define oname mutagen

Name: python3-module-%oname
Version: 1.20.1
Release: alt1.bzr20130802.1

Summary: Python module to handle audio metadata
License: GPLv2
Group: Development/Python3

Url: https://code.launchpad.net/~berdario/mutagen/mutagen-py3
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python-tools-2to3
#BuildPreReq: faad flac liboggz python3-module-eyeD3 vorbis-tools

%py3_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python3 python3-base xz
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

%package -n %oname-py3
Summary: Various mutagen (python module to handle audio metadata) binary tools
Group: Sound

%description -n %oname-py3
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd

%files
%doc API-NOTES NEWS README TODO TUTORIAL
%python3_sitelibdir/*

%files -n %oname-py3
%_bindir/*

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.20.1-alt1.bzr20130802.1
- NMU: Use buildreq for BR.

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.20.1-alt1.bzr20130802
- Initial build for Sisyphus

