Name: chimbabenchcl
Version: 1.2
Release: alt1

Summary: OpenCL benchmark for CPUs and GPUs

License: MIT
Group: System/Configuration/Hardware
Url: https://github.com/Shedou/ChimbaBenchCL
# Source-url: https://github.com/Shedou/ChimbaBenchCL/archive/refs/tags/CBCL_12.tar.gz
Source: %name-%version.tar
Patch0: chimbabenchcl-1.2-system-build.patch
Patch1: chimbabenchcl-1.2-executable-path.patch

BuildRequires: ocl-icd-devel opencl-headers

%description
ChimbaBenchCL measures CPU and GPU performance through OpenCL. It tests
memory bandwidth and latency, floating-point and integer arithmetic, and
image processing. Results are saved in the current directory.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%make_build CFLAGS="%optflags" LDFLAGS="%optflags"

%install
%makeinstall_std PREFIX=%_prefix

%check
./ChimbaBenchCL-Linux --help < /dev/null | grep -F 'ChimbaBenchCL v%version'

%files
%_bindir/ChimbaBenchCL-Linux
%doc LICENSE README.md ChangeLog.txt

%changelog
* Sun Nov 01 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- initial build for ALT Linux.
- drop explicit gcc and make build requirements.

