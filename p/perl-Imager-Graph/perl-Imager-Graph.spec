## SPEC file for Perl module Imager::Graph

%define real_name Imager-Graph

Name: perl-Imager-Graph
Version: 0.09
Release: alt2

Summary: producing Graphs using the Imager library

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/~tonyc/Imager-Graph/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Fri Nov 04 2011
# optimized out: perl-Devel-Symdump perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel
BuildRequires: perl-Imager perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module Imager::Graph is intended to produce good looking
graphs with a minimum effort on the part of the user. 

Currently only the pie graph class, Imager::Graph::Pie, 
is provided.

%prep
%setup -q -n %real_name-%version

sed -e 's#200#400#' -i t/t33_long_labels.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README TODO Changes
%exclude /.perl.req
%perl_vendor_privlib/Imager/Graph*

%changelog
* Fri Nov 04 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.09-alt2
- Fix build with Imager > 0.84

* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.09-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Oct 18 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.07-alt1
- New version

* Sat May 24 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.06-alt1
- New version

* Sun Mar 02 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.05-alt1
- Initial build for ALT Linux Sisyphus
