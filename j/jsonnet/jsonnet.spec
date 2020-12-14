Name:     jsonnet
Version:  0.17.0
Release:  alt1

Summary:  Jsonnet - The data templating language
License:  Apache-2.0
Group:    Other
Url:      https://github.com/google/jsonnet

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires: gcc-c++

%description
%summary

%prep
%setup

%build
%make_build

%install
install -Dpm 755 %name %buildroot/%_bindir/%name
install -Dpm 755 %{name}fmt %buildroot/%_bindir/%{name}fmt

%check
make test

%files
%_bindir/*
%doc *.md examples

%changelog
* Tue Dec 15 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Wed Oct 28 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Tue Mar 31 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Wed Jul 24 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.0-alt1
- Initial build for Sisyphus
