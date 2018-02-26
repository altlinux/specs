%define theme oxygen

Name: icon-theme-%theme
Version: 4.8.3
Release: alt1

Summary: A set of Icons for KDE
Group: Graphics
Url: http://www.oxygen-icons.org/
License: LGPL

BuildArch: noarch

Provides: kde4-%name = %version-%release
Provides: kde4-icon-theme = %version-%release
Conflicts: kde4libs < 4.2.60

Source: %theme-icons-%version.tar
Source10: exclude.txt
Patch1: oxygen-icons-4.8.1-alt-toolbar-default-size.patch

BuildRequires: cmake gcc-c++ kde-common-devel
BuildRequires: icon-naming-utils

%description
A set of Icons for KDE

%prep
%setup -qn %theme-icons-%version
%patch1 -p1

%build
%K4build

%install
%K4install

#5707
pushd %buildroot/%_iconsdir/%theme
for sz in 16x16 22x22 32x32 48x48 64x64 128x128 256x256
do
    if [ -d $sz ]; then
	pushd $sz
	for ctx in `ls -1`; do
	    [ -d $ctx ] \
		&& %_libexecdir/icon-name-mapping -c $ctx
	done
	popd
    fi
done
popd

# fix broken symlinks
find %buildroot/%_iconsdir/%theme -type l | \
while read l
do
    POINTS_TO=`readlink $l`
    FILENAME_TO=${POINTS_TO##*/}
    if [ "$POINTS_TO" != "$FILENAME_TO" ] ; then
	DIRPATH=`dirname $l`
	if [ -e "$DIRPATH/$FILENAME_TO" ] ; then
	    ln -snf "$FILENAME_TO" $l
	else
	    rm -f $l
	fi
    else
	continue
    fi
done


>exlude-list
while read ex
do
    [ -e %buildroot$ex ] \
	&& echo "%%exclude $ex" >> exlude-list
done < %SOURCE10


%files -f exlude-list
%doc AUTHORS COPYING CONTRIBUTING
#
%dir %_iconsdir/%theme
%_iconsdir/%theme/index.*
%_iconsdir/%theme/?x?
%_iconsdir/%theme/??x??
%_iconsdir/%theme/???x???

%changelog
* Wed May 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Mon Apr 09 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Mon Mar 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version
- increase main toolbar icons default size

* Fri Feb 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- fix provides

* Mon Jan 23 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Sun Oct 30 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Tue Sep 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Fri Jul 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Wed Jun 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Tue May 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Tue Apr 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Mon Feb 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Wed Jan 26 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Mon Nov 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Mon Aug 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Tue Aug 10 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Fri Apr 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Mon Mar 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Tue Feb 09 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Fri Jan 15 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Wed Dec 02 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Thu Nov 12 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt2
- fix using icon-name-mapping
- don't require tango icons to build package

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Thu Nov 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Wed Sep 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version
- process icons trought icon-name-mapping

* Wed Aug 12 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt3
- add symlinks for GTK icons

* Wed Aug 12 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt2
- add symlinks for GNOME icons

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- new version

* Wed Jul 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- new version

* Thu Jul 16 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- initial spec

