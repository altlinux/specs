Name: rpm-build-perl6
Version: 0.3
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
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot%_rpmmacrosdir
install -pm644 perl6-macros %buildroot%_rpmmacrosdir/perl6

%files
%doc README.md
%config %_rpmmacrosdir/perl6

%changelog
* Tue Sep 26 2017 Vladimir Lettiev <crux@altlinux.org> 0.3-alt1
- new release

* Tue Sep 13 2016 Vladimir Lettiev <crux@altlinux.ru> 0.2-alt1
- new release

* Tue Dec 29 2015 Vladimir Lettiev <crux@altlinux.ru> 0.1-alt1
- initial release


