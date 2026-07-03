%global import_path github.com/cli/cli
Name:     github-cli
Version:  2.96.0
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
* Fri Jul 03 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.96.0-alt1
- new version 2.96.0

* Fri Jun 19 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.95.0-alt1
- new version 2.95.0

* Thu Jun 11 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.94.0-alt1
- new version 2.94.0

* Fri May 29 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.93.0-alt1
- new version 2.93.0

* Wed Apr 29 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.92.0-alt1
- new version 2.92.0

* Wed Apr 22 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.91.0-alt1
- new version 2.91.0

* Mon Apr 20 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.90.0-alt1
- new version 2.90.0

* Fri Mar 13 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.88.1-alt1
- new version 2.88.1

* Wed Mar 11 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.88.0-alt1
- new version 2.88.0

* Wed Feb 25 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.87.3-alt1
- new version 2.87.3

* Fri Feb 20 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.87.0-alt1
- new version 2.87.0

* Wed Jan 21 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.86.0-alt1
- new version 2.86.0

* Fri Jan 16 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.85.0-alt1
- new version 2.85.0

* Mon Dec 15 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.83.2-alt1
- new version 2.83.2

* Mon Nov 17 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.83.1-alt1
- new version 2.83.1

* Wed Nov 05 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.83.0-alt1
- new version 2.83.0

* Thu Oct 23 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.82.1-alt1
- new version 2.82.1

* Wed Sep 24 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.80.0-alt1
- new version 2.80.0

* Wed Sep 10 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.79.0-alt1
- new version 2.79.0

* Fri Aug 22 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.78.0-alt1
- new version 2.78.0

* Thu Jul 31 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.76.2-alt1
- new version 2.76.2

* Thu Jul 24 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.76.1-alt1
- new version 2.76.1

* Fri Jul 18 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.76.0-alt1
- new version 2.76.0

* Tue Jul 15 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.75.1-alt1
- new version 2.75.1

* Thu Jul 10 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.75.0-alt1
- new version 2.75.0

* Thu Jun 19 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.74.2-alt1
- new version 2.74.2

* Wed Jun 11 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.74.1-alt1
- new version 2.74.1

* Mon Jun 02 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.74.0-alt1
- new version 2.74.0

* Wed May 21 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.73.0-alt1
- new version 2.73.0

* Sun May 04 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.72.0-alt1
- new version 2.72.0

* Mon Apr 28 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.71.2-alt1
- new version 2.71.2

* Tue Apr 15 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.70.0-alt1
- new version 2.70.0

* Thu Mar 20 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.69.0-alt1
- new version 2.69.0

* Thu Mar 06 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.68.1-alt1
- new version 2.68.1

* Wed Feb 12 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.67.0-alt1
- new version 2.67.0

* Mon Feb 03 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.66.1-alt1
- new version 2.66.1

* Fri Jan 31 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.66.0-alt1
- new version 2.66.0

* Wed Jan 08 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.65.0-alt1
- new version 2.65.0

* Sun Dec 22 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.64.0-alt1
- new version 2.64.0

* Mon Dec 09 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.63.2-alt1
- new version 2.63.2

* Thu Nov 28 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.63.0-alt1
- new version 2.63.0

* Fri Nov 15 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.62.0-alt1
- new version 2.62.0

* Thu Nov 07 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.61.0-alt1
- new version 2.61.0

* Mon Oct 28 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.60.1-alt1
- new version 2.60.1

* Fri Oct 25 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.60.0-alt1
- new version 2.60.0

* Thu Oct 24 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.59.0-alt1
- new version 2.59.0

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
