%define _unpackaged_files_terminate_build 1
%define dist File-pushd
Name: perl-%dist
Version: 1.014
Release: alt1

Summary: Change directory temporarily for a limited scope
License: %asl
Group: Development/Perl
Packager: Artem Zolochevskiy <azol@altlinux.ru>

URL: %CPAN %dist
# http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/File-pushd-1.00.tar.gz
Source: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/File-pushd-%{version}.tar.gz
Patch: %name-1.005.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Fri Jan 15 2010
BuildRequires: perl-Module-Build

%description
File::pushd does a temporary "chdir" that is easily and automatically
reverted, similar to "pushd" in some Unix command shells. It works by
creating an object that caches the original working directory. When the
object is destroyed, the destructor calls "chdir" to revert to the
original working directory. By storing the object in a lexical variable
with a limited scope, this happens automatically at the end of the
scope.

This is very handy when working with temporary directories for tasks
like testing; a function is provided to streamline getting a temporary
directory from File::Temp.

For convenience, the object stringifies as the canonical form of the
absolute pathname of the directory entered.

%prep
%setup -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README Todo examples
%perl_vendor_privlib/File/

%changelog
* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.014-alt1
- automated CPAN update

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.009-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.007-alt1
- automated CPAN update

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.006-alt1
- automated CPAN update

* Fri Oct 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.005-alt1
- automated CPAN update
- rediffed patch

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jan 15 2010 Artem Zolochevskiy <azol@altlinux.ru> 1.00-alt1
- initial build for Sisyphus
