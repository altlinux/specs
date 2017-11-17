%define _unpackaged_files_terminate_build 1
%define dist Gnome2

Name: perl-%dist
Version: 1.047
Release: alt1.1

Summary: Gnome2 Perl module
License: LGPLv2.1+
Group: Development/Perl

Url: %CPAN %dist
Source0: http://www.cpan.org/authors/id/X/XA/XAOC/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: libgnomeui-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Gnome2-Canvas-devel perl-Gnome2-VFS-devel perl-podlators zsh

%package devel
Summary: Gnome2 Perl module (development files)
License: LGPLv2.1+
Group: Development/Perl
Requires: %name = %version-%release
Requires: libgnomeui-devel
# Gnome2/Install/Files.pm:deps
Requires: perl-Pango-devel
Requires: perl-Gnome2-Canvas-devel
Requires: perl-Glib-devel
Requires: perl-Gnome2-VFS-devel
Requires: perl-Gtk2-devel
Requires: perl-Cairo-devel

%description
Perl bindings to the 2.x series of the Gnome widget set. This module allows
you to write graphical user interfaces in a perlish and object-oriented way,
freeing you from the casting and memory management in C, yet remaining very 
close in spirit to original API.

%description devel
Perl bindings to the 2.x series of the Gnome widget set. This module allows
you to write graphical user interfaces in a perlish and object-oriented way,
freeing you from the casting and memory management in C, yet remaining very 
close in spirit to original API.

This package contains Gnome2 development files and documentation
for developers (overview of internals and internal API reference).

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	AUTHORS NEWS README ChangeLog.pre-git copyright.pod examples
	%perl_vendor_archlib/Gnome2.pm
	%perl_vendor_autolib/Gnome2

%files devel
%dir	%perl_vendor_archlib/Gnome2
%doc	%perl_vendor_archlib/Gnome2/*.pod
	%perl_vendor_archlib/Gnome2/Install

%doc	%perl_vendor_archlib/Gnome2/Bonobo
%doc	%perl_vendor_archlib/Gnome2/Config

%changelog
* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.047-alt1.1
- automated CPAN update

* Wed Nov 08 2017 Igor Vlasenko <viy@altlinux.ru> 1.047-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.046-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.046-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.046-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.045-alt1.1
- rebuild with new perl 5.20.1

* Tue Dec 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.045-alt1
- automated CPAN update

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.044-alt1
- automated CPAN update

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.043-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.042-alt5
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 1.042-alt4
- rebuilt for perl-5.16

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 1.042-alt3
- rebuilt for perl-5.14

* Wed Mar 09 2011 Vladimir Lettiev <crux@altlinux.ru> 1.042-alt2
- Updated BuildRequires
- Enabled tests

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 1.042-alt1.1
- rebuilt with perl 5.12

* Fri Oct 26 2007 Victor Forsyuk <force@altlinux.org> 1.042-alt1
- 1.042

* Wed Jul 04 2007 Victor Forsyuk <force@altlinux.org> 1.041-alt2
- Update build requirements (libSM-devel now have to be listed explicitly).

* Sat Jan 20 2007 Victor Forsyuk <force@altlinux.org> 1.041-alt1
- 1.041
- Spec simplification.
- Updated BuildRequires.

* Tue Aug 16 2005 LAKostis <lakostis at altlinux.ru> 1.023-alt1
- 1.023.

* Wed Mar 16 2005 LAKostis <lakostis at altlinux.ru> 1.021-alt1.1
- cleanup buildreq/requires.
- fix URL entry.
- add missing requries to -devel package.

* Sun Mar 07 2005 LAKostis <lakostis at altlinux.ru> 1.021-alt1
- manual pages not packaged (use perldoc)
- first build for Sisyphus.
