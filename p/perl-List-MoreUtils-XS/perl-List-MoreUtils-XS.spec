Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		perl-List-MoreUtils-XS
Version:	0.426
Release:	alt1_1
Summary:	Provide compiled List::MoreUtils functions
# Code from List-MoreUtils < 0.417 is GPL+ or Artistic
# Anything after that is ASL 2.0
# "git blame" on the upstream repo will probably be needed to
# determine the license of any particular chunk of code
License:	(GPL+ or Artistic) and ASL 2.0
URL:		http://search.cpan.org/dist/List-MoreUtils-XS/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RE/REHSACK/List-MoreUtils-XS-%{version}.tar.gz
Patch0:		List-MoreUtils-XS-0.421-unbundle.patch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	perl-devel
BuildRequires:	rpm-build-perl
BuildRequires:	perl-devel
BuildRequires:	perl(Capture/Tiny.pm)
BuildRequires:	perl(Config/AutoConf.pm)
BuildRequires:	perl(ExtUtils/CBuilder.pm)
# Module Runtime
BuildRequires:	perl(base.pm)
BuildRequires:	perl(Exporter.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(vars.pm)
BuildRequires:	perl(warnings.pm)
BuildRequires:	perl(XSLoader.pm)
# Test Suite
BuildRequires:	perl(JSON/PP.pm)
BuildRequires:	perl(List/Util.pm)
BuildRequires:	perl(Math/Trig.pm)
BuildRequires:	perl(overload.pm)
BuildRequires:	perl(Storable.pm)
BuildRequires:	perl(Test/Builder/Module.pm)
BuildRequires:	perl(Test/LeakTrace.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Tie/Array.pm)
# Runtime

# Don't "provide" private Perl libs

Source44: import.info

%description
This module provides accelerated versions of functions in List::MoreUtils.

%prep
%setup -q -n List-MoreUtils-XS-%{version}

# Unbundle bundled modules except private inc::Config::AutoConf::LMU
%patch0
find inc/ -type f ! -name LMU.pm -print -delete

%build
perl Makefile.PL \
	INSTALLDIRS=vendor \
	OPTIMIZE="%{optflags}"\
	NO_PERLLOCAL=1 \
	NO_PACKLIST=1
%make_build

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -empty -delete
# %{_fixperms} -c %{buildroot}

%check
make test

%files
%doc ARTISTIC-1.0 GPL-1 LICENSE
%doc Changes MAINTAINER.md README.md
%{perl_vendor_archlib}/auto/List/
%{perl_vendor_archlib}/List/

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.426-alt1_1
- new version

