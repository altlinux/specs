Name: postgresql_autodoc
Summary: Create documentation from PostgreSQL database
Version: 1.41
Release: alt1

Url: http://www.rbt.ca/autodoc/

License: BSD
Group: Databases
BuildArch: noarch
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

Requires: perl-DBD-Pg

# Automatically added by buildreq on Sat Jan 07 2012 (-bb)
BuildRequires: perl-DBI perl-HTML-Template perl-Term-ReadKey

%description
%summary

%prep
%setup
sed 's,/usr/local/share/postgresql_autodoc,@@TEMPLATE-DIR@@,' < postgresql_autodoc.1 > postgresql_autodoc.1.in

%build
%make_build PREFIX=/usr

%install
%make_install PREFIX=/usr DESTDIR=%buildroot install

%files
%_bindir/%name
%_man1dir/*
%_datadir/%name/*.tmpl

%changelog
* Sat Jan 07 2012 Denis Smirnov <mithraen@altlinux.ru> 1.41-alt1
- initial build for ALT Linux Sisyphus

