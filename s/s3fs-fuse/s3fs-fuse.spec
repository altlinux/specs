Name:     s3fs-fuse
Version:  1.91
Release:  alt1

Summary:  FUSE-based file system backed by Amazon S3

License:  GPL-2.0
Group:    System/Kernel and hardware
Url:      https://github.com/s3fs-fuse/s3fs-fuse

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires: gcc-c++ make
BuildRequires: libfuse-devel
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
BuildRequires: libssl-devel

Conflicts: s3fs
Obsoletes: s3fs

%description
s3fs is a FUSE file system that allows you to mount an Amazon S3 bucket as a
local file system. It stores files natively and transparently in S3 (i.e.,
you can use other programs to access the same files). Maximum file size is
5 TB when using multipart upload.

s3fs is stable and is being used in number of production environments, e.g.,
rsync backup to s3.

%prep
%setup

%build
./autogen.sh
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README.md ChangeLog
%_bindir/*
%_man1dir/*.1.xz

%changelog
* Wed Mar 30 2022 Grigory Ustinov <grenka@altlinux.org> 1.91-alt1
- Automatically updated to 1.91.

* Sat Oct 16 2021 Grigory Ustinov <grenka@altlinux.org> 1.90-alt1
- Initial build for Sisyphus.
