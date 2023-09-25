%define _unpackaged_files_terminate_build 1
%define module_name File-Copy-Recursive-Reduced
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Capture/Tiny.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Copy.pm) perl(File/Copy/Recursive.pm) perl(File/Find.pm) perl(File/Path.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(Path/Tiny.pm) perl(Test/Simple.pm) perl(parent.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.007
Release: alt1
Summary: Recursive copying of files and directories within Perl 5 toolchain
Group: Development/Perl
License: perl
URL: http://thenceforward.net/perl/modules/File-Copy-Recursive-Reduced/

Source0: http://www.cpan.org/authors/id/J/JK/JKEENAN/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This library is intended as a not-quite-drop-in replacement for certain
functionality provided by CPAN distribution File-Copy-Recursive.  The
library provides methods similar enough to that distribution's `fcopy()' and
`dircopy()' functions to be usable in those CPAN distributions often
described as being part of the Perl toolchain.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Todo Changes
%perl_vendor_privlib/F*

%changelog
* Mon Sep 25 2023 Igor Vlasenko <viy@altlinux.org> 0.007-alt1
- automated CPAN update

* Wed May 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- automated CPAN update

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2
- to Sisyphus as perl-Module-Build-XSUtil dep

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- regenerated from template by package builder

* Sat Apr 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial import by package builder

