%define _unpacakged_files_terminate_build 1

Name: baikal-openuds
Version: 0.0.3
Release: alt1
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
Workaround for xfreerdp with OpenUDS on Baikal-M. Must be installed on
a client machine.

%prep
%setup -q

%build
install -D xfreerdp %buildroot%_bindir/xfreerdp

%files
%_bindir/xfreerdp

%changelog
* Wed Nov 10 2021 Igor Chudov <nir@altlinux.org> 0.0.3-alt1
- Fixed logging errors

* Tue Nov 09 2021 Igor Chudov <nir@altlinux.org> 0.0.2-alt1
- Logging functionality added.

* Wed Oct 20 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.0.1-alt2
- Initial build

* Mon Oct 18 2021 Igor Chudov <nir@altlinux.org> 0.0.1-alt1
- Initial release

