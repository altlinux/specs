Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(AnyEvent.pm) perl(AnyEvent/Handle.pm) perl(AnyEvent/Socket.pm) perl(CPAN.pm) perl(Encode.pm) perl(ExtUtils/CBuilder.pm) perl(JSON.pm) perl(JSON/XS.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-AnyEvent-I3
Version:        0.17
Release:        alt1_9
Summary:        Communicate with the i3 window manager
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/anyevent-i3
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTPLBG/AnyEvent-I3-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Module/Install/Metadata.pm)
BuildRequires:  perl(Module/Install/WriteAll.pm)
BuildRequires:  sed
# Run-time
#BuildRequires:  perl(AnyEvent)
#BuildRequires:  perl(AnyEvent::Handle)
#BuildRequires:  perl(AnyEvent::Socket)
#BuildRequires:  perl(base)
#BuildRequires:  perl(constant)
#BuildRequires:  perl(Encode)
#BuildRequires:  perl(Exporter)
#BuildRequires:  perl(JSON::XS)
#BuildRequires:  perl(Scalar::Util)
#BuildRequires:  perl(strict)
#BuildRequires:  perl(warnings)
# Tests
#BuildRequires:  perl(Test::More)


Source44: import.info

%description
This module connects to the i3 window manager using the UNIX socket based
IPC interface it provides (if enabled in the configuration file). You can
then subscribe to events or send messages and receive their replies.

%prep
%setup -qn AnyEvent-I3-%{version}
rm -rf inc
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
# %{_fixperms} %{buildroot}/*

#%%check
#make test

%files
%doc Changes README
%{perl_vendor_privlib}/AnyEvent/I3.pm

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_9
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_5
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_3
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_2
- update to new release by fcimport

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_6
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_3
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_1
- update to new release by fcimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_4
- new version

* Tue Jun 17 2014 Andrey Bergman <vkni@altlinux.org> 0.12-alt1
- Initial release for Sisyphus

