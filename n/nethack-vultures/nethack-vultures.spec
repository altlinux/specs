%define vulturesdir %_datadir

Name: nethack-vultures
Version: 2.1.2
Release: alt2
Summary: NetHack - Vulture's Eye and Vulture's Claw

Group: Games/Adventure 
License: NetHack General Public License
Url: http://www.darkarts.co.za/projects/vultures/
Source0: http://www.darkarts.co.za/projects/vultures/downloads/vultures-%version/vultures-%version-full.tar.bz2
Patch0: %name-1.11.0-optflags.patch
Patch1: %name-2.1.2-config.patch
Patch2: %name-1.10.1-clawguide.patch
Patch3: %name-2.1.2-tabfullscreen.patch
Patch4: %name-2.1.2-fixbuild.patch
Patch5: %name-desktop.patch

Requires: %name-data = %version-%release

# Automatically added by buildreq on Mon Jun 18 2007
BuildRequires: flex libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libncurses-devel libpng-devel desktop-file-utils

BuildRequires:  hardlink

%description
Vulture's Eye is a mouse-driven interface for NetHack that enhances
the visuals, audio and accessibility of the game, yet retains all the
original gameplay and game features.  Vulture's Eye is based on
Falcon's Eye, but is greatly extended.  Also included is Vulture's
Claw, which is based on the Slash'Em core.

%package data
Summary: Data files for NetHack - Vulture's Eye and Vulture's Claw games
Group: Games/Adventure 
BuildArch: noarch

%description data
Data files for Vulture's Eye and Vulture's Claw games.

%prep
%setup -q -n vultures-%version
%patch0 -p1
%patch1 -p1
%patch2
%patch3 -p1
%patch4 -p1
%patch5 -p0
sed -i -e 's|/usr/games/lib/nethackdir|%vulturesdir/vultureseye|g' \
    nethack/doc/{nethack,recover}.6 nethack/include/config.h
sed -i -e 's|/var/lib/games/nethack|%_var/games/vultureseye|g' \
    nethack/include/unixconf.h
sed -i -e 's|/usr/games/lib/nethackdir|%vulturesdir/vulturesclaw|g' \
    slashem/doc/{nethack,recover}.6 slashem/include/config.h
sed -i -e 's|/var/lib/games/nethack|%_var/games/vulturesclaw|' \
    slashem/include/unixconf.h
for N in dist/unix/desktop/*.desktop; do \
    sed -i -e '/Categories=/s/=.*/=Game;RolePlaying;/' $N; done

%build
# Note: no %{?_smp_mflags} in any of these: various parallel build issues.
for i in nethack slashem ; do
    make $i/Makefile
    make -C $i
    make -C $i/util recover dlb dgn_comp lev_comp
    make -C $i/dat spec_levs quest_levs
done

%install
make -C nethack install CHGRP=: CHOWN=: \
    GAMEDIR=$RPM_BUILD_ROOT%vulturesdir/vultureseye \
    VARDIR=$RPM_BUILD_ROOT%_var/games/vultureseye \
    SHELLDIR=$RPM_BUILD_ROOT%_bindir
make -C slashem install CHGRP=: CHOWN=: \
    GAMEDIR=$RPM_BUILD_ROOT%vulturesdir/vulturesclaw \
    VARDIR=$RPM_BUILD_ROOT%_var/games/vulturesclaw \
    SHELLDIR=$RPM_BUILD_ROOT%_bindir

install -dm 755 $RPM_BUILD_ROOT%_mandir/man6
install -pm 644 nethack/doc/nethack.6 \
    $RPM_BUILD_ROOT%_mandir/man6/vultureseye.6
install -pm 644 nethack/doc/recover.6 \
    $RPM_BUILD_ROOT%_mandir/man6/vultureseye-recover.6
install -pm 644 slashem/doc/nethack.6 \
    $RPM_BUILD_ROOT%_mandir/man6/vulturesclaw.6
install -pm 644 slashem/doc/recover.6 \
    $RPM_BUILD_ROOT%_mandir/man6/vulturesclaw-recover.6

install -dm 755 $RPM_BUILD_ROOT%_datadir/icons/hicolor/48x48/apps
for i in vultureseye vulturesclaw ; do
    desktop-file-install \
        --vendor="" \
        --dir=$RPM_BUILD_ROOT%_datadir/applications \
        --mode=644 \
        dist/unix/desktop/$i.desktop
    mv $RPM_BUILD_ROOT%vulturesdir/$i/*.png \
        $RPM_BUILD_ROOT%_datadir/icons/hicolor/48x48/apps/$i.png
    mv $RPM_BUILD_ROOT%vulturesdir/$i/recover \
        $RPM_BUILD_ROOT%_bindir/$i-recover
done

rm -r $RPM_BUILD_ROOT%vulturesdir/vultureseye/manual
rm -r $RPM_BUILD_ROOT%vulturesdir/vulturesclaw/manual

# hardlink instead
# Save some space
#for f in music sound; do
#    cp $RPM_BUILD_ROOT%vulturesdir/vulturesclaw/$f/* $RPM_BUILD_ROOT%vulturesdir/vultureseye/$f/
#    rm -r $RPM_BUILD_ROOT%vulturesdir/vulturesclaw/$f
#    ln -s ../vultureseye/$f \
#        $RPM_BUILD_ROOT%vulturesdir/vulturesclaw/$f
#done

chmod -s $RPM_BUILD_ROOT%vulturesdir/vultures*/vultures* # for stripping

# Clean up
sed -i -e "s|$RPM_BUILD_ROOT||" $RPM_BUILD_ROOT%_bindir/vultures{eye,claw}
rm $RPM_BUILD_ROOT%vulturesdir/vultures*/*.ico

# viy /usr/share hacks
sed -i -e 's,HACK=$HACKDIR/vulturesclaw,HACK=%_bindir/vulturesclaw.bin,' $RPM_BUILD_ROOT%_bindir/vulturesclaw
sed -i -e 's,HACK=$HACKDIR/vultureseye,HACK=%_bindir/vultureseye.bin,' $RPM_BUILD_ROOT%_bindir/vultureseye
mv $RPM_BUILD_ROOT%vulturesdir/vulturesclaw/vulturesclaw $RPM_BUILD_ROOT%_bindir/vulturesclaw.bin
mv $RPM_BUILD_ROOT%vulturesdir/vultureseye/vultureseye $RPM_BUILD_ROOT%_bindir/vultureseye.bin

# Save quite a bit of space
hardlink -cv $RPM_BUILD_ROOT%vulturesdir/vultures*

%pre
/usr/sbin/groupadd -r vultures 2> /dev/null || :
# eliminate the old graphics directory symlink that was confusing rpm
rm -rf %vulturesdir/vulturesclaw/graphics

%files
%_bindir/vultureseye
%_bindir/vulturesclaw
%_bindir/vultureseye-recover
%_bindir/vulturesclaw-recover
%attr(2711,root,vultures) %_bindir/vultureseye.bin
%attr(2711,root,vultures) %_bindir/vulturesclaw.bin
%defattr(664,root,vultures,775)
%dir %_var/games/vultureseye/
%config(noreplace) %_var/games/vultureseye/record
%config(noreplace) %_var/games/vultureseye/perm
%config(noreplace) %_var/games/vultureseye/logfile
%dir %_var/games/vultureseye/save/
%dir %_var/games/vulturesclaw/
%config(noreplace) %_var/games/vulturesclaw/record
%config(noreplace) %_var/games/vulturesclaw/perm
%config(noreplace) %_var/games/vulturesclaw/logfile
%dir %_var/games/vulturesclaw/save/

%files data
%doc nethack/README nethack/dat/license nethack/dat/history nethack/dat/*help
%doc slashem/readme.txt slashem/history.txt slashem/slamfaq.txt vultures/gamedata/manual/
%dir %vulturesdir/vultureseye/
%vulturesdir/vultureseye/config/
%vulturesdir/vultureseye/defaults.nh
%vulturesdir/vultureseye/graphics/
%vulturesdir/vultureseye/license
%vulturesdir/vultureseye/music/
%vulturesdir/vultureseye/nhdat
%vulturesdir/vultureseye/sound/
%vulturesdir/vultureseye/fonts/
%vulturesdir/vultureseye/tiles/
%dir %vulturesdir/vulturesclaw/
%vulturesdir/vulturesclaw/config/
%vulturesdir/vulturesclaw/defaults.nh
%vulturesdir/vulturesclaw/graphics/
%vulturesdir/vulturesclaw/Guidebook.txt
%vulturesdir/vulturesclaw/license
%vulturesdir/vulturesclaw/music/
%vulturesdir/vulturesclaw/nh*share
%vulturesdir/vulturesclaw/sound/
%vulturesdir/vulturesclaw/fonts/
%vulturesdir/vulturesclaw/tiles/
%_datadir/applications/*vultures*.desktop
%_liconsdir/vultures*.png
%_mandir/man6/vultures*.6*

%changelog
* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt2
- added data subpackage

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1
- new version

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt2.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for nethack-vultures

* Sun Sep 23 2007 Fr. Br. George <george@altlinux.ru> 2.1.0-alt2
- Desktop file fixed

* Mon Jun 18 2007 Fr. Br. George <george@altlinux.ru> 2.1.0-alt1
- Initial build from FC

* Sat Mar 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> - 2.1.0-9
- Make the binaries run with their own gid instead of gid games, to minimize
  results of a possible privelidge escalation (bz 187382)
- Fix the crashes on fs<->window toggle on a 16bpp X-server

* Tue Oct 10 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-8
- Add in pre-tag to eliminate the old graphics directory symlink that was confusing rpm.

* Fri Sep 15 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-7
- Rebuild

* Tue Aug 29 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-6
- Attempting to stop graphics duplication.

* Thu Aug 24 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-5
- Attempting to stop graphics duplication.

* Wed Aug 16 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-4
- Attempting to stop graphics duplication.

* Sun Aug 13 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-3
- Attempting to stop graphics duplication.

* Mon Jun 26 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-2
- Dealt with the gametiles.bin eye bug not present in claw.

* Thu Jun 08 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-1
- Upgraded patches 2.1.1

* Wed Jun 07 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.1.0-0
- Upgraded to 2.1.0

* Fri Apr 14 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.0.0-5
- Upped the release tag to keep up with FC-3

* Sun Apr 09 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.0.0-3
- Packaged extra fonts

* Sun Apr 09 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.0.0-2
- Upped the release to try and make the plague server use the right source tarball.

* Sat Apr 08 2006 Karen Pease <meme@daughtersoftiresias.org> - 2.0.0-1
- Upgraded to 2.0.0

* Sun Mar 01 2006 Karen Pease <meme@daughtersoftiresias.org> - 1.11.2-5
- Rebuilt for FC5

* Sun Feb 02 2006 Frank Arnold <frank@scirocco-5v-turbo.de> - 1.11.2-4
- Got a working plague build by working around util-linux bug #176441.

* Sun Jan 08 2006 Karen Pease <meme@daughtersoftiresias.org> - 1.11.2-3
- To fix a strange error on the plague server, added a req for util-linux.

* Sun Jan 08 2006 Karen Pease <meme@daughtersoftiresias.org> - 1.11.2-2
- Upped revision to try to get package to build on the server.

* Fri Jan 06 2006 Karen Pease <meme@daughtersoftiresias.org> - 1.11.2-1
- Upgraded the tarball to the latest version.

* Fri Dec 23 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.1-3
- Modified the specfile to duplicate the slash'em contents into the vultures dirs before rm'ing, to fix a missing-file crash

* Wed Dec 21 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.1-2
- Upped revision to try to get package to build on the server.

* Tue Dec 20 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.1-1
- Upgraded source package; fixes some keyboard bugs and problems for 64bit/big endian machines concerning transparency.

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-8
- Forgot to relocate moved docs for postbuild.

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-7
- Apparently we're using libpng-devel now also (nobody told me)

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-6
- SDL image devel required for build to complete properly.

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-6
- SDL image devel required for build to complete properly.

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-5
- That patch was fixed, but.. the folly of not checking all patches  :P

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-4
- Once again with the patch - ah, the folly of doing diffs by hand.  Last error.

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-3
- Didn't quite get that patch right.

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-2
- Forgot to update the patches previously; done.

* Thu Dec 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.11.0-1
- Upgraded the tarball to the latest release
- Upped the version
- Removed a patch that's now part of the source

* Mon Nov 21 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.10.1-1
- Made it so I don't have to manually tinker with revisions between dists
- Using a 1.x release
- Removed excess tarball

* Mon Nov 21 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.10.1-0.5
- Upped revision in order to make tag

* Mon Nov 21 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.10.1-0.3
- Applied patch 3 (log2stderr)

* Tue Nov 16 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.10.1-0.2
- Upped revision
- Removed timidity++ dep
- Fixed manual installation
- Put stderr patch back in.

* Tue Nov 15 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.10.1-0.1
- Took over maintainership of package
- Handled TODOs

* Tue Nov 15 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.10.1-0.1
- 1.10.1, log crash fix applied upstream.

* Mon Nov  7 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.10.0-0.1
- First build, based on my, Karen Pease's and Luke Macken's related work.
