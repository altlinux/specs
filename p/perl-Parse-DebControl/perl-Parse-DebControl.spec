%define module_version 2.005
%define module_name Parse-DebControl
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Compress/Zlib.pm) perl(Error.pm) perl(Exporter/Lite.pm) perl(ExtUtils/MakeMaker.pm) perl(IO/Scalar.pm) perl(LWP/Simple.pm) perl(LWP/UserAgent.pm) perl(Test/Exception.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.005
Release: alt3
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/J/JA/JAYBONCI/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch
Patch33: 0001-Parse-DebControl-error-handling.patch
Patch34: 0002-Strict-parse.patch
Patch35: 0003-Parse-DebControl-Patch.patch
Patch36: 0004-Manpage-spelling-fixes.patch
Patch37: 0005-More-thorough-comment-parsing.patch
Patch38: 0006-Better-line-number-tracking.patch

%description
%summary

%prep
%setup -n %{module_name}-%{module_version}
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES
%perl_vendor_privlib/P*

%changelog
* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 2.005-alt3
- moved to Sisyphus by request of George V. Kouryachy

* Thu Oct 23 2014 Igor Vlasenko <viy@altlinux.ru> 2.005-alt2
- new release - added debian patches

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 2.005-alt1
- initial import by package builder

