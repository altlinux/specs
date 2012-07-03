Name: groupdel-cvsadmin
Version: 0.1
Release: alt1

Summary: Remove cvsadmin group
License: GPLv2+
Group: Development/Other
BuildArch: noarch

%description
This package removes cvsadmin group during install.

%pre
[ -d /.host -a ! -r /.host ] || {
	echo >&2 '%name: Cowardly refusing to change things in a real system.'
	exit 1
}
groupdel cvsadmin ||:

%files

%changelog
* Sun Jun 07 2009 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
