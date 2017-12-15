Name:           perl-RPM2
Version:        1.3
Release:        alt1.1.1
Summary:        Perl bindings for the RPM Package Manager API
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/RPM2/
Source0:        %name-%version.tar

BuildRequires: librpm-devel
BuildRequires: perl-ExtUtils-CBuilder
BuildRequires: perl-Module-Build
BuildRequires: perl-JSON-PP

%description
The RPM2 module provides an object-oriented interface to querying both the
installed RPM database as well as files on the filesystem, providing Perl
bindings for the RPM Package Manager API.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/RPM*
%perl_vendor_autolib/RPM*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1.1
- rebuild with new perl 5.24.1

* Tue Aug 30 2016 Alexey Gladkov <legion@altlinux.ru> 1.3-alt1
- First build for ALTLinux.

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.3-2
- Perl 5.24 rebuild

* Wed Feb 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.3-1
- 1.3 bump

* Tue Feb 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-1
- 1.2 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Petr Pisar <ppisar@redhat.com> - 1.0-15
- Rebuild against rpm-4.13

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-13
- Perl 5.22 rebuild

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.0-12
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.0-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 1.0-5
- Perl 5.16 rebuild

* Thu May 31 2012 Petr Pisar <ppisar@redhat.com> - 1.0-4
- Round Module::Build version to 2 digits

* Thu Apr 26 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.0-3
- switch off some functions for now, which were defined as "private" in new rpm
- rebuild with new rpm-4.10

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Petr Sabata <contyk@redhat.com> - 1.0-1
- 1.0 bump
- Switching to Module::Build
- Removing redundant buildroot and defattr stuff
- Adding testplan patch to match test count

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.69-4
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.69-3
- Perl 5.14 mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 08 2011 Lubomir Rintel <lkundrak@v3.sk> - 0.69-1
- Release 0.69

* Fri Jan 21 2011 Petr Pisar <ppisar@redhat.com> - 0.68-10
- Partial adjustment to rpm-4.9.0. Can compile, cannot run (see bug #671389).

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.68-9
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.68-8
- Mass rebuild with perl-5.12.0

* Sat Feb 13 2010 Chris Weyl <cweyl@alumni.drew.edu> - 0.68-7
- add perl_default_filter (to remove errant private so metadata)
- PERL_INSTALL_ROOT => DESTDIR

* Fri Dec 11 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.68-6
- Rebuild for RPM 4.8.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.68-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 06 2009 Jesse Keating <jkeating@redhat.com> - 0.68-3
- Rebuild for new rpm

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.68-1
- New upstream release
- Drop patches

* Fri Dec 12 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.67-7
- Port to RPM 4.6

* Thu Sep 11 2008 Jesse Keating <jkeating@redhat.com> - 0.67-6
- Rebuild for rpm deps

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.67-5
- Rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.67-4
- Autorebuild for GCC 4.3

* Fri Oct 26 2007 Lubomir Kundrak <lkundrak@redhat.com> - 0.67-3
- Fix reading of non-32bit int tag values
- Correct the License tag

* Mon May  7 2007 Robin Norwood <rnorwood@redhat.com> - 0.67-2
- Add BuildRequires perl(ExtUtils::MakeMaker)

* Wed Jan  3 2007 Paul Howarth <paul@city-fan.org> 0.67-1
- update to 0.67, which clarifies license
- dispense with redundant (for Fedora) reqs and buildreqs
- don't use autogenerated file lists, which can miss directory ownership
  (fixes #73921)

* Wed Mar 08 2006 Jason Vas Dias <jvdias@redhat.com> - 0.66-12
- fix bug 152535: correct Provides: file list
- make .spec file conform to fedora-rpmdevtools/spectemplate-perl.spec

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 0.66-11.1
- rebuild for new perl-5.8.8, gcc, glibc, rpm

* Thu Nov 10 2005 Tomas Mraz <tmraz@redhat.com> 0.66-11
- rebuilt against new openssl
- fixed filelist for compressed man page

* Wed Mar 30 2005 Warren Togami <wtogami@redhat.com>
- remove brp-compress

* Tue Mar 22 2005 Joe Orton <jorton@redhat.com> 0.66-9
- rebuild

* Sun Feb 13 2005 Florian La Roche <laroche@redhat.com>
- rebuild

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jan 13 2004 Dan Walsh <dwalsh@redhat.com> 0.45-6
- rebuilt to pick up new rpm

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Nov 07 2002 Elliot Lee <sopwith@redhat.com> 0.45-2
- Rebuild

* Wed Sep  4 2002 Chip Turner <cturner@redhat.com>
- fix segfaults and destructor issues related to typing overlap in
  perl XS mappings

* Mon Aug 26 2002 Chip Turner <cturner@redhat.com>
- add -lelf temporarily

* Wed Aug 07 2002 cturner@redhat.com
- Specfile autogenerated

