Name: autoconf-common
Version: 0.3.2
Release: alt1

Summary: Wrapper and common files for different versions of the GNU Autoconf
License: GPLv2+
Group: Development/Other
Url: http://git.altlinux.org/gears/a/autoconf-common.git
BuildArch: noarch

Source: autoconf_wrapper

Conflicts: autoconf_2.5 < 2:2.54-alt2
Conflicts: autoconf_2.13 < 2:2.13-alt8
Conflicts: autoconf < 2:2.13-alt8

%description
This package contains files that provide co-existence of various
versions of the GNU Autoconf.

%install
install -pD -m755 %_sourcedir/autoconf_wrapper \
	%buildroot%_bindir/autoconf_wrapper
for n in autoconf autoheader autom4te autoreconf autoscan autoupdate ifnames; do
	ln -s autoconf_wrapper %buildroot%_bindir/$n
done

%files
%_bindir/*

%changelog
* Thu Dec 24 2020 Dmitry V. Levin <ldv@altlinux.org> 0.3.2-alt1
- Simplified autoconf_wrapper a bit.

* Sat Aug 04 2018 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt1
- Cleaned up autoconf_wrapper.

* Tue Aug 25 2009 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Removed obsolete %%pre script and all its requirements.

* Fri Oct 17 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Rewritten %%pre script using new %%uninstall_info.
- Updated autoconf wrapper.

* Sun Oct 27 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
