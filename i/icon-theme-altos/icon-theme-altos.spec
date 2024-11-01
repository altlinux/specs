Name: icon-theme-altos
Version: 0.0.1
Release: alt1

Group: Graphics
Summary: ALT icons theme
Url: http://www.kde.org
License: LGPL-3.0-only

BuildArch: noarch

Requires: icon-theme-breeze

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: icon-naming-utils xml-utils python3-module-lxml
BuildRequires: hardlink

%description
%summary.

%prep
%setup

# kiconthemes5 compatibility
#find . -type f -name '*.svg' | xargs sed -i 's/ColorScheme-Accent/ColorScheme-Highlight/'

%build
#%cmake_build

%install
#%cmake_install
# FAKE
touch COPYING-ICONS README.md
mkdir -p %buildroot/%_iconsdir/{altos,altos-dark,altos-cursors}
for t in altos altos-dark altos-cursors; do
    install -m 0644 index.theme %buildroot/%_iconsdir/$t/
    cp -ar actions %buildroot/%_iconsdir/$t/
done
sed -i '/^Inherits=.*/d' %buildroot/%_iconsdir/altos-cursors/index.theme
sed -i '/^Directories=.*/d' %buildroot/%_iconsdir/altos-cursors/index.theme
sed -i 's|^Inherits=.*|Inherits=breeze,hicolor|' %buildroot/%_iconsdir/altos/index.theme
sed -i 's|^Name=.*|Name=ALT OS|'            %buildroot/%_iconsdir/altos/index.theme
sed -i 's|^Inherits=.*|Inherits=breeze-dark,hicolor|' %buildroot/%_iconsdir/altos-dark/index.theme
sed -i 's|^Name=.*|Name=ALT OS Dark|'                 %buildroot/%_iconsdir/altos-dark/index.theme
# END FAKE

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

# optimize disk space
hardlink -c -v %buildroot/%_iconsdir/

%files
%doc COPYING* README.md
%_iconsdir/altos/
%_iconsdir/altos-dark/
%_iconsdir/altos-cursors/

%changelog
* Fri Nov 01 2024 Sergey V Turchin <zerg at altlinux dot org> 0.0.1-alt1
- initial build
