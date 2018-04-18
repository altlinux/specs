%define origname krename

Name: kde5-%origname
Version: 5.0.0
Release: alt2%ubt

Summary: A powerful batch renamer for KDE5
Group: File tools
License: GPL
Url: https://userbase.kde.org/KRename

Source: %origname-%version.tar

BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: kf5-kcompletion-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kcrash-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kitemviews-devel kf5-kjobwidgets-devel
BuildRequires: kf5-kjs-devel kf5-kio-devel kf5-kservice-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: libexiv2-devel libfreetype-devel libpodofo-devel libtag-devel
BuildRequires: qt5-base-devel

%description
Krename is a very powerful batch file renamer for KDE5 which can rename a list
of files based on a set of expressions. It can copy/move the files to another
directory or simply rename the input files. Krename supports many conversion
operations, including conversion of a filename to lowercase or to uppercase,
conversion of the first letter of every word to uppercase, adding numbers to
filenames, finding and replacing parts of the filename, and many more.
It can also change access and modification dates, permissions, and file ownership.

%prep
%setup -n %origname-%version

%build
%K5build

%install
%K5install
%find_lang --all-name --with-kde %origname

%files -f %origname.lang
%_K5bin/%origname
%_K5xdgapp/*.desktop
%_K5icon/*/*/apps/*.png
%_K5srv/*

%changelog
* Wed Apr 18 2018 Oleg Solovyov <mcpain@altlinux.org> 5.0.0-alt2%ubt
- add %%ubt tag for backporting

* Mon Apr 16 2018 Oleg Solovyov <mcpain@altlinux.org> 5.0.0-alt1
- initial build for ALT

