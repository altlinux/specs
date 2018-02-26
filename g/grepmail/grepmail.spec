Name: grepmail
Version: 5.30.34
Release: alt2

Summary: Search mailboxes for a particular email
License: GPL
Group: File tools
URL: http://search.cpan.org/dist/grepmail/
BuildArch: noarch
# http://git.altlinux.org/gears/g/grepmail.git
Source: %name-%version-%release.tar

# Automatically added by buildreq on Tue Feb 27 2007
BuildRequires: perl-Date-Manip perl-Mail-Mbox-MessageParser perl-Module-Install perl-Pod-Parser perl-TimeDate

%description
Grepmail searches a normal, gzip'd, bzip'd, or tzip'd mailbox
for a given regular expression, and returns those emails that
match it. Piped input is allowed, and date and size restrictions
are supported, as are searches using logical operators.

%prep
%setup -n %name-%version-%release

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc CHANGES README *.el
%_bindir/grepmail
%_man1dir/grepmail.*

%changelog
* Mon Dec 20 2010 Alexey Tourbin <at@altlinux.ru> 5.30.34-alt2
- fixed build with new Module::Install

* Tue Nov 16 2010 Dmitry V. Levin <ldv@altlinux.org> 5.30.34-alt1
- Updated to 5.3034.
- Fixed build with new perl.

* Tue Feb 27 2007 Alexey Tourbin <at@altlinux.ru> 5.30.32-alt2
- imported into git and adapted for gear
- fixed end_of_file check for new Mail::Mbox::MessageParser (cpan #24341)
- changed Makefile.PL to avoid extra build dependencies

* Thu Aug 10 2006 Alexey Tourbin <at@altlinux.ru> 5.30.32-alt1
- 5.3030 -> 5.3032

* Tue May 03 2005 Alexey Tourbin <at@altlinux.ru> 5.30.30-alt1
- 5.30 -> 5.3030
- use system Test::More for building (remove inc/Test)
- clarified dependencies (eliminated eval constructs)
- updated vm-grepmail.el

* Mon Aug 09 2004 Alexey Tourbin <at@altlinux.ru> 5.30-alt1
- 5.23 -> 5.30

* Tue May 18 2004 Alexey Tourbin <at@altlinux.ru> 5.23-alt1
- 4.80 -> 5.23 (now uses Mail::Mbox::MessageParser)
- vm-grepmail.el updated (1.4 -> 1.12)
- BuildArch: noarch

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 4.80-alt1
- Updated to 4.80.
- Enforce build of FastReader.
- Built with perl-5.8.

* Fri Oct 11 2002 Dmitry V. Levin <ldv@altlinux.org> 4.72-alt1
- 4.72
- Added anonymize_mailbox.

* Fri Dec 07 2001 Dmitry V. Levin <ldv@alt-linux.org> 4.60-alt1
- 4.60
- Added grepmail plugins for VM and Gnus.

* Mon Sep 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.51-alt1
- 4.51

* Mon Jun 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.48-alt1
- 4.48
- Rebuilt with perl-5.6.1

* Thu Feb 22 2001 Dmitry V. Levin <ldv@fandra.org> 4.46-ipl1
- 4.46

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 4.45-ipl1
- 4.45
- RE adaptions.

* Fri Apr 28 2000 Dmitry V. Levin <ldv@fandra.org>
- 4.23

* Wed Nov 10 1999 Dmitry V. Levin <ldv@fandra.org>
- initial revision
