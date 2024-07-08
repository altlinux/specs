%define soname 1
%define rocm_name rocm_smi

Name: rocm-smi-lib
Version: 6.1.2
Release: alt0.2
License: MIT
Summary: ROCm System Management Interface (ROCm SMI) Library
Url: https://github.com/ROCm/amdsmi
Group: System/Libraries

Source: %name-%version.tar
Patch: rocm-smi-alt-rocm-path.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++ rpm-build-python3 help2man

%description
The AMD System Management Interface Library, or AMD SMI library, is a C library
for Linux that provides a user space interface for applications to monitor and
control AMD devices.

%package -n rocm-smi
Summary: ROCm System Management Interface utility
Group: System/Configuration/Hardware
Requires: librocm-smi = %EVR

%description -n rocm-smi
rocm-smi application using librocm-smi library.

%package -n librocm-smi%soname
Summary: ROCm System Management Interface (ROCm SMI) Library
Group: System/Libraries
Provides: librocm-smi = %EVR

%description -n librocm-smi%soname
The AMD System Management Interface Library, or AMD SMI library, is a C library
for Linux that provides a user space interface for applications to monitor and
control AMD devices.

%package -n librocm-smi-devel
Summary: Development headers for %name
Group: Development/C

%description -n librocm-smi-devel
Development headers for %name.

%prep
%setup
%patch -p1

%build
%cmake \
	-DCMAKE_CXX_FLAGS="%optflags -Wno-error=return-type" \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_SHARED_LIBS=on \
	-DCMAKE_INSTALL_LIBDIR=%_lib
%cmake_build

%install
%cmake_install

mkdir -p %buildroot{%_logdir/%{rocm_name}_lib,%_sysconfdir/logrotate.d}
touch %buildroot%_logdir/%{rocm_name}_lib/ROCm-SMI-lib.log
cat > %buildroot%_sysconfdir/logrotate.d/%name.conf << EOF
%_logdir/%{rocm_name}_lib/ROCm-SMI-lib.log {
	hourly
	missingok
	notifempty
	rotate 4
	size 1M
	copytruncate
	dateext
	dateformat .%%Y-%%m-%%d_%%H:%%M:%%S
}
EOF
mkdir -p %buildroot%_man1dir
help2man -N --name "ROCm System Management Interface" --version-string="%version" \
	%buildroot%_prefix/libexec/%rocm_name/%rocm_name.py > %buildroot%_man1dir/rocm-smi.1

%files -n rocm-smi
%_bindir/rocm-smi
%_man1dir/rocm-smi.1.*
%prefix/libexec/%rocm_name
%_sysconfdir/logrotate.d/%name.conf
%dir %attr(0700,root,root) %_logdir/%{rocm_name}_lib
%ghost %_logdir/%{rocm_name}_lib/ROCm-SMI-lib.log

%files -n librocm-smi%soname
%_libdir/lib%{rocm_name}64.so.%{soname}*
%_libdir/liboam.so.%{soname}*

%files -n librocm-smi-devel
%doc %rocm_name/docs/ROCm_SMI_Manual.pdf
%_includedir/oam
%_includedir/%rocm_name
%_libdir/lib%{rocm_name}64.so
%_libdir/liboam.so
%_libdir/cmake/%rocm_name

%changelog
* Mon Jul 08 2024 L.A. Kostis <lakostis@altlinux.ru> 6.1.2-alt0.2
- .spec: fix -devel package deps.
- rocm-smi: added man page.

* Fri Jul 05 2024 L.A. Kostis <lakostis@altlinux.ru> 6.1.2-alt0.1
- Initial build for ALTLinux.

