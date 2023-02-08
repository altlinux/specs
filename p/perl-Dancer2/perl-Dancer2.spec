%define _unpackaged_files_terminate_build 1
%global oname Dancer2

Name: perl-Dancer2
Version: 0.400001
Release: alt1

Summary: Lightweight yet powerful web application framework
Group: Development/Perl
License: perl

Url: %CPAN %oname
# https://cpan.metacpan.org/authors/id/C/CR/CROMEDOME/Dancer2-%version.tar.gz
Source: %oname-%version.tar

BuildArch: noarch
BuildRequires: perl(Import/Into.pm) perl(Capture/Tiny.pm) perl(YAML.pm) perl(Pod/Usage.pm) perl(Template/Tiny.pm) perl(Encode.pm) perl(HTTP/Headers.pm) perl(Config/Any.pm) perl(Plack/Request.pm) perl(Module/Build.pm) perl-devel perl(HTTP/Body.pm) perl(MooX/Types/MooseLike.pm) perl(URI/Escape.pm) perl(Role/Tiny.pm) perl(Test/MockTime.pm) perl(Test/Fatal.pm) perl(URI.pm) perl-libwww perl(Pod/Simple.pm) perl(Test/TCP.pm) perl(Digest/SHA.pm) perl(parent.pm) perl(HTTP/Request/Common.pm) perl(Hash/Merge/Simple.pm) perl(Moo/Role.pm) perl(Test/Script.pm) perl(YAML/Any.pm) perl(HTTP/Server/Simple/PSGI.pm) perl(Class/Load.pm) perl(Moo.pm) perl(Template.pm) perl(MIME/Types.pm) perl(HTTP/Date.pm) perl(JSON.pm) perl(Return/MultiLevel.pm) perl(App/Cmd/Setup.pm) perl(Safe/Isa.pm) perl(Plack/Middleware/FixMissingBodyInRedirect.pm) perl(Plack/Middleware/RemoveRedundantBody.pm) perl(Test/Memory/Cycle.pm) perl(File/ShareDir/Install.pm) perl(HTTP/Headers/Fast.pm)
BuildRequires: perl(Type/Library.pm) perl(Ref/Util.pm) perl(Attribute/Handlers.pm) perl(File/Share.pm) perl(CLI/Osprey.pm)

%description
%summary

%prep
%setup -q -n %oname-%version

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%doc AUTHORS Changes GitGuide.md examples
%_bindir/dancer2
%_man1dir/dancer2.*
%perl_vendor_privlib/Dancer2*
%perl_vendor_privlib/auto/share/dist/*
%doc AUTHORS Changes *.md

%changelog
* Thu Feb 09 2023 Igor Vlasenko <viy@altlinux.org> 0.400001-alt1
- new version

* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 0.400000-alt1
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0.301004-alt1
- new version

* Wed Apr 28 2021 Igor Vlasenko <viy@altlinux.org> 0.301002-alt1
- new version

* Wed Mar 24 2021 Igor Vlasenko <viy@altlinux.org> 0.301001-alt1
- new version

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.301000-alt1
- new version

* Mon Feb 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.300005-alt1
- new version

* Sat Jun 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.300004-alt1
- new version

* Tue Apr 14 2020 Igor Vlasenko <viy@altlinux.ru> 0.300003-alt1
- new version

* Wed Jan 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.300000-alt1
- new version

* Thu Aug 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.208001-alt1
- new version

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.208000-alt1
- new version

* Thu Dec 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.207000-alt1
- automated CPAN update

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.206000-alt1
- automated CPAN update

* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.205002-alt1
- automated CPAN update

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.205001-alt1
- Updated to upstream version 0.205001.

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.166001-alt1
- automated CPAN update

* Thu Oct 29 2015 Vladimir Lettiev <crux@altlinux.ru> 0.163000-alt1
- 1.163000
- fixed FTBFS

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.162000-alt1
- automated CPAN update

* Sat Jan 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.158000-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.157001-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.157000-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.143000-alt1
- automated CPAN update

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.142000-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.141000-alt1
- automated CPAN update

* Tue Sep 17 2013 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- initial build for ALTLinux

