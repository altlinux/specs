# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(MouseX/Getopt.pm) perl(MouseX/Types/Mouse.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Pod/ParseLink.pm) perl(Pod/Parser.pm) perl(Pod/Text.pm) perl(Socket.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm) perl(parent.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    MouseX-Types-Path-Class
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt3_7

Summary:    A Path::Class type library for Mouse
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MouseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Mouse.pm)
BuildRequires: perl(MouseX/Types.pm)
BuildRequires: perl(Path/Class.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/UseAllModules.pm)
BuildArch:  noarch
Source44: import.info

%description
MouseX::Types::Path::Class creates common the Mouse manpage types,
coercions and option specifications useful for dealing with the Path::Class
manpage objects as the Mouse manpage attributes.

Coercions (see the Mouse::Util::TypeConstraints manpage) are made from both
'Str' and 'ArrayRef' to both the Path::Class::Dir manpage and the
Path::Class::File manpage objects. If you have the MouseX::Getopt manpage
installed, the Getopt option type ("=s") will be added for both the
Path::Class::Dir manpage and the Path::Class::File manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml  README
%perl_vendor_privlib/*

%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt3_7
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt3_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt3_4
- update by mgaimport

* Tue Dec 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt3_3
- Sisyphus build

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2_3
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.07-alt2_2
- rebuild to get rid of unmets

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_1
- converted for ALT Linux by srpmconvert tools

