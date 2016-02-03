
%define lng ru
%define lngg Russian

Name: kf5-i18n-%lng
Version: 5.5.4
Release: alt2

Group: Graphical desktop/KDE
Summary: %lngg language support for KDE Workspace
License: GPL
Url: http://www.kde.org/

Requires: kf5-filesystem
BuildArch: noarch

Source0: kf5-l10n-%lng-messages-%version.tar
Source1: kf5-l10n-%lng-docs-%version.tar
Source100: template-main
Source101: template-messages

Patch1: alt-userswitcher.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: libdb4-devel qt5-tools-devel
BuildRequires: kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-ki18n-devel

%description
%lngg language support for KDE.


%prep
%setup -T -c -n %name-%version -a0 -a1
for d in *-l10n-* ; do
    simplename=`echo "$d" | sed -e 's|^kf5-l10n-%lng-||' -e 's|-[[:digit:]].*||'`
    mv $d $simplename
done

pushd messages
%patch1 -p0
popd

find docs -type d | \
while read d ; do
    pushd $d
    if [ -f index.docbook ] ; then
	echo "kdoctools_create_handbook(index.docbook INSTALL_DESTINATION \${HTML_INSTALL_DIR}/\${CURRENT_LANG}/ SUBDIR `basename $d` )" >CMakeLists.txt
    elif [ -n "`find ./* -type d`" ] ; then
	ls -1d * | \
	while read docd ; do
	    [ -d "$docd" ] || continue
	    echo "add_subdirectory( $docd )" >>CMakeLists.txt
	done
    else
	echo >CMakeLists.txt
    fi
    popd
done

cat %SOURCE101 >messages/CMakeLists.txt

cat %SOURCE100 >CMakeLists.txt
sed -i 's|@LANGSHORT@|%lng|' CMakeLists.txt
ls -1d * | \
while read d ; do
    [ -d "$d" ] || continue
    echo "add_subdirectory( $d )" >> CMakeLists.txt
done


%build
%K5build


%install
%K5install
%K5install_move data all

%files
%dir %_K5doc/%lng/
%lang(%lng) %_K5doc/%lng/*
#
%dir %_K5i18n/%lng/
#%_K5i18n/%lng/entry.desktop
#
%dir %_K5i18n/%lng/LC_MESSAGES/
%lang(%lng) %_K5i18n/%lng/LC_MESSAGES/*.mo
#%lang(%lng) %_K5i18n/%lng/LC_MESSAGES/*.qm
#%dir %_K5i18n/%lng/LC_SCRIPTS/
#%lang(%lng) %_K5i18n/%lng/LC_SCRIPTS/*
#
#%lang(%lng) %_K5data/autocorrect/%{lng}_*.xml

%changelog
* Wed Feb 03 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt2
- update user switcher translation

* Tue Feb 02 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- initial build
