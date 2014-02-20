%define module_version 1.4
%define module_name Geometry-AffineTransform
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Hash/Util.pm) perl(List/Util.pm) perl(Math/Trig.pm) perl(Test/Class.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.4
Release: alt2
Summary: Affine Transformation to map 2D coordinates to other 2D coordinates
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/L/LI/LIYANAGE/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/G*

%changelog
* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Wed Nov 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1
- regenerated from template by package builder

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1
- initial import by package builder

