Name: perl6-File-Find
Version: 0.1
Release: alt1.cfc6865
Summary: File::Find Perl 6 module

Group: Development/Other
License: Artistic 2
URL: https://github.com/tadzik/File-Find

Source: %name-%version.tar

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: rakudo

BuildArch: noarch

AutoReq: noperl
AutoProv: noperl

%description
File::Find - Get a lazy list of a directory tree

%prep
%setup

%build

%check
perl6 -Ilib t/*.t

%install
mkdir -p %buildroot%_datadir/perl6/vendor/lib
cp -r lib/* %buildroot%_datadir/perl6/vendor/lib

%files
%_datadir/perl6/vendor/lib/File/Find.pm
%doc LICENSE README.md

%changelog
* Wed Oct 28 2015 Vladimir Lettiev <crux@altlinux.ru> 0.1-alt1.cfc6865
- commit cfc6865
- initial build


