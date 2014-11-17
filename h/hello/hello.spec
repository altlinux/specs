Name: hello
Version: 2.10
Release: alt1

Summary: GNU hello, THE greeting printing program
Group: Development/C
License: GPLv3+

Url: ftp://ftp.gnu.org/gnu/hello/

Source: %name-%version.tar.gz

%description
The GNU `hello' program produces a familiar, friendly greeting.  It
allows nonprogrammers to use a classic computer science tool which
would otherwise be unavailable to them.  Because it is protected by the
GNU General Public License, users are free to share and change it.

%prep
%setup -a0

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog ChangeLog.O NEWS README THANKS TODO
%doc %name-%version
%_bindir/*
%_infodir/*
%_mandir/man?/*

%changelog
* Mon Nov 17 2014 Fr. Br. George <george@altlinux.ru> 2.10-alt1
- Autobuild version bump to 2.10
- Use autoreconf for educational purpose
- Add full source tree in documentation

* Thu Apr 17 2014 Fr. Br. George <george@altlinux.ru> 2.9-alt1
- Autobuild version bump to 2.9

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.4-alt2.qa1
- NMU: rebuilt for debuginfo.

* Thu May 21 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.4-alt2
- remove obsolete %%{,un}install_info calls

* Sat Dec 13 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.4-alt1
- 2.4

* Wed Aug 15 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.3-alt1
- 2.3

* Thu Feb 15 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.2-alt1
- 2.2

* Thu Oct 23 2003 Andrey Rahmatullin <wrar@altlinux.ru> 2.1.1-alt1
- initial build

