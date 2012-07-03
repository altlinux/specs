%set_verify_elf_method textrel=relaxed
%define rev 113340

%if_enabled debug
%define buildtype Debug
%else
%define buildtype Release
%endif

%def_disable nacl

Name: chromium-browser
Version: 17.0.963.1
Release: alt3.r%rev

Summary: An open source web browser developed by Google.
License: BSD
Group: Networking/WWW
Url: http://code.google.com/p/chromium/

Source0: %name-%version.tar
Source1: %name.desktop
Source2: %name.default
Source3: %name.sh

Patch:   %name-%version-%release.patch
Patch1:	 chromium-libav0.8-fix.patch

%add_findreq_skiplist %_libdir/%name/xdg-settings

BuildRequires: /proc
%define __nprocs %(N="$(LC_ALL=C egrep -cs '^cpu[0-9]+' /proc/stat ||:)"; [ "$N" -gt 0 ] 2>/dev/null && printf %%s "$(( 2*$N - 1))" || echo 1)

BuildPreReq: bzlib-devel flex gcc-c++ gperf libGConf-devel libXext-devel libXt-devel
BuildPreReq: libalsa-devel libevent1.4-devel libexpat-devel libgtk+2-devel
BuildPreReq: libjpeg-devel libnss-devel libXScrnSaver-devel libdbus-glib-devel
BuildPreReq: perl-Switch python-module-PyXML python-modules-compiler
BuildPreReq: python-modules-email python-modules-encodings python-modules-logging
BuildPreReq: libcups-devel libgcrypt-devel libgnome-keyring-devel libpulseaudio-devel
BuildPreReq: libavcodec-devel >= 1:0.7 libavformat-devel >= 1:0.7 libavutil-devel >= 1:0.7
BuildPreReq: libvpx-devel >= 0.9.7.1 libXtst-devel libflac-devel libspeex-devel libpng-devel
BuildPreReq: libpam-devel libXdamage-devel libicu-devel libXinerama-devel libkrb5-devel
BuildPreReq: libelf-devel python-module-simplejson libXcomposite-devel

Provides: webclient, /usr/bin/xbrowser
BuildPreReq: alternatives >= 0.2.0
PreReq(post,preun): alternatives >= 0.2

#See https://bugzilla.altlinux.org/25785
Conflicts: mozilla-plugin-xine

%description
Chromium is an open-source browser project that aims to build a safer,
faster, and more stable way for all Internet users to experience the web.

%package codecs
Group: Networking/WWW
Summary: FFmpeg codecs for Chromium web browser
Requires: %name = %version-%release

%description codecs
Chromium is an open-source browser project that aims to build a safer,
faster, and more stable way for all Internet users to experience the web.

This package contains symlinks and package requirements necessary to
view HTML5 video in Chromium.

%prep
%setup
%patch -p1
%patch1 -p1

echo '%rev' > build/LASTCHANGE.in

# Scrape out incorrect optflags and hack in the correct ones
PARSED_OPT_FLAGS=`echo \'%optflags -fno-strict-aliasing -fno-ipa-cp -fno-exceptions \' | sed "s/ /',/g" | sed "s/',/', '/g"`
for i in build/common.gypi; do
#        sed -i "s|'-march=pentium4',||g" $i
#        sed -i "s|'-msse2',||g" $i
#        sed -i "s|'-mfpmath=sse',||g" $i
#        sed -i "s|'-mmmx',||g" $i
        sed -i "s|'-O<(debug_optimize)',||g" $i
        sed -i "s|'-m32',||g" $i
        sed -i "s|'-fno-exceptions',|$PARSED_OPT_FLAGS|g" $i
done

sed -i 's,/etc/chromium/policies,/etc/%name/policies,' \
	chrome/common/chrome_paths.cc

%if_disabled nacl
sed -i "/'nacl.gypi',/d" chrome/chrome.gyp
%endif

GYP_GENERATORS=make python build/gyp_chromium build/all.gyp \
	--depth=%_builddir/%name-%version \
	-D disable_pie=1 \
%ifarch x86_64
	-D target_arch=x64 \
%endif
	-D werror= \
	-D disable_sse2=1 \
	-D proprietary_codecs=1 \
	-D linux_use_seccomp_sandbox=1 \
	-D linux_link_kerberos=1 \
%if_disabled nacl
	-D disable_nacl=1 \
%endif
	-D use_system_bzip2=1 \
	-D use_system_libevent=1 \
	-D use_system_libjpeg=0 \
	-D use_system_libpng=1 \
	-D use_system_libxml=0 \
	-D use_system_ssl=0 \
	-D use_system_zlib=1 \
	-D use_system_ffmpeg=1 \
	-D use_system_vpx=1 \
	-D use_system_sqlite=0

%if_enabled debug
sed -i 's,-O0,-O1,' third_party/WebKit/WebCore/WebCore.gyp/webcore.target.mk
%endif

%build
%make_build BUILDTYPE=%buildtype chrome V=1

%install
pushd out/%buildtype
install -pD -m755 chrome %buildroot%_libdir/%name/%name
cp -a chrome.pak resources.pak locales xdg-settings %buildroot%_libdir/%name/
%if_enabled nacl
cp -a libppGoogleNaClPluginChrome.so %buildroot%_libdir/%name/
%ifarch %ix86
cp -a nacl_irt_x86_32.nexe %buildroot%_libdir/%name/
%endif
%ifarch x86_64
cp -a nacl_irt_x86_64.nexe %buildroot%_libdir/%name/
%endif
%endif
install -pD -m644 chrome.1 %buildroot%_man1dir/%name.1
popd

for i in 16 32 48 256; do
    install -pD -m644 chrome/app/theme/chromium/product_logo_$i.png \
        %buildroot%_iconsdir/hicolor/${i}x$i/apps/%name.png
done

install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/%name/default
install -pD -m755 %SOURCE3 %buildroot%_bindir/%name
sed -i "s|/usr/lib/|%_libdir/|g" %buildroot%_bindir/%name

mkdir -p %buildroot%_libdir/%name/plugins/

rm -f %buildroot%_libdir/%name/locales/*.d
# remove leading comment to make file(1) work right
sed -i '1,2d' %buildroot%_man1dir/%name.1

mkdir -p %buildroot%_sysconfdir/%name/policies/{managed,recommended}

for i in libavutil.so.51 libavformat.so.53 libavcodec.so.53; do
    ln -s ../$i %buildroot%_libdir/%name/
done
    

mkdir -p %buildroot%_altdir
cat <<__EOF__ >%buildroot%_altdir/%name
%_bindir/xbrowser	%_bindir/%name	50
__EOF__


%files
%_bindir/%name
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/default
%_sysconfdir/%name/policies/
%_altdir/%name
%dir %_libdir/%name/
%_libdir/%name/%name
%_libdir/%name/chrome.pak
%_libdir/%name/resources.pak
%_libdir/%name/locales/
%_libdir/%name/plugins/
%_libdir/%name/xdg-settings
%if_enabled nacl
%_libdir/%name/lib*.so
%ifarch %ix86
%_libdir/%name/nacl_irt_x86_32.nexe
%endif
%ifarch x86_64
%_libdir/%name/nacl_irt_x86_64.nexe
%endif
%endif
%exclude %_libdir/%name/libav*.so.*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_man1dir/*
%doc AUTHORS LICENSE

%files codecs
%_libdir/%name/libav*.so.*

%changelog
* Mon Feb 06 2012 Andrey Cherepanov <cas@altlinux.org> 17.0.963.1-alt3.r113340
- Chromium FTBFS against libav 0.8b2

* Thu Jan 26 2012 Andrey Cherepanov <cas@altlinux.org> 17.0.963.1-alt2.r113340
- Workaround to fix failing render JPEG images with external libjpeg-turbo
  (see http://code.google.com/p/chromium/issues/detail?id=106954)

* Mon Jan 23 2012 Andrey Cherepanov <cas@altlinux.org> 17.0.963.1-alt1.r113340
- New version 17.0.963.1 (thanks raorn@)

* Tue Dec 27 2011 Andrey Cherepanov <cas@altlinux.org> 17.0.938.0-alt9.r109860
- Disable seccomp sandbox by default to avoid hangs in x86_64 (thanks astroiLL)

* Fri Dec 16 2011 Andrey Cherepanov <cas@altlinux.org> 17.0.938.0-alt8.r109860
- Fix crash on yandex.ru. (see http://code.google.com/p/chromium/issues/detail?id=104016) (closes #26716)

* Fri Dec 02 2011 Andrey Cherepanov <cas@altlinux.org> 17.0.938.0-alt7.r109860
- New version 17.0.938.0 in Sisyphus
- Use system version of ffmpeg

* Wed Nov 23 2011 Lenar Shakirov <snejok@altlinux.ru> 17.0.938.0-alt6.r109860
- Push raorn's repo to Sisyphus

* Tue Nov 15 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:17.0.938.0-alt5uxx.r109860
- [17.0.938.0]

* Tue Nov 08 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:17.0.932.0-alt5uxx.r108831
- [17.0.932.0]

* Fri Oct 28 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:16.0.912.15-alt5uxx.r107520
- [16.0.912.15]

* Tue Oct 11 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:16.0.904.0-alt5uxx.r104676
- [16.0.904.0]

* Tue Oct 04 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:16.0.899.0-alt5uxx.r103696
- [16.0.899.0]

* Sat Oct 01 2011 Lenar Shakirov <snejok@altlinux.ru> 15.0.874.5-alt6.r100120
- Push raorn's repo to Sisyphus

* Fri Sep 09 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:15.0.874.5-alt5uxx.r100120
- [15.0.874.5]

* Thu Sep 08 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:15.0.874.1-alt5uxx.r99959
- [15.0.874.1]
- Disabled NaCl

* Wed Aug 17 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:15.0.854.0-alt5uxx.r96952
- [15.0.854.0]

* Thu Aug 11 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:14.0.835.35-alt5uxx.r96120
- [14.0.835.35]

* Tue Aug 09 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:14.0.835.29-alt5uxx.r95797
- [14.0.835.29]

* Wed Aug 03 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:14.0.835.15-alt5uxx.r94881
- [14.0.835.15]

* Tue Aug 02 2011 Lenar Shakirov <snejok@altlinux.ru> 14.0.835.8-alt6.r94423
- Push raorn's repo to Sisyphus
- Conflicts: mozilla-plugin-xine: see #25785

* Fri Jul 29 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:14.0.835.8-alt5uxx.r94423
- [14.0.835.8]

* Wed Jul 27 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:14.0.835.0-alt5uxx.r94072
- [14.0.835.0]

* Tue Jul 19 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:14.0.825.0-alt5uxx.r92815
- [14.0.825.0]

* Wed Jul 13 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:14.0.814.0-alt5uxx.r91687
- [14.0.814.0]

* Tue Jun 28 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:14.0.803.0-alt5uxx.r90502
- [14.0.803.0]

* Thu Jun 23 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:14.0.797.0-alt5uxx.r89651
- r89651

* Fri Jun 17 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:14.0.794.0-alt5uxx.r89312
- r89312

* Tue Jun 14 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:13.0.782.20-alt5uxx.r88805
- r88805

* Fri Jun 10 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:13.0.782.15-alt5uxx.r88538
- r88538

* Thu Jun 09 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:13.0.782.13-alt5uxx.r88288
- r88288

* Wed Jun 08 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:13.0.782.11-alt5uxx.r88088
- r88088

* Thu Jun 02 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:13.0.782.1-alt5uxx.r87467
- r87467

* Tue May 24 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:13.0.772.0-alt1.r86213r
- r86213

* Wed May 18 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:13.0.767.1-alt1.r85533
- r85533

* Wed May 11 2011 Mykola Grechukh <gns@altlinux.ru> 12.0.742.21-alt2.r84415
- push raom's repo to sisyphus

* Fri May 06 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:12.0.742.21-alt1.r84415
- r84415

* Tue May 03 2011 Alexey I. Froloff <raorn@altlinux.org> 1024:12.0.742.16-alt1.r83872
- r83872

* Tue Apr 26 2011 Alexey I. Froloff <raorn@altlinux.org> 12.0.742.9-alt1.r82993
- r82993
- Package NaCl plugin

* Sun Apr 24 2011 Alexey I. Froloff <raorn@altlinux.org> 12.0.742.5-alt1.r82802
- r82802

* Thu Apr 21 2011 Alexey I. Froloff <raorn@altlinux.org> 12.0.742.0-alt1.r82465
- r82465

* Fri Mar 25 2011 Alexey I. Froloff <raorn@altlinux.org> 12.0.712.0-alt1.r79393
- r79393

* Fri Mar 11 2011 Alexey I. Froloff <raorn@altlinux.org> 11.0.696.3-alt1.r77804
- r77804

* Thu Mar 10 2011 Alexey I. Froloff <raorn@altlinux.org> 11.0.696.1-alt1.r77636
- r77636

* Thu Mar 10 2011 Mykola Grechukh <gns@altlinux.ru> 11.0.696.0-alt2.r77458
- rebuilt for Sisyphus

* Wed Mar 09 2011 Alexey I. Froloff <raorn@altlinux.org> 11.0.696.0-alt1.r77458
- r77458

* Wed Jan 12 2011 Alexey I. Froloff <raorn@altlinux.org> 10.0.634.0-alt1.r71201
- r71201

* Sat Jan 08 2011 Alexey I. Froloff <raorn@altlinux.org> 10.0.628.0-alt1.r70505
- r70505

* Tue Dec 21 2010 Alexey I. Froloff <raorn@altlinux.org> 10.0.612.1-alt1.r69289
- r69289
- Shared build, import patches from Fedora

* Tue Dec 14 2010 Alexey I. Froloff <raorn@altlinux.org> 9.0.597.19-alt1.r68937
- r68937

* Wed Oct 27 2010 Sir Raorn <raorn@altlinux.ru> 9.0.565.0-alt1.r63988
- r63988

* Fri Oct 22 2010 Sir Raorn <raorn@altlinux.ru> 8.0.561.0-alt1.r63484
- r63484

* Thu Oct 14 2010 Sir Raorn <raorn@altlinux.ru> 8.0.554.0-alt1.r62525
- r62525

* Fri Sep 24 2010 Andrey Rahmatullin <wrar@altlinux.org> 7.0.534.0-alt1.r60470
- r60470

* Sun Sep 19 2010 Andrey Rahmatullin <wrar@altlinux.org> 7.0.529.0-alt1.r59900
- r59900

* Thu Sep 16 2010 Andrey Rahmatullin <wrar@altlinux.org> 7.0.526.0-alt1.r59629
- r59629

* Thu Sep 16 2010 Andrey Rahmatullin <wrar@altlinux.org> 7.0.526.0-alt1.r59499
- r59499

* Thu Sep 09 2010 Andrey Rahmatullin <wrar@altlinux.org> 7.0.520.0-alt1.r58924
- r58924

* Wed Sep 01 2010 Andrey Rahmatullin <wrar@altlinux.org> 7.0.513.0-alt1.r58159
- r58159

* Mon Aug 30 2010 Andrey Rahmatullin <wrar@altlinux.org> 7.0.509.0-alt1.r57833
- r57833

* Wed Aug 25 2010 Andrey Rahmatullin <wrar@altlinux.org> 7.0.505.0-alt1.r57189
- r57189 (closes: #23939)

* Sun Aug 15 2010 Andrey Rahmatullin <wrar@altlinux.org> 6.0.495.0-alt1.r56150
- r56150

* Wed Aug 11 2010 Andrey Rahmatullin <wrar@altlinux.org> 6.0.491.0-alt1.r55558
- r55558
- build with -D enable_gpu

* Thu Jul 22 2010 Andrey Rahmatullin <wrar@altlinux.org> 6.0.474.0-alt1.r53315
- r53315

* Sat Jul 17 2010 Andrey Rahmatullin <wrar@altlinux.org> 6.0.469.0-alt1.r52814
- r52814
- enable seccomp sandbox by default

* Mon Jul 12 2010 Andrey Rahmatullin <wrar@altlinux.org> 6.0.464.0-alt1.r52072
- r52072

* Sat Jul 03 2010 Andrey Rahmatullin <wrar@altlinux.ru> 6.0.455.0-alt2.r51588
- r51588
- disable -Werror

* Fri Jul 02 2010 Andrey Rahmatullin <wrar@altlinux.ru> 6.0.455.0-alt2.r51515
- r51515

* Sun Jun 27 2010 Andrey Rahmatullin <wrar@altlinux.ru> 6.0.451.0-alt2.r50932
- add libgnome-keyring-devel to buildrequires

* Sat Jun 26 2010 Andrey Rahmatullin <wrar@altlinux.ru> 6.0.451.0-alt1.r50932
- r50932

* Wed May 12 2010 Andrey Rahmatullin <wrar@altlinux.ru> 6.0.401.0-alt1.r47010
- r47010
- mark /etc/chromium-browser/default as %%config(noreplace)

* Tue May 04 2010 Andrey Rahmatullin <wrar@altlinux.ru> 5.0.396.0-alt1.r46331
- r46331
- add the support for debug builds

* Thu Apr 29 2010 Andrey Rahmatullin <wrar@altlinux.ru> 5.0.392.0-alt1.r45898
- r45898
- build with OMIT_DLOG_AND_DCHECK=1 (Ubuntu)

* Thu Apr 22 2010 Andrey Rahmatullin <wrar@altlinux.ru> 5.0.384.0-alt1.r45279
- r45279

* Thu Apr 15 2010 Andrey Rahmatullin <wrar@altlinux.ru> 5.0.378.0-alt1.r44604
- r44604
- build with MMX support
- do not build and install SUID sandbox

* Tue Mar 30 2010 Andrey Rahmatullin <wrar@altlinux.ru> 5.0.366.0-alt1.r43078
- r43078

* Wed Mar 24 2010 Andrey Rahmatullin <wrar@altlinux.ru> 5.0.362.0-alt1.r42462
- r42462

* Sat Mar 20 2010 Andrey Rahmatullin <wrar@altlinux.ru> 5.0.359.0-alt1.r42179
- r42179

* Wed Feb 24 2010 Andrey Rahmatullin <wrar@altlinux.ru> 5.0.337.0-alt1.r39883
- r39883
- build with bundled libxml2, libxslt and v8

* Thu Jan 28 2010 Andrey Rahmatullin <wrar@altlinux.ru> 5.0.308.0-alt1.r37387
- r37387

* Sat Jan 23 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.305.0-alt1.r36862
- r36862
- add upstream #21318 workaround from Ubuntu (HTML5 video support fix)

* Tue Jan 12 2010 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.297.0-alt1.r36007
- r36007 (closes: #22607)

* Sun Dec 20 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.277.0-alt1.r35069
- r35069

* Tue Dec 08 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.267.0-alt1.r34035
- r34035

* Tue Dec 01 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.261.0-alt1.r33425
- r33425

* Tue Nov 24 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.257.0-alt1.r32919
- r32919

* Tue Nov 17 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.250.0-alt1.r32157
- r32157
- fix getting KDE4 proxy settings
- add alternatives config for /usr/bin/xbrowser (closes: #22302)
- remove obsolete options from /etc/chromium-browser/default

* Sat Nov 14 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.247.0-alt1.r32001
- r32001
- fix plugin search paths
- add revision info into the About dialog

* Fri Nov 13 2009 Andrey Rahmatullin <wrar@altlinux.ru> 4.0.246.0-alt1.r31782
- initial build for ALT Linux, based on Fedora spec and Ubuntu package

* Tue Oct 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.0.227.0-0.1.20091027svn30269
- 20091027svn30269
- apply hack fix to stop double free bug (http://code.google.com/p/chromium/issues/detail?id=23362)

* Tue Oct 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.0.222.6-0.1.20091013svn28872
- 20091013svn28872

* Thu Oct  8 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.0.222.2-0.1.20091008svn28391
- 20091008svn28391

* Wed Sep 30 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.0.220.0-0.1.20090930svn27599
- 20090930svn27599

* Tue Sep 29 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.0.219.8-0.1.20090929svn27489
- 20090929svn27489

* Wed Sep 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.0.212.0-0.1.20090916svn26424
- 20090916svn26424
- revert http://src.chromium.org/viewvc/chrome/trunk/src/chrome/common/sqlite_utils.cc?r1=24321&r2=25633
  to stop crashes when typing in url bar

* Thu Sep 10 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.0.208.0-0.1.20090910svn25958
- 20090910svn25958

* Wed Sep 9 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.0.208.0-0.1.20090909svn25824
- 20090909svn25824
- drop hardcoded Requires on bug-buddy (fixes issue where it is being obsoleted by abrt in rawhide)
- disable webkit deopt, flash bug is fixed now
- use system libicu

* Thu Aug 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.0.204.0-0.1.20090827svn24640
- 20090827svn24640

* Tue Aug 25 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.0.203.0-0.1.20090824svn24148
- 20090824svn24148
- find proper plugin dir on x86_64
- pass --enable-user-scripts (instead of old --enable-greasemonkey)

* Tue Aug 18 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.0.202.0-0.1.20090818svn23628
- 20090818svn23628

* Fri Aug 14 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.0.202.0-0.1.20090814svn23460
- 20090814svn23460

* Wed Aug 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> 4.0.202.0-0.1.20090812svn23201
- Bump to 4.0.202 (we're not tracking 3.0, no one can tell me exactly how to manage that)

* Mon Aug 10 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.198.0-0.1.20090810svn22925
- 20090810svn22925

* Fri Aug  7 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.198.0-0.1.20090807svn22807
- 20090807svn22807

* Wed Aug  5 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.198.0-0.1.20090805svn22496
- 20090805svn22496

* Mon Aug  3 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.197.0-0.1.20090803svn22262
- 20090803svn22262

* Fri Jul 31 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.197.0-0.1.20090731svn22188
- 20090731svn22188

* Thu Jul 30 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.197.0-0.1.20090730svn22105
- 20090730svn22105

* Mon Jul 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.196.0-0.1.20090727svn21648
- 20090727svn21648

* Fri Jul 24 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.196.0-0.1.20090724svn21567
- 20090724svn21567
- drop ffmpeg binaries (only code remaining is headers, doesn't infringe patents)
- package up manpage

* Mon Jul 20 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.195.0-0.1.20090720svn21073
- 20090720svn21073

* Thu Jul 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.195.0-0.1.20090716svn20889
- 20090716svn20889

* Wed Jul 15 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.195.0-0.1.20090715svn20726
- 20090715svn20726

* Mon Jul 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.194.0-0.1.20090713svn20473
- 20090713svn20473

* Sat Jul 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.194.0-0.1.20090711svn20464
- 20090711svn20464
- fix sandboxing up to match code changes (no longer need to be read-only, doesn't need /var/run/chrome-sandbox)

* Wed Jul  8 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.193.0-0.1.20090708svn20141
- 20090708svn20141
- support LinuxZygote sandboxing

* Sat Jul  4 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.192.0-0.1.20090704svn19929
- 20090704svn19929
- hack in correct optflags

* Sun Jun 28 2009 Tom "spot" Callaway <tcallawa@redhat.com> 
- 20090628svn19474

* Fri Jun 26 2009 Tom "spot" Callaway <tcallawa@redhat.com>
- 20090626svn19370

* Thu Jun 25 2009 Tom "spot" Callaway <tcallawa@redhat.com> 
- 3.0.191.0 20090625svn19237

* Thu Jun 18 2009 Tom "spot" Callaway <tcallawa@redhat.com>
- 3.0.190.0 20090618svn18706

* Mon Jun 8 2009 Tom "spot" Callaway <tcallawa@redhat.com>
- 20090608svn17870

* Sat Jun 6 2009 Tom "spot" Callaway <tcallawa@redhat.com>
- 20090606svn17834
