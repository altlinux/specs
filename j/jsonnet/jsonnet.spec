Name:     jsonnet
Version:  0.20.0
Release:  alt2

Summary:  Jsonnet - The data templating language
License:  Apache-2.0
Group:    Other
Url:      https://github.com/google/jsonnet

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar
Patch1:   fix-build-ppc64le.patch
Patch3500: loongarch.patch

BuildRequires: gcc-c++
BuildRequires: python3

%description
%summary

%package -n lib%name
Summary:  Jsonnet library
Group: System/Libraries

%description -n lib%name
%summary

%package -n lib%name-devel
Summary:  Jsonnet development files
Group: Development/Other

%description -n lib%name-devel
%summary

%prep
%setup
%patch1 -p1
%patch3500 -p1

%build
%make_build

%install
mkdir -p %buildroot%_bindir
cp -p %name %{name}fmt -t %buildroot%_bindir
mkdir -p %buildroot%_libdir
cp -dp libjsonnet*.so* %buildroot%_libdir
mkdir -p %buildroot%_includedir
cp -p include/libjsonnet*.h %buildroot%_includedir

%check
make test

%files -n lib%name-devel
%_includedir/*
%_libdir/lib%{name}*.so

%files -n lib%name
%_libdir/lib%{name}*.so.*

%files
%_bindir/*
%doc *.md doc examples

%changelog
* Wed Aug 23 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.20.0-alt2
- Support LoongArch architecture (lp64d ABI).

* Mon Apr 24 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.20.0-alt1
- New version 0.20.0.

* Wed Mar 02 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.18.0-alt1
- new version 0.18.0
- add lib packages

* Tue Dec 15 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Wed Oct 28 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Tue Mar 31 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Wed Jul 24 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.0-alt1
- Initial build for Sisyphus
