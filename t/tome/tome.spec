%define		varpath		/var/lib/tome/

Name:		tome
Version: 	2.3.5
Release: 	alt2

Packager:	Alexey Voinov <voins@altlinux.ru>

Summary:	Troubles of Middle Earth
License:	Moria/Angband license
Group:		Games/Adventure
Source:		%name-%version.tar
Patch0:		%name-2.2.6-alt-make.patch
Patch1:         %name-%version-alt-exit.patch
URL:		http://t-o-m-e.net/

# Automatically added by buildreq on Mon May 05 2008
BuildRequires: libX11-devel libncurses-devel

%description
ToME is a popular descendant of Moria/Angband. ToME has many unique features
that set it apart from other Angband/Moria descendants, with a nice mix of
races/classes available.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cd src
make -f makefile.std COPTS="$RPM_OPT_FLAGS" \
	DEFINES="-DUSE_X11 -DUSE_GCU -DUSE_EGO_GRAPHICS -DUSE_TRANSPARENCY -DSUPPORT_GAMMA -DUSE_PRECISE_CMOVIE -DUSE_UNIXSOCK" \
	LIBS="-lX11 -lncurses" \
	LIBDIR=%varpath

%install
cd src
make -f makefile.std install DESTDIR="$RPM_BUILD_ROOT" \
	BINDIR=%_bindir \
	LIBDIR=%varpath
find $RPM_BUILD_ROOT -name delete.me -exec rm -f '{}' ';'
touch $RPM_BUILD_ROOT%varpath/apex/scores.raw

%preun
if [ -d %varpath/data/ ]; then
	rm -rf %varpath/data/*
fi

%files
%doc changes.txt
%dir %varpath
%attr(02711,games,games) %_bindir/%name
%attr(0775,games,games) %dir %varpath/apex/
%attr(0664,games,games) %config(noreplace) %varpath/apex/*
%attr(0070,games,games) %varpath/bone/
%attr(0755,games,games) %varpath/cmov/
%attr(0755,games,games) %varpath/core/
%attr(0775,games,games) %varpath/data/
%attr(0755,games,games) %varpath/dngn/
%attr(0755,games,games) %varpath/edit/
%attr(0755,games,games) %varpath/file/
%attr(0755,games,games) %varpath/help/
%attr(0755,games,games) %varpath/info/
%attr(0755,games,games) %varpath/mods/
%attr(0755,games,games) %varpath/note/
%attr(0755,games,games) %varpath/patch/
%attr(0755,games,games) %varpath/pref/
%attr(0070,games,games) %varpath/save/
%attr(0755,games,games) %varpath/scpt/
%attr(0775,games,games) %varpath/user/
%attr(0755,games,games) %varpath/xtra/
%varpath/module.lua

%changelog
* Tue Aug 12 2008 Alexey Voinov <voins@altlinux.ru> 2.3.5-alt2
- update_menus removed
- /usr/games -> /usr/bin migration

* Tue Aug 12 2008 Alexey Voinov <voins@altlinux.ru> 2.3.5-alt1
- new version (2.3.5)
- traces of /usr/X11R6 cleaned up

* Mon May 05 2008 Alexey Voinov <voins@altlinux.ru> 2.3.4-alt2
- directory permissions fixed, directory ownership fixed [#7993]
- buildreqs updated
- buffer overflow at game exit fixed.

* Wed Oct 25 2006 Alexey Voinov <voins@altlinux.ru> 2.3.4-alt1
- new version(2.3.4)

* Sun Jan 15 2006 Alexey Voinov <voins@altlinux.ru> 2.3.3-alt1
- new version(2.3.3)

* Wed Oct 19 2005 Alexey Voinov <voins@altlinux.ru> 2.3.2-alt1
- new version(2.3.2)

* Tue Jan 11 2005 Alexey Voinov <voins@altlinux.ru> 2.3.1-alt1
- new version(2.3.1)
- buildreqs updated

* Thu Dec 16 2004 Alexey Voinov <voins@altlinux.ru> 2.3.0-alt1
- new version(2.3.0)

* Wed Aug 04 2004 Alexey Voinov <voins@altlinux.ru> 2.2.7-alt1
- new version(2.2.7)

* Tue Mar 09 2004 Alexey Voinov <voins@altlinux.ru> 2.2.6-alt1
- initial build

