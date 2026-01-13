%define pypi_name mingus

%def_with check

Name: python3-module-%pypi_name
Version: 0.6.1
Release: alt1

Summary: Cross-platform music theory and notation package for Python with MIDI file and playback support
License: GPLv3
Group: Development/Python3

Url: https://pypi.org/project/mingus
VCS: https://github.com/bspaans/python-mingus

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-six
BuildRequires: python3-module-numpy
%endif

%description
Mingus is an advanced, cross-platform music theory and notation package for
Python with MIDI file and playback support. It can be used to play around
with music theory, to build editors, educational tools and other
applications that need to process and/or play music. It can also
be used to create sheet music with LilyPond.

%package examples
Summary: Examples for %name
Group: Development/Python3
Requires: %name = %version-%release

%description examples
Example programs and demo scripts for python3-module-mingus,
including pygame-based piano and drum demos.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot%_datadir/%name/examples
cp -a %buildroot/usr/mingus_examples/* %buildroot%_datadir/%name/examples/
rm -rf %buildroot/usr/mingus_examples

%check
# Skip FluidSynth integration tests: they require a real SoundFont (.sf2)
# file and the SOUNDFONT environment variable, which are not available
# in the isolated build environment.
%pyproject_run_pytest \
    --ignore=tests/integration/test_fluidsynth.py

%files
%doc README.md  CHANGELOG.md CONTRIBUTING.md LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info

%files examples
%dir %_datadir/%name
%_datadir/%name/examples


%changelog
* Wed Nov 19 2025 Valentin Sokolov <sova@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus.
