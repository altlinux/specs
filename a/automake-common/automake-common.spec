Name: automake-common
Version: 0.4.2
Release: alt1

Summary: Wrapper and common files for different versions of the GNU Automake
License: GPLv2+
Group: Development/Other
BuildArch: noarch

Source: automake_wrapper
Source1: README

Conflicts: automake_1.6 < 1:1.6.3-alt2
Conflicts: automake_1.4 < 1:1.4-alt7.p5
Conflicts: automake < 1:1.4-alt7.p5

%description
This package contains files that provide co-existence of various
versions of the GNU Automake.

%install
install -pD -m644 %_sourcedir/README \
	%buildroot%_datadir/aclocal/README
install -pD -m755 %_sourcedir/automake_wrapper \
	%buildroot%_bindir/automake_wrapper
for n in aclocal automake; do
	ln -s automake_wrapper %buildroot%_bindir/$n
done

%files
%_bindir/*
%_datadir/aclocal/

%changelog
* Thu Dec 24 2020 Dmitry V. Levin <ldv@altlinux.org> 0.4.2-alt1
- Simplified automake_wrapper a bit.

* Wed Aug 08 2018 Dmitry V. Levin <ldv@altlinux.org> 0.4.1-alt1
- Cleaned up automake_wrapper.

* Mon Oct 28 2013 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt1
- Packaged /usr/share/aclocal/README.

* Tue Aug 25 2009 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Removed obsolete %%pre script and all its requirements.

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Rewritten %%pre script using new %%uninstall_info.
- Updated automake wrapper.

* Sun Oct 27 2002 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
