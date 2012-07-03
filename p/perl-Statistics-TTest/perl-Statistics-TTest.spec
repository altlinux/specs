%define module Statistics-TTest

Name: perl-%module
Version: 1.1.0
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Perl module to perform T-test on 2 independent samples
License: unknown
Group: Development/Perl

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/Y/YU/YUNFANG/%module-%version.tar.gz
Patch1: Statistics-TTest-1.1.0-unneededshebang.patch

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 22 2010
BuildRequires: perl-Statistics-Descriptive perl-Statistics-Distributions perl-devel

%description
This is the Statistical T-Test module to compare 2 independent samples. It
takes 2 array of point measures, compute the confidence intervals using the
PointEstimation module (which is also included in this package) and use the
T-statistic to test the null hypothesis. If the null hypothesis is rejected,
the difference will be given as the lower_clm and upper_clm of the TTest
object.

%prep
%setup -n %module-%version
%patch1 -p1

%build

%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Statistics

%changelog
* Mon Nov 22 2010 Victor Forsiuk <force@altlinux.org> 1.1.0-alt1
- Initial build.
