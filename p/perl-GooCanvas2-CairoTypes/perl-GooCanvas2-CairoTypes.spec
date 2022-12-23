# BEGIN SourceDeps(oneline):
BuildRequires: perl(Cairo.pm) perl(Cairo/Install/Files.pm) perl(ExtUtils/Depends.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/PkgConfig.pm) perl(File/Spec.pm) perl(Glib.pm) perl(Glib/Install/Files.pm) perl(Gtk3.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(strict.pm) perl(warnings.pm) pkgconfig(goocanvas-2.0)
# END SourceDeps(oneline)
%define module_name GooCanvas2-CairoTypes
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.001
Release: alt3
Summary: Bridge between GooCanvas2 and Cairo types
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/A/AS/ASOKOLOV/%{module_name}-%{version}.tar.gz

%description
There is an issue in the interaction between GooCanvas, GObject Introspection, Cairo, and their Perl bindings, which causes some functionality to be unusable from Perl side. This is better described here, and there was an attempt to fix it upstream. Until it's fixed, this can serve as a workaround for it.

Currently this module only "fixes" `Cairo::Pattern/GooCanvas2::CairoPattern' interop. For certain calls it just works if this module was included; for some other calls you need to explicitly convert the type.

If you have any idea how to fix those cases to not require such call, or need to bridge more types, pull requests are welcome!

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes
%perl_vendor_archlib/G*
%perl_vendor_autolib/*

%changelog
* Fri Dec 23 2022 Igor Vlasenko <viy@altlinux.org> 0.001-alt3
- to Sisyphus

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 0.001-alt2
- rebuild with perl 5.34.0

* Mon Feb 22 2021 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial import by package builder

