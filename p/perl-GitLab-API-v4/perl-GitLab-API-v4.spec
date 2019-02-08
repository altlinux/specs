%define module_name GitLab-API-v4
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Const/Fast.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Getopt/Long.pm) perl(HTTP/Tiny.pm) perl(HTTP/Tiny/Multipart.pm) perl(IO/Prompter.pm) perl(IPC/Cmd.pm) perl(JSON.pm) perl(Log/Any.pm) perl(Log/Any/Adapter.pm) perl(Log/Any/Adapter/Screen.pm) perl(Log/Any/Adapter/TAP.pm) perl(MIME/Base64.pm) perl(Moo.pm) perl(Path/Tiny.pm) perl(Pod/Usage.pm) perl(Test/More.pm) perl(Test2/V0.pm) perl(Try/Tiny.pm) perl(Types/Common/Numeric.pm) perl(Types/Common/String.pm) perl(Types/Standard.pm) perl(URI.pm) perl(URI/Escape.pm) perl(namespace/clean.pm) perl(strictures.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.15
Release: alt2
Summary: A complete GitLab API v4 client.
Group: Development/Perl
License: perl
URL: https://github.com/bluefeet/GitLab-API-v4

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/B/BL/BLUEFEET/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This module provides a one-to-one interface with the GitLab
API v4.  Much is not documented here as it would just be duplicating
GitLab's own API Documentation.

Note that this distribution also includes the the gitlab-api-v4 manpage command-line
interface (CLI).

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %module_name

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes
%perl_vendor_privlib/G*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Thu Feb 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2
- to Sisyphus as devscripts dep

* Sat Jan 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- regenerated from template by package builder

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- regenerated from template by package builder

* Fri Nov 09 2018 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- regenerated from template by package builder

* Wed Sep 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- regenerated from template by package builder

* Fri Jun 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- regenerated from template by package builder

* Wed May 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- regenerated from template by package builder

* Thu May 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

