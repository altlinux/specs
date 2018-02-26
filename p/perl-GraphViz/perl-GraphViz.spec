%define module GraphViz

Name: perl-%module
Version: 2.10
Release: alt1

Summary: Interface to the GraphViz graphing tool
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/R/RS/RSAVAGE/GraphViz-%version.tgz

BuildArch: noarch

Requires: graphviz

# Automatically added by buildreq on Sun Mar 25 2012 (-bi)
BuildRequires: fonts-type1-urw graphviz perl-File-Which perl-IPC-Run perl-Module-Build perl-Parse-RecDescent perl-Test-Pod perl-XML-Twig

%description
This module provides an interface to layout and image generation of directed and
undirected graphs in a variety of formats (PostScript, PNG, etc.) using the
"dot", "neato", "twopi", "circo" and "fdp" programs from the GraphViz project.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/GraphViz*
%perl_vendor_privlib/Devel/GraphViz*

%changelog
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
