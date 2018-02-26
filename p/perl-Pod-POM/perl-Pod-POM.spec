%define dist Pod-POM
Name: perl-%dist
Version: 0.27
Release: alt2

Summary: Pod Object Model
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-Encode perl-File-Slurp perl-Test-Differences perl-devel perl-parent

%description
This module implements a parser to convert Pod documents into a simple
object model form known hereafter as the Pod Object Model.  The object
model is generated as a hierarchical tree of nodes, each of which
represents a different element of the original document.  The tree can
be walked manually and the nodes examined, printed or otherwise
manipulated.  In addition, Pod::POM supports and provides view objects
which can automatically traverse the tree, or section thereof, and
generate an output representation in one form or another.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/pod*
%_bindir/pom*
%perl_vendor_privlib/Pod

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.27-alt2
- rebuilt as plain src.rpm

* Thu Jun 10 2010 Alexey Tourbin <at@altlinux.ru> 0.27-alt1
- 0.25 -> 0.27

* Mon Sep 28 2009 Alexey Tourbin <at@altlinux.ru> 0.25-alt1
- 0.17 -> 0.25
- packaged scripts

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.17-alt6.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Nov 25 2003 Andrey Brindeew <abr@altlinux.ru> 0.17-alt6
- Summary tag was fixed.

* Thu Sep 04 2003 Andrey Brindeew <abr@altlinux.ru> 0.17-alt5
- Fixed typo in URL.

* Mon Aug 11 2003 Andrey Brindeew <abr@altlinux.ru> 0.17-alt4
- Ugly test removed.

* Mon Aug 11 2003 Andrey Brindeew <abr@altlinux.ru> 0.17-alt3
- Buildreqs updates.
- changed URL.

* Thu Aug 07 2003 Andrey Brindeew <abr@altlinux.ru> 0.17-alt2
- Added missed POM.pm

* Wed Jul 30 2003 Andrey Brindeew <abr@altlinux.ru> 0.17-alt1
- 0.17

* Tue Jul 29 2003 Andrey Brindeew <abr@altlinux.ru> 0.15-alt2
- Minor specfile fixes.
- BuildArch was changed to `noarch'.

* Wed Jul 16 2003 Andrey Brindeew <abr@altlinux.ru> 0.15-alt1
- First build for ALTLinux.
