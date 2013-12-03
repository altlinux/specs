%define module_version 0.92
%define module_name App-Nopaste
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Cwd.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(FileHandle.pm) perl(HTTP/Request/Common.pm) perl(LWP/Protocol.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Module/Manifest/Skip.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Socket.pm) perl(URI/Escape.pm) perl(YAML/Tiny.pm) perl(base.pm) perl-devel
# END SourceDeps(oneline)
Name:           perl-App-Nopaste
Version:        0.92
Release:        alt1
Summary:        Easy access to any pastebin
License:        perl
Group:          Development/Perl
URL:            https://github.com/sartak/app-nopaste/tree
Source0:        http://cpan.org.ua/authors/id/S/SA/SARTAK/%module_name-%module_version.tar.gz
BuildArch:      noarch
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Browser/Open.pm)
BuildRequires:  perl(Class/Load.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Getopt/Long/Descriptive.pm)
BuildRequires:  perl(JSON.pm)
BuildRequires:  perl(Module/Pluggable.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(WWW/Mechanize.pm)
# necessary for optional modules
BuildRequires:  perl(Clipboard.pm)
BuildRequires:  perl(Config/GitLike.pm)
BuildRequires:  perl(WWW/Pastebin/PastebinCom/Create.pm)
# autoreq doesn't catch this
Requires:       perl(Browser/Open.pm)
# necessary for optional modules
Requires:       perl(Clipboard.pm)
Requires:       perl(Config/GitLike.pm)
Requires:       perl(WWW/Pastebin/PastebinCom/Create.pm)
# for ssh plugin
Requires:       /usr/bin/scp
Source44: import.info

%description
Pastebins (also known as nopaste sites) let you post text, usually code,
for public viewing. They're used a lot in IRC channels to show code that
would normally be too long to give directly in the channel (hence the
name nopaste).

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %module_name

%package -n nopaste
# needs to beat old nopaste-2835-3
Epoch:          1
License:        GPL+ or Artistic
Group:          Development/Perl
Summary:        Access pastebins from the command line
Requires:       %{name} = 0:%{version}-%{release}

%description -n nopaste
This application lets you post text to pastebins from the command line.

Pastebins (also known as nopaste sites) let you post text, usually code, for
public viewing. They're used a lot in IRC channels to show code that would
normally be too long to give directly in the channel (hence the name nopaste).


%prep
%setup -n %module_name-%module_version
find lib -type f | xargs chmod -x

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendor_privlib}/*

%files scripts
%_bindir/*

%files -n nopaste
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1
- uploaded to Sisyphus as Scalar-Does dependency

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.90-alt1_4
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.90-alt1_2
- update to new release by fcimport

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.90-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1_1
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1_1
- fc import

