%define _unpackaged_files_terminate_build 1
%define module_name Unicode-UTF8
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(App/pod2pdf.pm) perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Cwd.pm) perl(Encode.pm) perl(Encode/CN.pm) perl(Encode/JP.pm) perl(Encode/KR.pm) perl(Encode/TW.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(IO/File.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Pod/Html.pm) perl(Pod/Man.pm) perl(Pod/Text.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Test/Builder.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.62
Release: alt1.1
Summary: Encoding and decoding of UTF-8 encoding form
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/C/CH/CHANSEN/%{module_name}-%{version}.tar.gz

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/U*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1.1
- rebuild with new perl 5.26.1

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.60-alt3.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.60-alt3.1
- rebuild with new perl 5.22.0

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.60-alt3
- dep for File-Slurper

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.60-alt2
- rebuild to get rid of unmets

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1
- initial import by package builder

