%define _unpackaged_files_terminate_build 1

%define ktype mainline

Name: kernel-%ktype
Version: 1
Release: alt1
Summary: Bring the latest %ktype kernel
Group: Development/Kernel
License: CC0
Buildarch: noarch

BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-image-%{expand:%%kernel_%ktype}

%define get_kernel_name %(set -x; rpm -qa 'kernel-image-*' --qf '%%{NAME}')
%define get_strict_dep() %(set -x; rpm --qf '%%{NAME} %1 %%|epoch?{%%{epoch}:}|%%{version}-%%{release}%%|disttag?{:%%{disttag}}|' -q %2 || echo 'kernel = unknown')

Requires: %{get_strict_dep = %get_kernel_name}
Conflicts: %{get_strict_dep < %get_kernel_name}

%description
This will bring and keep a single %ktype kernel.

%files

%changelog
* Tue Dec 03 2024 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- Experimental build for mainline.
