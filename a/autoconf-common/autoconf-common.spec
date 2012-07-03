Name: autoconf-common
Version: 0.3
Release: alt1

Summary: Common files for different versions of autoconf
License: GPL
Group: Development/Other
Packager: Dmitry V. Levin <ldv@altlinux.org>
BuildArch: noarch

Source: autoconf_wrapper

Conflicts: autoconf_2.5 < 2:2.54-alt2
Conflicts: autoconf_2.13 < 2:2.13-alt8
Conflicts: autoconf < 2:2.13-alt8

%description
This package contains files shared by various versions of GNU autoconf.

%install
mkdir -p %buildroot%_bindir
install -pm755 %SOURCE0 %buildroot%_bindir/
for n in autoconf autoheader autom4te autoreconf autoscan autoupdate ifnames; do
	ln -s autoconf_wrapper %buildroot%_bindir/$n
done

%files
%_bindir/*

%changelog
* Tue Aug 25 2009 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Removed obsolete %%pre script and all its requirements.

* Fri Oct 17 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Rewritten %%pre script using new %%uninstall_info.
- Updated autoconf wrapper.

* Sun Oct 27 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
