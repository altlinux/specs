%define rname ktextaddons
%define sover 1
%define libkf5textaddonswidgets libkf5textaddonswidgets%sover
%define libkf5texttranslator libkf5texttranslator%sover
%define libkf5textedittexttospeech libkf5textedittexttospeech%sover
%define libkf5textgrammarcheck libkf5textgrammarcheck%sover
%define libkf5textemoticonscore libkf5textemoticonscore%sover
%define libkf5textemoticonswidgets libkf5textemoticonswidgets%sover
%define libkf5textautocorrectionwidgets libkf5textautocorrectionwidgets%sover
%define libkf5textautocorrectioncore libkf5textautocorrectioncore%sover
%define libkf5textutils libkf5textutils%sover
%define libkf5textcustomeditor libkf5textcustomeditor%sover

Name: kde5-%rname
Version: 1.5.2
Release: alt2
%K5init altplace

Group: System/Libraries
Summary: Various text handling addons
Url: https://invent.kde.org/libraries/ktextaddons
License: CC0-1.0 AND LGPL-2.0-or-later AND GPL-2.0-or-later AND BSD-3-Clause

Source: %rname-%version.tar

# Automatically added by buildreq on Mon May 29 2023 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kwidgetsaddons-devel libctf-nobfd0 libglvnd-devel libgpg-error libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-texttospeech libqt5-waylandclient libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-devel rpm-build-file rpm-build-python3 rpm-macros-python sh4 tzdata
#BuildRequires: appstream clang-tools extra-cmake-modules kf5-karchive-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kxmlgui-devel libqtkeychain-qt5-devel python-modules-compiler python3-module-mpl_toolkits python3-module-setuptools python3-module-zope qt5-imageformats qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-webengine-devel tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: kf5-karchive-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kxmlgui-devel kf5-kio-devel
BuildRequires: kf5-sonnet-devel kf5-syntax-highlighting-devel
BuildRequires: libqtkeychain-qt5-devel
BuildRequires: qt5-speech-devel qt5-tools-devel

%description
Various text handling addons

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Configuration/Other
%description common
Common %name files

%package -n %libkf5textaddonswidgets
Summary: %name library
Group: System/Libraries
Requires: %name-common
%description -n %libkf5textaddonswidgets
%name library

%package -n %libkf5texttranslator
Summary: %name library
Group: System/Libraries
Requires: %name-common
%description -n %libkf5texttranslator
%name library

%package -n %libkf5textedittexttospeech
Summary: %name library
Group: System/Libraries
Requires: %name-common
%description -n %libkf5textedittexttospeech
%name library

%package -n %libkf5textgrammarcheck
Summary: %name library
Group: System/Libraries
Requires: %name-common
%description -n %libkf5textgrammarcheck
%name library

%package -n %libkf5textemoticonscore
Summary: %name library
Group: System/Libraries
Requires: %name-common
%description -n %libkf5textemoticonscore
%name library

%package -n %libkf5textemoticonswidgets
Summary: %name library
Group: System/Libraries
Requires: %name-common
%description -n %libkf5textemoticonswidgets
%name library

%package -n %libkf5textautocorrectionwidgets
Summary: %name library
Group: System/Libraries
Requires: %name-common
%description -n %libkf5textautocorrectionwidgets
%name library

%package -n %libkf5textautocorrectioncore
Summary: %name library
Group: System/Libraries
Requires: %name-common
%description -n %libkf5textautocorrectioncore
%name library

%package -n %libkf5textutils
Summary: %name library
Group: System/Libraries
Requires: %name-common
%description -n %libkf5textutils
%name library

%package -n %libkf5textcustomeditor
Summary: %name library
Group: System/Libraries
Requires: %name-common
%description -n %libkf5textcustomeditor
%name library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: libgcrypt-devel libqca-qt5-devel
%description devel
This package contains the development files for %name.


%prep
%setup -qn %rname-%version
#%patch1 -p1

%build
%K5build \
    #

%install
%K5install
%find_lang --with-kde --all-name %name


%files common -f %name.lang
%_datadir/qlogging-categories5/*.*categories

%files
%_K5plug/kf5/translator/translator_*.so

%files -n %libkf5textaddonswidgets
%_K5lib/libKF5TextAddonsWidgets.so.*
%_K5lib/libKF5TextAddonsWidgets.so.%sover
%files -n %libkf5texttranslator
%_K5lib/libKF5TextTranslator.so.*
%_K5lib/libKF5TextTranslator.so.%sover
%files -n %libkf5textedittexttospeech
%_K5lib/libKF5TextEditTextToSpeech.so.*
%_K5lib/libKF5TextEditTextToSpeech.so.%sover
%files -n %libkf5textgrammarcheck
%_K5lib/libKF5TextGrammarCheck.so.*
%_K5lib/libKF5TextGrammarCheck.so.%sover
%files -n %libkf5textemoticonscore
%_K5lib/libKF5TextEmoticonsCore.so.*
%_K5lib/libKF5TextEmoticonsCore.so.%sover
%files -n %libkf5textemoticonswidgets
%_K5lib/libKF5TextEmoticonsWidgets.so.*
%_K5lib/libKF5TextEmoticonsWidgets.so.%sover
%files -n %libkf5textautocorrectionwidgets
%_K5lib/libKF5TextAutoCorrectionWidgets.so.*
%_K5lib/libKF5TextAutoCorrectionWidgets.so.%sover
%files -n %libkf5textautocorrectioncore
%_K5lib/libKF5TextAutoCorrectionCore.so.*
%_K5lib/libKF5TextAutoCorrectionCore.so.%sover
%files -n %libkf5textutils
%_K5lib/libKF5TextUtils.so.*
%_K5lib/libKF5TextUtils.so.%sover
%files -n %libkf5textcustomeditor
%_K5lib/libKF5TextCustomEditor.so.*
%_K5lib/libKF5TextCustomEditor.so.%sover


%files devel
%_K5plug/designer/*text*.so
%_K5inc/Text*/
%_K5link/lib*.so
%_libdir/cmake/KF5Text*/
%_K5archdata/mkspecs/modules/qt_?ext*.pri

%changelog
* Tue Dec 12 2023 Sergey V Turchin <zerg@altlinux.org> 1.5.2-alt2
- update russian translation

* Tue Dec 12 2023 Sergey V Turchin <zerg@altlinux.org> 1.5.2-alt1
- new version

* Mon May 29 2023 Sergey V Turchin <zerg@altlinux.org> 1.3.2-alt1
- initial build
