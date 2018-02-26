%define dist HTML-Template
Name: perl-%dist
Version: 2.10
Release: alt1

Summary: Perl module to use HTML Templates from CGI scripts
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# from Fedora
Patch: perl-HTML-Template-2.10-versioning.patch

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-CGI perl-Encode perl-devel

%description
This module attempts make using HTML templates simple and natural. It
extends standard HTML with a few new HTML-esque tags - <TMPL_VAR>,
<TMPL_LOOP>, <TMPL_INCLUDE>, <TMPL_IF> and <TMPL_ELSE>.  The file
written with HTML and these new tags is called a template.  It is
usually saved separate from your script - possibly even created by
someone else!  Using this module you fill in the values for the
variables, loops and branches declared in the template.  This allows
you to seperate design - the HTML - from the data, which you generate
in the Perl script.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README scripts templates
%perl_vendor_privlib/HTML

%changelog
* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 2.10-alt1
- 2.9 -> 2.10
- applied versioning.patch from Fedora

* Sun Mar 08 2009 Alexey Tourbin <at@altlinux.ru> 2.9-alt1
- 2.8 -> 2.9

* Fri Aug 11 2006 Alexey Tourbin <at@altlinux.ru> 2.8-alt1
- 2.6 -> 2.8

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.6-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 2.6-alt2
- rebuild with new perl

* Sat Mar 9 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.5-alt1
- First build for Sisyphus.
