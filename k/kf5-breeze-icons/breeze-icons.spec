%define rname breeze-icons

Name: kf5-%rname
Version: 5.19.0
Release: alt2
%K5init no_altplace

Group: Graphical desktop/KDE
Summary: Breeze icons theme
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

BuildArch: noarch

Source: %rname-%version.tar
Patch1: alt-icons-defaults.patch

# Automatically added by buildreq on Fri Dec 11 2015 (-bi)
# optimized out: cmake cmake-modules gtk-update-icon-cache libqt5-core libstdc++-devel perl-Encode perl-XML-LibXML perl-XML-SAX perl-XML-SAX-Base perl-XML-Simple perl-parent python-base python3 python3-base
#BuildRequires: extra-cmake-modules gcc-c++ icon-naming-utils qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++ qt5-base-devel
BuildRequires: icon-naming-utils

%description
%summary

%package -n icon-theme-breeze
Summary: Breeze icons theme
Group: Graphics
%description -n icon-theme-breeze
%summary


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install

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

# fix broken symlinks
find %buildroot/%_iconsdir -type l | \
while read l ; do
    [ -e $l ] || rm -f $l
done

%files -n icon-theme-breeze
%_iconsdir/breeze*/

%changelog
* Fri Feb 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.19.0-alt2
- fix icon-name-mapping usage

* Tue Feb 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.19.0-alt1
- new version

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.18.0-alt1
- new version

* Fri Dec 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Fri Dec 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.16.0-alt1
- initial build
