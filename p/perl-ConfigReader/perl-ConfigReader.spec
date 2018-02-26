Name: perl-ConfigReader
Version: 0.5
Release: alt1.1
Summary: Read directives from a configuration file
License: LGPLv2+
Group: Development/Perl
Url: http://search.cpan.org/dist/ConfigReader/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://www.cpan.org/modules/by-module/ConfigReader/ConfigReader-%version.tar.gz
BuildArch: noarch
BuildRequires: perl-podlators

%description
The ConfigReader library is a set of classes which reads directives from a
configuration file. The library is completely object oriented, and it is
envisioned that parsers for new styles of configuration files can be
easily added.

%prep
%setup -q -n ConfigReader-%version

%build
pod2man ConfigReader.pod ConfigReader.3

%install
install -m 644 -D DirectiveStyle.pm %buildroot%perl_vendor_privlib/ConfigReader/DirectiveStyle.pm
install -m 644 -D Spec.pm %buildroot%perl_vendor_privlib/ConfigReader/Spec.pm
install -m 644 -D Values.pm %buildroot%perl_vendor_privlib/ConfigReader/Values.pm
install -m 644 -D ConfigReader.3 %buildroot%_man3dir/ConfigReader.3

find %buildroot -type f -name .packlist -exec rm -f {} \;
find %buildroot -depth -type d -exec rmdir {} 2>/dev/null \;

%files
%doc COPYING.LIB README
%perl_vendor_privlib/ConfigReader
%_man3dir/ConfigReader.3*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Dec 01 2008 Boris Savelev <boris@altlinux.org> 0.5-alt1
- initial build

