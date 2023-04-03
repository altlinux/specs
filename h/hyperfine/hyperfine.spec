Name:     hyperfine
Version:  1.16.1
Release:  alt1

Summary:  A command-line benchmarking tool
License:  Apache-2.0
Group:    Development/Tools
Url:      https://github.com/sharkdp/hyperfine

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
%summary

%prep
%setup
%patch -p1

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/*
%doc *.md

%changelog
* Mon Apr 03 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.16.1-alt1
- new version 1.16.1

* Wed Mar 15 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.16.0-alt1
- new version 1.16.0

* Fri Oct 28 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.15.0-alt1
- new version 1.15.0

* Wed May 25 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.14.0-alt1
- new version 1.14.0

* Tue Mar 15 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.13.0-alt1
- new version 1.13.0

* Wed Oct 27 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.12.0-alt1
- new version 1.12.0

* Tue Aug 03 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.0-alt4
- Remove ExclusiveArch

* Wed Jun 23 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.0-alt3
- Use rpm-build-rust macros

* Tue Jan 19 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.0-alt2
- Add generation of debuginfo

* Mon Nov 09 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.0-alt1
- Initial build for Sisyphus
