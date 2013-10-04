%define dist Alien-wxWidgets

Name: perl-%dist
Version: 0.64
Release: alt1

Summary: Alien-wxWidgets - building, finding and using wxWidgets binaries

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Slava Dubrovskiy <dubrsl@altlinux.org>
Source: http://www.cpan.org/authors/id/M/MD/MDOOTSON/Alien-wxWidgets-%{version}.tar.gz

BuildRequires: gcc-c++ perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage wxGTK-devel wxGTK-contrib-stc-devel perl-autodie perl-Module-Pluggable

%description
Alien::wxWidgets allows wxPerl to easily find information about
your wxWidgets installation. It can store this information for multiple
wxWidgets versions or configurations (debug, Unicode, etc.). It can also
build and install a private copy of wxWidgets as part of the build process

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_autolib/Alien/wxWidgets
%perl_vendor_archlib/Alien/wxWidgets*

%changelog
* Fri Oct 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1
- automated CPAN update

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 0.60-alt1
- 0.52 -> 0.60

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- automated CPAN update

* Sat Nov 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.51-alt1
- New version
- Remove patch
- Add description

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.50-alt2.1
- rebuilt with perl 5.12
- fixed build

* Mon Mar 29 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.50-alt2
- Fix build (Thanks at@)

* Fri Jan 29 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.50-alt1
- New version

* Fri Nov 21 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.42-alt1
- New version
- Remove BuildArch: noarch

* Fri Oct 17 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.40-alt1
- New version

* Thu Sep 11 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.39-alt1
- New version

* Tue Nov 13 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.32-alt1
- first build for ALT Linux Sisyphus

