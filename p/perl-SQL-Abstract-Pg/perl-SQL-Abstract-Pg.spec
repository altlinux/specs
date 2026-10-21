# Automatically added by buildreq on Wed Oct 21 2026 (-bi)
# optimized out: elfutils libgpg-error perl perl-CPAN-Meta-Requirements perl-Encode perl-Moo perl-Sub-Quote perl-devel perl-parent python3 python3-base rpm-build-file sh5
BuildRequires: perl-SQL-Abstract perl-Test-Deep

# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(SQL/Abstract.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define module_name SQL-Abstract-Pg
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.0
Release: alt2.1
Summary: PostgreSQL features for SQL::Abstract
Group: Development/Perl
License: artistic_2
URL: https://mojolicious.org

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/S/SR/SRI/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
the SQL::Abstract::Pg manpage extends the SQL::Abstract manpage with a few PostgreSQL features used by the Mojo::Pg manpage.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes LICENSE
%perl_vendor_privlib/S*

%changelog
* Wed Oct 21 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2.1
- NMU: regenerated BuildRequires: perl-SQL-Abstract, perl-Test-Deep.

* Wed Feb 24 2021 Igor Vlasenko <viy@altlinux.org> 1.0-alt2
- to Sisyphus as Mojo-Pg dep

* Mon Feb 22 2021 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- initial import by package builder

