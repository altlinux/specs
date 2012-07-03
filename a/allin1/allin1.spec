Name: allin1
Version: 0.5.0
Release: alt4

Summary: The all-in-one monitoring dockapplet
License: GPLv2+
Group: Graphical desktop/Window Maker
Url: http://ilpettegolo.altervista.org/linux_allin1.en.shtml

Packager: Igor Zubkov <icesik@altlinux.org>

Source0: %name-%version.tar.gz

Patch0: allin1-0.5.0-alt-disable-debug.patch
Patch1: allin1-0.5.0-alt-nodocs.patch
Patch2: allin1-0.5.0-alt-destdir.patch
Patch3: allin1-0.5.0-alt-optflags.patch
Patch4: allin1-0.5.0-alt-seti-off.patch
Patch5: allin1-0.5.0-alt-config.patch

# Automatically added by buildreq on Thu Jul 10 2008
BuildRequires: flex libXext-devel libXpm-devel

%description
Allin1 is a monitoring dockapplet that displays RAM and SWAP space 
usage with colorful histogram, the CPU load with moving graph, 
power and battery status for notebooks, Ethernet and PPP traffic 
load, used space in up to three file systems and Seti@home progress bar. 
It was designed for FluxBox window manager, but is useful with any other 
window manager.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%make_build CFLAGS="%optflags"

%install
%make_install DESTDIR=%buildroot install

%files
%doc README.it README ChangeLog BUGS INSTALL NEWS TODO
%config(noreplace) %_sysconfdir/allin1.conf
%_bindir/allin1
%_man1dir/allin1.*
%_mandir/it/man1/allin1.*

%changelog
* Thu Jul 10 2008 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt4
- move config file from /usr to /etc

* Thu Jul 10 2008 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt3
- remove desktop file

* Thu Apr 10 2008 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt2
- update license to GPLv2+
- buildreq
- clean up spec file
- replace old menu file with new allin1.desktop

* Fri Aug 19 2005 Igor Zubkov <icesik@altlinux.ru> 0.5.0-alt1.1
- fix url

* Sat Jul 02 2005 Igor Zubkov <icesik@altlinux.ru> 0.5.0-alt1
- Initial build for Sisyphus.
