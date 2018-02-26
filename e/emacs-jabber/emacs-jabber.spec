# -*- coding: latin-1; mode: rpm-spec -*-

%define pkg_name jabber
Epoch: 1

Version: 0.8.91
Release: alt3
Name: emacs-jabber
License: %gpl2plus
Group: Networking/Instant messaging
Url: http://emacs-jabber.sourceforge.net
Summary: A minimal jabber client for Emacs

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: %name-%version.tar

BuildArch: noarch
Requires: emacs-common emacs-gnus >= 5.10

BuildPreReq: emacs-devel >= 0.0.1-alt2

BuildPreReq: emacs-common
BuildPreReq: rpm-build-licenses
BuildPreReq: emacs-gnus >= 5.10
BuildPreReq: automake >= 1.9

%description
jabber.el is a minimal Jabber client running under Emacs.

Recommends: xprintidle

%package el
Summary: The Emacs Lisp sources for bytecode included in %name
Group: Development/Other
Requires: %name = %version-%release

%description el
%name-el contains the Emacs Lisp sources for the bytecode
included in the %name package, that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.

%prep
%setup
%build

%install
%autoreconf
%configure --with-lispdir=%_emacslispdir/%pkg_name
make install DESTDIR=%buildroot abs_builddir="%_builddir/%name-%version"
pushd tests
make check
popd

mkdir -p %buildroot%_bindir
mv -v %buildroot%_libexecdir/%name-uri-handler %buildroot%_bindir

mkdir -p %buildroot%_emacs_sitestart_dir
install -m 644 jabber-emacs.el %buildroot%_emacs_sitestart_dir/%pkg_name.el

# Hexrgb
%byte_compile_file compat/hexrgb.el
install -m 644 compat/hexrgb.el %buildroot%_emacslispdir/%pkg_name/hexrgb.el
install -m 644 compat/hexrgb.elc %buildroot%_emacslispdir/%pkg_name/hexrgb.elc

%files
%_bindir/*
%dir %_emacslispdir/%pkg_name
%_emacslispdir/%pkg_name/*.elc
%_emacslispdir/%pkg_name/jabber-autoloads.el
%_infodir/%pkg_name.info*
%config(noreplace) %_emacs_sitestart_dir/%pkg_name.el
%doc README AUTHORS NEWS

%files el
%_emacslispdir/%pkg_name/*.el
%exclude %_emacslispdir/%pkg_name/jabber-autoloads.el
%doc %pkg_name.texi

%changelog
* Sat Jun 16 2012 Terechkov Evgenii <evg@altlinux.org> 1:0.8.91-alt3
- git-20120616

* Fri Apr 13 2012 Terechkov Evgenii <evg@altlinux.org> 1:0.8.91-alt2
- Fix build with new automake

* Fri Mar 23 2012 Terechkov Evgenii <evg@altlinux.org> 1:0.8.91-alt1
- git-20120323

* Wed Oct 20 2010 Terechkov Evgenii <evg@altlinux.org> 1:0.8.0-alt5.18
- git-20101020

* Wed Apr 21 2010 Terechkov Evgenii <evg@altlinux.ru> 1:0.8.0-alt5.16
- git-20100421

* Sun Feb 14 2010 Terechkov Evgenii <evg@altlinux.ru> 1:0.8.0-alt5.14
- git-20100213

* Wed Jan 27 2010 Terechkov Evgenii <evg@altlinux.ru> 1:0.8.0-alt5.9
- Milestone to 0.8.1
- Autoaway methods and Extended away
- Nick coloring
- XML console

* Fri Jan 15 2010 Terechkov Evgenii <evg@altlinux.ru> 1:0.8.0-alt5.8
- git-20100115

* Mon Jan  4 2010 Terechkov Evgenii <evg@altlinux.ru> 1:0.8.0-alt4
- git-20100104

* Thu Dec 31 2009 Terechkov Evgenii <evg@altlinux.ru> 1:0.8.0-alt3
- Minor fixes from SF upstream

* Sat Oct  3 2009 Terechkov Evgenii <evg@altlinux.ru> 1:0.8.0-alt2.1
- jabber-libnotify.el fixed in upsteam

* Mon Sep 14 2009 Terechkov Evgenii <evg@altlinux.ru> 1:0.8.0-alt2
- jabber-libnotify.el added

* Sun Sep 13 2009 Terechkov Evgenii <evg@altlinux.ru> 1:0.8.0-alt1
- 0.8.0 finally released
- If you used xmppuri.sh with your browser, please replace it with %name-uri-handler

* Tue Aug 18 2009 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt1.20090818
- git-20090818

* Sat Jul  4 2009 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt1.20090704
- git-20090704

* Sat Jun 27 2009 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt1.20090627
- git-20090627

* Mon Jun 15 2009 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt1.20090615
- git-20090615
- Obsoleted install-info removed

* Sat May  2 2009 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt1.20090502
- git-20090502

* Wed Apr 29 2009 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt1.20090429
- git-20090429
- Experimental support for roster groups introduced in upstream. Beware the ogres!

* Sun Apr 12 2009 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt1.20090412
- git-20090412

* Mon Mar 23 2009 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt1.20090323
- git-20090323

* Sun Mar  8 2009 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt1.20090308
- cvs-20090308
- Presence-highlight patch from tracker applied

* Sun Feb 15 2009 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt1.20090215
- Bump release tag to succesfuly build in girar

* Sun Feb 15 2009 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20090215
- cvs-20090215

* Mon Nov 10 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20081110
- cvs-20081110
- Patch0 added to avoid gconf dependencity

* Mon Sep 29 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080929
- cvs-20080929

* Mon Sep 22 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080922
- cvs-20080922

* Sun Sep 21 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080921
- cvs-20080921

* Sat Sep 20 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080920
- cvs-20080920

* Fri Sep 19 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080919
- cvs-20080919

* Sat Sep 13 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080913
- cvs-20080913

* Thu Jul 17 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080717
- cvs-20080717
- Automake >= 1.9 needed for fresh jabber.el

* Sat May 31 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080531
- cvs-20080531

* Thu May  1 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080501
- cvs-20080501
- Migrate to new autotools build system

* Thu May  1 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080429
- cvs-20080429

* Tue Apr 15 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080415
- cvs-200804115

* Sat Mar  8 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080308
- cvs-20080308

* Sun Mar  2 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080302
- cvs-20080302

* Sun Feb 24 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080223
- cvs-20080223

* Thu Feb 21 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080221
- cvs-20080221

* Wed Feb 20 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080220
- cvs-20080220

* Tue Feb 19 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080219
- cvs-20080219
- All patches dropped (me gain write access to jabber.el CVS)

* Mon Feb 18 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080218
- cvs-20080218
- Unneeded patches removed (merged in upstream)

* Sun Feb 17 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080217
- cvs-20080217
- Texinfo documentation source code included in -el package

* Wed Feb  6 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080206
- cvs-2008206 (build for emacs23)

* Sun Feb  3 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080203
- cvs-20080203

* Fri Jan 25 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080122
- cvs-20080122

* Fri Jan 18 2008 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20080118
- cvs-20080118

* Sun Nov 18 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20071117
- cvs-20071117
- Patch1 removed (merged in upstream)

* Wed Nov  7 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20071106
- cvs-20071106
- Patch1 added

* Sun Oct 28 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20071028
- cvs-20071028
- Patch1 removed (replaced in upstream)
- Init script cleanup

* Sat Sep  1 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20070831.1
- Patch1 added

* Fri Aug 31 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20070831
- CVS-20070831
- Init script cleanup (obsoleted and frustrating code removed)

* Fri Aug 24 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20070824
- cvs-20070824

* Sun Aug 19 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20070819
- cvs-20070819
- License tag now macro (buildreq to rpm-build-licenses)
- Spec cleanup

* Sat Aug  4 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20070804
- Patch1 removed (merged in upstream)

* Thu Jul 12 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20070606.1
- Patch1 added

* Wed Jun  6 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20070606
- cvs-20070606

* Wed May  9 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20070509
- git-20070509 (git://git.catap.ru/emacs-jabber)
- Patch1 removed (merged in upstream)

* Sat Apr 28 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20070428
- Patch1 added

* Sat Apr 28 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20070428
- cvs-20070428

* Thu Apr 19 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20070419
- cvs-20070419
- All patches removed (commited in upstream)

* Mon Feb 19 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20070219
- Patch0 added again
- Patch1 added (temporary)
- cvs-20070219

* Thu Feb  1 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20070201
- cvs-20070201
- xmppuri.sh handler added

* Mon Jan  8 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20070108
- Patch0 removed (fixed in upstream)

* Mon Jan  8 2007 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20070108
- cvs-20070108

* Thu Dec 14 2006 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20061214
- Patch0 replaced by new version

* Tue Dec 12 2006 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20061212
- Long actions patch added (#0)

* Fri Dec  8 2006 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20061208
- jabber-emacs.el additionals

* Sun Nov 19 2006 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20061119
- cvs-alt0.20061119

* Sun Oct 22 2006 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20061022
- cvs-20061022
- Obsolete patch really removed (author claims that he really fix bug)

* Sat Oct 21 2006 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20061021
- cvs-20061021
- Obsolete patch removed

* Fri Oct 13 2006 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20061013
- cvs-20061013

* Sat Aug 26 2006 Terechkov Evgenii <evg@altlinux.ru> 0.8-alt0.20060826
- cvs-20060826

* Thu Mar 02 2006 Eugene Vlasov <eugvv@altlinux.ru> 0.7-alt1
- Initial build for Sisyphus
