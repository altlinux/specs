Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(AnyEvent.pm) perl(AnyEvent/Handle.pm) perl(AnyEvent/Socket.pm) perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(Encode.pm) perl(Exporter.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(JSON.pm) perl(JSON/XS.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(YAML/Tiny.pm) perl(base.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-AnyEvent-I3
Version:        0.16
Release:        alt1_4
Summary:        Communicate with the i3 window manager
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/anyevent-i3/
Source0:        http://search.cpan.org/CPAN/authors/id/M/MS/MSTPLBG/AnyEvent-I3-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Module/Install.pm)


Source44: import.info

%description
This module connects to the i3 window manager using the UNIX socket based
IPC interface it provides (if enabled in the configuration file). You can
then subscribe to events or send messages and receive their replies.

%prep
%setup -qn AnyEvent-I3-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir NO_PACKLIST=1 INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%files
%doc Changes README
%{perl_vendor_privlib}/AnyEvent/I3.pm

%changelog
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

