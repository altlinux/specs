%global import_path github.com/cli/cli
Name:     github-cli
Version:  2.57.0
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
* Wed Sep 18 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.57.0-alt1
- new version 2.57.0

* Tue Sep 10 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.56.0-alt1
- new version 2.56.0

* Tue Aug 20 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.55.0-alt1
- new version 2.55.0

* Fri Aug 02 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.54.0-alt1
- new version 2.54.0

* Mon Jul 22 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.53.0-alt1
- new version 2.53.0

* Tue Jun 25 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.52.0-alt1
- new version 2.52.0

* Thu Jun 13 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.51.0-alt1
- new version 2.51.0

* Thu May 30 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.50.0-alt1
- new version 2.50.0

* Tue May 14 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.49.2-alt1
- new version 2.49.2

* Mon May 13 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.49.1-alt1
- new version 2.49.1

* Thu May 02 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.49.0-alt1
- new version 2.49.0

* Wed Apr 17 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.48.0-alt1
- new version 2.48.0

* Thu Apr 04 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.47.0-alt1
- new version 2.47.0

* Thu Mar 21 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.46.0-alt1
- new version 2.46.0

* Tue Mar 05 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.45.0-alt1
- new version 2.45.0

* Mon Feb 19 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.44.1-alt1
- new version 2.44.1

* Fri Feb 16 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.44.0-alt1
- new version 2.44.0

* Thu Feb 01 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.43.1-alt1
- new version 2.43.1

* Mon Jan 22 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.42.1-alt1
- new version 2.42.1

* Mon Jan 15 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.42.0-alt1
- new version 2.42.0

* Fri Dec 15 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.40.1-alt1
- new version 2.40.1

* Sat Dec 09 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.40.0-alt1
- new version 2.40.0

* Tue Nov 28 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.39.2-alt1
- new version 2.39.2

* Wed Nov 15 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.39.1-alt1
- new version 2.39.1

* Tue Nov 14 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.39.0-alt1
- new version 2.39.0

* Thu Nov 02 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.38.0-alt1
- new version 2.38.0

* Sat Oct 28 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.37.0-alt1
- new version 2.37.0

* Tue Sep 19 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.35.0-alt1
- new version 2.35.0

* Thu Sep 07 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.34.0-alt1
- new version 2.34.0

* Tue Aug 22 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.33.0-alt1
- new version 2.33.0

* Tue Jul 25 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.32.1-alt1
- new version 2.32.1

* Mon Jul 17 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.32.0-alt1
- new version 2.32.0

* Wed Jun 21 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.31.0-alt1
- new version 2.31.0

* Wed May 31 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.30.0-alt1
- new version 2.30.0

* Wed May 10 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.29.0-alt1
- new version 2.29.0

* Tue Apr 25 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.28.0-alt1
- new version 2.28.0

* Mon Apr 17 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.27.0-alt1
- new version 2.27.0

* Sat Mar 25 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.25.1-alt1
- new version 2.25.1

* Fri Feb 17 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.23.0-alt1
- new version 2.23.0

* Wed Jan 11 2023 Mikhail Gordeev <obirvalger@altlinux.org> 2.21.2-alt1
- new version 2.21.2

* Fri Dec 23 2022 Mikhail Gordeev <obirvalger@altlinux.org> 2.21.1-alt1
- new version 2.21.1

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
