%define rname oxygen-icons

Name: kf5-oxygen-icons
Version: 6.1.0
Release: alt1
%K6init no_altplace

Group: Graphical desktop/KDE
Summary: Oxygen icons theme
Url: http://www.kde.org
License: LGPL-2.1-or-later

BuildArch: noarch

Source: %rname-%version.tar
Patch1: alt-icons-defaults.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++ qt6-base-devel
BuildRequires: icon-naming-utils

%description
%summary

%package -n icon-theme-oxygen
Summary: Oxygen icons theme
Group: Graphics
%description -n icon-theme-oxygen
%summary


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build

%install
%K6install

# 6971
for t in %buildroot/%_iconsdir/* ; do
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

# fix broken symlinks
find %buildroot/%_iconsdir -type l | \
while read l ; do
    [ -e $l ] || rm -f $l
done

# clean "package" icon
if [ -z "`find %buildroot/%_iconsdir -name package-installed-updated.\*`" ] ; then
    find %buildroot/%_iconsdir -name package.\* | \
    while read f ; do
	rm -f "$f"
    done
fi

# create custom icons
for e in \
    "inode-directory application-x-smb-share" \
    #
do
    icon_from=`echo "$e"| cut -d\  -f1`
    icon_to=`echo "$e"| cut -d\  -f2`
    find %buildroot/%_iconsdir/ -type f -name ${icon_from}.png | \
    while read p; do
	icon_dir=`dirname $p`
	ln -s ${icon_from}.png $icon_dir/${icon_to}.png ||:
    done
done

%files -n icon-theme-oxygen
%doc COPYING*
%_iconsdir/oxygen*/

%changelog
* Tue Oct 22 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- new version

* Fri Jul 12 2024 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt1
- new version

* Thu May 23 2024 Sergey V Turchin <zerg@altlinux.org> 5.116.0-alt1
- new version

* Mon Feb 12 2024 Sergey V Turchin <zerg@altlinux.org> 5.115.0-alt1
- new version

* Mon Jan 15 2024 Sergey V Turchin <zerg@altlinux.org> 5.114.0-alt1
- new version

* Fri Dec 15 2023 Sergey V Turchin <zerg@altlinux.org> 5.113.0-alt1
- new version

* Wed Nov 15 2023 Sergey V Turchin <zerg@altlinux.org> 5.112.0-alt1
- new version

* Thu Oct 19 2023 Sergey V Turchin <zerg@altlinux.org> 5.111.0-alt1
- new version

* Mon Sep 11 2023 Sergey V Turchin <zerg@altlinux.org> 5.110.0-alt1
- new version

* Thu Aug 31 2023 Sergey V Turchin <zerg@altlinux.org> 5.109.0-alt1
- new version

* Mon Jul 10 2023 Sergey V Turchin <zerg@altlinux.org> 5.108.0-alt1
- new version

* Wed Jul 05 2023 Sergey V Turchin <zerg@altlinux.org> 5.107.0-alt1
- new version

* Mon May 15 2023 Sergey V Turchin <zerg@altlinux.org> 5.106.0-alt1
- new version

* Mon Apr 10 2023 Sergey V Turchin <zerg@altlinux.org> 5.105.0-alt1
- new version

* Tue Mar 14 2023 Sergey V Turchin <zerg@altlinux.org> 5.104.0-alt1
- new version

* Mon Feb 13 2023 Sergey V Turchin <zerg@altlinux.org> 5.103.0-alt1
- new version

* Mon Jan 16 2023 Sergey V Turchin <zerg@altlinux.org> 5.102.0-alt1
- new version

* Mon Jan 09 2023 Sergey V Turchin <zerg@altlinux.org> 5.101.0-alt2
- add application-x-smb-share icon

* Fri Dec 16 2022 Sergey V Turchin <zerg@altlinux.org> 5.101.0-alt1
- new version

* Mon Nov 14 2022 Sergey V Turchin <zerg@altlinux.org> 5.100.0-alt1
- new version

* Tue Oct 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.99.0-alt1
- new version

* Mon Sep 12 2022 Sergey V Turchin <zerg@altlinux.org> 5.98.0-alt1
- new version

* Mon Aug 15 2022 Sergey V Turchin <zerg@altlinux.org> 5.97.0-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.96.0-alt1
- new version

* Tue Jun 14 2022 Sergey V Turchin <zerg@altlinux.org> 5.95.0-alt1
- new version

* Mon May 16 2022 Sergey V Turchin <zerg@altlinux.org> 5.94.0-alt1
- new version

* Mon Apr 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.93.0-alt1
- new version

* Mon Mar 14 2022 Sergey V Turchin <zerg@altlinux.org> 5.92.0-alt1
- new version

* Mon Feb 14 2022 Sergey V Turchin <zerg@altlinux.org> 5.91.0-alt1
- new version

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 5.90.0-alt1
- new version

* Thu Dec 16 2021 Sergey V Turchin <zerg@altlinux.org> 5.89.0-alt1
- new version

* Mon Nov 15 2021 Sergey V Turchin <zerg@altlinux.org> 5.88.0-alt1
- new version

* Mon Oct 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.87.0-alt1
- new version

* Mon Sep 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.86.0-alt1
- new version

* Mon Aug 16 2021 Sergey V Turchin <zerg@altlinux.org> 5.85.0-alt1
- new version

* Tue Jul 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.84.0-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.83.0-alt1
- new version

* Wed May 12 2021 Sergey V Turchin <zerg@altlinux.org> 5.82.0-alt1
- new version

* Mon Apr 12 2021 Sergey V Turchin <zerg@altlinux.org> 5.81.0-alt1
- new version

* Thu Mar 18 2021 Sergey V Turchin <zerg@altlinux.org> 5.80.0-alt1
- new version

* Mon Feb 15 2021 Sergey V Turchin <zerg@altlinux.org> 5.79.0-alt1
- new version

* Sun Jan 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.78.0-alt1
- new version

* Mon Dec 14 2020 Sergey V Turchin <zerg@altlinux.org> 5.77.0-alt1
- new version

* Mon Nov 16 2020 Sergey V Turchin <zerg@altlinux.org> 5.76.0-alt1
- new version

* Tue Oct 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.75.0-alt1
- new version

* Mon Sep 14 2020 Sergey V Turchin <zerg@altlinux.org> 5.74.0-alt1
- new version

* Tue Aug 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.73.0-alt1
- new version

* Thu Jul 23 2020 Sergey V Turchin <zerg@altlinux.org> 5.72.0-alt1
- new version

* Tue May 12 2020 Sergey V Turchin <zerg@altlinux.org> 5.70.0-alt1
- new version

* Wed Apr 15 2020 Sergey V Turchin <zerg@altlinux.org> 5.69.0-alt1
- new version

* Mon Mar 16 2020 Sergey V Turchin <zerg@altlinux.org> 5.68.0-alt1
- new version

* Mon Feb 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.67.0-alt1
- new version

* Mon Jan 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.66.0-alt1
- new version

* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.65.0-alt1
- new version

* Mon Nov 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.64.0-alt1
- new version

* Tue Oct 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.63.0-alt1
- new version

* Mon Sep 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.62.0-alt1
- new version

* Mon Aug 12 2019 Sergey V Turchin <zerg@altlinux.org> 5.61.0-alt1
- new version

* Mon Jul 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.60.0-alt1
- new version

* Tue Jun 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.59.0-alt1
- new version

* Mon Jun 03 2019 Sergey V Turchin <zerg@altlinux.org> 5.58.0-alt1
- new version

* Mon Apr 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.57.0-alt1
- new version

* Fri Mar 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.56.0-alt1
- new version

* Mon Feb 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.55.0-alt1
- new version

* Thu Jan 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.54.0-alt2
- new version

* Tue Jan 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.54.0-alt1
- new version

* Tue Dec 11 2018 Sergey V Turchin <zerg@altlinux.org> 5.53.0-alt1
- new version

* Mon Nov 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.52.0-alt1
- new version

* Wed Oct 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.51.0-alt1
- new version

* Mon Sep 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.50.0-alt1
- new version

* Tue Aug 21 2018 Sergey V Turchin <zerg@altlinux.org> 5.49.0-alt1
- new version

* Thu Jul 19 2018 Sergey V Turchin <zerg@altlinux.org> 5.48.0-alt1
- new version

* Fri Jun 15 2018 Sergey V Turchin <zerg@altlinux.org> 5.47.0-alt1
- new version

* Mon May 14 2018 Sergey V Turchin <zerg@altlinux.org> 5.46.0-alt1
- new version

* Fri May 04 2018 Sergey V Turchin <zerg@altlinux.org> 5.45.0-alt1
- new version

* Tue Mar 20 2018 Sergey V Turchin <zerg@altlinux.org> 5.44.0-alt1
- new version

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 5.42.0-alt1
- new version

* Tue Dec 12 2017 Sergey V Turchin <zerg@altlinux.org> 5.41.0-alt1
- new version

* Tue Nov 21 2017 Sergey V Turchin <zerg@altlinux.org> 5.40.0-alt1
- new version

* Tue Oct 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.39.0-alt1
- new version

* Wed Oct 04 2017 Sergey V Turchin <zerg@altlinux.org> 5.38.0-alt2
- remove package.png

* Tue Sep 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.38.0-alt1
- new version

* Wed Aug 16 2017 Sergey V Turchin <zerg@altlinux.org> 5.37.0-alt1
- new version

* Mon Jul 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.36.0-alt1
- new version

* Thu Jun 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.35.0-alt1
- new version

* Fri May 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.34.0-alt1
- new version

* Mon Apr 17 2017 Sergey V Turchin <zerg@altlinux.org> 5.33.0-alt1
- new version

* Wed Mar 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.32.0-alt1
- new version

* Mon Feb 13 2017 Sergey V Turchin <zerg@altlinux.org> 5.31.0-alt1
- new version

* Wed Feb 08 2017 Sergey V Turchin <zerg@altlinux.org> 5.30.0-alt1
- new version

* Tue Dec 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.29.0-alt1
- new version

* Fri Nov 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.28.0-alt0.M80P.1
- build for M80P

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.28.0-alt1
- new version

* Thu Oct 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt0.M80P.1
- build for M80P

* Tue Oct 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.26.0-alt2
- don't increase main toolbar icons by default

* Mon Sep 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.26.0-alt1
- new version

* Mon Aug 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.25.0-alt1
- new version

* Mon Jul 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.24.0-alt1
- new version

* Tue Jun 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.23.0-alt1
- new version

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.22.0-alt1
- new version

* Mon Apr 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.21.0-alt1
- new version

* Tue Mar 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.20.0-alt1
- new version

* Tue Feb 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.19.0-alt1
- new version

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.18.0-alt1
- initial build
