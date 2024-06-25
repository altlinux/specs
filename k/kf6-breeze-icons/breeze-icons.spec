%define rname breeze-icons

Name: kf6-%rname
Version: 6.3.0
Release: alt2
%K6init no_altplace

Group: Graphical desktop/KDE
Summary: Breeze icons theme
Url: http://www.kde.org
License: LGPL-3.0-only

Source: %rname-%version.tar
Patch1: alt-icons-defaults.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++ qt6-base-devel
BuildRequires: icon-naming-utils xml-utils python3-module-lxml

%description
%summary

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package -n icon-theme-breeze
Summary: Breeze icons theme
Group: Graphics
BuildArch: noarch
Provides: kde4-icon-theme = %version-%release
Provides: kde-icon-theme = %version-%release
%description -n icon-theme-breeze
%summary

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package files for developing applications that use %name.


%package -n libkf6breezeicons
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6breezeicons
KF6 library

%prep
%setup -n %rname-%version
%patch1 -p1

chmod a+x *.sh

# remove some icons
for n in 'yandex-browser.*' ; do
    find ./ -type f -name $n | while read f; do rm -f $f;  done
done

%build
%K6build \
    -DBINARY_ICONS_RESOURCE:BOOL=ON \
    #

%install
%K6install

# 5858 7498
for t in %buildroot/%_iconsdir/* ; do
    [ -d $t ] || continue
    theme_subdir=`basename $t`
    mkdir %buildroot/%_iconsdir/tmp-$theme_subdir
    pushd $t
    ls -1d */* | \
    while read subdir ; do
	[ -d $subdir ] || continue
	ctx=`dirname $subdir`
	sz=`basename $subdir`
	mkdir -p %buildroot/%_iconsdir/tmp-$theme_subdir/$sz
	ln -s $t/$ctx/$sz %buildroot/%_iconsdir/tmp-$theme_subdir/$sz/$ctx
    done
    popd
done

for t in %buildroot/%_iconsdir/tmp-* ; do
    [ -d $t ] || continue
    pushd $t
	ls -1d * | \
	while read sz ; do
	    [ -d $sz ] || continue
	    pushd $sz
	    ls -1d * | \
	    while read ctx ; do
		[ -d $ctx ] || continue
		%_libexecdir/icon-name-mapping -c $ctx
	    done
	    popd
	done
    popd
done

rm -rf %buildroot/%_iconsdir/tmp-*

# remove unappropriate icons symlinks
for i in calc
do
    find %buildroot/%_iconsdir -type l \( -name ${i}.png -o -name ${i}.svg \) | \
	while read f; do rm -f ${f} ||: ; done
done

# fix broken symlinks
find %buildroot/%_iconsdir -type l | \
while read l ; do
    [ -e $l ] || rm -f $l
done

# create custom icons
for e in \
    "inode-directory application-x-smb-share" \
    #
do
    icon_from=`echo "$e"| cut -d\  -f1`
    icon_to=`echo "$e"| cut -d\  -f2`
    find %buildroot/%_iconsdir/ -name ${icon_from}.svg | \
    while read p; do
	icon_dir=`dirname $p`
	ln -s ${icon_from}.svg $icon_dir/${icon_to}.svg ||:
    done
done

%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING* README.md

%files -n icon-theme-breeze
%_iconsdir/breeze*/

%files devel
%_libdir/cmake/KF6BreezeIcons/
%_K6link/lib*.so
%_K6inc/BreezeIcons/

%files -n libkf6breezeicons
%_K6lib/libKF6BreezeIcons.so.*

%changelog
* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt2
- package binary icons resource file

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

