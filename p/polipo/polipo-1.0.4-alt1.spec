Packager: Repocop Q. A. Robot <repocop@altlinux.org>
Name: polipo
Version: 1.0.4
Release: alt1.1
Summary: Single-threaded non blocking HTTP proxy
License: %mit
Group: System/Servers
URL: http://www.pps.jussieu.fr/~jch/software/%name/
Source0: http://www.pps.jussieu.fr/~jch/software/files/%name/%name-%version.tar.bz2
Source1: %name.init
Patch: %name-1.0.2-alt-install.patch

# Automatically added by buildreq on Sat Sep 01 2007 (-bi)
BuildRequires: symlinks

BuildRequires: rpm-build-licenses

%description
Polipo is single-threaded, non blocking HTTP proxy. It listens to
requests for web pages from your browser and forwards them to web
servers, and forwards the servers' replies to your browser. In the
process, it optimises and cleans up the network traffic.


%prep
%setup
%patch -p1


%build
%define _optlevel s
%make_build CDEBUGFLAGS="%optflags"


%install
%make_install TARGET=%buildroot PREFIX=%_prefix MANDIR=%_mandir INFODIR=%_infodir install
install -d -m 0755 %buildroot{{%_sysconfdir,%_cachedir}/%name,%_docdir/%name-%version}
touch %buildroot%_sysconfdir/%name/{config,forbidden}
bzip2 --best --stdout CHANGES > %buildroot%_docdir/%name-%version/CHANGES.bz2
install -m 0644 README %buildroot%_docdir/%name-%version/
ln -sf %buildroot{%_datadir/%name/www/doc,%_docdir/%name-%version/html}
symlinks -c %buildroot%_docdir/%name-%version
symlinks -cs %buildroot%_docdir/%name-%version
install -pD -m 0755 %SOURCE1 %buildroot%_initdir/%name


%post
%post_service %name ||:


%preun
%preun_service %name ||:


%files
%_docdir/%name-%version/*
%_bindir/*
%_man1dir/*
%_infodir/*
%_datadir/%name
%dir %_cachedir/%name
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_initdir/*
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/polipo-%version 


%changelog
* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1.1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for polipo
  * docdir-is-not-owned for polipo

* Thu Jan 10 2008 Led <led@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sun Oct 07 2007 Led <led@altlinux.ru> 1.0.3-alt1
- 1.0.3
- updated init script

* Sat Sep 01 2007 Led <led@altlinux.ru> 1.0.2-alt1
- added init script

* Sat Sep 01 2007 Led <led@altlinux.ru> 1.0.2-alt0.1
- initial build
