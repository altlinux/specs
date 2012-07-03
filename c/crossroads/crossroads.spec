Name: crossroads
Version: 2.77
Release: alt1

Summary: Load balance and fail over utility for TCP based services
License: GPLv3+
Group: System/Servers

Url: http://crossroads.e-tunity.com/
Source: http://crossroads.e-tunity.com/downloads/versions/crossroads-%version.tar.gz

# Automatically added by buildreq on Fri Feb 11 2011 (-bi)
BuildRequires: gcc-c++ perl-Term-ANSIColor

%description
Crossroads is an open source load balance and fail over utility for TCP based
services. It is a daemon running in user space, and features extensive
configurability, polling of back ends using 'wakeup calls', detailed status
reporting, 'hooks' for special actions when backend calls fail, and much more.
Crossroads is service-independent: it is usable for HTTP(S), SSH, SMTP, DNS,
etc. In the case of HTTP balancing, Crossroads can provide 'session stickiness'
for back end processes that need sessions, but aren't session-aware of other
back ends.

%prep
%setup

%build
# We want verbose compiling:
subst 's/@\$/\$/g' xr/etc/Makefile.class
%make_build local

%install
subst 's/strip/#strip/g' xr/Makefile
install -d %buildroot%_sbindir
%makeinstall_std

%files
%doc doc/xr.pdf test/{*.xml,*.xslt}
%_sbindir/*
%_man1dir/*
%_man5dir/*

%changelog
* Sun Feb 26 2012 Victor Forsiuk <force@altlinux.org> 2.77-alt1
- 2.77
- Remove 'strip' of xr before install, thus allowing debuginfo package.

* Sat Jun 11 2011 Victor Forsiuk <force@altlinux.org> 2.76-alt1
- 2.76

* Fri Feb 11 2011 Victor Forsiuk <force@altlinux.org> 2.73-alt1
- 2.73

* Wed Jan 12 2011 Victor Forsiuk <force@altlinux.org> 2.72-alt1
- 2.72

* Mon Dec 06 2010 Victor Forsiuk <force@altlinux.org> 2.71-alt1
- 2.71

* Mon Nov 15 2010 Victor Forsiuk <force@altlinux.org> 2.70-alt1
- 2.70

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 2.69-alt1.1
- rebuilt with perl 5.12

* Mon Oct 18 2010 Victor Forsiuk <force@altlinux.org> 2.69-alt1
- 2.69

* Mon Sep 27 2010 Victor Forsiuk <force@altlinux.org> 2.68-alt1
- 2.68

* Wed Jun 16 2010 Victor Forsiuk <force@altlinux.org> 2.67-alt1
- 2.67

* Fri Jan 29 2010 Victor Forsyuk <force@altlinux.org> 2.64-alt1
- 2.64

* Thu Jan 14 2010 Victor Forsyuk <force@altlinux.org> 2.63-alt1
- 2.63

* Fri Nov 06 2009 Victor Forsyuk <force@altlinux.org> 2.59-alt1
- 2.59

* Thu Jul 09 2009 Victor Forsyuk <force@altlinux.org> 2.55-alt1
- 2.55

* Fri Mar 13 2009 Victor Forsyuk <force@altlinux.org> 2.47-alt1
- 2.47

* Wed Jan 14 2009 Victor Forsyuk <force@altlinux.org> 2.41-alt1
- 2.41

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 2.18-alt1
- 2.18

* Sun Aug 17 2008 Victor Forsyuk <force@altlinux.org> 2.05-alt1
- Initial build.
