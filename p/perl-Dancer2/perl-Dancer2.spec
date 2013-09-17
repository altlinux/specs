Name: perl-Dancer2
Version: 0.09
Release: alt1

Summary: Lightweight yet powerful web application framework
Group: Development/Perl
License: perl

Url: %CPAN Dancer2
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl(Capture/Tiny.pm) perl(YAML.pm) perl(Pod/Usage.pm) perl(Template/Tiny.pm) perl(Encode.pm) perl(HTTP/Headers.pm) perl(Config/Any.pm) perl(Plack/Request.pm) perl(Module/Build.pm) perl-devel perl(HTTP/Body.pm) perl(MooX/Types/MooseLike.pm) perl(URI/Escape.pm) perl(Role/Tiny.pm) perl(Test/MockTime.pm) perl(Test/Fatal.pm) perl(URI.pm) perl-libwww perl(Pod/Simple.pm) perl(Test/TCP.pm) perl(Digest/SHA.pm) perl(parent.pm) perl(HTTP/Request/Common.pm) perl(Hash/Merge/Simple.pm) perl(Moo/Role.pm) perl(Test/Script.pm) perl(YAML/Any.pm) perl(HTTP/Server/Simple/PSGI.pm) perl(Class/Load.pm) perl(Moo.pm) perl(Template.pm) perl(MIME/Types.pm) perl(HTTP/Date.pm) perl(JSON.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/dancer2
%_man1dir/dancer2.*
%perl_vendor_privlib/Dancer2*
%doc AUTHORS Changes LICENSE README.md

%changelog
* Tue Sep 17 2013 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- initial build for ALTLinux

