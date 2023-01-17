Name:    tldr
Version: 3.1.0
Release: alt1

Summary: Python command-line client for tldr pages
License: MIT
Group:   Documentation
URL:     https://github.com/tldr-pages/tldr-python-client

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-sphinx-argparse python3-module-sphinx
BuildRequires: python3-module-termcolor python3-module-colorama
BuildRequires: python3-module-shtab

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary.

%prep
%setup

%build
# First make docs or else error
make SPHINXBUILD="sphinx-build-3" -C docs
%pyproject_build
%__python3 tldr.py --print-completion bash > tldr.bash
%__python3 tldr.py --print-completion zsh > tldr.zsh

%install
%pyproject_install
install -Dpm644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dpm644 %name.zsh %buildroot%_datadir/zsh/site-functions/_%name

%check
%tox_create_default_config
%tox_check_pyproject -- -k 'not test_error_message' -v

%files
%_bindir/%name
%python3_sitelibdir/%name.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%name-%version.dist-info
%doc README.md
%_man1dir/tldr.1*
%dir %_datadir/bash-completion
%dir %_datadir/bash-completion/completions
%_datadir/bash-completion/completions/%name
%dir %_datadir/zsh
%dir %_datadir/zsh/site-functions
%_datadir/zsh/site-functions/_%name

%changelog
* Mon Dec 26 2022 Alexander Stepchenko <geochip@altlinux.org> 3.1.0-alt1
- Initial build for ALT.
