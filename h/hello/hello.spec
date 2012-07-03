Name: hello
Version: 2.4
Release: alt2

Summary: GNU hello, THE greeting printing program
Group: Development/C
License: GPLv3+

Url: ftp://ftp.gnu.org/gnu/hello/

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: %url/%name-%version.tar.gz

%description
The GNU `hello' program produces a familiar, friendly greeting.  It
allows nonprogrammers to use a classic computer science tool which
would otherwise be unavailable to them.  Because it is protected by the
GNU General Public License, users are free to share and change it.
   
%prep
%setup

%build
%configure
%make_build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%doc ABOUT-NLS AUTHORS ChangeLog ChangeLog.O NEWS README THANKS TODO contrib/ tests/
%_bindir/*
%_infodir/*
%_mandir/man?/*

%changelog
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

