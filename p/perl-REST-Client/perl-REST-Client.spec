%define _unpackaged_files_terminate_build 1
%define module_name REST-Client
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(FileHandle.pm) perl(HTTP/Server/Simple.pm) perl(JSON.pm) perl(LWP/Protocol/https.pm) perl(LWP/Simple.pm) perl(LWP/UserAgent.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Socket.pm) perl(Test/More.pm) perl(URI.pm) perl(XML/LibXML.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 281
Release: alt1
Summary: A simple client for interacting with RESTful http/https resources
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/A/AK/AKHUETTEL/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
REST::Client provides a simple way to interact with HTTP RESTful resources.


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes
%perl_vendor_privlib/R*

%changelog
* Tue Dec 21 2021 Igor Vlasenko <viy@altlinux.org> 281-alt1
- automated CPAN update

* Wed Dec 15 2021 Igor Vlasenko <viy@altlinux.org> 280-alt1
- automated CPAN update

* Thu Mar 19 2020 Igor Vlasenko <viy@altlinux.ru> 273-alt2
- to Sisyphus as LINSTOR Proxmox Plugin dep

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 273-alt1
- regenerated from template by package builder

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 272-alt1
- regenerated from template by package builder

* Wed Nov 20 2013 Igor Vlasenko <viy@altlinux.ru> 271-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 249-alt1
- initial import by package builder

