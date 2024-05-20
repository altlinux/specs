%define _unpackaged_files_terminate_build 1
%def_with check

Name: casr
Version: 2.11.0
Release: alt1

Summary: Collect crash (or UndefinedBehaviorSanitizer error) reports, triage, and estimate severity.
License: Apache-2.0
Group: Development/Tools
Url: https://github.com/ispras/casr

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-rust
%if_with check
BuildRequires: java-devel-default
BuildRequires: python3-devel
BuildRequires: clang15.0
BuildRequires: llvm15.0
BuildRequires: gcc-c++
BuildRequires: /proc
BuildRequires: gdb
BuildRequires: npm
BuildRequires: gcc
%endif
Requires: gdb

%description
CASR is a set of tools that allows you to collect crash reports
in different ways. Use casr-core binary to deal with coredumps.
Use casr-san to analyze ASAN reports or casr-ubsan to analyze UBSAN reports.
Try casr-gdb to get reports from gdb. Use casr-python to analyze python reports
and get report from Atheris. Use casr-java to analyze java reports and
get report from Jazzer. Use casr-js to analyze JavaScript reports and
get report from Jazzer.js or jsfuzz.

%prep
%setup -a1

mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build -F dojo

%install
install -D -m755 target/release/casr-afl -t %buildroot%_bindir/
install -D -m755 target/release/casr-cluster -t %buildroot%_bindir/
install -D -m755 target/release/casr-dojo -t %buildroot%_bindir/
install -D -m755 target/release/casr-java -t %buildroot%_bindir/
install -D -m755 target/release/casr-libfuzzer -t %buildroot%_bindir/
install -D -m755 target/release/casr-san -t %buildroot%_bindir/
install -D -m755 target/release/casr-cli -t %buildroot%_bindir/
install -D -m755 target/release/casr-core -t %buildroot%_bindir/
install -D -m755 target/release/casr-gdb -t %buildroot%_bindir/
install -D -m755 target/release/casr-js -t %buildroot%_bindir/
install -D -m755 target/release/casr-python -t %buildroot%_bindir/
install -D -m755 target/release/casr-ubsan -t %buildroot%_bindir/

%check
# tweak hard-coded parts of tests
sed -i 's,"ret ","ret",' casr/tests/tests.rs
sed -i 's,"java-17-openjdk-amd64","java",' casr/tests/tests.rs

# Disable tests that require jsfuzz & jazzer.js
export SKIP_TESTS="$SKIP_TESTS --skip test_casr_js_jazzer \
    --skip test_casr_js_jsfuzz \
    --skip test_casr_js_native_jazzer \
    --skip test_casr_js_native_jsfuzz \
    --skip test_casr_libfuzzer_jazzer_js \
    --skip test_casr_libfuzzer_jazzer_js_xml2js \
    --skip test_casr_libfuzzer_jsfuzz"

# Disable tests that require unpackaged python3-module-atheris
export SKIP_TESTS="$SKIP_TESTS --skip test_casr_python_atheris \
    --skip test_casr_python_call_san_df \
    --skip test_casr_san_python_df \
    --skip test_casr_san_atheris_df \
    --skip test_casr_libfuzzer_atheris"

# Disable tests that require unpackaged node bindings
export SKIP_TESTS="$SKIP_TESTS --skip test_casr_js_native"

# Disable tests that require rust nightly toolchain
export SKIP_TESTS="$SKIP_TESTS --skip test_casr_san_rust_panic"

# Disable tests that require libclang_rt
export SKIP_TESTS="$SKIP_TESTS --skip test_casr_java"

# Disable unstable tests
export SKIP_TESTS="$SKIP_TESTS --skip test_js_stacktrace \
    --skip test_casr_afl \
    --skip test_casr_cluster_c \
    --skip test_casr_cluser_u"

# Disalble tests due to errors of running gdb on 32-bit files in hasher
export SKIP_TESTS="$SKIP_TESTS --skip gdb32"

%ifarch ppc64le
export SKIP_TESTS="$SKIP_TESTS --skip test_abort \
    --skip test_bad_instruction \
    --skip test_call_av_tainted \
    --skip test_dest_av \
    --skip test_dest_av_near_null \
    --skip test_dest_av_tainted \
    --skip test_segfault_on_pc \
    --skip test_source_av \
    --skip test_source_av_near_null"
%endif

%rust_test -- $SKIP_TESTS

%files
%doc docs/*
%_bindir/*

%changelog
* Mon Apr 08 2024 Alexander Kuznetsov <kuznetsovam@altlinux.org> 2.11.0-alt1
- Initial build.
