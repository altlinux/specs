%define soversion 2301.0.0

# about -DCMAKE_CXX_STANDARD=17 see https://github.com/desktop-app/tg_owt/pull/55#discussion_r599718405
# from tg_owt: HINT: System abseil should be built with -DCMAKE_CXX_STANDARD=20
%define cxx_standard 17

# Can't be build with packaged GTest: https://github.com/abseil/abseil-cpp/issues/1102
# And these tests are very long
%def_enable check

Name: libabseil-cpp%soversion
Version: 20230125.3
Release: alt4

Summary: C++ Common Libraries

License: Apache-2.0
Group: Development/C++
Url: https://abseil.io

# Source-url: https://github.com/abseil/abseil-cpp/archive/%version/abseil-cpp-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake ninja-build
BuildRequires: gcc-c++
BuildRequires: /proc

%if_enabled check
BuildRequires: libgtest-devel >= 1.13.0
BuildRequires: libgmock-devel ctest
%endif

# https://bugzilla.altlinux.org/42411
Conflicts: libclickhouse-cpp-devel <= 1.2.2-alt1

%description
Abseil is an open-source collection of C++ library code designed to augment
the C++ standard library. The Abseil library code is collected from
Google's own C++ code base, has been extensively tested and used in
production, and is the same code we depend on in our daily coding lives.

In some cases, Abseil provides pieces missing from the C++ standard; in
others, Abseil provides alternatives to the standard for special needs we've
found through usage in the Google code base. We denote those cases clearly
within the library code we provide you.

Abseil is not meant to be a competitor to the standard library; we've just
found that many of these utilities serve a purpose within our code base,
and we now want to provide those resources to the C++ community as a whole.


%package -n libabseil-cpp
Group: Development/C++
Summary: %summary

%description -n libabseil-cpp
Abseil is an open-source collection of C++ library code designed to augment
the C++ standard library. The Abseil library code is collected from
Google's own C++ code base, has been extensively tested and used in
production, and is the same code we depend on in our daily coding lives.

In some cases, Abseil provides pieces missing from the C++ standard; in
others, Abseil provides alternatives to the standard for special needs we've
found through usage in the Google code base. We denote those cases clearly
within the library code we provide you.

Abseil is not meant to be a competitor to the standard library; we've just
found that many of these utilities serve a purpose within our code base,
and we now want to provide those resources to the C++ community as a whole.


%prep
%setup
%ifarch %e2k
# unsupported option
sed -i "/-Wvarargs/d" absl/copts/{copts.py,GENERATED_{copts.bzl,AbseilCopts.cmake}}
# EDG frontend fails at this
sed -i "/static_assert(value.empty()/{N;d}" absl/strings/internal/string_constant.h
%endif

%build
%add_optflags -fPIC
%cmake \
    -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCMAKE_CXX_STANDARD:STRING=%cxx_standard \
    -DABSL_ENABLE_INSTALL:BOOL=ON \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
%if_enabled check
    -DABSL_BUILD_TESTING:BOOL=ON \
    -DABSL_BUILD_TEST_HELPERS:BOOL=ON \
    -DABSL_USE_EXTERNAL_GOOGLETEST:BOOL=ON \
    -DABSL_FIND_GOOGLETEST:BOOL=ON \
%endif
    -GNinja
%cmake_build

%install
%cmake_install


%files -n libabseil-cpp
%doc LICENSE
%doc FAQ.md README.md UPGRADES.md
%_libdir/libabsl_bad_any_cast_impl.so.%soversion
%_libdir/libabsl_bad_optional_access.so.%soversion
%_libdir/libabsl_bad_variant_access.so.%soversion
%_libdir/libabsl_base.so.%soversion
%_libdir/libabsl_city.so.%soversion
%_libdir/libabsl_civil_time.so.%soversion
%_libdir/libabsl_cord.so.%soversion
%_libdir/libabsl_cord_internal.so.%soversion
%_libdir/libabsl_cordz_functions.so.%soversion
%_libdir/libabsl_cordz_handle.so.%soversion
%_libdir/libabsl_cordz_info.so.%soversion
%_libdir/libabsl_cordz_sample_token.so.%soversion
%_libdir/libabsl_crc32c.so.%soversion
%_libdir/libabsl_crc_cord_state.so.%soversion
%_libdir/libabsl_crc_cpu_detect.so.%soversion
%_libdir/libabsl_crc_internal.so.%soversion
%_libdir/libabsl_debugging_internal.so.%soversion
%_libdir/libabsl_demangle_internal.so.%soversion
%_libdir/libabsl_die_if_null.so.%soversion
%_libdir/libabsl_examine_stack.so.%soversion
%_libdir/libabsl_exponential_biased.so.%soversion
%_libdir/libabsl_failure_signal_handler.so.%soversion
%_libdir/libabsl_flags.so.%soversion
%_libdir/libabsl_flags_commandlineflag.so.%soversion
%_libdir/libabsl_flags_commandlineflag_internal.so.%soversion
%_libdir/libabsl_flags_config.so.%soversion
%_libdir/libabsl_flags_internal.so.%soversion
%_libdir/libabsl_flags_marshalling.so.%soversion
%_libdir/libabsl_flags_parse.so.%soversion
%_libdir/libabsl_flags_private_handle_accessor.so.%soversion
%_libdir/libabsl_flags_program_name.so.%soversion
%_libdir/libabsl_flags_reflection.so.%soversion
%_libdir/libabsl_flags_usage.so.%soversion
%_libdir/libabsl_flags_usage_internal.so.%soversion
%_libdir/libabsl_graphcycles_internal.so.%soversion
%_libdir/libabsl_hash.so.%soversion
%_libdir/libabsl_hashtablez_sampler.so.%soversion
%_libdir/libabsl_int128.so.%soversion
%_libdir/libabsl_leak_check.so.%soversion
%_libdir/libabsl_log_entry.so.%soversion
%_libdir/libabsl_log_flags.so.%soversion
%_libdir/libabsl_log_globals.so.%soversion
%_libdir/libabsl_log_initialize.so.%soversion
%_libdir/libabsl_log_internal_check_op.so.%soversion
%_libdir/libabsl_log_internal_conditions.so.%soversion
%_libdir/libabsl_log_internal_format.so.%soversion
%_libdir/libabsl_log_internal_globals.so.%soversion
%_libdir/libabsl_log_internal_log_sink_set.so.%soversion
%_libdir/libabsl_log_internal_message.so.%soversion
%_libdir/libabsl_log_internal_nullguard.so.%soversion
%_libdir/libabsl_log_internal_proto.so.%soversion
%_libdir/libabsl_log_severity.so.%soversion
%_libdir/libabsl_log_sink.so.%soversion
%_libdir/libabsl_low_level_hash.so.%soversion
%_libdir/libabsl_malloc_internal.so.%soversion
%_libdir/libabsl_periodic_sampler.so.%soversion
%_libdir/libabsl_random_distributions.so.%soversion
%_libdir/libabsl_random_internal_distribution_test_util.so.%soversion
%_libdir/libabsl_random_internal_platform.so.%soversion
%_libdir/libabsl_random_internal_pool_urbg.so.%soversion
%_libdir/libabsl_random_internal_randen.so.%soversion
%_libdir/libabsl_random_internal_randen_hwaes.so.%soversion
%_libdir/libabsl_random_internal_randen_hwaes_impl.so.%soversion
%_libdir/libabsl_random_internal_randen_slow.so.%soversion
%_libdir/libabsl_random_internal_seed_material.so.%soversion
%_libdir/libabsl_random_seed_gen_exception.so.%soversion
%_libdir/libabsl_random_seed_sequences.so.%soversion
%_libdir/libabsl_raw_hash_set.so.%soversion
%_libdir/libabsl_raw_logging_internal.so.%soversion
%_libdir/libabsl_scoped_set_env.so.%soversion
%_libdir/libabsl_spinlock_wait.so.%soversion
%_libdir/libabsl_stacktrace.so.%soversion
%_libdir/libabsl_status.so.%soversion
%_libdir/libabsl_statusor.so.%soversion
%_libdir/libabsl_str_format_internal.so.%soversion
%_libdir/libabsl_strerror.so.%soversion
%_libdir/libabsl_strings.so.%soversion
%_libdir/libabsl_strings_internal.so.%soversion
%_libdir/libabsl_symbolize.so.%soversion
%_libdir/libabsl_synchronization.so.%soversion
%_libdir/libabsl_throw_delegate.so.%soversion
%_libdir/libabsl_time.so.%soversion
%_libdir/libabsl_time_zone.so.%soversion

%changelog
* Fri Aug 30 2024 Anton Farygin <rider@altlinux.ru> 20230125.3-alt4
- built as compat libraty without devel package

* Mon Dec 18 2023 Michael Shigorin <mike@altlinux.org> 20230125.3-alt3
- fix build with check disabled

* Mon Jul 31 2023 Vitaly Lipatov <lav@altlinux.ru> 20230125.3-alt2
- move test only libs to subpackage testing

* Sun Jul 30 2023 Vitaly Lipatov <lav@altlinux.ru> 20230125.3-alt1
- Abseil LTS branch, Jan 2023, Patch 3
- required libgtest-devel >= 1.13.0

* Mon Apr 10 2023 Alexey Shabalin <shaba@altlinux.org> 20230125.2-alt1
- 20230125.2
- switched build from static to shared libs

* Tue Aug 30 2022 Yuri N. Sedunov <aris@altlinux.org> 20211102.0-alt3
- rebuilt with -DCMAKE_POSITION_INDEPENDENT_CODE=ON
  (see https://github.com/abseil/abseil-cpp/issues/225)

* Wed Apr 20 2022 Vitaly Lipatov <lav@altlinux.ru> 20211102.0-alt2
- add Conflicts: libclickhouse-cpp-devel

* Sun Apr 10 2022 Vitaly Lipatov <lav@altlinux.ru> 20211102.0-alt1
- Abseil LTS branch, Nov 2021
- new version (20211102.0) with rpmgs script

* Wed Nov 17 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 20210324.2-alt3
- fixed build for Elbrus

* Fri Sep 03 2021 Vitaly Lipatov <lav@altlinux.ru> 20210324.2-alt2
- set optflags_lto to -ffat-lto-objects

* Sun Jul 04 2021 Vitaly Lipatov <lav@altlinux.ru> 20210324.2-alt1
- Abseil LTS branch, March 2021, Patch 2
- new version 20210324.2 (with rpmrb script)

* Fri Mar 26 2021 Vitaly Lipatov <lav@altlinux.ru> 20200923.3-alt1
- new version (20200923.3) with rpmgs script
- build with -DCMAKE_CXX_STANDARD=17

* Thu Jan 28 2021 Arseny Maslennikov <arseny@altlinux.org> 20200923.2-alt2
- NMU: enable -fPIC.

* Mon Nov 02 2020 Vitaly Lipatov <lav@altlinux.ru> 20200923.2-alt1
- new version 20200923.2 (with rpmrb script)
- temp. disable test (wait for new libgtest)

* Sun Aug 23 2020 Vitaly Lipatov <lav@altlinux.ru> 20200225.2-alt2
- enable tests

* Sun Aug 23 2020 Vitaly Lipatov <lav@altlinux.ru> 20200225.2-alt1
- initial build for ALT Sisyphus

* Wed May 27 2020 Rich Mattes <richmattes@gmail.com> - 20200225.2-2
- Don't remove buildroot in install

* Sun May 24 2020 Rich Mattes <richmattes@gmail.com> - 20200225.2-1
- Initial package.
