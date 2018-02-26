%define sitedocroot %_var/www/%name
%define apache_user apache
%define apache2_user apache2

Name: xsp
Version: 2.10.2
Release: alt1

Summary: standalone web server written in C# that can be used to run your ASP.NET applications
License: LGPL
Group: System/Servers

Url: http://www.mono-project.com
Packager: Mono Maintainers Team <mono@packages.altlinux.org>

#http://go-mono.com/sources/xsp/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: %name.init
Source2: %name.sysconfig
Patch: %name-%version-alt-lib-path.patch

Requires: mono mono-web mono-data mono-mcs

BuildPreReq: /proc
BuildRequires: mono-devel >= 2.8
BuildRequires: mono-data mono-data-sqlite mono-data-oracle mono-mcs monodoc-devel
BuildRequires: mono-nunit-devel mono-web-devel rpm-build-mono

%package devel
Summary: Development files %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package includes development files for the %name.

%package doc
Summary: Documentation for xsp
Group: Documentation
BuildArch: noarch
Requires: monodoc >= 2.2

%description doc
This package contains the documentation for the Mono Web Server Library (XSP)


%package samples
Summary: ASP.NET Samples for XSP server
Group: System/Servers
Requires: %name = %version-%release

%description
This package contains XSP, a standalone web server written in C#
that can be used to run ASP.NET applications as well as a set of
pages, controls and web services that you can use to experience
ASP.NET.

%description samples
ASP.NET Samples for XSP server

%prep
%setup -q
%patch -p1

%build
./autogen.sh
%configure
%make

%install
%make install DESTDIR=%buildroot
mkdir -p %buildroot%_sysconfdir/mono/mod-mono-applications
mkdir -p %buildroot%sitedocroot/
mv %buildroot%_libdir/%name/test/* %buildroot%sitedocroot/

mkdir -p %buildroot%_var/run/%name

install -m0755 %SOURCE1 -D %buildroot%_initdir/%name
install -m0644 %SOURCE2 -D %buildroot%_sysconfdir/sysconfig/%name

%pre
%_sbindir/groupadd -r -f webmaster &>/dev/null ||:
%_sbindir/groupadd -r -f %name &>/dev/null ||:
%_sbindir/useradd -r -g %name -G webmaster,%name -d %_var/www/%name -s /dev/null \
        -c "XSP Web Server" -M -n %name &>/dev/null ||:

# Add apache pseudousers to xsp group
%_sbindir/usermod -G %name$(groups %apache_user | \
	cut -d ':' -f 2 | sed 's/ /,/g') %apache_user &>/dev/null ||:
%_sbindir/usermod -G %name$(groups %apache2_user | \
	cut -d ':' -f 2 | sed 's/ /,/g') %apache2_user &>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/*
%_libdir/%name
%_monodir/?.0/*
%_monogacdir/Mono.WebServer*
%_monogacdir/mod-mono-server*
%_monogacdir/fastcgi-mono-server*
%_monogacdir/%{name}*
%_man1dir/*
%_sysconfdir/mono/mod-mono-applications
%config(noreplace) %_sysconfdir/sysconfig/%name
%_initdir/%name
%attr(2775,root,webmaster) %dir %sitedocroot
%attr(0730,root,%name) %dir %_var/run/%name

%files devel
%_pkgconfigdir/*

%files doc
%_monodocdir/*

%files samples
%sitedocroot/*

%changelog
* Thu Feb 09 2012 Alexey Shabalin <shaba@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Tue Nov 23 2010 Alexey Shabalin <shaba@altlinux.ru> 2.8.1-alt1
- 2.8.1
- add doc subpackage

* Wed Mar 17 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Wed Dec 16 2009 Alexey Shabalin <shaba@altlinux.ru> 2.6-alt1
- 2.6

* Thu Dec 10 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Mon Jul 13 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.2-alt1
- 2.4.2
- move pkgconfig files from main to devel package

* Sat Apr 18 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4-alt1
- 2.4

* Tue Aug 12 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt0.pre1
- 2.0 preview1

* Wed Apr 23 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Wed Dec 19 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Thu Aug 09 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Tue Apr 17 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.3-alt2
- Do not start on any runlevel by default

* Thu Mar 22 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.3-alt1
- 1.2.3
- Patch source instead of using sed
- Switch to use .gear-tags

* Mon Dec 04 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.1-alt1
- 1.2.1
- Rename /etc/sysconfig/xsp.conf to /etc/sysconfig/xsp
- Add dependency on mono-mcs

* Thu Nov 09 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1.18-alt1
- 1.1.18
- Move xsp.conf from /etc/ to /etc/sysconfig/
- Add apache{1,2} pseudousers to xsp group
- Use %%_sysconfdir/mono/mod-mono-applications as default path for search for
  mod_mono applications
- Use full url in Source
- Minor spec cleanup

* Wed Nov 23 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.10-alt1
- Update to release

* Sat Oct 08 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.9.2-alt1
- update to release

* Sun Aug 07 2005 Pavel Mironchik <tibor@altlinux.ru> 1.0.9-alt2
- fixed xsp-run script
- added tmpdirs to /etc/xsp.conf

* Sun May 22 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.0.9-alt1
- release

* Mon Aug  9 2004 Pavel S. Mironchik <tibor@altlinux.ru> 1.0-alt1
- release

* Thu Feb 26 2004 Pavel S. Mironchik <tibor@altlinux.ru> 0.9-alt1
- new version release

* Wed Dec 17 2003 Pavel S. Mironchik <tibor@altlinux.ru> 0.8-alt1
- new release

* Thu Oct 16 2003 Pavel S. Mironchik <tibor@altlinux.ru> 0.6-alt1
- new version

* Thu Sep 18 2003 Pavel S. Mironchik <tibor@altlinux.ru> 0.5-alt1
- Initial build for ALTLinux.
