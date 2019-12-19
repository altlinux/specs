Name: rastertokpsl-re
Version: 1.0.1422
Release: alt2

Summary: Reverse engineered Kyocera rastertokpsl filter

Group: System/Configuration/Printing
License: Apache-2.0
Url: https://github.com/sv99/rastertokpsl-re

Source: %name-%version.tar

BuildRequires: libcups-devel libjbig-devel

Requires: cups

%description
Reverse engineered Kyocera rastertokpsl filter

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%_libexecdir/cups/filter/%name
%_prefix/lib/cups/filter/rastertokpsl
%_datadir/cups/model/Kyocera/Kyocera_FS-1060DN.ppd

%changelog
* Thu Dec 19 2019 Paul Wolneykien <manowar@altlinux.org> 1.0.1422-alt2
- Initial release for Sisyphus.

* Tue Nov 05 2019 Paul Wolneykien <manowar@altlinux.org> 1.0.1422-alt1
- Test release.
