Name: perl-Boulder
Version: 1.30
Release: alt2

Summary: An API for hierarchical tag/value structures
License: Perl
Group: Development/Perl

Url: %CPAN Boulder
Source: http://www.cpan.org/modules/by-module/Boulder/Boulder-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jan 30 2011 (-bi)
BuildRequires: perl-CGI perl-DBM perl-XML-Parser perl-devel

%description
Boulder provides a simple stream-oriented format for transmitting data objects
between one or more processes. It does not provide for the serialization of
Perl objects the way FreezeThaw or Data::Dumper do, but it does provide the
advantage of being language independent.

%prep
%setup -n Boulder-%version

%build
#Uses a non-existent module
rm Boulder/Labbase.pm

%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Boulder*
%perl_vendor_privlib/Stone*

%changelog
* Sun Jan 30 2011 Victor Forsiuk <force@altlinux.org> 1.30-alt2
- Fix FTBFS (refresh BuildRequires).

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Dec 01 2008 Boris Savelev <boris@altlinux.org> 1.30-alt1
- initial build

