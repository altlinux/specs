%define module_name             %name
%define module_version          %version
%define module_release          %release

Name: dst
Version: 0.1
Release: alt2

Summary: Userspace program for DST.
License: GPL
Group: System/Kernel and hardware
URL: http://tservice.net.ru/~s0mbre/blog/devel/dst/
Packager: Boris Savelev <boris@altlinux.org>
ExclusiveOS: Linux
Source: %name-%version.tar.bz2
BuildRequires: rpm-build-kernel kernel-source-%module_name-%module_version

%description
DST is a block layer network device

%prep
rm -rf kernel-source-%module_name-%module_version
tar -jxvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup

%build
export CFLAGS="-I %_builddir/kernel-source-%module_name-%module_version"
%make_build

%install
%__install -d %buildroot%_sbindir
%__install -m 755 %name %buildroot%_sbindir

%files
%doc EXAMPLES
%_sbindir/%name

%changelog
* Thu Sep 25 2008 Boris Savelev <boris@altlinux.org> 0.1-alt2
- Warn if there is no security file during exporting node initialization.
- Bump default maximum amount of pages to 32: 31 is maximum number of pages from ext3 on common block device in single request.

* Tue Sep 02 2008 Boris Savelev <boris@altlinux.org> 0.1-alt1
- initial build for Sisyphus

