## SPEC file for Perl module Hash::Merge::Simple

%define real_name Hash-Merge-Simple

Name: perl-Hash-Merge-Simple
Version: 0.052
Release: alt1

Summary: Recursively merge two or more hashes

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Hash-Merge-Simple/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Wed Nov 05 2025
# optimized out: libgpg-error perl perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-parent python-modules python2-base python3 python3-base sh5
BuildRequires: perl-CPAN-Meta perl-Clone perl-devel

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
* Wed Nov 12 2025 Nikolay A. Fetisov <naf@altlinux.org> 0.052-alt1
- New version
- Update package URL

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.051-alt1
- Initial build for ALT Linux Sisyphus
