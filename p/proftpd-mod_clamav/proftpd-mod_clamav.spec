Name:     proftpd-mod_clamav
Version:  0.14
Release:  alt3.f277f033

Summary:  Mod_Clamav for ProFTPd
License:  GPL-2.0
Group:    System/Servers
Url:      https://github.com/jbenden/mod_clamav

Source:   %name-%version.tar

BuildRequires: proftpd-devel

Provides: mod_clamav = %EVR
Obsoletes: mod_clamav < %EVR

Requires: proftpd

%description
%summary.

%prep
%setup

%build
prxs -c mod_clamav.c

%install
mkdir -p %buildroot%_libdir/proftpd
install -m 644 .libs/mod_clamav.so %buildroot%_libdir/proftpd

%files
%doc README.md
%_libdir/proftpd/mod_clamav.so

%changelog
* Wed Aug 14 2024 Anton Midyukov <antohami@altlinux.org> 0.14-alt3.f277f033
- Obsoletes: mod_clamav < %%EVR

* Wed Aug 14 2024 Anton Midyukov <antohami@altlinux.org> 0.14-alt2.f277f033
- new snapshot
- rename package to proftpd-mod_clamav
- fix License field
- drop Packager field

* Thu May 28 2020 Anton Midyukov <antohami@altlinux.org> 0.14-alt1.1e555d35
- Initial build
