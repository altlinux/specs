Name: sdf
Version: 2.001
Release: alt2
Epoch: 1

Summary: Simple Document Format (SDF) Parser
Group: Development/Other
License: BSD-style
# http://www.mincom.com/mtr/sdf/
Url: http://search.cpan.org/src/IANC/
BuildArch: noarch

Source: sdf-%version.tar
Patch1: sdf-2.001-deb-perl_loc_and_ini_fixes.patch
Patch2: sdf-2.001-deb-pod_man_conventions.patch
Patch3: sdf-2.001-deb-tablepackstr_spin.patch

# Automatically added by buildreq on Wed Jan 10 2001
BuildRequires: perl-devel perl-Pod-Parser

%def_without test

%package doc
Summary: Documentation and examples for the Simple Document Format (SDF) Parser
Group: Development/Other
Requires: %name = %version-%release

%description
SDF (Simple Document Format) is a freely available document development
system which generates high quality outputs in a variety of formats
from a single source. The output formats supported include
PostScript(tm), PDF, HTML, plain text, POD, man pages, LaTeX,
MIF, SGML, Windows(tm) help, RTF, MIMS F6 help and MIMS HTX help.
If the idea of specifying documents in a logical manner via a
simple markup language sounds appealing, SDF may be useful to you.

%description doc
SDF (Simple Document Format) is a freely available document development
system which generates high quality outputs in a variety of formats
from a single source. The output formats supported include
PostScript(tm), PDF, HTML, plain text, POD, man pages, LaTeX,
MIF, SGML, Windows(tm) help, RTF, MIMS F6 help and MIMS HTX help.
If the idea of specifying documents in a logical manner via a
simple markup language sounds appealing, SDF may be useful to you.

This package contains Documentation and examples for the
Simple Document Format (SDF) Parser.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

find -type f -print0 |
	xargs -r0 grep -FZl /bin/perl5 -- |
	xargs -r0 sed -i 's,/bin/perl5,/bin/perl,g' --
find -type f -print0 |
	xargs -r0 grep -FZl /usr/local -- |
	xargs -r0 sed -i 's,/usr/local,/usr,g' --

%build
%perl_vendor_build

%install
%perl_vendor_install

mkdir -p %buildroot%_sysconfdir
mv %buildroot%perl_vendor_privlib/%name/home/%name.ini \
	%buildroot%_sysconfdir/
ln -s %_sysconfdir/%name.ini \
	%buildroot%perl_vendor_privlib/%name/home/

%define _customdocdir %_docdir/%name-%version

%files
%config(noreplace) %_sysconfdir/%name.ini
%_bindir/*
%perl_vendor_privlib/Pod
%perl_vendor_privlib/%name

%files doc
%doc LICENSE README doc/* examples/2001/stylesheets

%changelog
* Mon Nov 15 2010 Dmitry V. Levin <ldv@altlinux.org> 1:2.001-alt2
- Fixed build with new perl.
- Dropped pod2sdf.1, use "perldoc pod2sdf" instead.

* Wed Apr 23 2008 Dmitry V. Levin <ldv@altlinux.org> 1:2.001-alt1
- Updated release numbering.

* Thu Jan 16 2003 Dmitry V. Levin <ldv@altlinux.org> 2.001-ipl4
- Merged debian fixes:
  + Patch #002: -DMAN_CONVENTIONS causes 'sdf -2man' to generate man pages
    in a more conventional style.
  + Patch #003: Fix a spin in _TablePackStr() (closes: #175578).
  + Moved sdf.ini to %_sysconfdir/.

* Sat Nov 02 2002 Dmitry V. Levin <ldv@altlinux.org> 2.001-ipl3
- Specfile cleanup.
- Rebuilt with perl-5.8.

* Mon Jun 25 2001 Sergie Pugachev <fd_rag@altlinux.ru> 2.001-ipl2
- Rebuild with perl-5.6.1

* Wed Jan 10 2001 Dmitry V. Levin <ldv@fandra.org> 2.001-ipl1
- Initial revision.
