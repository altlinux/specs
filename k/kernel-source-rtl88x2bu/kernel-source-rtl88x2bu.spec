%define module_name     rtl88x2bu
%define module_version  35809.20191129
%define git_rev         e1e98a4

Name: kernel-source-rtl88x2bu
Version: 5.8.7.1
Release: alt6.git%git_rev

Summary: Linux %module_name for Realtek DWA-182 Wireless AC Dual Band USB Adapter
URL: https://support.dlink.ca/ProductInfo.aspx?m=DWA-182
Group: Development/Kernel
License: GPL-2.0

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
BuildArch: noarch

# Original code from ftp://ftp.dlink.ca/PRODUCTS/DWA-182/DWA-182_REVD_DRIVERS_v5.8.7.1_LINUX.ZIP
# Fixes from https://github.com/cilynx/rtl88x2bu
Source: %name-%version.tar

BuildRequires(pre): rpm-build-kernel

%description
%{summary}.

%prep
%setup -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Thu Sep 14 2023 Andrey Cherepanov <cas@altlinux.org> 5.8.7.1-alt6.gite1e98a4
- Fixed build for kernel 6.5.2.

* Sat Apr 22 2023 Andrey Cherepanov <cas@altlinux.org> 5.8.7.1-alt5.gitc866ad2
- Fixed build for kernel 6.1.

* Sun Jan 23 2022 Andrey Cherepanov <cas@altlinux.org> 5.8.7.1-alt4.gite3339ad
- Upstream fix for kernel-5.15.

* Tue Apr 06 2021 Andrey Cherepanov <cas@altlinux.org> 5.8.7.1-alt3.gitaac7c35
- Fix build with kernel-5.12.

* Fri Mar 05 2021 Andrey Cherepanov <cas@altlinux.org> 5.8.7.1-alt2.gitba12c4f
- Set upstream source to https://github.com/cilynx/rtl88x2bu.
- Build from upstream commit.

* Sat Oct 24 2020 Andrey Cherepanov <cas@altlinux.org> 5.8.7.1-alt1
- Initial build for Sisyphus.
