# BEGIN SourceDeps(oneline):
BuildRequires: perl(UNIVERSAL/require.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
%define dist FileHandle-Unget
Name: perl-%dist
Version: 0.1634
Release: alt2

Summary: FileHandle which supports multi-byte unget
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/D/DC/DCOPPIT/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Dec 20 2010
BuildRequires: perl-Devel-Leak perl-Module-Install perl(File/Slurp.pm) perl(Test/Compile.pm) perl(File/Slurper.pm)

%description
FileHandle::Unget operates exactly the same as FileHandle, except that
it provides a version of ungetc that allows you to unget more than one
character.  It also provides ungets to unget a string.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%dir %perl_vendor_privlib/FileHandle
%perl_vendor_privlib/FileHandle/Unget.pm

%changelog
* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 0.1634-alt2
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.1634-alt1
- automated CPAN update

* Sun Jul 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.1631-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.1628-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.1624-alt1
- automated CPAN update

* Mon Dec 20 2010 Alexey Tourbin <at@altlinux.ru> 0.1623-alt1
- 0.1621 -> 0.1623

* Tue Feb 27 2007 Alexey Tourbin <at@altlinux.ru> 0.16.21-alt2
- imported into git and adapted for gear

* Tue May 03 2005 Alexey Tourbin <at@altlinux.ru> 0.16.21-alt1
- 0.14 -> 0.1621
- alt-weakref.patch needed no more (cpan #6375)
- use simply bytes instead of ExtUtils::MakeMaker::bytes
- use system modules for building (removed inc/File inc/Test inc/Scalar)
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.14-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri May 21 2004 Alexey Tourbin <at@altlinux.ru> 0.14-alt2
- patched to use Scalar::Util instead of WeakRef (cpan #6375)

* Mon May 17 2004 Alexey Tourbin <at@altlinux.ru> 0.14-alt1
- initial revision (required by Mail-Mbox-MessageParser,
  which in turn is required by grepmail)
- License: GPL
