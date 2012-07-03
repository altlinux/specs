Name: libnoch
Version: 0.4.1
Release: alt1

Summary: Stab wrappers for chmod and chown calls
License: GPL
Group: System/Libraries

Source0: noch.c
Source1: chtest.c

%description
Stab wrappers for *chmod and *chown calls.

%prep
%setup -qcT
install -pm644 %SOURCE0 %SOURCE1 .

%build
readelf -Ws /%_lib/libc.so.6 | awk '
$4 == "FUNC" && $6 == "DEFAULT" && $8 ~ /@@/ {
	sym=$8;
	name=gensub("@@.*", "", 1, sym);
	vers=gensub("^[^@]*@@", "", 1, sym);
	printf("#define %%s_vers \"%%s\"\n", name, vers);
}' >vers.h
gcc %optflags %optflags_shared noch.c -ldl -shared -o libnoch.so
gcc %optflags chtest.c -o chtest
LD_PRELOAD=./libnoch.so ./chtest

%install
install -pDm755 libnoch.so %buildroot%_libdir/libnoch.so

%files
%_libdir/libnoch.so

%changelog
* Mon Feb 07 2011 Dmitry V. Levin <ldv@altlinux.org> 0.4.1-alt1
- Specfile cleanup.

* Mon Feb 14 2005 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt1
- Wrap functions using default versioning.

* Thu Feb 10 2005 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Fixed multilib (closes #6035).

* Fri Nov 07 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Build the shared library with -fPIC.

* Tue Jan 14 2003 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt1
- Initial release.
