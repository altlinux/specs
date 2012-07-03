%define dist Devel-DProf
Name: perl-%dist
Version: 20110802.00
Release: alt1

Summary: A DEPRECATED Perl code profiler
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Deprecated in perl-5.14.
Requires: perl-base >= 1:5.14

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: perl-devel

%description
Devel::DProf is DEPRECATED and will be removed from a future version
of Perl.  We strongly recommend that you install and use Devel::NYTProf
instead, as it offers significantly improved profiling and reporting.

The Devel::DProf package is a Perl code profiler.  This will collect
information on the execution time of a Perl script and of the subs in
that script.  This information can be used to determine which subroutines
are using the most time and which subroutines are being called most often.
This information can also be used to create an execution graph of the script,
showing subroutine relationships.

%prep
%setup -q -n %dist-%version

%build
export XSUBPP_NO_STATIC_XS=1
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/dprofpp
%perl_vendor_archlib/Devel
%perl_vendor_autolib/Devel

%changelog
* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 20110802.00-alt1
- initial revision
