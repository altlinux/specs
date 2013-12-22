Name: parallel
Version: 20131222
Release: alt1

Summary: A shell tool for executing jobs in parallel
License: GPLv3
Group: File tools

Url: http://www.gnu.org/software/parallel
Source: http://ftp.gnu.org/gnu/parallel/%name-%version.tar.bz2
Source100: parallel.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Tue Apr 16 2013
# optimized out: perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators
BuildRequires: perl-Pod-Parser perl-devel

BuildArch: noarch

%description
GNU parallel is a shell tool for executing jobs in parallel
locally or using remote machines. A job is typically a single
command or a small script that has to be run for each of the
lines in the input. The typical input is a list of files, a list
of hosts, a list of users, a list of URLs, or a list of tables.

%prep
%setup

%build
%configure
%make

%install
%makeinstall
rm -r %buildroot%_defaultdocdir/%name/

%files
%doc README NEWS src/*.html
%_bindir/*
%_man1dir/*

%changelog
* Sun Dec 22 2013 Michael Shigorin <mike@altlinux.org> 20131222-alt1
- new version (watch file uupdate)
- NB: "this release is alpha quality"

* Sat Nov 23 2013 Michael Shigorin <mike@altlinux.org> 20131122-alt1
- new version (watch file uupdate)

* Tue Oct 22 2013 Michael Shigorin <mike@altlinux.org> 20131022-alt1
- new version (watch file uupdate)

* Sat Sep 21 2013 Michael Shigorin <mike@altlinux.org> 20130922-alt1
- new version (watch file uupdate)

* Thu Aug 22 2013 Michael Shigorin <mike@altlinux.org> 20130822-alt1
- new version (watch file uupdate)

* Mon Jul 22 2013 Michael Shigorin <mike@altlinux.org> 20130722-alt1
- new version (watch file uupdate)

* Sat Jun 22 2013 Michael Shigorin <mike@altlinux.org> 20130622-alt1
- new version (watch file uupdate)

* Wed May 22 2013 Michael Shigorin <mike@altlinux.org> 20130522-alt1
- new version (watch file uupdate)

* Mon Apr 22 2013 Michael Shigorin <mike@altlinux.org> 20130422-alt1
- new version (watch file uupdate)

* Tue Apr 16 2013 Michael Shigorin <mike@altlinux.org> 20130222-alt2
- buildreq (thus cleaned up extremely weird BRs from 2011)

* Fri Feb 22 2013 Michael Shigorin <mike@altlinux.org> 20130222-alt1
- new version (watch file uupdate)
- dropped bzr from BR

* Tue Jan 22 2013 Michael Shigorin <mike@altlinux.org> 20130122-alt1
- new version (watch file uupdate)

* Sun Dec 23 2012 Michael Shigorin <mike@altlinux.org> 20121222-alt1
- new version (watch file uupdate)

* Thu Nov 22 2012 Michael Shigorin <mike@altlinux.org> 20121122-alt1
- new version (watch file uupdate)

* Tue Oct 23 2012 Michael Shigorin <mike@altlinux.org> 20121022-alt1
- new version (watch file uupdate)

* Thu Aug 23 2012 Michael Shigorin <mike@altlinux.org> 20120822-alt1
- new version (watch file uupdate)

* Sat Jun 23 2012 Michael Shigorin <mike@altlinux.org> 20120622-alt1
- new version (watch file uupdate)

* Tue May 22 2012 Michael Shigorin <mike@altlinux.org> 20120522-alt1
- new version (watch file uupdate)

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 20120422-alt2
- added watch file

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 20120422-alt1
- 20120422

* Fri Mar 23 2012 Michael Shigorin <mike@altlinux.org> 20120322-alt1
- 20120322 (bugfixes only, no new features)

* Tue Feb 28 2012 Michael Shigorin <mike@altlinux.org> 20120222-alt1
- 20120222

* Sun Jan 22 2012 Michael Shigorin <mike@altlinux.org> 20120122-alt1
- 20120122

* Thu Dec 22 2011 Michael Shigorin <mike@altlinux.org> 20111222-alt1
- 20111222

* Wed Nov 23 2011 Michael Shigorin <mike@altlinux.org> 20111122-alt1
- 20111122

* Sun Oct 23 2011 Michael Shigorin <mike@altlinux.org> 20111022-alt1
- 20111022

* Mon Aug 22 2011 Michael Shigorin <mike@altlinux.org> 20110822-alt1
- 20110822

* Fri Jul 22 2011 Michael Shigorin <mike@altlinux.org> 20110722-alt1
- 20110722

* Wed Jun 22 2011 Michael Shigorin <mike@altlinux.org> 20110622-alt1
- 20110622

* Sun May 22 2011 Michael Shigorin <mike@altlinux.org> 20110522-alt1
- 20110522

* Fri Apr 22 2011 Michael Shigorin <mike@altlinux.org> 20110422-alt1
- 20110422

* Tue Mar 22 2011 Michael Shigorin <mike@altlinux.org> 20110322-alt1
- 20110322

* Tue Feb 08 2011 Michael Shigorin <mike@altlinux.org> 20110205-alt1
- 20110205

* Sun Jan 23 2011 Michael Shigorin <mike@altlinux.org> 20110122-alt1
- 20110122

* Wed Dec 22 2010 Michael Shigorin <mike@altlinux.org> 20101222-alt1
- 20101222

* Sat Dec 04 2010 Michael Shigorin <mike@altlinux.org> 20101202-alt1
- 20101202

* Thu Nov 18 2010 Michael Shigorin <mike@altlinux.org> 20101113-alt1
- 20101113

* Thu Sep 23 2010 Michael Shigorin <mike@altlinux.org> 20100922-alt1
- 20100922

* Tue Sep 07 2010 Michael Shigorin <mike@altlinux.org> 20100906-alt1
- 20100906
  + added sem(1) and sql(1)

* Sat Aug 21 2010 Michael Shigorin <mike@altlinux.org> 20100722-alt1
- built for ALT Linux (based on cooker spec)
- include HTML documentation
- noarch

* Thu Jul 29 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100722-3mdv2011.0
+ Revision: 563194
- fix summary with "shell tool", recommended by upstream.
- fix summary (thanks Samuel Verschelde)

* Sat Jul 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100722-1mdv2011.0
+ Revision: 557949
- fix description (it's a perl tool!)
- update to 20100722

  + Jani Välimaa <wally@mandriva.org>
    - split one-liner description to a multiple lines
    - fix one file appearing twice in file list

* Fri Jul 16 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100620-2mdv2011.0
+ Revision: 554151
- Add Require

* Fri Jul 16 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100620-1mdv2011.0
+ Revision: 554150
- import parallel

