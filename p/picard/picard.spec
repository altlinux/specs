
%define autoupdate_on      'disable-autoupdate', None
%define autoupdate_off     'disable-autoupdate', True
%define selfauto_on        self.disable_autoupdate = None
%define selfauto_off       self.disable_autoupdate = True

%def_enable check

Name: picard
Version: 2.13.3
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
# BuildRequires: discid
%if_enabled check
BuildRequires: python3(dateutil)
BuildRequires: python3(fasteners)
BuildRequires: python3(jwt)
BuildRequires: python3(makefun)
BuildRequires: python3(markdown)
BuildRequires: python3(mutagen)
BuildRequires: python3(PyQt5)
BuildRequires: python3(pytest)
BuildRequires: python3(yaml)
BuildRequires: python3-module-charset-normalizer
BuildRequires: xvfb-run
%endif

Requires: hicolor-icon-theme

%description
Picard is an audio tagging application using data from the MusicBrainz
database. The tagger is album or release oriented, rather than
track-oriented.

%prep
%setup

%build
sed -r -i -e "s|%{autoupdate_on}|%{autoupdate_off}|g" \
          -e "s|%{selfauto_on}|%{selfauto_off}|g" setup.py
%pyproject_build

%install
%pyproject_install

desktop-file-install \
  --delete-original --remove-category="Application"   \
  --dir=%buildroot%_datadir/applications      \
  %buildroot%_datadir/applications/*

rm -r %buildroot%_datadir/locale/{es_419,zh-Hans,zh_Hans,zh_Hant}

%find_lang %name
%find_lang %name-attributes
%find_lang %name-constants
%find_lang %name-countries
cat %name-attributes.lang %name-constants.lang %name-countries.lang >> %name.lang

%check
%pyproject_run_pytest

%files -f %name.lang
%doc AUTHORS.txt COPYING.txt
%_bindir/picard
%_datadir/applications/org.musicbrainz.Picard.desktop
%_datadir/icons/hicolor/*/apps/org.musicbrainz.Picard.*
%_datadir/metainfo/org.musicbrainz.Picard.appdata.xml
%python3_sitelibdir/%name
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Wed Apr 15 2026 Andrew A. Vasilyev <andy@altlinux.org> 2.13.3-alt1
- Initial build for ALT.

