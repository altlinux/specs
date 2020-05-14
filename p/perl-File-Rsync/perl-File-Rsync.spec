%define	upstream_name	 File-Rsync
%define	upstream_version 0.49

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt2

Summary:    Perl module interface to rsync
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Path.pm)
BuildRequires: perl(IPC/Run3.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl-devel
BuildRequires: rsync
BuildArch:  noarch

%description
Perl Convenience wrapper for the rsync(1) program. Written for rsync-2.3.2 and
updated for rsync-2.6.0 but should perform properly with most recent versions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%perl_vendor_build

%check
make test

%install
%makeinstall_std

%files 
%doc Changelog META.json META.yml README TODO
%perl_vendorlib/File/*

%changelog
* Thu May 14 2020 Andrey Cherepanov <cas@altlinux.org> 0.49-alt2
- Initial build to Sisyphus.

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1_4
- update by mgaimport

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1_3
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1_2
- update by mgaimport

* Sat May 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1_1
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1_2
- update by mgaimport

* Tue Oct 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1_1
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.43-alt3_12
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.43-alt3_11
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.43-alt3_10
- rebuild to get rid of unmets

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.43-alt2_10
- update by mgaimport

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.43-alt2_9
- mga update

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.43-alt2_8
- rebuild with new perl

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_8
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_6
- converted for ALT Linux by srpmconvert tools

