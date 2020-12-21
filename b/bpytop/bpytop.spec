Name: bpytop
Version: 1.0.50
Release: alt1
Summary: Linux resource monitor
BuildArch: noarch

License: Apache-2.0
Group: Monitoring
Url: https://github.com/aristocratos/bpytop

Packager: Anna Khrustova <khab@altlinux.org>
Source0: %url/archive/v%version/%name-%version.tar.gz

Patch0: bpytop-1.0.50-alt-explicit-imports.patch
BuildRequires: rpm-build-python3

%description
Resource monitor that shows usage and stats for processor, memory, disks,
network and processes.

Python port of bashtop.


%prep
%setup
%patch0 -p1

%build
%make_build

%install
%makeinstall_std PREFIX=/usr

%files
%_bindir/%name
%_datadir/%name/

%changelog
* Thu Dec 17 2020 Anna Khrustova <khab@altlinux.org> 1.0.50-alt1
- Initial build for Sisyphus.
