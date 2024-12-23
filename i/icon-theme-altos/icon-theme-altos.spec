Name: icon-theme-altos
Version: 0.1.1
Release: alt1

Group: Graphics
Summary: ALT icons theme
Url: https://altlinux.org
License: GPL-3.0 and LGPL-2.1

BuildArch: noarch

PreReq(post,preun): alternatives >= 0.2
Requires: icon-theme-breeze menu-icons-default

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++ qt6-base-devel
BuildRequires: icon-naming-utils xml-utils python3-module-lxml
BuildRequires: hardlink

%description
%summary.

%prep
%setup

# kiconthemes5 compatibility
#find . -type f -name '*.svg' | xargs sed -i 's/ColorScheme-Accent/ColorScheme-Highlight/'

%build
%K6build

%install
%K6install

%if 0
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
%endif

# fix broken symlinks
find %buildroot/%_iconsdir -type l | \
while read l ; do
    [ -e $l ] || rm -f $l
done

# add icons alternatives
mkdir -p %buildroot/%_sysconfdir/alternatives/packages.d/
> %buildroot/%_sysconfdir/alternatives/packages.d/%name
for n in alt-distro-logo alterator alt-main-menu ; do
ln -sr %buildroot/%_iconsdir/hicolor/scalable/apps/basealt.svg %buildroot/%_iconsdir/altos/apps/16/${n}.svg
ln -sr %buildroot/%_iconsdir/hicolor/scalable/apps/basealt.svg %buildroot/%_iconsdir/altos-dark/apps/16/${n}.svg
cat >> %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_iconsdir/altos/apps/16/${n}.svg %_iconsdir/hicolor/scalable/apps/basealt.svg 1
%_iconsdir/altos-dark/apps/16/${n}.svg %_iconsdir/hicolor/scalable/apps/basealt.svg 1
__EOF__
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
%doc COPYING* AUTHORS
%config %_sysconfdir/alternatives/packages.d/%name
%_iconsdir/altos/
%_iconsdir/altos-dark/

%changelog
* Mon Dec 23 2024 Sergey V Turchin <zerg at altlinux dot org> 0.1.1-alt1
- add branding icons alternatives

* Mon Dec 16 2024 Sergey V Turchin <zerg at altlinux dot org> 0.1.0-alt1
- update icons

* Thu Dec 05 2024 Sergey V Turchin <zerg at altlinux dot org> 0.0.2-alt2
- don't create symlinks for aliases

* Tue Nov 05 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 0.0.2-alt1
- add icons themes

* Fri Nov 01 2024 Sergey V Turchin <zerg at altlinux dot org> 0.0.1-alt1
- initial build
