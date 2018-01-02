%define module Source-Shared-CLI

Name: perl-%module
Version: 0.008
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - yet another framework for CLI module configuration
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl(Module/Build/Tiny.pm)

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
#doc Changes
#doc README
%perl_vendor_privlib/S*

%changelog
* Tue Jan 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- new version

* Sat May 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- new version

* Mon Jan 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- new version

* Mon Jan 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- new version

* Sun Jan 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- bugfix release

* Sat Jan 21 2017 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- new version

* Sat Jan 21 2017 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- new version

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version
