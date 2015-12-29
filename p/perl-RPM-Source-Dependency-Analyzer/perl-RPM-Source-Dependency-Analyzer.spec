#define module Source-Text-Dependency-Analyser
%define module RPM-Source-Dependency-Analyzer
%def_without hashertarbuild

Name: perl-%module
Version: 0.001
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Perl library for finding build dependencies from software sources
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

BuildRequires: perl-devel /usr/bin/pod2man perl-podlators perl-RPM-Source-Editor
BuildRequires: perl-DistroMap 
#perl(Pod/Strip.pm)

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

# TODO! distrodb!
install -Dm644 stdheaders.txt %buildroot%_datadir/%module/headers-ignore/stdheaders.txt

%files
%doc Changes
%perl_vendor_privlib/R*
%_datadir/%module
#%_bindir/buildreq-*
#%_man1dir/buildreq-*

%changelog
* Tue Dec 29 2015 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version

