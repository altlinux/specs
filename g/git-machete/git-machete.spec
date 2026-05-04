%define pypi_name git-machete

Name: %pypi_name
Version: 3.40.1
Release: alt1

Summary: Git repository organizer and rebase/merge workflow automation tool

License: MIT
Group: Development/Tools
URL: https://github.com/VirtusLab/git-machete

BuildArch: noarch
AutoProv: no

# Source-url: https://github.com/VirtusLab/git-machete/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
git-machete is a versatile tool for organizing your git repo, including:
- Automatic discovery of branch relations
- Neat, customizable status command
- Automatic traversal of branches, rebasing and pushing/pulling
- Semi-automatic update of branches to their parent branches

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# Remove completion and docs installed to site-packages
rm -rf %buildroot%python3_sitelibdir/completion
rm -rf %buildroot%python3_sitelibdir/docs

# Install completions from source
install -Dm644 completion/git-machete.completion.bash %buildroot%_datadir/bash-completion/completions/git-machete
install -Dm644 completion/git-machete.completion.zsh %buildroot%_datadir/zsh/site-functions/_git-machete
install -Dm644 completion/git-machete.fish %buildroot%_datadir/fish/vendor_completions.d/git-machete.fish

# Install man page from source
install -Dm644 docs/man/git-machete.1 %buildroot%_man1dir/git-machete.1

%files
%doc README.md
%_bindir/git-machete
%_man1dir/git-machete.1*
%_datadir/bash-completion/completions/git-machete
%_datadir/zsh/site-functions/_git-machete
%_datadir/fish/vendor_completions.d/git-machete.fish
%python3_sitelibdir/git_machete/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue May 05 2026 Vitaly Lipatov <lav@altlinux.ru> 3.40.1-alt1
- new version 3.40.1

* Fri Mar 06 2026 Vitaly Lipatov <lav@altlinux.ru> 3.39.0-alt1
- new version 3.39.0

* Sun Jan 05 2025 Vitaly Lipatov <lav@altlinux.ru> 3.38.0-alt1
- initial build for ALT Sisyphus
