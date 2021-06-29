%define openfprintdlibdir %_libexecdir/open-fprintd

Name: open-fprintd
Version: 0.6
Release: alt0.2
Group: System/Servers
Summary: Replacement of package fprintd for standalone backend services

License: GPLv2
Url: https://github.com/uunicorn/%name
Source0: https://github.com/uunicorn/open-fprintd/archive/refs/tags/0.6.tar.gz#/%name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

Requires: python3-module-%name = %EVR

# as we mimic fprintd behaviour
Conflicts: fprintd

%package -n python3-module-%name
Group: Development/Python
Summary: Python3 modules for %name

%description
Replacement of package fprintd which allows you to have your own backend as a
standalone service.


%description -n python3-module-%name
Python3 modules for %name

%prep
%setup
%patch

%build
%python3_build

%install
%python3_install

mkdir -p %buildroot/%_unitdir
install -m 0644 debian/open-fprintd.service %buildroot/%_unitdir/
install -m 0644 debian/open-fprintd-suspend.service %buildroot/%_unitdir/
install -m 0644 debian/open-fprintd-resume.service %buildroot/%_unitdir/

%files
%doc README.md COPYING
%dir %openfprintdlibdir
%openfprintdlibdir/open-fprintd
%openfprintdlibdir/suspend.py
%openfprintdlibdir/resume.py
%_unitdir/%{name}*.service
%_datadir/dbus-1/system-services/net.reactivated.Fprint.service
%_datadir/dbus-1/system.d/net.reactivated.Fprint.conf

%files -n python3-module-%name
%python3_sitelibdir/openfprintd/
%python3_sitelibdir/open_fprintd-%version-py*.egg-info/

%changelog
* Tue Jun 29 2021 L.A. Kostis <lakostis@altlinux.ru> 0.6-alt0.2
- Fix unowned dirs.

* Tue Jun 29 2021 L.A. Kostis <lakostis@altlinux.ru> 0.6-alt0.1
- Rebuild for ALTLinux.
- Adopt .spec from Fedora.

* Wed Jun 16 2021 Arkady L. Shane <ashejn@gmail.com> - 0.12-2
- skip possible transaction errors

* Tue Nov 03 2020 Veit Wahlich <cru@zodia.de> - 0.6-1
- Initial build.
