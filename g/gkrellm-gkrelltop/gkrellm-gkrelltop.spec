%define shortname gkrelltop

Name: gkrellm-%shortname
Version: 2.2.13
Release: alt1

Summary: GKrellM plugin which shows 3 most cpu intensive processes
License: GPL
Group: Monitoring
Url: http://sourceforge.net/projects/gkrelltop

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: %shortname-%version.tar.gz
Patch0: %shortname-2.2.10-alt-link-fixes.patch

BuildPreReq: gkrellm-devel libgtk+2-devel pkgconfig

%description
Display the top three cpu intensive processes in a small window inside
gkrellm, similar to wmtop. Useful to check out anytime what processes
are consuming most cpu power on your machine.

%prep
%setup -n %shortname-%version
%patch0 -p2
sed -i 's|^CFLAGS[2D] =.*|\0 %optflags|' Makefile

%build
%make_build

%install
mkdir -p %buildroot%_libdir/gkrellm2/plugins
%makeinstall INSTALLDIR=%buildroot%_libdir/gkrellm2/plugins INSTALLDIRD=%buildroot%_libdir/gkrellm2/plugins

%files
%doc README
%_libdir/gkrellm2/plugins/*.so

%changelog
* Thu Aug 20 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.2.13-alt1
- 2.2.13

* Wed Feb 13 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.2.11-alt1
- 2.2.11

* Mon Nov 05 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.2.10-alt1
- 2.2.10

* Sat Mar 31 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.2.9-alt1
- 2.2.9

* Mon Oct 24 2005 Andrey Rahmatullin <wrar@altlinux.ru> 2.2.6-alt1
- initial build

