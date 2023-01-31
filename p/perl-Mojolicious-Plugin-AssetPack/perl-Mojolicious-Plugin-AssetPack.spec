%define _unpackaged_files_terminate_build 1

Name: perl-Mojolicious-Plugin-AssetPack
Version: 2.14
Release: alt1
Summary: Compress and convert CSS, Less, Sass, JavaScript and CoffeeScript files
License: Artistic 2.0
Group: Development/Perl
Url: http://search.cpan.org/dist/Mojolicious-Plugin-AssetPack/
Source0: http://www.cpan.org/authors/id/S/SR/SRI/Mojolicious-Plugin-AssetPack-%{version}.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: node-devel
BuildRequires: perl-devel
BuildRequires: perl-Package-Generator
BuildRequires: perl(constant.pm)
BuildRequires: perl(CSS/Minifier/XS.pm)
BuildRequires: perl(Cwd.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Fcntl.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(File/Find.pm)
BuildRequires: perl(File/Path.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(File/Spec/Functions.pm)
BuildRequires: perl(File/Which.pm)
BuildRequires: perl(Imager/File/PNG.pm)
BuildRequires: perl(IO/File.pm)
BuildRequires: perl(IPC/Run3.pm)
BuildRequires: perl(JavaScript/Minifier/XS.pm)
BuildRequires: perl(Mojo/Base.pm)
BuildRequires: perl(Mojo/ByteStream.pm)
BuildRequires: perl(Mojo/EventEmitter.pm)
BuildRequires: perl(Mojo/JSON.pm)
BuildRequires: perl(Mojolicious.pm)
BuildRequires: perl(Mojolicious/Lite.pm)
BuildRequires: perl(Mojolicious/Types.pm)
BuildRequires: perl(Mojolicious/Plugin.pm)
BuildRequires: perl(Mojo/UserAgent.pm)
BuildRequires: perl(Mojo/Util.pm)
BuildRequires: perl(POSIX.pm)
BuildRequires: perl(Test/Mojo.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Pod.pm)
BuildRequires: perl(Test/Pod/Coverage.pm)
BuildRequires: perl(overload.pm)
BuildRequires: perl(warnings.pm)

Requires: perl(Imager/File/PNG.pm)
Requires: perl(Mojo/UserAgent.pm)

%description
Mojolicious::Plugin::AssetPack is a Mojolicious plugin which can be used to
cram multiple assets of the same type into one file. This means that if you
have a lot of CSS files (.css, .less, .sass, ...) as input, the AssetPack
can make one big CSS file as output. This is good, since it will often
speed up the rendering of your page. The output file can even be minified,
meaning you can save bandwidth and browser parsing time.

%prep
%setup -q -n Mojolicious-Plugin-AssetPack-%{version}
for PL in sprites.pl rollup.pl; do
    sed -i -e '1s,#!.*perl,#!perl,' examples/"$PL"
done
sed -i -e '1s,#!.*node,,' lib/Mojolicious/Plugin/AssetPack/Pipe/*.js

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -f %buildroot%perl_vendorlib/Mojolicious/Plugin/README.pod

%files
%doc Changes examples README.md
%perl_vendorlib/Mojolicious/Plugin/AssetPack*

%changelog
* Tue Jan 31 2023 Igor Vlasenko <viy@altlinux.org> 2.14-alt1
- automated CPAN update

* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 2.13-alt2
- drop BR python2 module

* Mon Mar 15 2021 Igor Vlasenko <viy@altlinux.org> 2.13-alt1
- automated CPAN update

* Sun Feb 21 2021 Igor Vlasenko <viy@altlinux.org> 2.11-alt1
- automated CPAN update

* Mon Dec 14 2020 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1
- automated CPAN update

* Wed Sep 09 2020 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1
- automated CPAN update

* Tue Oct 01 2019 Alexandr Antonov <aas@altlinux.org> 2.08-alt2
- Drop alt-corrected-ruby-sass-name.patch

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.08-alt1
- automated CPAN update

* Mon Nov 19 2018 Alexandr Antonov <aas@altlinux.org> 2.06-alt2
- Corrected the name of the called application

* Thu Sep 20 2018 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1
- automated CPAN update

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 2.05-alt1
- automated CPAN update

* Wed Jul 25 2018 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1
- automated CPAN update
- removed Patch0: fixassetpack.patch - deprecated

* Mon Jul 02 2018 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1
- automated CPAN update

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 2.02-alt1
- initial build for ALT
