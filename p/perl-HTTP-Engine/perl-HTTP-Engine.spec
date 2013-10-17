%add_findreq_skiplist %perl_vendor_privlib/HTTP/Engine/Interface/ModPerl.pm
# BEGIN SourceDeps(oneline):
BuildRequires: perl(APR/Table.pm) perl(Any/Moose.pm) perl(Apache/Test.pm) perl(Apache/TestMM.pm) perl(Apache2/Connection.pm) perl(Apache2/Const.pm) perl(Apache2/RequestIO.pm) perl(Apache2/RequestRec.pm) perl(Apache2/RequestUtil.pm) perl(Apache2/ServerRec.pm) perl(CGI/Simple.pm) perl(CGI/Simple/Cookie.pm) perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Cwd.pm) perl(Data/Dumper.pm) perl(Encode.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(FCGI.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Copy.pm) perl(File/Find.pm) perl(File/Path.pm) perl(File/Spec.pm) perl(File/Spec/Unix.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(Filter/Util/Call.pm) perl(FindBin.pm) perl(HTTP/Body.pm) perl(HTTP/Headers.pm) perl(HTTP/Headers/Fast.pm) perl(HTTP/Request.pm) perl(HTTP/Request/AsCGI.pm) perl(HTTP/Request/Common.pm) perl(HTTP/Response.pm) perl(HTTP/Server/Simple.pm) perl(HTTP/Server/Simple/CGI.pm) perl(HTTP/Status.pm) perl(IO/File.pm) perl(IO/Handle.pm) perl(IO/Scalar.pm) perl(IO/Select.pm) perl(IO/Socket.pm) perl(IO/Socket/INET.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(LWP/UserAgent.pm) perl(MIME/Base64.pm) perl(Module/Build.pm) perl(Moose.pm) perl(Mouse.pm) perl(MouseX/Types.pm) perl(Net/FTP.pm) perl(Net/HTTP.pm) perl(POE.pm) perl(POSIX.pm) perl(Parse/CPAN/Meta.pm) perl(PerlIO.pm) perl(Plack/Loader.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Storable.pm) perl(String/TT.pm) perl(Test/Deep.pm) perl(Text/Diff.pm) perl(Tie/Array.pm) perl(Tie/Scalar.pm) perl(Time/HiRes.pm) perl(URI.pm) perl(URI/QueryParam.pm) perl(URI/WithBase.pm) perl(YAML.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm) perl(mod_perl2.pm) perl(overload.pm) perl(threads/shared.pm)
# END SourceDeps(oneline)
%define module_version 0.03005
%define module_name HTTP-Engine
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.03005
Release: alt1
Summary: Web Server Gateway Interface and HTTP Server Engine Drivers
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/Y/YA/YAPPO/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
HTTP::Engine abstracts handling the input and output of various web
server environments, including CGI, mod_perl and FastCGI. Most of the
code is ported over from Catalyst::Engine.

If you're familiar with WSGI for Python or Rack for Ruby, HTTP::Engine
exactly does the same thing, for Perl.


%prep
%setup -n %module_name-%module_version
# depends on order
rm t/010_core/request-uri.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc TODO README Changes examples
%perl_vendor_privlib/H*

%changelog
* Thu Oct 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.03005-alt1
- initial import by package builder

