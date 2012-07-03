%define module_name Carp-Datum

Name: perl-%module_name
Version: 0.1.3
Release: alt1.1

Summary: %module_name module for perl
License: Artistic
Group: Development/Perl

Url: %CPAN %module_name
Source: http://www.cpan.org/modules/by-module/Carp/%module_name-%version.tar.gz

BuildArch: noarch
# Automatically added by buildreq on Tue Jul 03 2007
BuildRequires: perl-devel perl-Getargs-Long

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
The Carp::Datum module brings powerful debugging and tracing features to
development code: automatic flow tracing, returned value tracing,
assertions, and debugging traces.

%prep
%setup -n %module_name-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/*
%perl_vendor_privlib/Carp/
%exclude /.perl.req

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 03 2007 Victor Forsyuk <force@altlinux.org> 0.1.3-alt1
- Initial build.
