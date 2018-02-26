%define pear_name I18N_UnicodeNormalizer

Name: pear-I18N_UnicodeNormalizer
Version: 1.0.0
Release: alt3

Summary: Unicode Normalizer

License: The BSD License
Group: Development/Other
Url: http://pear.php.net/package/I18N_UnicodeNormalizer

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/I18N_UnicodeNormalizer-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
"...Unicode's normalization is the concept of character composition and
decomposition.
Character composition is the process of combining simpler characters into
fewer precomposed characters, such as the n character and the combining ~
character into the single n+~ character. Decomposition is the opposite
process, breaking precomposed characters back into their component
pieces...
...Normalization is important when comparing text strings for searching
and sorting (collation)..." [Wikipedia]
Performs the 4 normalizations:
NFD: Canonical Decomposition NFC:  Canonical Decomposition, followed by
Canonical Composition NFKD: Compatibility Decomposition NFKC: Compatibility
Decomposition, followed by Canonical Composition Complies with the official
Unicode.org regression test.
Uses UTF8 binary strings natively but can normalize a string in any UTF
format.
Fully tested with phpUnit. Code coverage test close to 100%%.

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/I18N/
%pear_datadir/%pear_name/
%pear_testdir/%pear_name/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

