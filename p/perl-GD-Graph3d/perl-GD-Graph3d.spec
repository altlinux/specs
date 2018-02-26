%define dist GD-Graph3d
Name: perl-%dist
Version: 0.63
Release: alt8

Summary: Create 3D Graphs with GD and GD::Graph
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-GD-Graph perl-devel

%description
This is the GD::Graph3d extensions module. It provides 3D graphs for the
GD::Graph module by Martien Verbruggen, which in turn generates graph using
Lincoln Stein's GD.pm.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/GD

%changelog
* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 0.63-alt8
- rebuilt

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.63-alt7.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Sep 29 2008 Afanasov Dmitry <ender@altlinux.org> 0.63-alt7
- pick orphaned package and change packager
- update BuildRequires

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.63-alt6.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Nov 25 2003 Andrey Brindeew <abr@altlinux.ru> 0.63-alt6
- Summary tag was fixed.

* Wed Aug 13 2003 Andrey Brindeew <abr@altlinux.ru> 0.63-alt5
- BuildArch was changed to `noarch'.
- Url updated.

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 0.63-alt4
- Updated BuildRequires list (again).

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 0.63-alt3
- Added a fix from at@

* Thu Jul 17 2003 Andrey Brindeew <abr@altlinux.ru> 0.63-alt2
- Updated BuildRequires list.

* Thu Jul 17 2003 Andrey Brindeew <abr@altlinux.ru> 0.63-alt1
- First build for ALTLinux.
