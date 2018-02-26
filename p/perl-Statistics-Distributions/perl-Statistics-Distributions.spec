%define module_name Statistics-Distributions

Name: perl-%module_name
Version: 1.02
Release: alt1.1

Summary: Critical values and upper probabilities of common statistical distributions
License: Perl
Group: Development/Perl

Url: %CPAN %module_name
Source: http://www.cpan.org/modules/by-module/Statistics/%module_name-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Jul 11 2007
BuildRequires: perl-devel

%description
Statistics::Distributions calculates percentage points (5 significant
digits) of the u (standard normal) distribution, the Student's t
distribution, the chi-square distribution and the F distribution. It
can also calculate the upper probability (5 significant digits) of the
u (standard normal), the chi-square, the t and the F distribution.

These critical values are needed to perform statistical tests, like
the u test, the t test, the F test and the chi-squared test, and to
calculate confidence intervals.

%prep
%setup -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Statistics

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Jul 11 2007 Victor Forsyuk <force@altlinux.org> 1.02-alt1
- Initial build.
