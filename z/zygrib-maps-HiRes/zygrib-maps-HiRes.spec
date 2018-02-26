Name: zygrib-maps-HiRes
Version: 2.4
Release: alt1

Summary: Higher resolution maps for ZYGrib

License: %gpl3plus
Group: Networking/Other
Url: http://www.zygrib.org
Source0: zyGrib_maps%{version}.tgz
BuildArch: noarch

Requires: zygrib-data

BuildRequires: rpm-build-licenses

%description
This package contain higher resolution maps (200 m and 100 m)
for ZYGrib (warning: size of package about 74Mb)

%prep

%build

%install

%__mkdir_p %{buildroot}%{_datadir}/zyGrib

# README excluded because it is contained in the package zygrib-data
tar xzf %{SOURCE0} -C %{buildroot}%{_datadir}/zyGrib --exclude=README.*

%files
%{_datadir}/zyGrib/data/*

%changelog
* Sun Nov 13 2011 Sergey Y. Afonin <asy@altlinux.ru> 2.4-alt1
- Initial build for AltLinux
