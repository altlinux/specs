%define _unpackaged_files_terminate_build 1
%define module_name Email-Outlook-Message
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Email/Address.pm) perl(Email/MIME.pm) perl(Email/MIME/ContentType.pm) perl(Email/Sender.pm) perl(Email/Simple.pm) perl(Encode.pm) perl(Encode/CN.pm) perl(Encode/JP.pm) perl(Encode/KR.pm) perl(Encode/TW.pm) perl(File/Basename.pm) perl(Getopt/Long.pm) perl(IO/All.pm) perl(IO/String.pm) perl(Module/Build.pm) perl(OLE/Storage_Lite.pm) perl(POSIX.pm) perl(Pod/Usage.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.921
Release: alt1
Summary: Read Outlook .msg files
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/M/MV/MVZ/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %module_name

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%doc README CHANGELOG
%perl_vendor_privlib/E*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Thu Jan 27 2022 Igor Vlasenko <viy@altlinux.org> 0.921-alt1
- automated CPAN update

* Mon Sep 28 2020 Igor Vlasenko <viy@altlinux.ru> 0.920-alt2
- to Sisyphus (#38978)

* Sun Sep 13 2020 Igor Vlasenko <viy@altlinux.ru> 0.920-alt1
- updated by package builder

* Sun Sep 24 2017 Igor Vlasenko <viy@altlinux.ru> 0.919-alt1
- regenerated from template by package builder

* Mon Nov 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.918-alt1
- regenerated from template by package builder

* Thu Oct 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.917-alt1
- regenerated from template by package builder

* Mon Sep 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.916-alt1
- regenerated from template by package builder

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.914-alt1
- initial import by package builder

