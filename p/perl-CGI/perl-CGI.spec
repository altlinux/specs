%define dist CGI.pm
Name: perl-CGI
Version: 3.59
Release: alt1

Summary: Simple CGI class for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# avoid dependency on FCGI backend
%add_findreq_skiplist */CGI/Fast.pm

# disable conditional dependencies on Apache
%filter_from_requires /^perl.APR/d
%filter_from_requires /^perl.Apache/d
%filter_from_requires /^perl.ModPerl/d

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-Encode perl-FCGI perl-devel

%description
This is CGI.pm, an easy-to-use Perl5 library for writing
World Wide Web CGI scripts.

%prep
%setup -q -n %dist-%version
bzip2 -k Changes

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes.bz2 README examples
%perl_vendor_privlib/CGI*

%changelog
* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 3.59-alt1
- 3.58 -> 3.59

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 3.58-alt1
- 3.55 -> 3.58
- reverted MOD_PERL consting, installed dependency filters instead
- reverted TMPDIR patch, since the default behaviour is documented
- rebuilt as plain src.rpm

* Wed Sep 21 2011 Alexey Tourbin <at@altlinux.ru> 3.55-alt1
- 3.49 -> 3.55

* Wed Jan 19 2011 Alexey Tourbin <at@altlinux.ru> 3.49-alt2
- fixes for CVE-2010-4410 and CVE-2010-4411 (v5.12.3-RC2-1-gb7fa2ac)

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 3.49-alt1
- 3.44 -> 3.49

* Thu Jul 30 2009 Alexey Tourbin <at@altlinux.ru> 3.44-alt1
- 3.43 -> 3.44

* Tue Apr 07 2009 Alexey Tourbin <at@altlinux.ru> 3.43-alt1
- 3.42 -> 3.43

* Sun Sep 21 2008 Alexey Tourbin <at@altlinux.ru> 3.42-alt1
- 3.41 -> 3.42

* Sun Sep 07 2008 Alexey Tourbin <at@altlinux.ru> 3.41-alt1
- 3.39 -> 3.41

* Mon Aug 04 2008 Alexey Tourbin <at@altlinux.ru> 3.39-alt1
- 3.38 -> 3.39

* Sat Jun 28 2008 Alexey Tourbin <at@altlinux.ru> 3.38-alt1
- 3.37 -> 3.38

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 3.37-alt1
- 3.35 -> 3.37

* Tue Apr 15 2008 Alexey Tourbin <at@altlinux.ru> 3.35-alt1
- 3.33 -> 3.35

* Sun Mar 02 2008 Alexey Tourbin <at@altlinux.ru> 3.33-alt1
- 3.29 -> 3.33

* Mon Aug 20 2007 Alexey Tourbin <at@altlinux.ru> 3.29-alt2
- changed src.rpm packaging to keep upstream tarball unchanged

* Tue Apr 17 2007 Alexey Tourbin <at@altlinux.ru> 3.29-alt1
- 3.28 -> 3.29

* Fri Mar 30 2007 Alexey Tourbin <at@altlinux.ru> 3.28-alt1
- 3.25 -> 3.28
- fixed insecure temporary file creation in CGI.pm

* Fri Oct 06 2006 Alexey Tourbin <at@altlinux.ru> 3.25-alt1
- 3.23 -> 3.25
- imported sources into git and built with gear
- turned mod_perl variables into constants so that constant folding works;
  relaxed mode for perl.req is not needed now

* Fri Aug 25 2006 Alexey Tourbin <at@altlinux.ru> 3.23-alt1
- 3.22 -> 3.23

* Thu Aug 24 2006 Alexey Tourbin <at@altlinux.ru> 3.22-alt1
- 3.21 -> 3.22

* Tue Aug 22 2006 Alexey Tourbin <at@altlinux.ru> 3.21-alt1
- 3.20 -> 3.21

* Wed Apr 26 2006 Alexey Tourbin <at@altlinux.ru> 3.20-alt1
- 3.17 -> 3.20

* Mon Apr 17 2006 Alexey Tourbin <at@altlinux.ru> 3.17-alt1
- 3.11 -> 3.17

* Mon Aug 08 2005 Alexey Tourbin <at@altlinux.ru> 3.11-alt1
- 3.10 -> 3.11

* Sat May 21 2005 Alexey Tourbin <at@altlinux.ru> 3.10-alt1
- 3.09 -> 3.10
- removed old dependencies

* Sat May 07 2005 Alexey Tourbin <at@altlinux.ru> 3.09-alt1
- 3.07 -> 3.09

* Sat Mar 19 2005 Alexey Tourbin <at@altlinux.ru> 3.07-alt1.1
- fixed $CGI::Apache::VERSION (cpan #11941)
- fixed $CGI::Switch::VERSION (cpan #11942)

* Wed Mar 16 2005 Alexey Tourbin <at@altlinux.ru> 3.07-alt1
- 3.06 -> 3.07

* Thu Mar 10 2005 Alexey Tourbin <at@altlinux.ru> 3.06-alt1
- 3.05 -> 3.06
- cgi_docs.html not packaged (no longer maintained)
- cgi-lib_porting.html not packaged (cgi-lib.pl was defunct)
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.05-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Jul 02 2004 Alexey Tourbin <at@altlinux.ru> 3.05-alt1
- 3.04 -> 3.05

* Tue Mar 16 2004 Alexey Tourbin <at@altlinux.ru> 3.04-alt1
- 3.04

* Fri Dec 19 2003 Alexey Tourbin <at@altlinux.ru> 3.01-alt1
- 3.01
- upload_tmpdir.patch not needed

* Thu Aug 21 2003 Alexey Tourbin <at@altlinux.ru> 3.00-alt1
- 3.00 (cross-site scripting vulnerability fixed)
- upload_tmpdir.patch updated

* Tue Jul 22 2003 Alexey Tourbin <at@altlinux.ru> 2.98-alt1
- 2.98 (crash in Dump function fixed)
- upload_tmpdir.patch updated

* Thu Jul 10 2003 Alexey Tourbin <at@altlinux.ru> 2.97-alt1
- 2.97 (bugfixes)

* Mon Jun 16 2003 Alexey Tourbin <at@altlinux.ru> 2.95-alt1
- 2.95
- merged packages down, with dependency tuning

* Fri Mar 21 2003 Stanislav Ievlev <inger@altlinux.ru> 2.91-alt1
- 2.91

* Tue Nov 12 2002 Stanislav Ievlev <inger@altlinux.ru> 2.89-alt2
- hack reqs

* Thu Oct 31 2002 Alexey Tourbin <at@altlinux.ru> 2.89-alt1
- 2.89
- package split: perl-CGI, perl-CGI-Apache, perl-CGI-FCGI
- perl-5.8 build with new rpm macros

* Sun Mar 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.80-alt1
- 2.80
- spec file skeletonization.

* Mon Jun 25 2001 Stanislav Ievlev <inger@altlinux.ru> 2.752-alt1
- Release for ALT Linux.

* Wed Apr 25 2001 Pixel <pixel@mandrakesoft.com> 2.752-2mdk
- rebuild with new perl

* Sat Mar  3 2001 Pixel <pixel@mandrakesoft.com> 2.752-1mdk
- cleanup (made by Alexander Skwar <ASkwar@Linux-Mandrake.com>)
- First seperate Mandrake version
- Added Upload Tmpdir patch from perl
- Requires perl *WITHOUT* CGI.pm!
