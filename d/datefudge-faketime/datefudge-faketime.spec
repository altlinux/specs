Name: datefudge-faketime
Version: 0.2
Release: alt1
Summary: datefudge-like wrapper for faketime
License: %gpl3plus
Group: Development/Other
Source0: datefudge.in
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

Requires: faketime
# This script was writen based on datefudge-1.21
Provides: datefudge = 1.21
Obsoletes: datefudge <= 1.12-alt2

%description
This package contains wrapper for faketime utility for compatibility
with datefudge.

%build
sed 's/@VERSION@/%version/' %SOURCE0 >datefudge

%install
install -Dm0755 datefudge %buildroot/%_bindir/datefudge

%files
%_bindir/datefudge

%changelog
* Tue Jan 10 2017 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- Add Provides/Obsoletes datefudge.
- Fix for date string with spaces.

* Thu Jun 30 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build.

