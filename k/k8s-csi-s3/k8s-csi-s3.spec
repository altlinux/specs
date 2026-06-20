%global import_path github.com/yandex-cloud/k8s-csi-s3
Name:    k8s-csi-s3
Version: 0.43.5
Release: alt1

Summary: GeeseFS-based CSI for mounting S3 buckets as PersistentVolumes
License: Apache-2.0
Group:   Other
Url:     https://github.com/yandex-cloud/k8s-csi-s3

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
This is a Container Storage Interface (CSI) for S3 (or S3 compatible) storage.
This can dynamically allocate buckets and mount them via a fuse mount into any
container.

%prep
%setup -a 1

%build
%make_build

%install
install -Dpm 0755 _output/s3driver %buildroot%_bindir/s3driver

%files
%doc AUTHORS *.md
%_bindir/s3driver

%changelog
* Sat Jun 20 2026 Andrey Cherepanov <cas@altlinux.org> 0.43.5-alt1
- Initial build for Sisyphus.
