# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: sipcalc
Version: 1.1.6
Release: alt1

Summary: Advanced console-based ip subnet calculator
License: BSD-3-Clause
Group: Networking/Other
Url: http://www.routemeister.net/projects/sipcalc/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
Sipcalc is an advanced console-based IP subnet calculator. It can take
multiple forms of input (IPv4/IPv6/interface/hostname) and output a multitude
of information about a given subnet.

%prep
%setup
%patch -p1

%build
%configure
%make_build --silent

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%_bindir/*
%_man1dir/*

%changelog
* Sun Mar 12 2023 Arseny Maslennikov <arseny@altlinux.org> 1.1.6-alt1
- 1.1.5 -> 1.1.6.

* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.5-alt2
- NMU: Fix license.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Jul 20 2009 Artem Zolochevskiy <azol@altlinux.ru> 1.1.5-alt1
- update to 1.1.5

* Mon Jul 20 2009 Artem Zolochevskiy <azol@altlinux.ru> 1.1.4-alt2
- fix FTBFS with GCC 4.4 (thx raorn@)

* Sun Oct 19 2008 Artem Zolochevskiy <azol@altlinux.ru> 1.1.4-alt1
- initial build for Sisyphus
