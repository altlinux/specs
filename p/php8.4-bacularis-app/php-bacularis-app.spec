%define php_extension bacularis-app
%define _libexecdir /usr/libexec

Name: php%_php_suffix-%php_extension
Version: 6.2.1
Release: alt1.%_php_release_version

Summary: Main component of the Bacula programming interface

License: AGPL-3.0-only
Group: System/Servers
Url: https://github.com/bacularis/bacularis-app
VCS: https://github.com/bacularis/bacularis-app

Source0: php-%php_extension-%version.tar
# composer install --no-dev
Source1: protected.tar
Source2: htdocs.tar
Patch0: %php_extension-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-php8.4-version

Requires: php%_php_suffix-ldap
Requires: php%_php_suffix-mysqlnd
Requires: php%_php_suffix-pdo
Requires: php%_php_suffix-pgsql
Requires: php%_php_suffix-intl
Requires: php%_php_suffix-bcmath
Requires: php%_php_suffix-curl
Requires: php%_php_suffix-dom
Requires: php%_php_suffix-json

Provides: php%_php_suffix-bacularis-api = %version
Provides: php%_php_suffix-bacularis-common = %version
Provides: php%_php_suffix-bacularis-web = %version

%description
Bacularis is a web interface designed to configure,
manage, and monitor the Bacula backup environment.
It offers a complete solution for setting up backup
jobs, restoring data, managing tape or disk volumes
on both local and remote storage, working with backup
clients, and handling daily backup administration tasks.
Autochanger management is also supported.

Bacularis includes advanced user management with
role-based access control, allowing configuration
for regular users. Each user can log in to the web
interface and perform backup and restore operations
for their own computer data only.

%prep
%setup -n php-%php_extension-%version -a1 -a2
%patch0 -p1

%install
mkdir -p %buildroot%php_moddir/%php_extension
cp -a * %buildroot%php_moddir/%php_extension

mkdir -p %buildroot%_libexecdir/bacularis-app
ln -s %php_moddir/%php_extension/protected/tools %buildroot%_libexecdir/bacularis-app

%files -n php%_php_suffix-%php_extension
%doc LICENSE README.md RELEASE_NOTES.md
%_libexecdir/bacularis-app/
%php_moddir/%php_extension/

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- rebuilt with php-devel = %php_version-%php_release

* Thu Mar 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.2.1-alt1
- 6.1.0 -> 6.2.1

* Thu Mar 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.1.0-alt1
- 6.0.0 -> 6.1.0
- built from upstream git
- added provides to detect vendored bacularis packages

* Thu Mar 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.0-alt1
- initial build for ALT Sisyphus
