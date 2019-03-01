%define _unpackaged_files_terminate_build 1

Name: phpunit8
Version: 8.0.4
Release: alt2

Summary: PHPUnit is a programmer-oriented testing framework for PHP.
License: BSD License
Group: Development/Other

URL: https://phpunit.de
Source: %name-%version.tar

BuildArch: noarch

Requires: php7
Requires: php7-openssl

%description
PHPUnit is a programmer-oriented testing framework for PHP.
It is an instance of the xUnit architecture for unit testing frameworks.


%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/%name
install -m 0755 phpunit-8.phar %buildroot%_datadir/%name

mkdir -p %buildroot%_bindir
install -m 0755 phpunit8.sh %buildroot%_bindir/%name

%files
%_bindir/%name
%_datadir/%name/phpunit-8.phar


%changelog
* Fri Mar 01 2019 Alexander Makeenkov <amakeenk@altlinux.org> 8.0.4-alt2
- Fix requires

* Thu Feb 28 2019 Alexander Makeenkov <amakeenk@altlinux.org> 8.0.4-alt1
- Initial build for ALT

