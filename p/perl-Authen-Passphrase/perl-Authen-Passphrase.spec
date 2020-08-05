# BEGIN SourceDeps(oneline):
BuildRequires: perl(Authen/DecHpwd.pm) perl(CPAN.pm) perl(Crypt/DES.pm) perl(Crypt/Eksblowfish/Bcrypt.pm) perl(Crypt/Eksblowfish/Uklblowfish.pm) perl(Crypt/MySQL.pm) perl(Crypt/PasswdMD5.pm) perl(Crypt/UnixCrypt_XS.pm) perl(Cwd.pm) perl(Data/Entropy/Algorithms.pm) perl(Digest.pm) perl(Digest/MD4.pm) perl(Digest/MD5.pm) perl(Digest/SHA.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(MIME/Base64.pm) perl(Module/Build.pm) perl(Module/Runtime.pm) perl(Params/Classify.pm) perl(Test/More.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define module_version 0.008
%define module_name Authen-Passphrase
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.008
Release: alt2
Summary: hashed passwords/passphrases as objects
Group: Development/Perl
License: Perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/Z/ZE/ZEFRAM/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/A*

%changelog
* Wed Aug 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.008-alt2
- import for Sisyphus

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- initial import by package builder

