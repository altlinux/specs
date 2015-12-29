Name: rpm-build-perl6
Version: 0.1
Release: alt1

Summary: RPM macroses for Rakudo Perl 6
License: GPL
Group: Development/Other

URL: https://github.com/vlet/rpm-build-perl6
Source: %name-%version.tar

BuildRequires: rakudo

BuildArch: noarch
AutoReq: noperl

%description
Install script and rpm macroses for Rakudo Perl 6

%prep
%setup

%build

%install
mkdir -p %buildroot{%_rpmmacrosdir,%_rpmlibdir}
install -pm644 perl6-macros %buildroot%_rpmmacrosdir/perl6
install -pm755 perl6-installer %buildroot%_rpmlibdir

%check
perl6 -c %buildroot%_rpmlibdir/perl6-installer

%files
%doc README.md
%_rpmlibdir/perl6-installer
%config %_rpmmacrosdir/perl6

%changelog
* Tue Dec 29 2015 Vladimir Lettiev <crux@altlinux.ru> 0.1-alt1
- initial release


