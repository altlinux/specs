%define _unpackaged_files_terminate_build 1

Name: angrysearch
Version: 1.0.4
Release: alt1

Summary: Linux file search, instant results as you type
License: GPL-2.0-only
Group: File tools
URL: https://github.com/DoTheEvo/ANGRYsearch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
Attempt at making Linux version of Everything Search Engine because
no one else bothered.

Everyone seems to be damn content with searches that are slow,
populating results as they go; or are cli based, making it difficult
to comfortably make use of the results; or are heavily integrated
with a file manager, often limiting search to just home; or are
trying to be everything with full-text file's content search.

%prep
%setup
sed -i "s/Categories=.*/Categories=Utility;FileTools;/" angrysearch.desktop

%build
%pyproject_build

%install
%pyproject_install

mkdir -pv %buildroot%_datadir/angrysearch
mkdir -pv %buildroot%_desktopdir
mkdir -pv %buildroot%_iconsdir/hicolor/scalable/apps

mv -v %buildroot%python3_sitelibdir/usr/share/angrysearch/angrysearch.svg %buildroot%_datadir/angrysearch/
mv -v %buildroot%python3_sitelibdir/usr/share/angrysearch/qdarkstylesheet.qss %buildroot%_datadir/angrysearch/
mv -v %buildroot%python3_sitelibdir/usr/share/applications/angrysearch.desktop %buildroot%_desktopdir/
mv -v %buildroot%python3_sitelibdir/usr/share/pixmaps/angrysearch.svg %buildroot%_iconsdir/hicolor/scalable/apps/

%files
%doc LICENSE README.md
%_bindir/angrysearch
%exclude %python3_sitelibdir/__pycache__
%python3_sitelibdir/angrysearch.py
%python3_sitelibdir/angrysearch_update_database.py
%python3_sitelibdir/resource_file.py
%python3_sitelibdir/scandir.py
%python3_sitelibdir/%{pyproject_distinfo %name}
%dir %_datadir/angrysearch
%_datadir/angrysearch/angrysearch.svg
%_datadir/angrysearch/qdarkstylesheet.qss
%_desktopdir/angrysearch.desktop
%_iconsdir/hicolor/scalable/apps/angrysearch.svg

%changelog
* Sat Dec 06 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus
