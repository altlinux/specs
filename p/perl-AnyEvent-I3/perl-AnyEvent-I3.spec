# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(AnyEvent.pm) perl(AnyEvent/Handle.pm) perl(AnyEvent/Socket.pm) perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(Encode.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(JSON.pm) perl(JSON/XS.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Test/More.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define srcname AnyEvent-I3

Name:           perl-AnyEvent-I3
Version:        0.15
Release:        alt2_4
Summary:        Communicate with the i3 window manager

Group:          Development/Perl
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/anyevent-i3/
Source0:        http://search.cpan.org/CPAN/authors/id/M/MS/MSTPLBG/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Module/Install.pm)


Source44: import.info


%description
This module connects to the i3 window manager using the UNIX socket based
IPC interface it provides (if enabled in the configuration file). You can
then subscribe to events or send messages and receive their replies.


%prep
%setup -q -n %{srcname}-%{version}


%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
# %{_fixperms} %{buildroot}/*


%files
%doc README Changes
%{perl_vendor_privlib}/AnyEvent/I3.pm


%changelog
* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_4
- new version

* Tue Jun 17 2014 Andrey Bergman <vkni@altlinux.org> 0.12-alt1
- Initial release for Sisyphus

