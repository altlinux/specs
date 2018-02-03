%def_with python3
%def_with test
#%%def_with docs
%define modulename mutagen

Name: python-module-%modulename
Version: 1.36
Release: alt1.1
Summary: Helpers for better testing

License: GPLv2
Group: Development/Python
Url: https://github.com/quodlibet/mutagen.git
Packager: Python Development Team <python@packages.altlinux.org>

Source: %name-%version.tar
BuildArch: noarch
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
%endif
%if_with docs
BuildRequires: /usr/bin/sphinx-build
%endif
%py_provides %modulename

%description
Mutagen is a Python module to handle audio metadata. It supports FLAC,
M4A, Musepack, MP3, Ogg FLAC, Ogg Speex, Ogg Theora, Ogg Vorbis, True
Audio, and WavPack audio files. All versions of ID3v2 are supported, and
all standard ID3v2.4 frames are parsed. It can read Xing headers to
accurately calculate the bitrate and length of MP3s. ID3 and APEv2 tags
can be edited regardless of audio format. It can also manipulate Ogg
streams on an individual packet/page level.

%package -n python3-module-%modulename
Summary: Helpers for better testing
Group: Development/Python3
%py3_provides %modulename

%description -n python3-module-%modulename
Mutagen is a Python module to handle audio metadata. It supports FLAC,
M4A, Musepack, MP3, Ogg FLAC, Ogg Speex, Ogg Theora, Ogg Vorbis, True
Audio, and WavPack audio files. All versions of ID3v2 are supported, and
all standard ID3v2.4 frames are parsed. It can read Xing headers to
accurately calculate the bitrate and length of MP3s. ID3 and APEv2 tags
can be edited regardless of audio format. It can also manipulate Ogg
streams on an individual packet/page level.

%package -n %modulename
Summary: Various mutagen (python module to handle audio metadata) binary tools
Group: Sound
Obsoletes: %modulename-py3
Provides: %modulename-py3

%description -n %modulename
%summary

%package docs
Summary: Documentation for mutagen
Group: Development/Documentation
BuildArch: noarch

%description docs
%summary

%prep
%setup
%if_with python3
cp -fR . ../python3-module-%modulename
%endif

%build
%python_build

%if_with python3
pushd ../python3-module-%modulename
%python3_build
popd
%endif

%if_with docs
%make -C docs
%endif

%install
%python_install

%if_with python3
pushd ../python3-module-%modulename
%python3_install
popd
%endif

%if_with test
%check
export LC_ALL=en_US.UTF-8
python setup.py test

%if_with python3
pushd ../python3-module-%modulename
python3 setup.py test
popd
%endif
%endif

%files
%doc COPYING NEWS README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modulename
%doc COPYING NEWS README.rst
%python3_sitelibdir/*
%endif

%files -n %modulename
%_bindir/*
%_man1dir/*

%if_with docs
%files docs
%doc docs/_build/*
%endif

%changelog
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
