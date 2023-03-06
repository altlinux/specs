%define _unpackaged_files_terminate_build 1
# we need a font
BuildRequires: fonts-ttf-liberation
%define module GraphViz

Name: perl-%module
Version: 2.26
Release: alt1

Summary: Interface to the GraphViz graphing tool
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source0: http://www.cpan.org/authors/id/E/ET/ETJ/%{module}-%{version}.tar.gz

BuildArch: noarch

Requires: graphviz

# Automatically added by buildreq on Sun Mar 25 2012 (-bi)
BuildRequires: fonts-type1-urw graphviz perl-File-Which perl-IPC-Run perl-Module-Build perl-Parse-RecDescent perl-Test-Pod perl-XML-Twig

%description
This module provides an interface to layout and image generation of directed and
undirected graphs in a variety of formats (PostScript, PNG, etc.) using the
"dot", "neato", "twopi", "circo" and "fdp" programs from the GraphViz project.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_privlib/GraphViz*
%perl_vendor_privlib/Devel/GraphViz*

%changelog
* Mon Mar 06 2023 Igor Vlasenko <viy@altlinux.org> 2.26-alt1
- automated CPAN update

* Mon Aug 22 2022 Igor Vlasenko <viy@altlinux.org> 2.25-alt1
- automated CPAN update

* Mon Apr 04 2022 Igor Vlasenko <viy@altlinux.org> 2.24-alt2
- fixed build

* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.24-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.22-alt1
- automated CPAN update

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 2.20-alt1
- automated CPAN update

* Tue Dec 08 2015 Igor Vlasenko <viy@altlinux.ru> 2.19-alt2
- NMU: fixed build with perl 522

* Fri Nov 13 2015 Igor Vlasenko <viy@altlinux.ru> 2.19-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.18-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.16-alt1
- automated CPAN update

* Thu Nov 28 2013 Igor Vlasenko <viy@altlinux.ru> 2.15-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.14-alt1
- automated CPAN update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1
- automated CPAN update

* Sun Apr 01 2012 Victor Forsiuk <force@altlinux.org> 2.10-alt1
- 2.10

* Sun Mar 25 2012 Victor Forsiuk <force@altlinux.org> 2.09-alt1
- 2.09

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Dec 29 2008 Victor Forsyuk <force@altlinux.org> 2.04-alt1
- 2.04

* Thu Jan 10 2008 Victor Forsyuk <force@altlinux.org> 2.03-alt1
- 2.03

* Thu Jul 26 2007 Victor Forsyuk <force@altlinux.org> 2.02-alt2
- Spec cleanups.

* Thu Aug 25 2005 Alexey Morozov <morozov@altlinux.org> 2.02-alt1
- Initial build for ALT Linux
