%define _unpacakged_files_terminate_build 1

Name: baikal-openuds
Version: 0.0.1
Release: alt2
License: %gpl2plus
Summary: Workaround for xfreerdp with OpenUDS on Baikal-M
Group: Other
Source0: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildRequires: rpm-build-python3
Requires: remmina
Requires: remmina-plugins-rdp
Conflicts: xfreerdp
Provides: freerdp

%description
Workaround for xfreerdp with OpenUDS on Baikal-M

%prep
%setup -q

%build
install -D xfreerdp %buildroot%_bindir/xfreerdp

%files
%_bindir/xfreerdp

%changelog
* Wed Oct 20 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.0.1-alt2
- Initial build

* Mon Oct 18 2021 Igor Chudov <nir@altlinux.org> 0.0.1-alt1
- Initial release

