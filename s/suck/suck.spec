%define BUILD_INN 0

Name: suck
Version: 4.3.2
Release: alt4.1.1

Summary: download news from remote NNTP server
License: Public Domain
Group: Networking/News

URL: http://www.sucknews.org
Source: %name-%version.tar.gz
Source1: sample.tar.gz
Source2: active-ignore
Patch0: %name-warn.patch
Patch1: %name-4.3.2-alt-configure.patch
Patch2: %name-4.3.2-rpost-ssl-alt.patch

Packager: Vladimir V Kamarzin <vvk@altlinux.ru>

BuildRequires: libdante libssl openssl-devel
%if %BUILD_INN
BuildRequires: inn-devel
%endif

%description
This package contains software for copying news from an NNTP server to your
local machine, and copying replies back up to an NNTP server.  It works
with most standard NNTP servers, including INN, CNEWS, DNEWS, and typhoon.

%prep
%setup -D -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
%if %BUILD_INN
%configure --enable-inn
%else
%configure
%endif
%make

%install
%makeinstall
mkdir -p %buildroot%_man1dir 
mv %buildroot%_mandir/*.1 %buildroot/%_man1dir
mkdir -p %buildroot%_localstatedir/sucknews/
install -m 664 %SOURCE2 %buildroot%_localstatedir/sucknews
mkdir -p %buildroot%_localstatedir/sucknews/Msgs
mkdir -p %buildroot%_localstatedir/sucknews/tmp

%files
%doc README CHANGELOG sample/{get,put}.news sample/put.news.sm
%_bindir/*
%_man1dir/*
%attr (3770,root,news) %dir %_localstatedir/sucknews
%attr (3770,root,news) %dir %_localstatedir/sucknews/Msgs
%attr (3770,root,news) %dir %_localstatedir/sucknews/tmp
%attr (660,root,news) %config(noreplace) %_localstatedir/sucknews/active-ignore

%changelog
* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 4.3.2-alt4.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 4.3.2-alt4.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Thu Feb 28 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 4.3.2-alt4
- Prevent overwriting "active-ignore" file at package upgrade

* Sun Jan 27 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 4.3.2-alt3
- Resurrected from orphaned
- Add sample INN-newsfeeds file

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 4.3.2-alt2.1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 4.3.2-alt2.1
- Rebuilt with openssl-0.9.7d.

* Wed Oct 01 2003 Sergey Budnevitch <svb@altlinux.ru> 4.3.2-alt2
- Fixed SSL support in rpost (Alexander Bokovoy)

* Sun Jul 06 2003 Sergey Budnevitch <svb@altlinux.ru> 4.3.2-alt1
- 4.3.2
- Adjusted patch

* Sun Oct 20 2002 Sergey Budnevitch <svb@altlinux.ru> 4.3.1-alt1
- 4.3.1
- Fixed typo in filename active-ignore
- Fixed directories permissions according to ALT SPP
- Removed suck-inn-2.3.patch
- Added suck-4.3.1-alt-configure.patch to provide 
  --enable-inn configure option

* Thu Apr 04 2002 Sergey Budnevitch <svb@altlinux.ru> 4.3.0-alt3
- inn support disabled by default
- build with ssl

* Wed Dec 12 2001 Sergey Budnevitch <svb@altlinux.ru>
- Fixed sample scripts

* Wed Sep 19 2001 Sergey Budnevitch <svb@altlinux.ru>
- 4.3.0
- Automatically added BuildRequires

* Thu Jun 14 2001 Sergey Budnevitch <fabler@mtu.ru>
- new version
- ALT Linux adaptations

* Tue Jan 30 2001 Lenny Cartier <lenny@mandrakesoft.com> 4.2.4-2mdk
- rebuild

* Mon Sep 18 2000 Lenny Cartier <lenny@mandrakesoft.com> 4.2.4-1mdk
- updated to 4.2.4
- BM
- macros
