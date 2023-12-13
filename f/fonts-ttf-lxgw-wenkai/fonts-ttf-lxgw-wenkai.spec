Name: fonts-ttf-lxgw-wenkai
Version: 1.312
Release: alt1
Summary: An open-source Chinese font derived from Fontworks' Klee One
License: OFL-1.1
Group: System/Fonts/True type
Url: https://github.com/lxgw/LxgwWenKai
# Source-url: https://github.com/lxgw/LxgwWenKai/releases/download/v%version/lxgw-wenkai-v%version.tar.gz
Source: lxgw-wenkai-%version.tar
BuildArch: noarch

Requires(pre): fontconfig

BuildRequires: rpm-build-fonts

%description
%summary.

%prep
%setup -n lxgw-wenkai-%version

%build

%install
%ttf_fonts_install lxgw-wenkai

%files -f lxgw-wenkai.files

%changelog
* Wed Dec 13 2023 Anton Midyukov <antohami@altlinux.org> 1.312-alt1
- new version (1.312) with rpmgs script

* Mon Oct 16 2023 Anton Midyukov <antohami@altlinux.org> 1.311-alt1
- new version (1.311) with rpmgs script

* Mon Oct 16 2023 Anton Midyukov <antohami@altlinux.org> 1.300-alt1
- initial build
