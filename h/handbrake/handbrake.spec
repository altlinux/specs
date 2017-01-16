%define svn git20161229

Name: handbrake
Version: 1.0.1
Release: alt1.%svn
Summary: Multithreaded Video Transcoder
Packager: Motsyo Gennadi <drool@altlinux.ru>
Source: http://prdownloads.sourceforge.net/handbrake/HandBrake-%version.tar.bz2
# #Source0: %name-%svn.tar.bz2

Source101: http://downloads.webmproject.org/releases/webm/libvpx-1.5.0.tar.bz2
Source102: http://download.handbrake.fr/handbrake/contrib/yasm-1.3.0.tar.gz
Source103: https://download.handbrake.fr/handbrake/contrib/libav-12.tar.gz
Source104: http://download.handbrake.fr/handbrake/contrib/libdvdread-5.0.0-6-gcb1ae87.tar.gz
Source105: http://download.videolan.org/pub/videolan/libdvdnav/5.0.1/libdvdnav-5.0.1.tar.bz2
Source106: https://download.videolan.org/pub/videolan/x265/x265_2.1.tar.gz
Source107: https://cmake.org/files/v3.3/cmake-3.3.2.tar.gz
Source108: http://download.videolan.org/pub/videolan/libbluray/0.9.3/libbluray-0.9.3.tar.bz2

Source151: handbrake-ffmpeg_fix_missing_return_in_nonvoid_function.patch
Source152: handbrake-svn5042-fix_libbluray_implicit_declaration_of_function_strdup.patch

Patch200: handbrake-svn5891-fdk_aac-autoreconf.patch
Patch250: handbrake-git20161018-category.patch

Url: http://handbrake.fr/
Group: Video
License: GPLv2+

BuildRequires: bzlib-devel doxygen gcc-c++ intltool libass-devel libdbus-glib-devel libfribidi-devel libglademm-devel libgtk+3-devel libharfbuzz-devel libjansson-devel liblame-devel libnotify-devel libopus-devel libsamplerate-devel libssl-devel libtheora-devel libvorbis-devel libx264-devel libxml2-devel python-modules-json

%description
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder.

%package cli
Summary: Multithreaded Video Transcoder
Group: Video

%description cli
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder.

This package contains a command-line interface for Handbrake.

%package gtk
Summary: Multithreaded Video Transcoder
Group: Video
Requires: %name-cli = %version-%release

%description gtk
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder.

This package contains a GTK+ graphical user interface for Handbrake.

%prep
%setup -n HandBrake-%version
# #%setup -n %name-svn
%patch200 -p1
%patch250 -p1

# Copy 3rd party dependencies into expected locations:
%__mkdir download
for f in \
%{S:101} %{S:102} %{S:103} %{S:104} %{S:105} %{S:106} \
%{S:107} %{S:108} \
; do
     %__ln_s "$f" download/
done
mv ./download/x265_2.1.tar.gz ./download/x265_2.1-1.tar.gz

%build
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"

# #%__cp "%{S:151}" contrib/ffmpeg/A99-fix-missing-return-in-nonvoid-function.patch
# #%__cp "%{S:152}" contrib/libbluray/A99-fix_libbluray_implicit_declaration_of_function_strdup.patch

./configure --prefix="%buildroot%prefix" --force --disable-gtk-update-checks
pushd build
# #%make_build
%__make build
popd build

%install
pushd build
%__make install
popd #build

%__ln_s ghb "%buildroot%_bindir/HandBrakeGUI"

%__rm "%buildroot%_datadir/icons"/*/*.cache

%find_lang --with-gnome ghb

%files cli
%doc AUTHORS.markdown COPYING LICENSE NEWS.markdown README.markdown THANKS.markdown
%_bindir/HandBrakeCLI

%files gtk -f ghb.lang
%_bindir/HandBrakeGUI
%_bindir/ghb
%_desktopdir/ghb.desktop
%_datadir/icons/*/*/apps/hb-icon.svg

%changelog
* Mon Jan 16 2017 Motsyo Gennadi <drool@altlinux.ru> 1.0.1-alt1.git20161229
- 1.0.1 (git 29.12.2016)

* Tue Oct 18 2016 Motsyo Gennadi <drool@altlinux.ru> 0.10.5-alt1.git20161018
- 0.10.5 (git 18.10.2016)

* Sun Feb 16 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.9.1-alt1.svn6036
- build svn6036

* Sat Feb 15 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.9.1-alt1.svn6031.1
- fix build

* Sat Feb 15 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.9.1-alt1.svn6031
- build svn6031

* Wed Feb 12 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.9.1-alt1.svn6028
- build svn6028

* Tue Feb 04 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.9.1-alt1.svn6013
- build svn6013 (now GTK3 only)

* Sun Feb 02 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn6011
- build svn6011

* Sun Nov 24 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5903
- build svn5903

* Sat Nov 09 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5891
- build svn5891

* Thu Sep 19 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5787
- build svn5787

* Wed Sep 04 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5767
- build svn5767

* Mon Sep 02 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5764
- build svn5764

* Tue Aug 06 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5693
- build svn5693

* Tue Aug 06 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5690
- build svn5690

* Fri Jun 14 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5577
- build svn5577

* Sun May 19 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5478
- 0.9.9 released
- build svn5433

* Wed May 01 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5433
- build svn5433

* Mon Apr 01 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5369
- build svn5369

* Thu Mar 07 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5307
- build svn5307

* Mon Feb 11 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5245
- build svn5245

* Wed Jan 02 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5127
- build svn5127

* Wed Nov 28 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5086
- build svn5086

* Fri Nov 16 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5065
- build svn5065
- cleanup BuildRequres

* Sat Nov 03 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt1.svn5042
- build svn5042
- cleanup spec
- cleanup BuildRequres

* Wed Oct 17 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt0.svn5017
- build svn5017

* Wed Oct 10 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.9-alt0.svn5010
- build svn5010

* Tue Jun 05 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1.3
- fir build for Sisyphus (thank azol@ for help)

* Sun Jun 03 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1.2
- test fix for sisyphus

* Sun Jun 03 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1.1
- test fix for sisyphus

* Fri Jun 01 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.5-alt1
- initial build for ALT Linux from OpenSUSE package
