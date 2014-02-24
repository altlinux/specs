%define module_version 0.03
%define module_name URL-Encode
# BEGIN SourceDeps(oneline):
BuildRequires: perl(App/pod2pdf.pm) perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Cwd.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Pod/Html.pm) perl(Pod/Man.pm) perl(Pod/Text.pm) perl(Socket.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.03
Release: alt1
Summary: Encoding and decoding of C<application/x-www-form-urlencoded> encoding.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/C/CH/CHANSEN/URL-Encode-%{version}.tar.gz
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
%perl_vendor_privlib/U*

%changelog
* Mon Feb 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- automated CPAN update

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2
- build for Sisyphus (required for perl update)

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

