%define _unpackaged_files_terminate_build 1
%define short_name beet

%def_with check

Name: beets
Version: 2.7.1
Release: alt1
Summary: Music library manager and MusicBrainz tagger.
License: MIT and ISC
Group: Sound
Url: https://github.com/beetbox/beets
Vcs: https://beets.io/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(sphinx)
BuildRequires: python3
BuildRequires: python3-module-pydata-sphinx-theme
BuildRequires: python3-module-pyyaml-env-tag 
BuildRequires: python3-module-musicbrainzngs
BuildRequires: python3(munkres)
BuildRequires: python3-module-mutagen
BuildRequires: python3(unidecode)
BuildRequires: python3-module-poetry-core
BuildRequires: python3(pip)
BuildRequires: python3(confuse)
BuildRequires: python3(click)
BuildRequires: python3(mediafile)
BuildRequires: python3(responses)
BuildRequires: python3(mock)
BuildRequires: python3(jellyfish)
BuildRequires: python3(numpy)
BuildRequires: python3(lap)
BuildRequires: python3(flask)
BuildRequires: python3-module-pyxdg
BuildRequires: python3(mpd)
BuildRequires: python3(langdetect)
BuildRequires: python3(pylast)
BuildRequires: python3-module-requests-oauthlib
BuildRequires: python3-module-discogs-client
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-distutils-extra
BuildRequires: gstreamer1.0
BuildRequires: ffmpeg
BuildRequires: ImageMagick-tools
BuildRequires: unrar
BuildRequires: bash-completion
BuildRequires: python3-module-requests-ratelimiter

Requires: python3
Requires: python3(jellyfish)
Requires: python3(munkres)
Requires: python3-module-musicbrainzngs
Requires: python3-module-mutagen
Requires: python3(unidecode)
Requires: python3-module-pyyaml-env-tag 
Requires: python3(confuse)
Requires: python3(acoustid)
Requires: python3(requests)
Requires: python3(pylast)
Requires: gstreamer1.0
Requires: ffmpeg
Requires: ImageMagick-tools
Requires: python3(flask)
Requires: python3(lap)
Requires: python3(beetsplug)


%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-requests-mock
BuildRequires: python3-module-pytest-flask
%endif

%add_python3_req_skip titlecase

%description
The purpose of beets is to get your music collection right once and for all. It
catalogs your collection, automatically improving its meta-data as it goes using
the MusicBrainz database. Then it provides a bouquet of tools for manipulating
and accessing your music.
Because beets is designed as a library, it can do almost anything you can
imagine for your music collection. Via plugins, beets becomes a panacea:
- Fetch or calculate all the meta-data you could possibly need: album art,
  lyrics, genres, tempos, ReplayGain levels, or acoustic fingerprints.
- Get meta-data from MusicBrainz, Discogs, or Beatport. Or guess meta-data using
  songs' file names or their acoustic fingerprints.
- Transcode audio to any format you like.
- Check your library for duplicate tracks and albums or for albums that are
  missing tracks.
- Browse your music library graphically through a Web browser and play it in
  any browser that supports HTML5 Audio.

%package -n python3-module-beetsplug
Summary: Plugins for %name
Group: Sound
Requires: %name == %version-%release
Requires: libgstreamer1.0
Requires: python3(acoustid)
Requires: python3-module-requests
Requires: python3(mpd)
Requires: python3-module-pygobject3
Requires: python3(flask)
Requires: python3(soco)
Provides: python3(beetsplug)

%description -n python3-module-beetsplug
Contains a number of plugins to improve meta-data, format paths,
inter-operability aids and so on.

%prep
%setup -q
%autopatch -p1
# replace distutils for python 3.12
sed -i 's/from distutils\.spawn import find_executable/from shutil import which/' beetsplug/absubmit.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --ignore=test/plugins/test_titlecase.py

%files
%doc *.md
%_bindir/%short_name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}/

%files -n python3-module-beetsplug
# beetsplug/mbcollection.py is the plugin that has ISC license
%python3_sitelibdir/beetsplug/

%changelog
* Fri Mar 27 2026 Pavel Shilov <zerospirit@altlinux.org> 2.7.1-alt1
- Update to new version 2.7.1.

* Tue Mar 10 2026 Pavel Shilov <zerospirit@altlinux.org> 2.6.2-alt2
- Update to fix (ALT #58167)

* Wed Mar 04 2026 Pavel Shilov <zerospirit@altlinux.org> 2.6.2-alt1
- Update to new version 2.6.2.

* Tue Oct 21 2025 Pavel Shilov <zerospirit@altlinux.org> 2.5.1-alt1
- 2.3.1 -> 2.5.1

* Tue Aug 26 2025 Pavel Shilov <zerospirit@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus.
