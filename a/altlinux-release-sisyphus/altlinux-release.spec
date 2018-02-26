%ifndef distro
%define distro Sisyphus
%endif
%ifndef timestamp
%define timestamp 20081222
%endif
%ifndef dtext
%define dtext %distribution %distro
%endif
%ifndef text_summary
%define text_summary %dtext
%endif
%ifndef text_descr
%define text_descr %dtext
%endif
%ifndef text_file
%define text_file %dtext (%timestamp)
%endif
%ifndef provide_list
%define provide_list altlinux fedora redhat system
%endif
%ifndef obsolete_list
%define obsolete_list altlinux-4.0 altlinux-release altlinux-release-4.0 altlinux-release-4.1 altlinux-release-5.0 altlinux-release-chainmail altlinux-release-desktop altlinux-release-homeros altlinux-release-hpc altlinux-release-junior altlinux-release-master altlinux-release-office-server altlinux-release-school-server altlinux-release-server altlinux-release-skif altlinux-release-small_business altlinux-release-terminal fedora-release redhat-release
%endif

Name: altlinux-release-sisyphus
Version: %timestamp
Release: alt1

Summary: %text_summary release file
Copyright: GPL
Group: System/Configuration/Other
BuildArch: noarch
Packager: Dmitry V. Levin <ldv@altlinux.org>

Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done)
Obsoletes: %obsolete_list

%description
%text_descr release file.

%install
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name
echo "%text_file" >%buildroot%_sysconfdir/altlinux-release
for n in fedora redhat system; do
	ln -s altlinux-release %buildroot%_sysconfdir/$n-release
done

%files
%_sysconfdir/*-*
%_sysconfdir/buildreqs/packages/ignore.d/*

%changelog
* Mon Dec 22 2008 Dmitry V. Levin <ldv@altlinux.org> 20081222-alt1
- Updated Obsoletes list.

* Thu Dec 20 2007 Dmitry V. Levin <ldv@altlinux.org> 20071221-alt1
- Updated Obsoletes list.

* Thu Dec 06 2007 Dmitry V. Levin <ldv@altlinux.org> 20071206-alt1
- Updated Provides/Obsoletes lists and /etc/*-release symlinks.
- Renamed from altlinux-release to altlinux-release-sisyphus.

* Fri Feb 14 2003 Dmitry V. Levin <ldv@altlinux.org> Sisyphus-alt20030214
- Enhanced %%ifdef logic.

* Tue Dec 31 2002 Dmitry V. Levin <ldv@altlinux.org> Sisyphus-alt20021231
- Implemented %%ifdef logic.

* Wed Aug 14 2002 Dmitry V. Levin <ldv@altlinux.org> Sisyphus-alt20020814
- Added %_sysconfdir/buildreqs/packages/ignore.d/%name.

* Mon Apr 23 2001 Dmitry V. Levin <ldv@altlinux.ru> Sisyphus-alt20010423
- Renamed to altlinux-release.

* Thu Jan 10 2001 Dmitry V. Levin <ldv@fandra.org> 7.2-ipl0.20010111
- Renamed to %name.
- Implemented autoversioning.

* Wed Dec 27 2000 Dmitry V. Levin <ldv@fandra.org> 7.2-ipl0.20001227
- Set 8-digit timestamp number.

* Tue Dec 26 2000 AEN <aen@logic.ru>
- adopted for sisyphus

* Thu Oct  5 2000 Warly <warly@mandrakesoft.com> 7.2-1mdk
- Odyssey
