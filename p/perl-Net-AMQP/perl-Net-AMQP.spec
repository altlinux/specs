%define _unpackaged_files_terminate_build 1
%define sname Net-AMQP

Name: perl-Net-AMQP
Version: 0.06
Release: alt1
Summary: Advanced Message Queue Protocol (de)serialization and representation
Group: Development/Perl
License: perl
Url: https://metacpan.org/release/Net-AMQP
Source: %sname-%version.tar
BuildArch: noarch

BuildRequires: perl(Benchmark.pm) perl(Class/Accessor/Fast.pm) perl(Class/Data/Inheritable.pm) perl(Exporter.pm) perl(FindBin.pm) perl(Module/Build.pm) perl(Scalar/Util.pm) perl(Test/Deep.pm) perl(Test/More.pm) perl(XML/LibXML.pm) perl(overload.pm)

%description
This module implements the frame (de)serialization and representation of
the Advanced Message Queue Protocol (http://www.amqp.org/). It is to be
used in conjunction with client or server software that does the actual
TCP/IP communication.

%prep
%setup -q -n %sname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE CHANGES
%perl_vendor_privlib/N*

%changelog
* Wed Jul 31 2019 Alexandr Antonov <aas@altlinux.org> 0.06-alt1
- initial build for ALT
