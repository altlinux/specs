Name: libx264
Version: 120
Release: alt0.1

Summary: H.264 codec shared library
License: GPL
Group: System/Libraries
Url: http://www.videolan.org/x264.html

Source: %name-%version-%release.tar

BuildRequires: yasm libX11-devel

%description
libx264 is a free library for encoding H264/AVC video streams. The code
is written from scratch.
Encoder features:
- CAVLC/CABAC
- Multi-references
- Intra: all macroblock types (16x16, 8x8, and 4x4 with all
  predictions)
- Inter P: all partitions (from 16x16 down to 4x4)
- Inter B: partitions from 16x16 down to 8x8 (including skip/direct)
- Ratecontrol: constant quantizer, single or multipass ABR, optional
  VBV
- Scene cut detection
- Adaptive B-frame placement
- B-frames as references / arbitrary frame order
- 8x8 and 4x4 adaptive spatial transform
- Lossless mode
- Custom quantization matrices
- Parallel encoding of multiple slices.

This package includes the shared library needed to run x264-based
software.

%package devel
Summary: Development files of H.264 codec library
Group: Development/C
Requires: %name = %version-%release

%description devel
%name is a free library for encoding H264/AVC video streams. The code is
written from scratch.
Encoder features:
- CAVLC/CABAC
- Multi-references
- Intra: all macroblock types (16x16, 8x8, and 4x4 with all
  predictions)
- Inter P: all partitions (from 16x16 down to 4x4)
- Inter B: partitions from 16x16 down to 8x8 (including skip/direct)
- Ratecontrol: constant quantizer, single or multipass ABR, optional
  VBV
- Scene cut detection
- Adaptive B-frame placement
- B-frames as references / arbitrary frame order
- 8x8 and 4x4 adaptive spatial transform
- Lossless mode
- Custom quantization matrices
- Parallel encoding of multiple slices.

This package includes the header files needed to develop lib%name-based
software.

%prep
%setup

%build
%define _optlevel 3
%configure \
	--disable-cli \
    	--enable-debug \
%ifarch x86_64
	--enable-pic \
%endif
%ifarch arm
	--disable-asm \
%endif
	--enable-shared \
	--enable-visualize \
	--bit-depth=8

%make_build 

%install
%make_install DESTDIR=%buildroot install

%ifnarch x86_64
%set_verify_elf_method textrel=relaxed
%endif

%files
%doc doc/*.txt AUTHORS
%_libdir/libx264.so.*

%files devel
%_includedir/x264.h
%_includedir/x264_config.h
%_pkgconfigdir/*
%_libdir/libx264.so

%changelog
* Sun Jan 29 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 120-alt0.1
- updated from git.f33c8cb

* Tue Oct 04 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 116-alt0.3
- updated from git.926a03a9

* Thu Sep 15 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 116-alt0.2
- built shared library only
- back to bit depth 8

* Mon Aug 01 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 116-alt0.1
- updated to 116
- built with bit depth 10

* Fri Jun 17 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 115-alt0.1
- updated to 115

* Fri Dec 24 2010 Afanasov Dmitry <ender@altlinux.org> 112-alt1
- API 112

* Fri Nov 05 2010 Afanasov Dmitry <ender@altlinux.org> 106-alt2
- rebuild with yasm-1.1.0

* Thu Nov  4 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 106-alt1
- updated to 106

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 85-alt0.1.1
- Rebuilt for soname set-versions

* Tue Feb 02 2010 Afanasov Dmitry <ender@altlinux.org> 85-alt0.1
- API 85
- new git snapshot (at 20100202)
- fix perl shebang in some tools
- change packager

* Sun Feb 15 2009 Led <led@altlinux.ru> 65-alt0.4
- fixed build with altivec

* Sun Dec 21 2008 Led <led@altlinux.ru> 65-alt0.3
- new git snapshot (at 20081216)

* Sun Nov 30 2008 Led <led@altlinux.ru> 65-alt0.2
- new git snapshot (at 20081129)

* Mon Oct 20 2008 Led <led@altlinux.ru> 65-alt0.1
- API 65
- removed gui, avc2avi

* Mon Oct 20 2008 Led <led@altlinux.ru> 0.64-alt0.5
- updated libx264-altlinux.ver

* Mon Oct 20 2008 Led <led@altlinux.ru> 0.64-alt0.4
- fixed/updated libx264-altlinux.ver

* Tue Sep 23 2008 Led <led@altlinux.ru> 0.64-alt0.3
- new git snapshot (at 20080922)
- added %name-git-20080922-compat-api.patch

* Mon Sep 22 2008 Led <led@altlinux.ru> 0.64-alt0.2
- new git snapshot (at 20080921)

* Fri Sep 19 2008 Led <led@altlinux.ru> 0.64-alt0.1
- new git snapshot (at 20080917)

* Sun Sep 14 2008 Led <led@altlinux.ru> 0.62-alt0.1
- new git snapshot (at 20080914)

* Tue Sep 02 2008 Led <led@altlinux.ru> 0.61-alt0.1
- new git snapshot (at 20080901)

* Fri Aug 29 2008 Led <led@altlinux.ru> 0.60-alt0.10
- new git snapshot (at 20080829)
- updated:
  + %name-git-20080829-build.patch
  + %name-git-20080829-alt.patch
- removed %name-20080731-yasm.patch

* Wed Aug 20 2008 Led <led@altlinux.ru> 0.60-alt0.9
- new git snapshot (at 20080819)
- added %name-git-20080819-alt.patch

* Wed Aug 13 2008 Led <led@altlinux.ru> 0.60-alt0.8
- new git snapshot (at 20080811)
- fixed *.desktop

* Sun Aug 10 2008 Led <led@altlinux.ru> 0.60-alt0.7
- new git snapshot (at 20080809)
- added version script (libx264-altlinux.ver)

* Sat Aug 02 2008 Led <led@altlinux.ru> 0.60-alt0.6
- new git snapshot (at 20080731)

* Fri Jul 25 2008 Led <led@altlinux.ru> 0.60-alt0.5
- new git snapshot (at 20080724)

* Sun Jul 20 2008 Led <led@altlinux.ru> 0.60-alt0.4
- new git snapshot (at 20080718)

* Sat Jul 12 2008 Led <led@altlinux.ru> 0.60-alt0.3
- new git snapshot (at 20080711)
- updated %name-20080711-avc2avi.patch

* Sat Jul 05 2008 Led <led@altlinux.ru> 0.60-alt0.2
- new git snapshot (at 20080704)

* Sun Jun 29 2008 Led <led@altlinux.ru> 0.60-alt0.1
- new git snapshot (at 20080625)

* Wed Jun 18 2008 Led <led@altlinux.ru> 0.59-alt0.20080618.1
- new git snapshot (at 20080618)

* Mon Jun 16 2008 Led <led@altlinux.ru> 0.59-alt0.20080615.1
- new git snapshot (at 20080615)

* Sat Jun 07 2008 Led <led@altlinux.ru> 0.59-alt0.20080604.1
- new git snapshot (at 20080604)

* Wed Jun 04 2008 Led <led@altlinux.ru> 0.59-alt0.20080603.1
- new git snapshot (at 20080603)

* Tue Jun 03 2008 Led <led@altlinux.ru> 0.59-alt0.20080602.1
- new git snapshot (at 20080602)

* Tue May 27 2008 Led <led@altlinux.ru> 0.59-alt0.20080521.1
- new git snapshot (at 20080521)

* Thu May 15 2008 Led <led@altlinux.ru> 0.59-alt0.20080513.1
- new git snapshot (at 20080513)

* Tue May 06 2008 Led <led@altlinux.ru> 0.59-alt0.20080427.1
- new git snapshot (at 20080427)

* Sat Apr 19 2008 Led <led@altlinux.ru> 0.59-alt0.20080418.1
- new git snapshot (at 20080418)

* Sat Apr 12 2008 Led <led@altlinux.ru> 0.59-alt0.20080411.1
- new git snapshot (at 20080411)

* Wed Apr 09 2008 Led <led@altlinux.ru> 0.59-alt0.20080402.2
- fixed unmets in libx264-devel

* Tue Apr 08 2008 Led <led@altlinux.ru> 0.59-alt0.20080402.1
- new git snapshot (at 20080402)
- updated %name-20080402-build.patch
- added %name-20080402-avc2avi.patch

* Thu Mar 20 2008 Led <led@altlinux.ru> 0.58-alt0.20080320.1
- new git snapshot (at 20080320)
- updated %name-20080319-yasm.patch

* Tue Mar 04 2008 Led <led@altlinux.ru> 0.58-alt0.745.1
- new SVN snapshot (revision 745)
- fixed %{name}_gtk_encode.desktop
- updated %name-svn-r745-yasm.patch

* Sun Mar 02 2008 Led <led@altlinux.ru> 0.58-alt0.742.1
- new SVN snapshot (revision 742)

* Fri Feb 29 2008 Led <led@altlinux.ru> 0.58-alt0.736.3
- used standard icon for menu
- fixed .desktop file

* Wed Feb 20 2008 Led <led@altlinux.ru> 0.58-alt0.736.2
- fixed #12364

* Sun Feb 10 2008 Led <led@altlinux.ru> 0.58-alt0.736.1
- new SVN snapshot (revision 736)

* Mon Jan 28 2008 Led <led@altlinux.ru> 0.58-alt0.735.1
- new SVN snapshot (revision 735)

* Mon Jan 21 2008 Led <led@altlinux.ru> 0.57-alt0.721.1
- new SVN snapshot (revision 721)

* Fri Jan 11 2008 Led <led@altlinux.ru> 0.57-alt0.719.1
- new SVN snapshot (revision 719)

* Fri Dec 21 2007 Led <led@altlinux.ru> 0.57-alt0.714.1
- new SVN snapshot (revision 714)

* Tue Dec 18 2007 Led <led@altlinux.ru> 0.57-alt0.712.1
- new SVN snapshot (revision 712)

* Sat Dec 08 2007 Led <led@altlinux.ru> 0.57-alt0.709.1
- new SVN snapshot (revision 709)

* Sun Dec 02 2007 Led <led@altlinux.ru> 0.57-alt0.705.1
- new SVN snapshot (revision 705)
- cleaned up spec

* Tue Nov 20 2007 Led <led@altlinux.ru> 0.56-alt0.694.1
- new SVN snapshot (revision 694)

* Mon Nov 19 2007 Led <led@altlinux.ru> 0.56-alt0.690.1
- new SVN snapshot (revision 690)

* Wed Nov 14 2007 Led <led@altlinux.ru> 0.56-alt0.685.1
- new SVN snapshot (revision 685)

* Sat Nov 10 2007 Led <led@altlinux.ru> 0.56-alt0.682.1
- new SVN snapshot (revision 682)

* Tue Oct 02 2007 Led <led@altlinux.ru> 0.56-alt0.680.1
- new SVN snapshot (revision 680)
- fixed License

* Fri Sep 21 2007 Led <led@altlinux.ru> 0.56-alt0.677.1
- new SVN snapshot (revision 677)

* Sat Sep 15 2007 Led <led@altlinux.ru> 0.56-alt0.675.1
- new SVN snapshot (revision 675)
- removed obsolete libx264.so.54 link

* Tue Aug 21 2007 Led <led@altlinux.ru> 0.56-alt0.671.1
- new SVN snapshot (revision 671)
- added %name-svn-r671-yasm.patch (fix #12604)
- cleaned up spec

* Fri Aug 17 2007 Led <led@altlinux.ru> 0.56-alt0.669.1
- new SVN snapshot (revision 669)
- cleaned up spec
- updated %name-svn-r669-build.patch

* Fri Aug 03 2007 Led <led@altlinux.ru> 0.56-alt0.667.3
- used yasm for x86_32

* Thu Jul 19 2007 Led <led@altlinux.ru> 0.56-alt0.667.2
- fixed libx264 Provides

* Thu Jul 19 2007 Led <led@altlinux.ru> 0.56-alt0.667.1
- new SVN snapshot (revision 667)
- fixed descriptions (#12364)
- fixed License

* Fri Jul 06 2007 Led <led@altlinux.ru> 0.0-alt55.664.1
- new SVN snapshot (revision 664)
- cleaned up spec

* Mon Jun 18 2007 Led <led@altlinux.ru> 0.0-alt55.661.1
- new SVN snapshot (revision 661)

* Tue Jun 12 2007 Led <led@altlinux.ru> 0.0-alt55.659.1
- new SVN snapshot (revision 659)

* Thu Jun 07 2007 Led <led@altlinux.ru> 0.0-alt55.658.1
- new SVN snapshot (revision 658)

* Tue May 29 2007 Led <led@altlinux.ru> 0.0-alt55.656.1
- new SVN snapshot (revision 656)

* Sun May 13 2007 Led <led@altlinux.ru> 0.0-alt55.655.1
- new SVN snapshot (revision 655): new lib's soname

* Mon Apr 23 2007 Led <led@altlinux.ru> 0.0-alt54.654.1
- new SVN snapshot (revision 654)

* Mon Apr 23 2007 Led <led@altlinux.ru> 0.0-alt54.652.1
- new SVN snapshot (revision 652)

* Thu Apr 12 2007 Led <led@altlinux.ru> 0.0-alt54.650.1
- new SVN snapshot (revision 650)

* Fri Apr 06 2007 Led <led@altlinux.ru> 0.0-alt54.645.1
- new SVN snapshot (revision 645)

* Sun Mar 25 2007 Led <led@altlinux.ru> 0.0-alt54.635.1
- new SVN snapshot (revision 635)

* Thu Mar 15 2007 Led <led@altlinux.ru> 0.0-alt54.634.1
- new SVN snapshot (revision 634)

* Thu Mar 15 2007 Led <led@altlinux.ru> 0.0-alt54.633.1
- new SVN snapshot (revision 633):
  + SSE3 optimization
- fixed BuildRequires

* Mon Mar 12 2007 Led <led@altlinux.ru> 0.0-alt54.628.1
- new SVN snapshot (revision 628)

* Thu Feb 22 2007 Led <led@altlinux.ru> 0.0-alt54.623.1
- new SVN snapshot (revision 623)

* Mon Jan 29 2007 Led <led@altlinux.ru> 0.0-alt54.622.1
- new SVN snapshot (revision 622)

* Mon Jan 22 2007 Led <led@altlinux.ru> 0.0-alt54.620.1
- new SVN snapshot (revision 620)

* Tue Jan 16 2007 Led <led@altlinux.ru> 0.0-alt54.618.1
- new SVN snapshot (revision 618)
- fixed %%changelog

* Wed Dec 20 2006 Led <led@altlinux.ru> 0.0-alt54.614.1
- new SVN snapshot (revision 614)
- fixed %%changelog

* Mon Dec 18 2006 Led <led@altlinux.ru> 0.0-alt54.611.1
- new SVN snapshot (revision 611)

* Thu Dec 14 2006 Led <led@altlinux.ru> 0.0-alt54.606.1
- new SVN snapshot (revision 606)

* Tue Nov 28 2006 Led <led@altlinux.ru> 0.0-alt54.604.1
- new SVN snapshot (revision 604)

* Thu Nov 23 2006 Led <led@altlinux.ru> 0.0-alt54.602.1
- new SVN snapshot (revision 602)

* Mon Nov 20 2006 Led <led@altlinux.ru> 0.0-alt54.601.1
- new SVN snapshot (revision 601)

* Wed Nov 08 2006 Led <led@altlinux.ru> 0.0-alt54.600.1
- new SVN snapshot (revision 600)

* Tue Oct 31 2006 Led <led@altlinux.ru> 0.0-alt54.598.1
- new SVN snapshot (revision 598)

* Mon Oct 30 2006 Led <led@altlinux.ru> 0.0-alt54.596.1
- new SVN snapshot (revision 596)

* Tue Oct 17 2006 Led <led@altlinux.ru> 0.0-alt54.593.1
- new SVN snapshot (revision 593): new lib's soname

* Fri Oct 13 2006 Led <led@altlinux.ru> 0.0-alt53.590.2
- enabled gui again

* Thu Oct 12 2006 Led <led@altlinux.ru> 0.0-alt53.590.1
- new SVN snapshot (revision 590)
- disabled gui

* Mon Oct 09 2006 Led <led@altlinux.ru> 0.0-alt53.584.1
- new SVN snapshot (revision 584)

* Thu Oct 05 2006 Led <led@altlinux.ru> 0.0-alt53.578.1
- new SVN snapshot (revision 578): new lib's soname

* Mon Oct 02 2006 Led <led@altlinux.ru> 0.0-alt52.575.1
- new SVN snapshot (revision 575): new lib's soname

* Tue Sep 26 2006 Led <led@altlinux.ru> 0.0-alt50.567.1
- new SVN snapshot (revision 567)
- updated %name-svn-r567-build.patch

* Sun Sep 24 2006 Led <led@altlinux.ru> 0.0-alt50.565.1
- new SVN snapshot (revision 565)
- updated %name-svn-r565-build.patch
- fixed %%changelog

* Wed Sep 06 2006 Led <led@altlinux.ru> 0.0-alt50.558.1
- new SVN snapshot (revision 558): new lib's soname

* Fri Aug 18 2006 Led <led@altlinux.ru> 0.0-alt49.553.1
- new release numbering (therewith SVN revision)
- new SVN snapshot (revision 551): new lib soname
- replaced %name-svn-*-shared.patch to %name-svn-r551-build.patch
- added uk.po
- added %{name}_gtk.desktop
- cleaned up spec

* Mon Jul 24 2006 Led <led@altlinux.ru> 0.0-alt0.20060724.1
- new SVN snapshot (revision 538)

* Thu Jul 20 2006 Led <led@altlinux.ru> 0.0-alt0.20060718.1
- new SVN snapshot (revision 537): changes in API
- cleaned up spec

* Mon Jul 17 2006 Led <led@altlinux.ru> 0.0-alt0.20060717.1
- new SVN snapshot (revision 536)

* Mon Jul 10 2006 Led <led@altlinux.ru> 0.0-alt0.20060710.1
- new SVN snapshot (revision 534)
- updated %name-svn-*-shared.patch

* Tue Jun 13 2006 Led <led@altlinux.ru> 0.0-alt0.20060613.1
- new SVN snapshot (revision 532)
- updated %name-svn-*-shared.patch

* Wed May 31 2006 Led <led@altlinux.ru> 0.0-alt0.20060531.1
- new snapshot (revision 530)

* Thu May 25 2006 Led <led@altlinux.ru> 0.0-alt0.20060525.1
- new snapshot (revision 527)

* Tue May 23 2006 Led <led@altlinux.ru> 0.0-alt0.20060523.1
- new snapshot (revision 525)

* Mon May 15 2006 Led <led@altlinux.ru> 0.0-alt0.20060515.1
- new snapshot (revision 523)

* Wed May 10 2006 Led <led@altlinux.ru> 0.0-alt0.20060510.1
- new snapshot (revision 519)
- cleaned up %name-svn-*-shared.patch
- fixed spec

* Thu May 04 2006 Led <led@altlinux.ru> 0.0-alt0.20060504.1
- new snapshot (revision 517)

* Wed May 03 2006 Led <led@altlinux.ru> 0.0-alt0.20060503.1
- new snapshot (revision 516)

* Wed Apr 26 2006 Led <led@altlinux.ru> 0.0-alt0.20060426.2
- updated %name-svn-*-shared.patch
- fixed spec

* Wed Apr 26 2006 Led <led@altlinux.ru> 0.0-alt0.20060426.1
- new snapshot (revision 512)
- removed unnecessary Provides in lib%name-devel package
- fixed %%changelog

* Thu Apr 25 2006 Led <led@altlinux.ru> 0.0-alt0.20060425.1
- new snapshot (revision 511)

* Thu Apr 20 2006 Led <led@altlinux.ru> 0.0-alt0.20060420.1
- new snapshot (revision 503)
- added xyuv to %name-utils package
- fixed %%changelog

* Mon Apr 17 2006 Led <led@altlinux.ru> 0.0-alt0.20060417.1
- new snapshot (revision 500)
- updated %name-svn-*-shared.patch

* Wed Apr 05 2006 Led <led@altlinux.ru> 0.0-alt0.20060330.2
- changed asm BuildRequires

* Mon Mar 27 2006 Led <led@altlinux.ru> 0.0-alt0.20060330.1
- new snapshot
- fixed spec
- added %name and %name-gtk packages

* Mon Mar 27 2006 Led <led@altlinux.ru> 0.0-alt0.20060220.2
- fixed lib%name-0.0-shared.patch.gz
- fixed spec

* Mon Feb 20 2006 Led <led@altlinux.ru> 0.0-alt0.20060220.1
- new snapshot
- textrel is normal now

* Thu Jan 31 2006 Led <led@altlinux.ru> 0.0-alt0.20060131.1
- new snapshot
- uk and ru Summary and description
- fixed spec
- renamed package x264 to x264-utils
- fixed requires

* Mon Jan 30 2006 Led <led@altlinux.ru> 0.0-alt0.20060129.1
- new snapshot
- fixed asflags
- removed subversion from BuildRequires

* Fri Dec 23 2005 Led <led@altlinux.ru> 0.0-alt0.20051222.2
- fixed spec for x86_64

* Fri Dec 23 2005 Led <led@altlinux.ru> 0.0-alt0.20051222.1
- new snapshot

* Fri Dec 23 2005 Led <led@altlinux.ru> 0.0-alt0.20051128.4
- lib%name-0.0-shared.patch
- added lib%name package

* Tue Dec 06 2005 Led <led@altlinux.ru> 0.0-alt0.20051128.3
- fixed %name-snapshot-20051128-2245-optimization.patch

* Wed Nov 30 2005 Led <led@altlinux.ru> 0.0-alt0.20051128.2
- new %name-snapshot-20051128-2245-optimization.patch

* Wed Nov 30 2005 Led <led@altlinux.ru> 0.0-alt0.20051128.1
- new build
- %name-snapshot-20051128-2245-optimization.patch

* Fri Jul 08 2005 Led <led@linux.kiev.ua> 0.0-alt0.20050624.1
- new build

* Fri Jul 08 2005 Led <led@linux.kiev.ua> 0.0-alt0.20040815.1
- initial build
