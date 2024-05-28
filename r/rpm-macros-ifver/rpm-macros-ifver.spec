
%define destfile %_rpmmacrosdir/ifver

Name: rpm-macros-ifver
Version: 0.1
Release: alt1

Group: Development/Other
Summary: Macros for comparing versions
Url: http://www.altlinux.org/
License: ALT-Public-Domain

BuildArch: noarch

Source1: macros

%description -n rpm-macros-ifver
This package contains macros for comparing versions.

%install
mkdir -p %buildroot/`dirname %destfile`
install -m 0644 %SOURCE1 %buildroot/%destfile

%files -n rpm-macros-ifver
%destfile

%changelog
* Tue May 28 2024 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
