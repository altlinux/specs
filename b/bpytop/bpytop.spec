%define _unpackaged_files_terminate_build 1

# To find all deps
%set_python3_req_method strict

Name: bpytop
Version: 1.0.68
Release: alt1
Summary: Linux resource monitor
BuildArch: noarch

License: Apache-2.0
Group: Monitoring
Url: https://github.com/aristocratos/bpytop

Packager: Anna Khrustova <khab@altlinux.org>
Source0: %url/archive/v%version/%name-%version.tar.gz

BuildRequires: rpm-build-python3

%description
Resource monitor that shows usage and stats for processor, memory, disks,
network and processes.

Python port of bashtop.


%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=/usr

%files
%_bindir/%name
%_datadir/%name/

%changelog
* Sat Oct 14 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 1.0.68-alt1
- Updated to upstream 1.0.68

* Thu Dec 17 2020 Anna Khrustova <khab@altlinux.org> 1.0.50-alt1
- Initial build for Sisyphus.
