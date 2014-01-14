Name: perl-Minilla
Version: 0.11.0
Release: alt1

Summary: CPAN module authoring tool
Group: Development/Perl
License: perl

Url: %CPAN Minilla
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl(Module/Metadata.pm) perl(Test/Requires.pm) perl(CPAN/Meta/Validator.pm) perl(File/Which.pm) perl(Time/Piece.pm) perl(TOML.pm) perl(Data/Section/Simple.pm) perl(CPAN/Meta.pm) perl(Module/Build.pm) perl(Archive/Tar.pm) perl(Pod/Markdown.pm) perl(Test/Output.pm) perl(CPAN/Meta/Prereqs.pm) perl-devel perl(Text/MicroTemplate.pm) perl(Try/Tiny.pm) perl(Term/ANSIColor.pm) perl(parent.pm) perl(File/pushd.pm) perl(Moo.pm) perl-App-cpanminus perl(Module/CPANfile.pm) perl(File/Copy/Recursive.pm)

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
* Tue Jan 14 2014 Vladimir Lettiev <crux@altlinux.ru> 0.11.0-alt1
- initial build for ALTLinux

