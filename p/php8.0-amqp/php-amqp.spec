%define php_extension amqp

Name: php%_php_suffix-%php_extension
Version: 2.1.1
Release: alt1.%php_version

Summary: PHP extension to communicate with any AMQP compliant server
License: PHP-3.01
Group: System/Servers

Url: https://github.com/php-amqp/php-amqp
Source0:  php-%php_extension-%version.tar
Source1: php-%php_extension.ini
Source2: php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.0-version
BuildRequires: rpm-build-php
BuildRequires: php-devel = %php_version
BuildRequires: librabbitmq-c-devel


%description
This extension can communicate with any AMQP spec 0-9-1 compatible server, 
such as RabbitMQ, OpenAMQP and Qpid, giving you the ability to create and 
delete exchanges and queues, as well as publish to any exchange and consume 
from any queue.

%prep
%setup -n php-%php_extension-%version

%build
phpize
%configure
%php_make

%install
%php_make_install
install -D -m 644 %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%check
NO_INTERACTION=1 php run-tests.php --offline

%files
%php_extdir/*

%doc README.md CREDITS DEVELOPMENT.md UPGRADING.md

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %version-%release

* Tue Nov 15 2023 Alexey Shemyakin <alexeys@altlinux.org> 2.1.1-alt1.%php_version
- Update to version 2.1.1.

* Tue Oct 10 2023 Alexey Shemyakin <alexeys@altlinux.org> 2.1.0-alt1
- Initial build for ALT.
