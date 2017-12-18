BuildRequires: perl(Module/Build.pm)
Name: perl-Minilla
Version: 3.0.14
Release: alt1

Summary: CPAN module authoring tool
Group: Development/Perl
License: perl

Url: %CPAN Minilla
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl(Module/Metadata.pm) perl(Test/Requires.pm) perl(CPAN/Meta/Validator.pm) perl(File/Which.pm) perl(Time/Piece.pm) perl(TOML.pm) perl(Data/Section/Simple.pm) perl(CPAN/Meta.pm) perl(Module/Build/Tiny.pm) perl(Archive/Tar.pm) perl(Pod/Markdown.pm) perl(Test/Output.pm) perl(CPAN/Meta/Prereqs.pm) perl-devel perl(Text/MicroTemplate.pm) perl(Try/Tiny.pm) perl(Term/ANSIColor.pm) perl(parent.pm) perl(File/pushd.pm) perl(Moo.pm) perl-App-cpanminus perl(Module/CPANfile.pm) perl(File/Copy/Recursive.pm) perl(Config/Identity/PAUSE.pm) perl(URI.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/minil
%perl_vendor_privlib/Module/BumpVersion.pm
%perl_vendor_privlib/Minilla*
%doc Changes LICENSE README.md

%changelog
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.14-alt1
- automated CPAN update

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.13-alt1
- automated CPAN update

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.10-alt1
- automated CPAN update

* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt1
- automated CPAN update

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.7-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.5-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1
- automated CPAN update

* Tue Jan 14 2014 Vladimir Lettiev <crux@altlinux.ru> 0.11.0-alt1
- initial build for ALTLinux

