%define _unpackaged_files_terminate_build 1

Name: perl-Mojo-IOLoop-ReadWriteProcess
Version: 0.20
Release: alt1
Summary: Execute external programs or internal code blocks as separate process
License: Artistic-1.0 or GPL-1.0+
Group: Development/Perl
Url: http://search.cpan.org/dist/Mojo-IOLoop-ReadWriteProcess/
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: perl-devel
BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Mojolicious.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(warnings.pm)
BuildRequires: perl(Mojo/Base.pm)
BuildRequires: perl(Mojo/File.pm)

Requires: perl(Mojolicious.pm)

%description
Mojo::IOLoop::ReadWriteProcess is yet another process manager.

%prep
%setup
%ifnarch %ix86 x86_64
# following test may fail on some architectures
rm -f t/12_mocked_container.t
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendorlib/Mojo/IOLoop*
%doc Changes LICENSE README.md

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.20-alt1
- initial build for ALT
