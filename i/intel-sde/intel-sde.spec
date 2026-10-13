%define _unpackaged_files_terminate_build 1
%define debug_package %{nil}

Name: intel-sde
Version: 10.13.1
Release: alt1

Summary: Intel Software Development Emulator
License: Intel-Simplified-Software-License
Group: Development/Debuggers
Url: https://www.intel.com/content/www/us/en/developer/articles/tool/software-development-emulator.html
ExclusiveArch: x86_64

Source: %name-%version.tar

# The vendor kit contains private Intel Pin libraries and 32-bit ELFs.
# Do not generate RPM requirements/provides from these bundled objects.
AutoReqProv: no
Requires: glibc
Requires: libstdc++6

# Preserve signed, prebuilt Intel ELF files and their private runtime.
%global kitdir %_libdir/intel-sde/%version
%brp_strip_none %_libdir/intel-sde/*
%set_verify_elf_method none

%description
Intel Software Development Emulator (Intel SDE) is a dynamic binary
instrumentation tool and instruction set emulator for Intel x86 CPUs.
It permits testing software that uses instructions unsupported by the
host processor, including AVX-512, AVX10 and APX.

This package contains the original Intel SDE binary kit, Intel Pin
runtime, Intel XED tools, development files, documentation and license
notices. The vendor directory layout is preserved below
/usr/lib64/intel-sde to allow the tools to find their private files.
Only the 64-bit entry points are exported to the system PATH.

%prep
%setup -q

%install
install -d -m 0755 %buildroot%kitdir

# Preserve Intel's relative layout; do not copy gear metadata.
cp -a Licenses README.txt doc ia32 intel64 misc pinkit \
    pin pin.sig sde sde.sig sde64 sde64.sig \
    xed xed.sig xed64 xed64.sig %buildroot%kitdir/

install -d -m 0755 %buildroot%_bindir

cat > %buildroot%_bindir/intel-sde <<'EOF'
#!/bin/sh
exec %kitdir/sde64 "$@"
EOF

cat > %buildroot%_bindir/intel-xed <<'EOF'
#!/bin/sh
exec %kitdir/xed64 "$@"
EOF

chmod 0755 %buildroot%_bindir/intel-sde %buildroot%_bindir/intel-xed
ln -s intel-sde %buildroot%_bindir/sde64
ln -s intel-xed %buildroot%_bindir/xed64

%check
# RPM postprocessing runs later; this checks the install stage only.
for file in pin pin.sig sde sde.sig sde64 sde64.sig \
            xed xed.sig xed64 xed64.sig README.txt; do
    cmp "$file" "%buildroot%kitdir/$file" || exit 1
done

for dir in Licenses doc ia32 intel64 misc pinkit; do
    test -d "%buildroot%kitdir/$dir" || exit 1
done

test -L %buildroot%kitdir/intel64/pinrt/pin.ld.so
test -L %buildroot%kitdir/ia32/pinrt/pin.ld.so
test -x %buildroot%kitdir/sde64
test -x %buildroot%kitdir/xed64
sh -n %buildroot%_bindir/intel-sde
sh -n %buildroot%_bindir/intel-xed
test "$(readlink %buildroot%_bindir/sde64)" = intel-sde
test "$(readlink %buildroot%_bindir/xed64)" = intel-xed

%files
%dir %_libdir/intel-sde
%kitdir
%_bindir/intel-sde
%_bindir/intel-xed
%_bindir/sde64
%_bindir/xed64

%changelog
* Tue Oct 13 2026 Timofei Fedotov <sovtouch@altlinux.org> 10.13.1-alt1
- Initial build for ALT Sisyphus.
