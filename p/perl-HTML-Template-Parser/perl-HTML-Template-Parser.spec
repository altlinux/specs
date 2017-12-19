# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Class/Accessor/Fast.pm) perl(Config.pm) perl(Cwd.pm) perl(Data/Dumper.pm) perl(English.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(FindBin/libs.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Parse/RecDescent.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Test/More.pm) perl(UNIVERSAL/require.pm) perl(YAML.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm)
# END SourceDeps(oneline)
%define module_version 0.1011
%define module_name HTML-Template-Parser
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.1011
Release: alt2
Summary: Parser for HTML::Template syntax template file & writer.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/S/SH/SHMORIMO/HTML-Template-Parser-%{version}.tar.gz
BuildArch: noarch

%description
HTML::Template::Parser is parser module for tempalte file that is written in HTML::Template.
It parse template file to tree object.
It can write tree as TextXslate::Metakolon format.

%prep
%setup -n %module_name-%module_version

# tmp hack for 0.1011
rm t/900_bug/003_name_and_expr.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog
%perl_vendor_privlib/H*

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.1011-alt2
- fixed build with new perl 5.26

* Sat Oct 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.1011-alt1
- automated CPAN update

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.1010-alt1
- initial import by package builder

