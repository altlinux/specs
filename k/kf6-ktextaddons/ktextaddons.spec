%define rname ktextaddons
%define sover 1
%define libkf6textaddonswidgets libkf6textaddonswidgets%sover
%define libkf6texttranslator libkf6texttranslator%sover
%define libkf6textedittexttospeech libkf6textedittexttospeech%sover
%define libkf6textgrammarcheck libkf6textgrammarcheck%sover
%define libkf6textemoticonscore libkf6textemoticonscore%sover
%define libkf6textemoticonswidgets libkf6textemoticonswidgets%sover
%define libkf6textautocorrectionwidgets libkf6textautocorrectionwidgets%sover
%define libkf6textautocorrectioncore libkf6textautocorrectioncore%sover
%define libkf6textutils libkf6textutils%sover
%define libkf6textcustomeditor libkf6textcustomeditor%sover
%define libtextautogenerateollama libtextautogenerateollama%sover
%define libkf6textspeechtotext libkf6textspeechtotext%sover
%define libkf6textautogeneratetext libkf6textautogeneratetext%sover
%define libtextautogenerategenericnetwork libtextautogenerategenericnetwork

%define libtextautogenerateollamacloud libtextautogenerateollamacloud%sover
%define libtextautogenerateollamacommon libtextautogenerateollamacommon%sover
%define libtextautogenerateollamaonline libtextautogenerateollamaonline%sover

%define rccopy_sover 0
%define libtextutils_cmark_rc_copy libtextutils-cmark-rc-copy%rccopy_sover

Name: kf6-%rname
Version: 2.0.2
Release: alt1
%K6init no_altplace

Group: System/Libraries
Summary: Various text handling addons
Url: https://invent.kde.org/libraries/ktextaddons
License: CC0-1.0 AND LGPL-2.0-or-later AND GPL-2.0-or-later AND BSD-3-Clause

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: qt6-speech-devel qt6-tools-devel qt6-declarative-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf6-karchive-devel kf6-kcoreaddons-devel kf6-ki18n-devel kf6-kxmlgui-devel kf6-kio-devel
BuildRequires: kf6-sonnet-devel kf6-syntax-highlighting-devel kf6-ktextwidgets-devel kf6-kiconthemes-devel
BuildRequires: libqtkeychain-qt6-devel

%description
Various text handling addons

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Configuration/Other
%description common
Common %name files

%package -n %libkf6textaddonswidgets
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkf6textaddonswidgets
%name library

%package -n %libkf6texttranslator
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkf6texttranslator
%name library

%package -n %libkf6textedittexttospeech
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkf6textedittexttospeech
%name library

%package -n %libkf6textgrammarcheck
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkf6textgrammarcheck
%name library

%package -n %libkf6textemoticonscore
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkf6textemoticonscore
%name library

%package -n %libkf6textemoticonswidgets
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkf6textemoticonswidgets
%name library

%package -n %libkf6textautocorrectionwidgets
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkf6textautocorrectionwidgets
%name library

%package -n %libkf6textautocorrectioncore
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkf6textautocorrectioncore
%name library

%package -n %libkf6textutils
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkf6textutils
%name library

%package -n %libkf6textcustomeditor
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkf6textcustomeditor
%name library

%package -n %libkf6textautogeneratetext
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkf6textautogeneratetext
%name library

%package -n %libkf6textspeechtotext
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libkf6textspeechtotext
%name library

%package -n %libtextautogenerateollama
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libtextautogenerateollama
%name library

%package -n %libtextutils_cmark_rc_copy
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Obsoletes: libtextautogenerate-cmark-rc-copy0 < %EVR
%description -n %libtextutils_cmark_rc_copy
%name library

%package -n %libtextautogenerategenericnetwork
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libtextautogenerategenericnetwork
%name library

%package -n %libtextautogenerateollamacloud
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libtextautogenerateollamacloud
%name library

%package -n %libtextautogenerateollamacommon
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libtextautogenerateollamacommon
%name library

%package -n %libtextautogenerateollamaonline
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libtextautogenerateollamaonline
%name library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: libgcrypt-devel libqca-qt6-devel qt6-speech-devel
%description devel
This package contains the development files for %name.


%prep
%setup -qn %rname-%version

for f in text*/CMakeLists.txt ; do
    sed -i '/DTRANSLATION_DOMAIN/s|\\")|6\\")|' $f
done

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    #

%install
%K6install
for f in %buildroot/%_K6i18n/*/LC_MESSAGES/*.mo ; do
    cutname=`echo "$f" | sed 's|.mo$||'`
    mv $f ${cutname}6.mo
done
%find_lang --with-kde --all-name %name


%files common -f %name.lang
%_datadir/qlogging-categories6/*.*categories

%files
%dir %_K6plug/kf6/translator/
%_K6plug/kf6/translator/translator_*.so
%_K6plug/kf6/speechtotext/speechtotext_*.so
%_K6plug/kf6/textautogeneratetext/autogeneratetext_*.so

%files -n %libtextutils_cmark_rc_copy
%_K6lib/libtextutils-cmark-rc-copy.so.*
%_K6lib/libtextutils-cmark-rc-copy.so.%rccopy_sover
%files -n %libtextautogenerategenericnetwork
%_K6lib/libtextautogenerategenericnetwork.so.*
%_K6lib/libtextautogenerategenericnetwork.so.%sover
%files -n %libkf6textaddonswidgets
%_K6lib/libKF6TextAddonsWidgets.so.*
%_K6lib/libKF6TextAddonsWidgets.so.%sover
%files -n %libkf6texttranslator
%_K6lib/libKF6TextTranslator.so.*
%_K6lib/libKF6TextTranslator.so.%sover
%files -n %libkf6textedittexttospeech
%_K6lib/libKF6TextEditTextToSpeech.so.*
%_K6lib/libKF6TextEditTextToSpeech.so.%sover
%files -n %libkf6textgrammarcheck
%_K6lib/libKF6TextGrammarCheck.so.*
%_K6lib/libKF6TextGrammarCheck.so.%sover
%files -n %libkf6textemoticonscore
%_K6lib/libKF6TextEmoticonsCore.so.*
%_K6lib/libKF6TextEmoticonsCore.so.%sover
%files -n %libkf6textemoticonswidgets
%_K6lib/libKF6TextEmoticonsWidgets.so.*
%_K6lib/libKF6TextEmoticonsWidgets.so.%sover
%files -n %libkf6textautocorrectionwidgets
%_K6lib/libKF6TextAutoCorrectionWidgets.so.*
%_K6lib/libKF6TextAutoCorrectionWidgets.so.%sover
%files -n %libkf6textautocorrectioncore
%_K6lib/libKF6TextAutoCorrectionCore.so.*
%_K6lib/libKF6TextAutoCorrectionCore.so.%sover
%files -n %libkf6textutils
%_K6lib/libKF6TextUtils.so.*
%_K6lib/libKF6TextUtils.so.%sover
%files -n %libkf6textcustomeditor
%_K6lib/libKF6TextCustomEditor.so.*
%_K6lib/libKF6TextCustomEditor.so.%sover
%files -n %libtextautogenerateollama
%_K6lib/libtextautogenerateollama.so.*
%_K6lib/libtextautogenerateollama.so.%sover
%files -n %libkf6textspeechtotext
%_K6lib/libKF6TextSpeechToText.so.*
%_K6lib/libKF6TextSpeechToText.so.%sover
%files -n %libkf6textautogeneratetext
%_K6lib/libKF6TextAutoGenerateText.so.*
%_K6lib/libKF6TextAutoGenerateText.so.%sover
%files -n %libtextautogenerateollamacloud
%_K6lib/libtextautogenerateollamacloud.so.*
%_K6lib/libtextautogenerateollamacloud.so.%sover
%files -n %libtextautogenerateollamacommon
%_K6lib/libtextautogenerateollamacommon.so.*
%_K6lib/libtextautogenerateollamacommon.so.%sover
%files -n %libtextautogenerateollamaonline
%_K6lib/libtextautogenerateollamaonline.so.*
%_K6lib/libtextautogenerateollamaonline.so.%sover

%files devel
%_K6plug/designer/*text*.so
%_K6inc/Text*/
%_K6link/lib*.so
%_libdir/cmake/*ext*/
#%_K6archdata/mkspecs/modules/qt_?ext*.pri

%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt1
- new version

* Thu Mar 19 2026 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1
- new version

* Wed Mar 04 2026 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt1
- new version

* Wed Feb 25 2026 Sergey V Turchin <zerg@altlinux.org> 1.9.1-alt1
- new version

* Wed Feb 04 2026 Sergey V Turchin <zerg@altlinux.org> 1.9.0-alt2
- update requires

* Mon Jan 12 2026 Sergey V Turchin <zerg@altlinux.org> 1.9.0-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 1.8.0-alt1
- new version

* Mon Jul 14 2025 Sergey V Turchin <zerg@altlinux.org> 1.6.0-alt1
- new version

* Wed Sep 11 2024 Sergey V Turchin <zerg@altlinux.org> 1.5.4-alt1
- initial build
