Name: howto-utils
Version: 0.2.13
Release: alt2

Summary: Index generator for HTML formatted HOWTO documents from LDP
License: GPL
Group: Text tools

Source: %name-%version.tar.bz2
Source1: makehowtoindex2
Source2: howto.xpm
Source3: lhowto.xpm
Source4: mhowto.xpm
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
Provides: howto-icons
Requires: sed

# Automatically added by buildreq on Sun Aug 08 2004 (-bi)
BuildRequires: perl-MDK-Common

%description
Linux HOWTOs are detailed documents which describe a specific aspect of
configuring or using Linux.  Linux HOWTOs are a great source of
practical information about your system.  The latest versions of these
documents are located at http://www.linuxdoc.org/docs.html#howto

Currently, availlable tools are:
- makehowtoindex: an index generator for html formatted HOWTO documents.
- makehowtoindex2: an index generator for html formatted HOWTO documents
  from *.dsc files

A few icons will be required by the generated index files and
other packages with HOWTOs installed on your system; they are
provided by this package, too.

%prep
%setup

%install
install -pDm755 makehowtoindex %buildroot%_bindir/makehowtoindex
install -pDm755 %SOURCE1 %buildroot%_bindir/makehowtoindex2
install -pDm644 %SOURCE2 %buildroot%_niconsdir/howto.xpm
install -pDm644 %SOURCE3 %buildroot%_liconsdir/howto.xpm
install -pDm644 %SOURCE4 %buildroot%_miconsdir/howto.xpm
for i in *.png; do
	install -pDm644 $i %buildroot%_docdir/HOWTO/HTML/$i
done

%files
%_bindir/*
%doc NEWS
%dir %_docdir/HOWTO/HTML
%_docdir/HOWTO/HTML/*.png
%_niconsdir/*.xpm
%_liconsdir/*.xpm
%_miconsdir/*.xpm

# TODO:
# - consider 0.2.15

%changelog
* Wed Jul 29 2009 Michael Shigorin <mike@altlinux.org> 0.2.13-alt2
- applied repocop patch
- spec cleanup

* Sun Aug 08 2004 Michael Shigorin <mike@altlinux.ru> 0.2.13-alt1
- 0.2.13
- included makehowtoindex2 from 0.2.3-alt
- updated BuildRequires

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.3-alt4
- rebuild

* Thu Mar 19 2002 Maxim Dzumanenko <mvd@altlinux.ru> 0.2.3-alt3
- makehowtoindex2 modified

* Sun Mar 17 2002 Maxim Dzumanenko <mvd@altlinux.ru> 0.2.3-alt2
- makehowtoindex2 added

* Tue Jul 24 2001 Sergie Pugachev <fd_rag@altlinux.ru> 0.2.3-alt1
- new version

* Sat Mar 10 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 0.2.2-ipl4mdk
- the way the titles are extracted improved (take dsc files into account)

* Fri Mar 09 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 0.2.2-ipl3mdk
- added possibility of inserting meta-information into the generated
  document (useful for charsets)

* Fri Mar 09 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 0.2.2-ipl2mdk
- fix duplicate titles for different items in generated lists
- include common howto icons

* Wed Mar 07 2001 Ivan Zakharyaschev <vanyaz@mccme.ru> 0.2.2-ipl1mdk
- updated version from Mdk

* Mon Mar 05 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.2-1mdk
- Merge Etienne Faure patch (Little fix to handle english howto that do
  not have pretty html
  [Last time someone patch an old version and upload it, i'll kill him)

* Thu Mar 01 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.1-1mdk
- let makehowtoindex fix howto location

##########
# Here was an RE release

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

#
##########

* Fri Aug 11 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2-1mdk
- add LN touch

* Fri Aug 11 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1.1-1mdk
- little fix to handle greek howto that don't follow LDP naming rules

* Fri Aug 11 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1-1mdk
- initial release

