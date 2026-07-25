%global import_path github.com/vmware-tanzu/velero-plugin-for-aws

Name:     velero-plugin-for-aws
Version:  1.14.2
Release:  alt1

Summary:  Velero plugins for AWS (S3 object storage and EBS volume snapshots)
License:  Apache-2.0
Group:    Archiving/Backup
Url:      https://github.com/velero-io/velero-plugin-for-aws

ExclusiveArch: %go_arches
Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
Requires: velero >= 1.18

%description
Velero plugins to support running Velero on AWS: an object store plugin
for persisting and retrieving backups in AWS S3 and a volume snapshotter
plugin for creating snapshots from EBS volumes.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

pushd $BUILDDIR/src/%import_path
%golang_build ./velero-plugin-for-aws
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md
%doc LICENSE

%changelog
* Wed Jul 22 2026 Nikolay Burykin <bne@altlinux.org> 1.14.2-alt1
- Initial build for Sisyphus
