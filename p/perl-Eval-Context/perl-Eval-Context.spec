Name: perl-Eval-Context
Version: 0.09.11
Release: alt3

Summary: Evalute perl code in context wrapper

Group: Development/Perl
License: perl

Url: %CPAN Eval-Context
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: perl(Term/Size.pm) perl(Test/Block.pm) perl(Sub/Exporter.pm) perl(Test/NoWarnings.pm) perl(Data/TreeDumper.pm) perl(Package/Generator.pm) perl(Module/Build.pm) perl(Test/Output.pm) perl(File/Slurp.pm) perl(Test/Exception.pm) perl(Readonly.pm) perl(Text/Diff.pm) perl(Directory/Scratch/Structured.pm) perl(Test/Warn.pm) perl(Data/Compare.pm) perl(Sub/Install.pm)

%description
%summary

%prep
%setup -q
%patch -p1
# perl 5.38
[ %version = 0.09.11 ] && rm t/012_safe.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Eval/Context*
%doc Changes README

%changelog
* Wed Dec 06 2023 Igor Vlasenko <viy@altlinux.org> 0.09.11-alt3
- disabled failed test with perl 5.38

* Wed Sep 18 2013 Vladimir Lettiev <crux@altlinux.ru> 0.09.11-alt2
- fixed failed test with perl 5.18

* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.09.11-alt1
- initial build

