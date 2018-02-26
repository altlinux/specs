#################### WARNING! ######################
# this spec file is for ALT Linux distro only.     #
# other distro may have problems with rpm macro!!! #
####################################################

%define module HTML-Template-Pro

Name: perl-%module
Version: 0.9509
Release: alt1

Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Perl+C/XS module to produce HTML from HTML Template files.
Group: Development/Perl
License: LGPL2+ or Artistic
#Source: http://www.cpan.org/modules/by-module/HTML/%module-%version.tar.gz
Source: %module-%version.tar.gz
Url: http://sourceforge.net/projects/html-tmpl-pro/

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel pcre libpcre-devel perl-JSON perl-JSON-XS

%description
HTML::Template::Pro is a fast lightweight C/Perl+XS reimplementation
of HTML::Template and HTML::Template::Expr. It is not intended 
to be a complete replacement, but to be a fast implementation 
of HTML::Template if you don't need quering, the extended facility
of HTML::Template. 
Designed for heavy upload, resource limitations, abcence of mod_perl.

HTML::Template module attempts make using HTML templates simple and natural. 
It extends standard HTML with a few new HTML-esque tags - <TMPL_VAR>,
<TMPL_LOOP>, <TMPL_INCLUDE>, <TMPL_IF> and <TMPL_ELSE>.  The file
written with HTML and these new tags is called a template.  It is
usually saved separate from your script - possibly even created by
someone else!  Using this module you fill in the values for the
variables, loops and branches declared in the template.  This allows
you to seperate design - the HTML - from the data, which you generate
in the Perl script.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes README.ru FAQ TODO
%perl_vendor_archlib/*
#perl_vendor_man3dir/*

%changelog
* Tue Feb 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.9509-alt1
- new version; see Changes

* Mon Dec 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.9508-alt1
- new version; see Changes

* Fri Dec 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.9507-alt1
- new version; see Changes

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 0.9506-alt2
- rebilt for perl-5.14

* Tue Oct 04 2011 Igor Vlasenko <viy@altlinux.ru> 0.9506-alt1
- new version; see Changes

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.9505-alt1
- new version; see Changes

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9504-alt1.1
- rebuilt with perl 5.12

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0.9504-alt1
- new version; see Changes

* Sat Aug 28 2010 Igor Vlasenko <viy@altlinux.ru> 0.9503-alt1
- new version; see Changes

* Thu Jun 17 2010 Igor Vlasenko <viy@altlinux.ru> 0.9502-alt1
- new version; see Changes

* Wed Jun 09 2010 Igor Vlasenko <viy@altlinux.ru> 0.9501-alt1
- new version; see Changes

* Fri May 21 2010 Igor Vlasenko <viy@altlinux.ru> 0.95-alt1
- new version; see Changes

* Tue Feb 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- new version; see Changes

* Sun Nov 15 2009 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1
- new version; see Changes

* Tue Sep 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1
- new version; see Changes

* Tue Sep 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1
- new version; see Changes

* Sat Sep 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.90-alt3
- release

* Fri Sep 11 2009 Igor Vlasenko <viy@altlinux.ru> 0.90-alt2
- rc2

* Mon Aug 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.90-alt1
- rc1

* Sat Aug 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.87-alt1
- new version; see Changes

* Sat Aug 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.86-alt1
- new version; see Changes

* Sun Aug 09 2009 Igor Vlasenko <viy@altlinux.ru> 0.85-alt1
- new version; see Changes

* Fri Aug 07 2009 Igor Vlasenko <viy@altlinux.ru> 0.84-alt1
- new version; see Changes

* Wed Aug 05 2009 Igor Vlasenko <viy@altlinux.ru> 0.83-alt1
- new version; see Changes

* Wed Jul 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.82-alt1
- new version; see Changes

* Tue Jul 28 2009 Igor Vlasenko <viy@altlinux.ru> 0.81-alt1
- new version; see Changes

* Thu Jul 23 2009 Igor Vlasenko <viy@altlinux.ru> 0.80-alt1
- new version; see Changes

* Tue Jul 21 2009 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1
- new version; see Changes

* Sat Jul 11 2009 Igor Vlasenko <viy@altlinux.ru> 0.76-alt1
- new version; see Changes

* Wed Jul 01 2009 Igor Vlasenko <viy@altlinux.ru> 0.75-alt1
- new version; see Changes

* Fri Apr 03 2009 Igor Vlasenko <viy@altlinux.ru> 0.74-alt1
- new version; see Changes

* Thu Apr 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1
- new version; see Changes

* Thu Dec 18 2008 Igor Vlasenko <viy@altlinux.ru> 0.72-alt1
- new version; see Changes

* Sat Aug 16 2008 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1
- new version; see Changes

* Thu Apr 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.70-alt1
- new version; see Changes

* Thu Feb 28 2008 Igor Vlasenko <viy@altlinux.ru> 0.69-alt1
- new version; see Changes

* Tue Jan 08 2008 Igor Vlasenko <viy@altlinux.ru> 0.68-alt2
- fix for ix86

* Tue Jan 08 2008 Igor Vlasenko <viy@altlinux.ru> 0.68-alt1
- new version; see Changes

* Sun Dec 02 2007 Igor Vlasenko <viy@altlinux.ru> 0.67-alt1
- new version; see Changes

* Thu Oct 04 2007 Igor Vlasenko <viy@altlinux.ru> 0.66-alt1
- new version; see Changes

* Fri Jun 01 2007 Igor Vlasenko <viy@altlinux.ru> 0.65-alt1
- new version

* Tue Apr 18 2006 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1
- new version

* Mon Apr 17 2006 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- new version

* Tue Feb 21 2006 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- new version

* Sat Feb 04 2006 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- new version

* Thu Feb 02 2006 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- new version

* Sun Jan 22 2006 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1
- new version

* Fri Dec 02 2005 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1
- new version

* Tue Nov 08 2005 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1
- new version

* Tue Nov 01 2005 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- new version

* Mon Oct 24 2005 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- new version

* Mon Oct 17 2005 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- new version

* Thu Oct 06 2005 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- new version

* Fri Sep 30 2005 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- new version

* Thu Sep 15 2005 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- new version

* Thu Sep 01 2005 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- new version

* Wed Aug 31 2005 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- new version

* Wed Aug 31 2005 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- new version

* Sat Aug 20 2005 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- new version

* Fri Aug 19 2005 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- new version

* Fri Aug 12 2005 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- new version

* Thu Aug 04 2005 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- new version

* Thu Aug 04 2005 Igor Vlasenko <viy@altlinux.org> 0.42-alt1
- new version

* Tue Jul 26 2005 Igor Vlasenko <viy@altlinux.org> 0.41-alt1
- new version

* Fri Jul 01 2005 Igor Vlasenko <viy@altlinux.org> 0.40-alt1
- basic support for string comparing (HTML::Template::Expr)

* Thu Jun 22 2005 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- new version

* Thu Jun 09 2005 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- new version, basic support for HTML::Template::Expr

* Thu Jun 02 2005 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- new version

* Mon May 23 2005 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- new version

* Thu May 19 2005 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- First build for Sisyphus.

* Sun May 15 2005 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1.1
- First build for Daedalus.
