%add_debuginfo_skiplist %_libexecdir/bun-bootstrap/*
%set_verify_elf_method relaxed
# The aarch64 binary names its interpreter as /usr/lib/ld-linux-aarch64.so.1,
# while ALT's glibc-core ships it as /lib/ld-linux-aarch64.so.1. The filter
# drops the unresolvable path require; the one for the file itself remains.
%filter_from_requires /^\/usr\/lib\/ld-linux-aarch64.*/d

Name: bun-bootstrap
Version: 1.4.2
Release: alt1

Summary: Prebuilt Bun runtime used to bootstrap the bun package
License: MIT
Group: Development/Other
Url: https://bun.sh/
Packager: Nazarov Denis <nenderus@altlinux.org>

# Prebuilt upstream binaries, build-time only. Bun cannot be built without an
# existing Bun: the code generation steps of its build use Bun.build and
# Bun.Transpiler, for which Node.js has no equivalent. So the first build of
# the bun package needs these. They are not installed on the runtime path and
# nothing links against them.
Source: https://github.com/oven-sh/bun/releases/download/bun-v%version/bun-linux-x64-baseline.zip
Source1: https://github.com/oven-sh/bun/releases/download/bun-v%version/bun-linux-aarch64.zip

# Upstream publishes Linux builds for x86_64 and aarch64 only.
ExclusiveArch: x86_64 aarch64

BuildRequires: unzip

%description
Prebuilt upstream Bun %version%, used only to bootstrap the build of the
bun package. It exists because Bun cannot be built without an existing Bun.

This package is not needed at run time and is not used by the bun package
installed on the system.

%prep
%setup -q -c -T
%ifarch x86_64
%__unzip -q %SOURCE0
%endif
%ifarch aarch64
%__unzip -q %SOURCE1
%endif

%install
%__mkdir_p %buildroot%_libexecdir/bun-bootstrap/bin
%__install -pm 0755 bun-linux-*/bun %buildroot%_libexecdir/bun-bootstrap/bin/bun

%check
%buildroot%_libexecdir/bun-bootstrap/bin/bun --version | grep -qx '%version'

%files
%_libexecdir/bun-bootstrap

%changelog
* Tue Sep 22 2026 Nazarov Denis <nenderus@altlinux.org> 1.4.2-alt1
- Initial build (prebuilt Bun for bootstrap)
