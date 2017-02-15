Name: mysqlsla
Version: 2.03
Release: alt2

Summary: MySQL log parser, filter, analizer

License: %gpl2plus
Group: Databases

Url: http://hackmysql.com

Packager: Boris Savelev <boris@altlinux.org>

Source: http://hackmysql.com/scripts/%name-%version.tar.gz
Patch0: %name-2.03-alt-printf.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Wed Feb 15 2017
# optimized out: perl python-base python-modules python3-base
BuildRequires: perl-Encode perl-devel perl-DBI

%description
mysqlsla parses, filters, analyzes and sorts MySQL slow, general, binary
and microslow patched slow logs in order to create a customizable report
of the queries and their meta-property values.

Since these reports are customizable, they can be used for human consumption
or be fed into other scripts to further analyze the queries.

%prep
%setup
%patch0

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%_bindir/%name
%perl_vendorlib/%name.pm

%changelog
* Wed Feb 15 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.03-alt2
- Fix incompatibility with Perl >= 5.22

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jan 29 2009 Boris Savelev <boris@altlinux.org> 2.03-alt1
- initial build for Sisyphus

