## SPEC file for Perl module Hash::Merge::Simple

%define real_name Hash-Merge-Simple

Name: perl-Hash-Merge-Simple
Version: 0.051
Release: alt1

Summary: Recursively merge two or more hashes

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Hash-Merge-Simple/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-Algorithm-Diff perl-Class-Data-Inheritable perl-Devel-StackTrace perl-Exception-Class perl-Sub-Uplevel perl-Text-Diff perl-Tree-DAG_Node perl-devel
BuildRequires: perl-Clone perl-Test-Deep perl-Test-Differences perl-Test-Exception perl-Test-Most perl-Test-Warn

%description
Perl module Hash::Merge::Simple will recursively merge two or more
hashes and return the result as a new hash reference. The merge
function will descend and merge hashes that exist under the same
node in both the left and right hash, but doesn't attempt to
combine arrays, objects, scalars, or anything else. The rightmost
hash also takes precedence, replacing whatever was in the left
hash if a conflict occurs.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Hash/Merge/Simple*

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.051-alt1
- Initial build for ALT Linux Sisyphus
