Name: perl6-JSON-Fast
Version: 0.2
Release: alt1.e9e648e
Summary: JSON::Fast Perl 6 module 

Group: Development/Other
License: Artistic 2
URL: https://github.com/timo/json_fast

Source: %name-%version.tar

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: rakudo

BuildArch: noarch

AutoReq: noperl
AutoProv: noperl

%description
%summary

%prep
%setup

%build

%check
perl6 -Ilib t/*.t

%install
mkdir -p %buildroot%_datadir/perl6/vendor/lib
cp -r lib/* %buildroot%_datadir/perl6/vendor/lib

%files
%_datadir/perl6/vendor/lib/JSON/Fast.pm
%doc LICENSE README.md

%changelog
* Wed Oct 28 2015 Vladimir Lettiev <crux@altlinux.ru> 0.2-alt1.e9e648e
- commit e9e648e
- initial build


