%define module_name PAR-Dist

Name: perl-%module_name
Version: 0.48
Release: alt1

Summary: %module_name module for perl
License: Perl
Group: Development/Perl

Url: %CPAN %module_name
Source: http://www.cpan.org/modules/by-module/PAR/%module_name-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 30 2009
BuildRequires: perl-Archive-Zip perl-Test-Pod perl-Test-Pod-Coverage perl-YAML-Syck
# NB: Author prefer YAML::Syck and describe YAML.pm (perl-YAML) as "slow and aging"

%description
PAR::Dist, a toolkit to create and manipulate PAR distributions.

%prep
%setup -n %module_name-%version

%build
export PERL_TEST_POD=1
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/PAR/

%changelog
* Fri Mar 09 2012 Victor Forsiuk <force@altlinux.org> 0.48-alt1
- 0.48

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Nov 30 2009 Victor Forsyuk <force@altlinux.org> 0.47-alt1
- 0.47

* Tue Dec 30 2008 Victor Forsyuk <force@altlinux.org> 0.41-alt1
- 0.41

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 0.36-alt1
- 0.36

* Wed Jun 04 2008 Victor Forsyuk <force@altlinux.org> 0.31-alt1
- 0.31

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 0.29-alt1
- 0.29

* Mon Aug 27 2007 Victor Forsyuk <force@altlinux.org> 0.25-alt1
- 0.25

* Wed Jul 25 2007 Victor Forsyuk <force@altlinux.org> 0.24-alt1
- 0.24

* Tue Jul 03 2007 Victor Forsyuk <force@altlinux.org> 0.23-alt1
- Initial build.
