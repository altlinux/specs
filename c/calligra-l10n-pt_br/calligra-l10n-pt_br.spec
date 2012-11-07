%define lng pt_BR
%define lngpkg pt_br
%define lngg Brazil Portuguese

Name: calligra-l10n-%lngpkg
Version: 2.5.3
Release: alt1
%define beta %nil

Group: Graphical desktop/KDE
Summary: %lngg language support for Calligra
License: GPL
Url: http://www.calligra.org/

Provides: calligra-i18n-%lngpkg = %version-%release
Provides: calligra-i18n-%lng = %version-%release
Provides: calligra-i18n-lang = %version-%release
Provides: koffice-i18n-%lng = %version-%release
Obsoletes: koffice-i18n-%lng < %version-%release
Requires: calligra-common

Source: calligra-l10n-%lngpkg-%version.tar

BuildArch: noarch
BuildRequires: gcc-c++ kde4base-runtime-devel kde4libs-devel

%description
%lngg language support for Calligra.


%prep
%setup -q
find -type f -name CMakeLists.txt | \
while read cm; do
    dirs=`grep add_subdirectory "$cm" | sed 's|.*[(]\(.*\)[)].*|\1|'`
    if [ -n "$dirs" ]; then
	pushd `dirname "$cm"`
	for d in $dirs; do
	    mkdir -p $d
	done
	popd
    fi
done

%build
%K4build

%install
%K4install

%files
%lang(%lng) %_K4i18n/%lng/LC_MESSAGES/*.mo
%lang(%lng) %_K4doc/%lng
#%lang(%lng) %_K4apps/calligra/autocorrect/%{lng}*.xml

%changelog
* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.3-alt1
- initial build
