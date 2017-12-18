%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Config.pm) perl(Encode.pm) perl(Encode/CN.pm) perl(Encode/JP.pm) perl(Encode/KR.pm) perl(Encode/TW.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(FindBin.pm) perl(HTML/Entities.pm) perl(IO/File.pm) perl(IO/Handle.pm) perl(Test/Deep.pm) perl(Test/More.pm) perl(Test/NoWarnings.pm) perl(Test/Warn.pm) perl(Text/ParseWords.pm) perl(overload.pm) perl(parent.pm) perl(strict.pm) perl(utf8.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_name CGI
Name: perl-CGI
Version: 4.38
Release: alt1

Summary: Simple CGI class for Perl
License: perl
Group: Development/Perl

URL: https://metacpan.org/module/CGI
Source0: http://www.cpan.org/authors/id/L/LE/LEEJO/%{module_name}-%{version}.tar.gz
Patch0:  CGI-4.15-Make-Test-Deep-and-Test-NoWarnings-tests-optional.patch

BuildArch: noarch

# avoid dependency on FCGI backend
%add_findreq_skiplist */CGI/Fast.pm

# disable conditional dependencies on Apache
%filter_from_requires /^perl.APR/d
%filter_from_requires /^perl.Apache/d
%filter_from_requires /^perl.ModPerl/d

# back compatibility package for any code explicitly checking
# that the filehandle object is a Fh
%filter_from_requires /^perl.Fh/d
%filter_from_provides /^perl.Fh/d

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-Encode perl-FCGI perl-devel perl-podlators

%description
This is CGI.pm, an easy-to-use Perl5 library for writing
World Wide Web CGI scripts.

CGI.pm is a stable, complete and mature solution for processing and preparing
HTTP requests and responses. Major features including processing form
submissions, file uploads, reading and writing cookies, query string
generation and manipulation, and processing and preparing HTTP headers. Some
HTML generation utilities are included as well.

CGI.pm performs very well in in a vanilla CGI.pm environment and also comes 
with built-in support for mod_perl and mod_perl2 as well as FastCGI.

%prep
%setup -q -n %{module_name}-%{version}
#patch0 -p1
iconv -f iso8859-1 -t utf-8 < Changes > Changes.1
mv Changes.1 Changes
sed -i 's?usr/bin perl?usr/bin/perl?' t/init.t
chmod -c -x examples/*

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md examples
%perl_vendor_privlib/CGI*
%perl_vendor_privlib/Fh.pm

%changelog
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 4.38-alt1
- automated CPAN update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 4.37-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 4.36-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 4.35-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 4.33-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 4.32-alt1
- automated CPAN update

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 4.31-alt1
- automated CPAN update

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 4.30-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 4.28-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 4.27-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 4.26-alt1
- automated CPAN update

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 4.25-alt1
- automated CPAN update

* Mon Dec 21 2015 Igor Vlasenko <viy@altlinux.ru> 4.23-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 4.22-alt1
- new version; switched branches:
  from L/LE/LEEJO/CGI.pm-4.03.tar.gz to L/LE/LEEJO/CGI-4.22.tar.gz

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.03-alt1
- automated CPAN update

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 4.02-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 4.01-alt1
- automated CPAN update

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.65-alt1
- automated CPAN update

* Thu Nov 15 2012 Vladimir Lettiev <crux@altlinux.ru> 3.63-alt1
- 3.60 -> 3.63

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 3.60-alt1
- 3.59 -> 3.60

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
