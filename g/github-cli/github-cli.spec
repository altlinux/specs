%global import_path github.com/cli/cli
Name:     github-cli
Version:  2.20.2
Release:  alt1

Summary:  GitHub's official command line tool
License:  MIT
Group:    Other
Url:      https://github.com/cli/cli

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
gh is GitHub on the command line. It brings pull requests, issues, and other
GitHub concepts to the terminal next to where you are already working with git
and your code.

%prep
%setup

%build
export GOFLAGS="${GOFLAGS-} -mod=vendor"
make GH_VERSION="v%version" bin/gh manpages
mkdir completions
bin/gh completion -s bash > completions/bash
bin/gh completion -s zsh > completions/zsh
bin/gh completion -s fish > completions/fish

%install
install -Dm 755 bin/gh %buildroot/%_bindir/gh
install -Dm644 completions/bash %buildroot/%_datadir/bash-completion/completions/gh
install -Dm644 completions/zsh %buildroot/%_datadir/zsh/site-functions/_gh
install -Dm644 completions/fish %buildroot/%_datadir/fish/vendor_completions.d/gh.fish
cp -a share/man -T %buildroot/%_mandir

%files
%_bindir/gh
%_datadir/bash-completion/completions/gh
%_datadir/zsh/site-functions/_gh
%_datadir/fish/vendor_completions.d/gh.fish
%_man1dir/*
%doc *.md

%changelog
* Tue Nov 15 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.20.2-alt1
- new version 2.20.2

* Fri Oct 28 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.18.1-alt1
- new version 2.18.1

* Mon Oct 03 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.16.1-alt1
- new version 2.16.1

* Fri Sep 09 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.15.0-alt1
- new version 2.15.0

* Tue Aug 16 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.14.4-alt1
- new version 2.14.4

* Mon Jul 18 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.14.2-alt1
- new version 2.14.2

* Wed Jun 22 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.12.1-alt1
- new version 2.12.1

* Thu May 12 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.10.1-alt1
- new version 2.10.1

* Thu May 05 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.9.0-alt1
- new version 2.9.0

* Fri Apr 15 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.8.0-alt1
- new version 2.8.0

* Thu Apr 07 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.7.0-alt1
- new version 2.7.0

* Wed Mar 16 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.6.0-alt1
- new version 2.6.0

* Tue Mar 15 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.5.2-alt1
- 2.5.2

* Sun Feb 20 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.5.1-alt1
- 2.5.1

* Tue Feb 15 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.5.0-alt1
- 2.5.0

* Mon Jan 17 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.4.0-alt1
- upate to 2.4.0

* Wed Oct 27 2021 Mikhail Gordeev <obirvalger@altlinux.org> 2.2.0-alt1
- upate to 2.2.0

* Fri Sep 24 2021 Mikhail Gordeev <obirvalger@altlinux.org> 2.0.0-alt1
- upate to 2.0.0

* Wed Feb 17 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.0-alt1
- update to 1.5.0

* Tue Dec 15 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.1-alt1
- update to 1.3.1

* Wed Dec 02 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.0-alt1
- update to 1.3.0

* Wed Oct 28 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt1
- update to 1.2.0

* Fri Sep 18 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
