%define _unpackaged_files_terminate_build 1

%def_with check

Name: mkosi
Version: 26
Release: alt1

Summary: Build Bespoke OS Images
License: LGPL-2.1-or-later AND GPL-2.0-only AND PSF-2.0
Group: System/Base
BuildArch: noarch

Url: https://github.com/airtai/FastStream
VCS: https://github.com/systemd/mkosi
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

AutoProv: nopython3

BuildRequires: python3-module-setuptools
BuildRequires: rpm-macros-systemd
BuildRequires: pandoc

%if_with check
BuildRequires: python3-module-pytest
%endif

# Filter self-requires in subpackages
%filter_from_requires /python3(mkosi\./d
%filter_from_requires /python3(mkosi)/d

%description
A fancy wrapper around dnf --installroot, apt, pacman and zypper that generates
customized disk images with a number of bells and whistles.

%package initrd
Summary: Build initrds locally using mkosi
Group: System/Base
Requires: %name = %EVR

%description initrd
%summary.

%package addon
Summary: Build PE addons locally using mkosi
Group: System/Base
Requires: %name = %EVR

%description addon
%summary.

%prep
%setup
%patch0 -p1

%build
%pyproject_build

tools/make-man-page.sh

bin/mkosi completion bash >mkosi.bash
bin/mkosi completion fish >mkosi.fish
bin/mkosi completion zsh >mkosi.zsh

%install
%pyproject_install

# Move resources to /usr/share to honor sisyphus-check
mkdir -p %buildroot%_datadir/mkosi
mv %buildroot%python3_sitelibdir_noarch/mkosi/resources \
   %buildroot%_datadir/mkosi
ln -sf %_datadir/mkosi/resources \
   %buildroot%python3_sitelibdir_noarch/mkosi/resources

# Install man pages
install -Dm 644 -t %buildroot%_man1dir \
         ./mkosi/resources/man/mkosi.1 \
         ./mkosi/resources/man/mkosi-sandbox.1 \
         ./mkosi/resources/man/mkosi-initrd.1 \
         ./mkosi/resources/man/mkosi-addon.1
install -Dm 644 -t %buildroot%_man7dir \
         ./mkosi/resources/man/mkosi.news.7

# Install the kernel-install plugins
install -D kernel-install/50-mkosi.install \
        -t %buildroot%_kernel_installdir
mkdir -p %buildroot%_libexecdir/mkosi-initrd
mkdir -p %buildroot%_sysconfdir/mkosi-initrd

install -D kernel-install/51-mkosi-addon.install \
        -t %buildroot%_kernel_installdir
mkdir -p %buildroot%_libexecdir/mkosi-addon
mkdir -p %buildroot%_sysconfdir/mkosi-addon

# Install completions
install -Dm 644 mkosi.bash %buildroot/%_datadir/bash-completion/completions/mkosi
install -Dm 644 mkosi.fish %buildroot/%_datadir/fish/vendor_completions.d/mkosi.fish
install -Dm 644 mkosi.zsh %buildroot/%_datadir/zsh/site-functions/_mkosi

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.md
%doc LICENSES/GPL-2.0-only.txt LICENSES/LGPL-2.1-or-later.txt  LICENSES/PSF-2.0.txt
%_bindir/mkosi
%_bindir/mkosi-sandbox
%_datadir/mkosi
%_man1dir/mkosi.1*
%_man1dir/mkosi-sandbox.1*
%_man7dir/mkosi.news.7*
%python3_sitelibdir_noarch/%{pyproject_distinfo mkosi}
%python3_sitelibdir_noarch/mkosi

%_datadir/bash-completion/completions/mkosi
%_datadir/fish/vendor_completions.d/mkosi.fish
%_datadir/zsh/site-functions/_mkosi

%files initrd
%_bindir/mkosi-initrd
%_man1dir/mkosi-initrd.1*
%_kernel_installdir/50-mkosi.install
%ghost %dir %_libexecdir/mkosi-initrd
%ghost %dir %_sysconfdir/mkosi-initrd

%files addon
%_bindir/mkosi-addon
%_man1dir/mkosi-addon.1*
%_kernel_installdir/51-mkosi-addon.install
%ghost %dir %_libexecdir/mkosi-addon
%ghost %dir %_sysconfdir/mkosi-addon

%changelog
* Wed Apr 15 2026 Egor Ignatov <egori@altlinux.org> 26-alt1
- New version 26.

* Tue Apr 15 2025 Egor Ignatov <egori@altlinux.org> 25.3-alt1
- First build for ALT.
