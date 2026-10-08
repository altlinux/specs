
%def_enable check

Name: picard
Version: 3.0.1
Release: alt1
Summary: MusicBrainz-based audio tagger
License: GPL-2.0-or-later
Group: Sound

URL: https://github.com/musicbrainz/picard/
Vcs: https://github.com/musicbrainz/picard.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: desktop-file-utils
BuildRequires: gettext
%if_enabled check
BuildRequires: python3(dateutil)
BuildRequires: python3(fasteners)
BuildRequires: python3(jwt)
BuildRequires: python3(makefun)
BuildRequires: python3(markdown)
BuildRequires: python3(mutagen)
BuildRequires: python3(PyQt6)
BuildRequires: python3(pytest)
BuildRequires: python3(yaml)
BuildRequires: python3-module-charset-normalizer
BuildRequires: xvfb-run
%endif

%add_python3_req_skip AppKit MediaPlayer

Requires: hicolor-icon-theme

%description
Picard is an audio tagging application using data from the MusicBrainz
database. The tagger is album or release oriented, rather than
track-oriented.

%prep
%setup

%build
export PICARD_DISABLE_AUTOUPDATE=1
%pyproject_build

%install
export PICARD_DISABLE_AUTOUPDATE=1
%pyproject_install

desktop-file-install \
  --delete-original --remove-category="Application"   \
  --dir=%buildroot%_datadir/applications      \
  %buildroot%_datadir/applications/*

# rm -r %buildroot%_datadir/locale/{es_419,zh-Hans,zh_Hans,zh_Hant}

%find_lang %name
%find_lang %name-attributes
%find_lang %name-constants
%find_lang %name-countries
cat %name-attributes.lang %name-constants.lang %name-countries.lang >> %name.lang

%check
%pyproject_run_pytest

%files -f %name.lang
%doc AUTHORS.txt COPYING.txt
%_bindir/picard*
%_datadir/applications/org.musicbrainz.Picard.desktop
%_datadir/icons/hicolor/*/apps/org.musicbrainz.Picard.*
%_datadir/metainfo/org.musicbrainz.Picard.appdata.xml
%python3_sitelibdir/%name
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Thu Oct 08 2026 Andrew A. Vasilyev <andy@altlinux.org> 3.0.1-alt1
- release-3.0.1

* Wed Jul 08 2026 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.13.3-alt2
- Backported upstream commit to fix test with Python 3.14.

* Wed Apr 15 2026 Andrew A. Vasilyev <andy@altlinux.org> 2.13.3-alt1
- Initial build for ALT.

