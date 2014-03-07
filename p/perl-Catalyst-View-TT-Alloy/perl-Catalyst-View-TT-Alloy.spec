# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Carp.pm) perl(Catalyst.pm) perl(Catalyst/Controller.pm) perl(Catalyst/View.pm) perl(Config.pm) perl(Cwd.pm) perl(Data/Dump.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(FileHandle.pm) perl(FindBin.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Path/Class.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Template/Alloy.pm) perl(Test/More.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm)
# END SourceDeps(oneline)
%define module_version 0.00003
%define module_name Catalyst-View-TT-Alloy
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.00003
Release: alt2
Summary: Template::Alloy (TT) View Class
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/P/PE/PERLER/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
This is the Catalyst view for the TT emulator 
the Template::Alloy manpage.

Your application should define a view class which is a subclass of
this module.  The easiest way to achieve this is using 
`script/myapp_create.pl' (replacing `myapp' with the name of your 
application).

    $ script/myapp_create.pl view TT::Alloy TT::Alloy

You can either manually forward to the `TT::Alloy' as normal, or use 
the Catalyst::Action::RenderView manpage to do it for you.

    # In MyApp::Controller::Root
    
    sub end : ActionClass('RenderView') { }


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/C*

%changelog
* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.00003-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.00003-alt1
- initial import by package builder

