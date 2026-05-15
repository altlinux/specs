%define _unpackaged_files_terminate_build 1
%define   gemname grpc
%def_without python3_bindings
%def_with ruby
%def_enable check
%def_enable doc
%def_enable devel

# ABI/SONAME versions from CMakeLists.txt (gRPC_CORE_SOVERSION / gRPC_CPP_SOVERSION).
# Bumped on ABI breakage - review when updating grpc version.
%define _sover_c   53
%define _sover_cxx 1.80

Name: grpc
Version: 1.80.0
Release: alt1.1

Summary: Modern, open source, high-performance remote procedure call (RPC) framework

License: Apache-2.0
Group: Networking/Other
Url: https://www.grpc.io
Vcs: https://github.com/grpc/grpc.git

Source0: grpc-%version.tar

Source101: grpc-%version-third_party-envoy-api.tar
Source102: grpc-%version-third_party-opencensus-proto.tar
Source103: grpc-%version-third_party-xds.tar


BuildRequires(pre): rpm-macros-cmake
%if_with ruby
BuildRequires(pre): rpm-build-ruby
%endif
BuildRequires: cmake ninja-build
BuildRequires: gcc-c++ libstdc++-devel
BuildRequires: libprotobuf-devel
BuildRequires: protobuf-compiler
BuildRequires: openssl-devel libssl-devel
BuildRequires: pkgconfig(zlib)
BuildRequires: libcares-devel
BuildRequires: libabseil-cpp-devel
BuildRequires: libre2-devel
BuildRequires: libxxhash-devel
BuildRequires: chrpath
%if_with ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.9
BuildRequires: gem(facter) >= 2.4
BuildRequires: gem(google-protobuf) >= 3.25
BuildRequires: gem(googleapis-common-protos-types) >= 1.0
BuildRequires: gem(googleauth) >= 1.0
BuildRequires: gem(logging) >= 2.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 1.1.2
BuildRequires: gem(rake-compiler-dock) >= 1.2.1
BuildRequires: gem(rspec) >= 3.6
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(signet) >= 0.7
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(syslog) >= 0.3.0
BuildConflicts: gem(facter) >= 5
BuildConflicts: gem(google-protobuf) >= 5.0
BuildConflicts: gem(googleapis-common-protos-types) >= 2
BuildConflicts: gem(googleauth) >= 2
BuildConflicts: gem(logging) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rake-compiler-dock) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(signet) >= 1
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(syslog) >= 0.4
%endif
%endif

Patch0: grpc-%version-alt.patch
Patch1: grpc-0001-enforce-system-crypto-policies.patch

%if_with ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names distribtest,grpc-demo,pubsub,grpc-native-debug
%ruby_use_gem_dependency facter >= 4.10,facter < 5
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
%ruby_use_gem_dependency rake-compiler-dock >= 1.2.1,rake-compiler-dock < 2
%endif

%description
gRPC is a modern open source high performance RPC framework that can run in any
environment. It can efficiently connect services in and across data centers with
pluggable support for load balancing, tracing, health checking and
authentication. It is also applicable in last mile of distributed computing to
connect devices, mobile applications and browsers to backend services.

The main usage scenarios:

* Efficiently connecting polyglot services in microservices style architecture
* Connecting mobile devices, browser clients to backend services
* Generating efficient client libraries

Core Features that make it awesome:

* Idiomatic client libraries in 10 languages
* Highly efficient on wire and with a simple service definition framework
* Bi-directional streaming with http/2 based transport
* Pluggable auth, tracing, load balancing and health checking

%package plugins
Summary: gRPC protocol buffers compiler plugins
Group: Networking/Other
Requires: protobuf-compiler

%description plugins
Plugins to the protocol buffers compiler to generate gRPC sources.

# %%package cli
# Summary: gRPC protocol buffers cli
# Group: Networking/Other

# %%description cli
# Plugins to the protocol buffers compiler to generate gRPC sources.

%package -n libgrpc%_sover_c
Summary: C API for gRPC
Group: System/Libraries

%description -n libgrpc%_sover_c
gRPC is a modern open source high performance RPC framework that can run in any
environment. It can efficiently connect services in and across data centers
with pluggable support for load balancing, tracing, health checking and
authentication. It is also applicable in last mile of distributed computing to
connect devices, mobile applications and browsers to backend services.

The main usage scenarios:

* Efficiently connecting polyglot services in microservices style architecture
* Connecting mobile devices, browser clients to backend services
* Generating efficient client libraries

Core Features that make it awesome:

* Idiomatic client libraries in 10 languages
* Highly efficient on wire and with a simple service definition framework
* Bi-directional streaming with http/2 based transport
* Pluggable auth, tracing, load balancing and health checking

%package -n libgrpc++%_sover_cxx
Summary: C++ API for gRPC
Group: System/Libraries

%description -n libgrpc++%_sover_cxx
gRPC is a modern open source high performance RPC framework that can run in any
environment. It can efficiently connect services in and across data centers
with pluggable support for load balancing, tracing, health checking and
authentication. It is also applicable in last mile of distributed computing to
connect devices, mobile applications and browsers to backend services.

The main usage scenarios:

* Efficiently connecting polyglot services in microservices style architecture
* Connecting mobile devices, browser clients to backend services
* Generating efficient client libraries

Core Features that make it awesome:

* Idiomatic client libraries in 10 languages
* Highly efficient on wire and with a simple service definition framework
* Bi-directional streaming with http/2 based transport
* Pluggable auth, tracing, load balancing and health checking

%package -n libgrpc-devel
Summary: gRPC library development files
Group: Development/C
Provides: libgrpc++-devel = %EVR
Obsoletes: libgrpc++-devel < %EVR

%description -n libgrpc-devel
Development headers and files for gRPC libraries (C and C++).

%if_with python3_bindings
%package -n python3-module-grpcio
Summary: Python language bindings for gRPC
Group: Development/Python3
Requires: grpc = %EVR

%description -n python3-module-grpcio
Python3 bindings for gRPC library.
%endif

%if_with ruby
%package -n gem-grpc
Summary: GRPC system in Ruby
Group: Development/Ruby
Provides: gem(grpc) = %version
Requires: libgrpc%_sover_c = %EVR
Requires: ruby >= 3.1
Requires: gem(google-protobuf) >= 3.25
Requires: gem(googleapis-common-protos-types) >= 1.0
Conflicts: gem(google-protobuf) >= 5.0
Conflicts: gem(googleapis-common-protos-types) >= 2

%description -n gem-grpc
protoc and the Ruby gRPC protoc plugin

%if_enabled    devel
%package -n gem-grpc-devel
Summary: Modern, open source, high-performance remote procedure call (RPC) framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета grpc
Group: Development/Ruby
BuildArch: noarch

Requires:      gem-grpc = %EVR
Requires:      gem(grpc) = 1.80.0
Requires:      gem(bundler) >= 1.9
Requires:      gem(facter) >= 2.4
Requires:      gem(googleauth) >= 1.0
Requires:      gem(logging) >= 2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 1.1.2
Requires:      gem(rake-compiler-dock) >= 1.2.1
Requires:      gem(rspec) >= 3.6
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(signet) >= 0.7
Requires:      gem(simplecov) >= 0.17
Requires:      gem(syslog) >= 0.3.0
Conflicts:     gem(facter) >= 5
Conflicts:     gem(googleauth) >= 2
Conflicts:     gem(logging) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rake-compiler-dock) >= 2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(signet) >= 1
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(syslog) >= 0.4

%description -n gem-grpc-devel
Modern, open source, high-performance remote procedure call (RPC) framework
development package.

gRPC is a modern open source high performance RPC framework that can run in any
environment. It can efficiently connect services in and across data centers with
pluggable support for load balancing, tracing, health checking and
authentication. It is also applicable in last mile of distributed computing to
connect devices, mobile applications and browsers to backend services.

The main usage scenarios:

* Efficiently connecting polyglot services in microservices style architecture
* Connecting mobile devices, browser clients to backend services
* Generating efficient client libraries

Core Features that make it awesome:

* Idiomatic client libraries in 10 languages
* Highly efficient on wire and with a simple service definition framework
* Bi-directional streaming with http/2 based transport
* Pluggable auth, tracing, load balancing and health checking

%description -n gem-grpc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета grpc.
%endif

%if_enabled    doc
%package -n gem-grpc-doc
Summary: GRPC system in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета grpc
Group: Development/Documentation
BuildArch: noarch
Requires: gem(grpc)

%description -n gem-grpc-doc
GRPC system in Ruby documentation files.

Modern, open source, high-performance remote procedure call (RPC) framework
documentation files.

gRPC is a modern open source high performance RPC framework that can run in any
environment. It can efficiently connect services in and across data centers with
pluggable support for load balancing, tracing, health checking and
authentication. It is also applicable in last mile of distributed computing to
connect devices, mobile applications and browsers to backend services.

The main usage scenarios:

* Efficiently connecting polyglot services in microservices style architecture
* Connecting mobile devices, browser clients to backend services
* Generating efficient client libraries

Core Features that make it awesome:

* Idiomatic client libraries in 10 languages
* Highly efficient on wire and with a simple service definition framework
* Bi-directional streaming with http/2 based transport
* Pluggable auth, tracing, load balancing and health checking


%description -n gem-grpc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета grpc.
%endif

%package -n gem-grpc-tools
Summary: Development tools for Ruby gRPC
Group: Development/Ruby
BuildArch: noarch
Provides: gem(grpc-tools) = %version

%description -n gem-grpc-tools
protoc and the Ruby gRPC protoc plugin

%package grpc-tools-ruby-protoc
Summary: Development tools for Ruby gRPC executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета grpc-tools
Group: Other
BuildArch: noarch
Requires: gem(grpc-tools) = %version

%description grpc-tools-ruby-protoc
Development tools for Ruby gRPC executable(s).

protoc and the Ruby gRPC protoc plugin

%description grpc-tools-ruby-protoc -l ru_RU.UTF-8
Исполнямка для самоцвета grpc-tools.
%endif

%prep
%setup -a101 -a102 -a103
%autopatch -p1
rm -rvf third_party/googletest
rm -rvf third_party/xxhash
rm -rfv \
    src/boringssl/boringssl_prefix_symbols.h \
    third_party/cares/ares_build.h \
    third_party/upb/third_party/lunit
rm -rvf examples/android src/android
rm -vf examples/node/package-lock.json

%if_with ruby
# platform.rb is a template filled in by upstream's native-debug build
# script; we do not build grpc-native-debug gem, but setup.rb scans all
# gemspecs and bails on the unexpanded placeholder.
sed -i 's|PLATFORM =.*GENERATED.*|PLATFORM = nil|' src/ruby/nativedebug/platform.rb
%endif

%build
rm -f Makefile
rm -f BUILD

# Prevent -Werror=return-type in switch/case blocks:
%add_optflags -Wno-error=return-type

%cmake \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
    -DgRPC_INSTALL_LIBDIR="$(relative %_libdir/ %prefix/)" \
    -DgRPC_INSTALL_PKGCONFIGDIR="$(relative %_pkgconfigdir/ %prefix/)" \
    -DgRPC_ZLIB_PROVIDER="package" \
    -DgRPC_CARES_PROVIDER="package" \
    -DgRPC_RE2_PROVIDER="package" \
    -DgRPC_SSL_PROVIDER="package" \
    -DgRPC_PROTOBUF_PROVIDER="package" \
    -DgRPC_PROTOBUF_PACKAGE_TYPE:STRING='MODULE' \
    -DgRPC_USE_PROTO_LITE:BOOL=OFF \
    -DgRPC_BENCHMARK_PROVIDER="package" \
    -DgRPC_ABSL_PROVIDER="package" \
    -DCMAKE_CXX_STANDARD=17 \
    -GNinja
#

%cmake_build
%if_with ruby
# Ruby native extension links dynamically against libgrpc.so (via
# --disable-static, set by ALT setup-rb). At %ruby_build time the
# library is not yet in system paths - point the linker at the
# cmake build directory so find_library('grpc', ...) resolves.
export LIBRARY_PATH="%_cmake__builddir${LIBRARY_PATH:+:$LIBRARY_PATH}"
export LD_LIBRARY_PATH="%_cmake__builddir${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
%ruby_build
%endif

%if_with python3_bindings
# build python module
export GRPC_PYTHON_BUILD_WITH_CYTHON=True
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=True
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=True
export GRPC_PYTHON_BUILD_SYSTEM_CARES=True
export CFLAGS="%optflags"
%py3_build
%endif

%ifarch %e2k
# error: cpio archive too big - 5000M
strip --strip-debug %_cmake__builddir/libgrpc{,_*}.so.*
%endif

%install
%cmake_install
%if_with ruby
%ruby_install
rm -rf %buildroot/%ruby_gemsextdir/grpc-%version/*-linux* %buildroot/%ruby_gemslibdir/grpc-%version/src/ruby/lib/*-linux*
# %ruby_install creates /usr/bin/grpc_tools_ruby_protoc_plugin as an absolute
# symlink into the gem. The file is never called directly (only via the
# grpc_tools_ruby_protoc wrapper which uses a relative path inside the gem),
# so drop the orphan.
rm -f %buildroot%_bindir/grpc_tools_ruby_protoc_plugin
# %ruby_install creates absolute symlinks (grpc_c.so, grpc_tools_ruby_protoc).
# ALT requires relative symlinks inside %buildroot.
find %buildroot -type l | while read link; do
    target=$(readlink "$link")
    case "$target" in
    /*) ln -sf "$(realpath -m --relative-to="$(dirname "$link")" "%buildroot$target")" "$link" ;;
    esac
done
%endif

%if_with python3_bindings
%py3_install
%endif

%check
%if_with ruby
%ruby_test
%endif

%files -n libgrpc%_sover_c
%doc README.md LICENSE
%_libdir/libgpr.so.%{_sover_c}*
%_libdir/libgrpc.so.%{_sover_c}*
%_libdir/libgrpc_unsecure.so.%{_sover_c}*
%_datadir/grpc
%dir %_libdir/grpc
%_libdir/grpc/*.so.%{_sover_c}*

%files -n libgrpc++%_sover_cxx
%doc README.md LICENSE
%_libdir/libgrpc++.so.%{_sover_cxx}*
%_libdir/libgrpc++_alts.so.%{_sover_cxx}*
%_libdir/libgrpc++_error_details.so.%{_sover_cxx}*
%_libdir/libgrpc++_reflection.so.%{_sover_cxx}*
%_libdir/libgrpc++_unsecure.so.%{_sover_cxx}*
%_libdir/libgrpcpp_channelz.so.%{_sover_cxx}*
%_libdir/libgrpc_authorization_provider.so.%{_sover_cxx}*
%_libdir/libgrpc_plugin_support.so.%{_sover_cxx}*

# %%files cli
# %%_bindir/grpc_cli

%files plugins
%doc README.md LICENSE
%_bindir/grpc_*_plugin

%files -n libgrpc-devel
%_libdir/libgpr.so
%_libdir/libgrpc.so
%_libdir/libgrpc_unsecure.so
%_libdir/libgrpc++.so
%_libdir/libgrpc++_alts.so
%_libdir/libgrpc++_error_details.so
%_libdir/libgrpc++_reflection.so
%_libdir/libgrpc++_unsecure.so
%_libdir/libgrpcpp_channelz.so
%_libdir/libgrpc_authorization_provider.so
%_libdir/libgrpc_plugin_support.so
%_pkgconfigdir/gpr.pc
%_pkgconfigdir/grpc.pc
%_pkgconfigdir/grpc_unsecure.pc
%_pkgconfigdir/grpc++.pc
%_pkgconfigdir/grpc++_unsecure.pc
%_includedir/grpc
%_includedir/grpc++
%_includedir/grpcpp
%prefix/lib/cmake/grpc
%_libdir/grpc/*.so

%if_with python3-bindings
%files -n python3-module-grpcio
%doc LICENSE
%python3_sitearch/grpc
%python3_sitearch/grpcio-%version-py%python3_version.egg-info
%endif

%if_with ruby
%files -n gem-grpc
%doc src/ruby/pb/README.md src/ruby/spec/testdata/README
%ruby_gemspecdir/*
%ruby_gemslibdir/*
%ruby_gemsextdir/*
%exclude %ruby_gemspecdir/grpc-tools-*
%exclude %ruby_gemslibdir/grpc-tools-*

%files -n gem-grpc-devel

%files -n gem-grpc-doc
%doc src/ruby/pb/README.md src/ruby/spec/testdata/README
%ruby_gemsdocdir/grpc-*

%files -n gem-grpc-tools
%doc README.md
%ruby_gemspecdir/grpc-tools-*
%ruby_gemslibdir/grpc-tools-*

%files grpc-tools-ruby-protoc
%doc README.md
%_bindir/grpc_tools_ruby_protoc
%endif

%changelog
* Thu May 14 2026 Pavel Skrylev <majioa@altlinux.org> 1.80.0-alt1.1
- ! fixed dep to gem google-protobuf
- ! fixed some enclosing macros for ruby subsystem

* Sun Apr 12 2026 Anton Farygin <rider@altlinux.org> 1.80.0-alt1
- updated from 1.70.1 to 1.80.0

* Mon Jul 07 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.70.1-alt1.1
- e2k build fix

* Fri Feb 21 2025 Paul Wolneykien <manowar@altlinux.org> 1.70.1-alt1
- NMU: Update to v1.70.1.
- NMU: Install third-party libraries to %_libdir/grpc.

* Mon Apr 10 2023 Alexey Shabalin <shaba@altlinux.org> 1.53.0-alt1
- 1.53.0

* Sat Jul 24 2021 Pavel Skrylev <majioa@altlinux.org> 1.38.0-alt1.2
- ! closes gem build requires with check condition

* Sat Jul 24 2021 Pavel Skrylev <majioa@altlinux.org> 1.38.0-alt1.1
- + ruby packages

* Tue Jun 01 2021 Pavel Skrylev <majioa@altlinux.org> 1.38.0-alt1
- ^ 1.35.0 -> 1.38.0

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 1.35.0-alt3
- spec: Fixed FTBFS.

* Tue May 11 2021 Slava Aseev <ptrnine@altlinux.org> 1.35.0-alt2
- Fix build with libabseil (-DCMAKE_CXX_STANDARD=17)

* Wed Jan 27 2021 Arseny Maslennikov <arseny@altlinux.org> 1.35.0-alt1
- Initial build for ALT Sisyphus.
