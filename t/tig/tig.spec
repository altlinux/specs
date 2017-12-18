Name: tig
Version: 2.3.1
Release: alt1

Summary: text-mode interface for git
License: GPL
Group: Development/Other

URL: http://jonas.nitro.dk/tig/
Source: tig-%version.tar
Patch: tig-%version-%release.patch

Requires: git-core

# Automatically added by buildreq on Thu Oct 05 2017
BuildRequires: asciidoc libncursesw-devel libreadline-devel xmlto

%description
Tig is a git repository browser that additionally can act as a pager
for output from various git commands.

When browsing repositories, it uses the underlying git commands to
present the user with various views, such as summarized revision log
and showing the commit with the log message, diffstat, and the diff.

Using it as a pager, it will display input from stdin and colorize it.

%prep
%setup -q
%patch -p1

%build
autoreconf
%configure
make V=1 src/tig doc-man

%install
install -pD -m755 src/tig %buildroot%_bindir/tig
install -pD -m644 doc/tig.1 %buildroot%_man1dir/tig.1
install -pD -m644 doc/tigrc.5 %buildroot%_man5dir/tigrc.5
install -pD -m644 doc/tigmanual.7 %buildroot%_man7dir/tigmanual.7

%files
%doc NEWS.adoc README.adoc
%_bindir/tig
%_man1dir/tig.1*
%_man5dir/tigrc.5*
%_man7dir/tigmanual.7*

%changelog
* Mon Dec 18 2017 Alexey Tourbin <at@altlinux.ru> 2.3.1-alt1
- 2.3.0 -> 2.3.1

* Thu Oct 05 2017 Alexey Tourbin <at@altlinux.ru> 2.3.0-alt2
- built with readline

* Wed Oct 04 2017 Alexey Tourbin <at@altlinux.ru> 2.3.0-alt1
- 2.2.2 -> 2.3.0

* Fri Aug 18 2017 Alexey Tourbin <at@altlinux.ru> 2.2.2-alt1
- 1.1 -> 2.2.2

* Wed Oct 24 2012 Alexey Tourbin <at@altlinux.ru> 1.1-alt1
- 1.0 -> 1.1

* Fri Sep 21 2012 Alexey Tourbin <at@altlinux.ru> 1.0-alt2
- packaged tigmanual(7)

* Fri May 11 2012 Alexey Tourbin <at@altlinux.ru> 1.0-alt1
- tig-1.0

* Tue Feb 14 2012 Alexey Tourbin <at@altlinux.ru> 0.18-alt1
- tig-0.18

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 0.17-alt2
- tig-0.17-43-gcc3ca7c

* Sun Mar 20 2011 Alexey Tourbin <at@altlinux.ru> 0.17-alt1
- tig-0.17

* Mon Nov 22 2010 Alexey Tourbin <at@altlinux.ru> 0.16.2-alt1
- tig-0.16.2

* Tue Jul 06 2010 Alexey Tourbin <at@altlinux.ru> 0.16-alt1
- tig-0.16

* Fri Dec 04 2009 Alexey Tourbin <at@altlinux.ru> 0.15-alt1
- tig-0.15

* Mon Jul 20 2009 Alexey Tourbin <at@altlinux.ru> 0.14.1-alt2
- tig-0.14.1-29-g1e69632

* Wed Apr 08 2009 Alexey Tourbin <at@altlinux.ru> 0.14.1-alt1
- 0.14 -> 0.14.1

* Sat Feb 14 2009 Alexey Tourbin <at@altlinux.ru> 0.14-alt2
- packaged NEWS.html

* Sat Feb 14 2009 Alexey Tourbin <at@altlinux.ru> 0.14-alt1
- 0.12.1 -> 0.14

* Sat Oct 11 2008 Alexey Tourbin <at@altlinux.ru> 0.12.1-alt1
- 0.12 -> 0.12.1

* Tue Sep 16 2008 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- 0.11 -> 0.12

* Tue Apr 15 2008 Alexey Tourbin <at@altlinux.ru> 0.11-alt1
- 0.10.1 -> 0.11

* Fri Mar 21 2008 Alexey Tourbin <at@altlinux.ru> 0.10.1-alt1
- 0.9.1 -> 0.10.1
- built with libncursesw

* Sun Oct 28 2007 Alexey Tourbin <at@altlinux.ru> 0.9.1-alt1
- updated to tig-0.9.1

* Sat Jul 21 2007 Alexey Tourbin <at@altlinux.ru> 0.8-alt1
- updated to tig-0.8-12-g56b6ea5

* Sat Jun 16 2007 Alexey Tourbin <at@altlinux.ru> 0.7-alt1
- updated to tig-0.7-18-gd1858de

* Wed Mar 28 2007 Alexey Tourbin <at@altlinux.ru> 0.6-alt1
- updated to tig-0.6-1-ga1d2855

* Thu Feb 22 2007 Alexey Tourbin <at@altlinux.ru> 0.5-alt5
- updated to tig-0.5-16-ge15ec88 (improved handling of remotes)

* Sun Jan 07 2007 Alexey Tourbin <at@altlinux.ru> 0.5-alt4
- updated to tig-0.5-g337d737

* Tue Oct 31 2006 Alexey Tourbin <at@altlinux.ru> 0.5-alt3
- new snapshot, fixes SEGV in tree view

* Wed Oct 18 2006 Alexey Tourbin <at@altlinux.ru> 0.5-alt2
- in main view, fix handling of headlines that start with whitespace

* Tue Oct 03 2006 Alexey Tourbin <at@altlinux.ru> 0.5-alt1
- new version

* Sat Sep 09 2006 Alexey Tourbin <at@altlinux.ru> 0.4-alt1
- new snapshot

* Thu Jul 06 2006 Alexey Tourbin <at@altlinux.ru> 0.3-alt1
- initial revision
