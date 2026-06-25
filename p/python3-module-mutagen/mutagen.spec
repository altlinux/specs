Name: python3-module-mutagen
Version: 1.48.1
Release: alt1

Summary: Python module to handle audio metadata
License: GPLv2
Group: Development/Python
URL: https://pypi.org/project/mutagen
VCS: https://github.com/quodlibet/mutagen

Provides: mutagen = %version-%release
Obsoletes: mutagen

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
Mutagen is a Python module to handle audio metadata. It supports FLAC,
M4A, Musepack, MP3, Ogg FLAC, Ogg Speex, Ogg Theora, Ogg Vorbis, True
Audio, and WavPack audio files. All versions of ID3v2 are supported, and
all standard ID3v2.4 frames are parsed. It can read Xing headers to
accurately calculate the bitrate and length of MP3s. ID3 and APEv2 tags
can be edited regardless of audio format. It can also manipulate Ogg
streams on an individual packet/page level.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%doc COPYING NEWS README.rst
%_bindir/*
%python3_sitelibdir/mutagen
%python3_sitelibdir/mutagen-%version.dist-info
%_man1dir/*

%changelog
* Thu Jun 25 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.48.1-alt1
- 1.48.1 released

* Tue Jun 23 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.48.0-alt1
- 1.48.0 released

* Mon Oct  2 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.47.0-alt1
- 1.47.0 released

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
