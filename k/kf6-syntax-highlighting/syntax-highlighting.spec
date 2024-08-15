%define rname syntax-highlighting

Name: kf6-%rname
Version: 6.4.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 syntax highlighting engine
Url: http://www.kde.org
License: GPL-2.0-only and LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules  qt6-declarative-devel qt6-tools-devel
BuildRequires: perl-Encode


%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6syntaxhighlighting
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6syntaxhighlighting
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/ksyntaxhighlighter*
%_bindir/ksyntaxhighlighter*

%files devel
%_K6inc/KSyntaxHighlighting/
%_K6link/lib*.so
%_K6lib/cmake/KF6SyntaxHighlighting/

%files -n libkf6syntaxhighlighting
%_K6lib/libKF6SyntaxHighlighting.so.*
%_K6qml/org/kde/syntaxhighlighting/


%changelog
* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

