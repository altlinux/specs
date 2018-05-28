%define pgver 10

Name: postgresql-acl
Version: 1.0.2
Release: alt2

Summary: PostgreSQL %pgver Access Control Lists Extension
License: BSD (2-clause)
Group: Databases

# git: https://github.com/arkhipov/acl
Url: http://www.softus.org
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: postgresql%pgver-devel

%description
You need this extension if you want to restrict access to rows in
tables based on an authenticated user.  Access Control List (ACL)
has become the de-facto standard for implementing a security
model in modern applications.  Complex scenarios can be handled
by using ACLs without having a complex permission model at the
application level.

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%doc CHANGELOG README.md
%_libdir/pgsql
%_datadir/pgsql/extension/

%changelog
* Mon May 28 2018 Michael Shigorin <mike@altlinux.org> 1.0.2-alt2
- built for pg10

* Mon May 28 2018 Michael Shigorin <mike@altlinux.org> 1.0.2-alt1
- initial release
