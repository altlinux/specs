Name: gnu-config
Version: 2023.01.21
Release: alt1

Summary: GNU config.guess and config.sub files
License: GPLv2+
Group: Development/Other
Url: https://www.gnu.org/software/config/
Vcs: https://git.savannah.gnu.org/cgit/config.git
BuildArch: noarch

# git://git.altlinux.org/gears/g/gnu-config.git
Source: %name-%version-%release.tar

Conflicts: autoconf < 2:2.69-alt5

%description
This packages contains a recent revision of GNU config.guess and
config.sub files.

%prep
%setup -n %name-%version-%release

%install
mkdir -p %buildroot{%_datadir/%name,%_man1dir}
install -pm755 config.guess config.sub %buildroot%_datadir/%name/
install -pm644 doc/config.guess.1 doc/config.sub.1 %buildroot%_man1dir/
%add_findreq_skiplist %_datadir/%name/config.guess
%define _unpackaged_files_terminate_build 1

%check
%make_build -k check

%files
%_datadir/%name/
%_man1dir/*.1*

%changelog
* Sat Jan 21 2023 Dmitry V. Levin <ldv@altlinux.org> 2023.01.21-alt1
- 2022.08.01 -> 2023.01.21.

* Mon Aug 01 2022 Dmitry V. Levin <ldv@altlinux.org> 2022.08.01-alt1
- 2022.05.08 -> 2022.08.01.

* Sun May 08 2022 Dmitry V. Levin <ldv@altlinux.org> 2022.05.08-alt1
- 2022.01.04 -> 2022.05.08.

* Tue Jan 04 2022 Dmitry V. Levin <ldv@altlinux.org> 2022.01.04-alt1
- 2021.12.25 -> 2022.01.04.

* Sat Dec 25 2021 Dmitry V. Levin <ldv@altlinux.org> 2021.12.25-alt1
- 2021-06-03 -> 2021.12.25.

* Fri Jun 04 2021 Dmitry V. Levin <ldv@altlinux.org> 2021.06.03-alt1
- 2021-05-05 -> 2021-06-03.

* Wed May 05 2021 Dmitry V. Levin <ldv@altlinux.org> 2021.05.05-alt1
- 2021-03-10 -> 2021-05-05.

* Wed Mar 10 2021 Dmitry V. Levin <ldv@altlinux.org> 2021.03.10-alt1
- 2021-01-01 -> 2021-03-10.

* Fri Jan 01 2021 Dmitry V. Levin <ldv@altlinux.org> 2021.01.01-alt1
- release-1-0-971-gff53d91 -> gnu-config-2021-01-01.

* Sun Dec 20 2020 Dmitry V. Levin <ldv@altlinux.org> 1.0.971.ff53-alt1
- release-1-0-968-g888c8e3 -> release-1-0-971-gff53d91.
- Packaged manpages.

* Thu Nov 19 2020 Dmitry V. Levin <ldv@altlinux.org> 1.0.968.888c-alt1
- release-1-0-961-g1c43980 -> release-1-0-968-g888c8e3.

* Wed Oct 21 2020 Dmitry V. Levin <ldv@altlinux.org> 1.0.961.1c43-alt1
- release-1-0-895-g9e514cc -> release-1-0-961-g1c43980.

* Fri Dec 21 2018 Dmitry V. Levin <ldv@altlinux.org> 1.0.895.9e51-alt1
- release-1-0-733-g4d34a6a -> release-1-0-895-g9e514cc.

* Mon Mar 20 2017 Dmitry V. Levin <ldv@altlinux.org> 1.0.733.4d3-alt1
- release-1-0-690-g869aecc -> release-1-0-733-g4d34a6a.

* Sun Sep 13 2015 Dmitry V. Levin <ldv@altlinux.org> 1.0.690.869a-alt1
- Updated to release-1-0-690-g869aecc.

* Wed Mar 04 2015 Dmitry V. Levin <ldv@altlinux.org> 1.0.678.9c71-alt1
- Updated to release-1-0-678-g9c71dc5.

* Wed Feb 19 2014 Dmitry V. Levin <ldv@altlinux.org> 1.0.655.6947a35-alt1
- Updated to release-1-0-655-g6947a35.

* Wed Jan 01 2014 Dmitry V. Levin <ldv@altlinux.org> 1.0.639.3bfabc1-alt1
- Updated to release-1-0-639-g3bfabc1.

* Sun Oct 27 2013 Dmitry V. Levin <ldv@altlinux.org> 1.0.634.5e4de70-alt1
- Updated to release-1-0-634-g5e4de70.

* Mon Jun 03 2013 Dmitry V. Levin <ldv@altlinux.org> 1.0.626.20f0b7e-alt1
- Updated to release-1-0-626-g20f0b7e.

* Sun Apr 07 2013 Dmitry V. Levin <ldv@altlinux.org> 1.0.619.fd4dee4-alt1
- Updated to release-1-0-619-gfd4dee4.

* Mon Aug 20 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0.603.062587e-alt1
- Updated to release-1-0-603-g062587e.

* Fri Aug 17 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0.602.6f8e28f-alt1
- Built GNU config.git release-1-0-602-g6f8e28f for Sisyphus.
- config.sub: Added armh support as proposed by Sergey Bolshakov.
