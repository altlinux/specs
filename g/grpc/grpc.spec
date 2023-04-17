%define _unpackaged_files_terminate_build 1
%def_without python3_bindings

Name: grpc
Version: 1.53.0
Release: alt1

Summary: Modern, open source, high-performance remote procedure call (RPC) framework

License: Apache-2.0
Group: Networking/Other
Url: https://www.grpc.io
Vcs: https://github.com/grpc/grpc.git

Source0: %name-%version.tar
Source11: envoy-api.tar
Source12: opencensus-proto.tar
Source13: xds.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-ruby
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
#BuildRequires: gflags-devel
#BuildRequires: gtest-devel
#BuildRequires: gperftools-devel
%if_enabled check
BuildRequires: gem(bundler) >= 1.9
BuildRequires: gem(google-protobuf) >= 3.21 gem(google-protobuf) < 4
BuildRequires: gem(googleapis-common-protos-types) >= 1.0 gem(googleapis-common-protos-types) < 2
BuildRequires: gem(facter) >= 2.4
BuildRequires: gem(logging) >= 2.0
BuildRequires: gem(simplecov) >= 0.14.1 gem(simplecov) < 1
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rake-compiler) >= 1.2.0
BuildRequires: gem(rake-compiler-dock) >= 1.2.0
BuildRequires: gem(rspec) >= 3.6
BuildRequires: gem(rubocop) >= 0.49.1 gem(rubocop) < 2
BuildRequires: gem(signet) >= 0.7 gem(signet) < 1
BuildRequires: gem(googleauth)
%endif

Patch1: grpc-0001-enforce-system-crypto-policies.patch

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names distribtest,grpc-demo,pubsub
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake-compiler >= 1.2.0,rake-compiler < 2
%ruby_use_gem_dependency rake-compiler-dock>= 1.2.0,rake-compiler-dock< 2
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.14.1,simplecov < 1
%ruby_use_gem_dependency  googleauth >= 1.0.0,googleauth < 2

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

%package -n lib%name
Summary: C API for gRPC
Group: System/Libraries

%description -n lib%name
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

%package -n lib%name++
Summary: C++ API for gRPC
Group: System/Libraries

%description -n lib%name++
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

%package -n lib%name-devel
Summary: gRPC library development files: C libraries
Group: Development/C

%description -n lib%name-devel
Development headers and files for gRPC libraries.

%package -n lib%name++-devel
Summary: gRPC library development files: C++ libraries
Group: Development/C++

%description -n lib%name++-devel
Development headers and files for gRPC libraries.

%if_with python3_bindings
%package -n python3-module-grpcio
Summary: Python language bindings for gRPC
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-grpcio
Python3 bindings for gRPC library.
%endif

%package -n gem-%name
Summary: GRPC system in Ruby
Group: Development/Ruby
Requires: lib%name = %EVR
Requires: gem(google-protobuf) >= 3.21 gem(google-protobuf) < 4
Requires: gem(googleapis-common-protos-types) >= 1.0 gem(googleapis-common-protos-types) < 2
Provides: gem(%name) = %version

%description -n gem-%name
protoc and the Ruby gRPC protoc plugin

%package -n gem-%name-devel
Summary: Modern, open source, high-performance remote procedure call (RPC) framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета grpc
Group: Development/Ruby
BuildArch: noarch

Requires: gem(grpc) = %version
Requires: gem(bundler) >= 1.9
Requires: gem(facter) >= 2.4
Requires: gem(logging) >= 2.0
Requires: gem(simplecov) >= 0.17
Requires: gem(rake) >= 13.0
Requires: gem(rake-compiler) >= 1.1.2
Requires: gem(rake-compiler-dock) >= 0.7.2
Requires: gem(rspec) >= 3.6
Requires: gem(rubocop) >= 1.15.0
Requires: gem(signet) >= 0.7
Requires: gem(googleauth) >= 0.5.1

%description -n gem-%name-devel
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

%package -n gem-%name-doc
Summary: GRPC system in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета grpc
Group: Development/Documentation
BuildArch: noarch
Requires: gem(%name)

%description -n gem-%name-doc
GRPC system in Ruby documentation files.

Send RPCs from Ruby using GRPC

%description -n gem-%name-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета grpc.

%package -n gem-%name-tools
Summary: Development tools for Ruby gRPC
Group: Development/Ruby
BuildArch: noarch
Provides: gem(%name-tools) = %version

%description -n gem-%name-tools
protoc and the Ruby gRPC protoc plugin

%package tools-ruby-protoc
Summary: Development tools for Ruby gRPC executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета grpc-tools
Group: Other
BuildArch: noarch
Requires: gem(%name-tools) = %version

%description tools-ruby-protoc
Development tools for Ruby gRPC executable(s).

protoc and the Ruby gRPC protoc plugin

%description tools-ruby-protoc -l ru_RU.UTF-8
Исполнямка для самоцвета grpc-tools.

%prep
%setup
tar -xf %SOURCE11 -C third_party/envoy-api
tar -xf %SOURCE12 -C third_party/opencensus-proto
tar -xf %SOURCE13 -C third_party/xds
%autopatch -p1
rm -rvf third_party/googletest
rm -rvf third_party/xxhash
rm -rfv \
    src/boringssl/boringssl_prefix_symbols.h \
    third_party/cares/ares_build.h \
    third_party/upb/third_party/lunit
rm -rvf examples/android src/android
rm -vf examples/node/package-lock.json

%build
rm -f Makefile
rm -f BUILD
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
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
%ruby_build

%if_with python3_bindings
# build python module
export GRPC_PYTHON_BUILD_WITH_CYTHON=True
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=True
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=True
export GRPC_PYTHON_BUILD_SYSTEM_CARES=True
export CFLAGS="%optflags"
%py3_build
%endif

%install
%cmake_install
%ruby_install
rm -rf %buildroot/%ruby_gemsextdir/grpc-%version/*-linux* %buildroot/%ruby_gemslibdir/grpc-%version/src/ruby/lib/*-linux*
#rm -rf %buildroot/usr/bin/grpc_tools_ruby_protoc_plugin
#echo ln -s ../lib/ruby/gems/%(%ruby_rubyconf ruby_version)/gems/grpc-tools-1.38.0/bin/grpc_tools_ruby_protoc_plugin %buildroot/usr/bin/grpc_tools_ruby_protoc_plugin
#ln -s ../lib/ruby/gems/2.7.0/gems/grpc-tools-1.38.0/bin/grpc_tools_ruby_protoc_plugin %buildroot/usr/bin/grpc_tools_ruby_protoc_plugin

%if_with python3_bindings
%py3_install
%endif

%check
%ruby_test

%files -n lib%name
%doc README.md LICENSE
%_libdir/libaddress_sorting.so.*
%_libdir/libgpr.so.*
%_libdir/libgrpc.so.*
%_libdir/libgrpc_authorization_provider.so.*
%_libdir/libgrpc_plugin_support.so.*
%_libdir/libgrpc_unsecure.so.*
%_libdir/libupb.so.*
%_datadir/grpc

%files -n lib%name++
%doc README.md LICENSE
%_libdir/libgrpc++.so.*
%_libdir/libgrpc++_alts.so.*
%_libdir/libgrpc++_error_details.so.*
%_libdir/libgrpc++_reflection.so.*
%_libdir/libgrpc++_unsecure.so.*
%_libdir/libgrpcpp_channelz.so.*

# %%files cli
# %%_bindir/grpc_cli

%files plugins
%doc README.md LICENSE
%_bindir/grpc_*_plugin

%files -n lib%name-devel
%_libdir/libaddress_sorting.so
%_libdir/libgpr.so
%_libdir/libgrpc.so
%_libdir/libgrpc_plugin_support.so
%_libdir/libgrpc_unsecure.so
%_libdir/libgrpc_authorization_provider.so
%_libdir/libupb.so
%_pkgconfigdir/gpr.pc
%_pkgconfigdir/grpc.pc
%_pkgconfigdir/grpc_unsecure.pc
%_includedir/grpc
%prefix/lib/cmake/grpc

%files -n lib%name++-devel
%_libdir/libgrpc++.so
%_libdir/libgrpc++_alts.so
%_libdir/libgrpc++_error_details.so
%_libdir/libgrpc++_reflection.so
%_libdir/libgrpc++_unsecure.so
%_libdir/libgrpcpp_channelz.so
%_pkgconfigdir/grpc++.pc
%_pkgconfigdir/grpc++_unsecure.pc
%_includedir/grpc++
%_includedir/grpcpp

%if_with python3-bindings
%files -n python3-module-grpcio
%doc LICENSE
%python3_sitearch/grpc
%python3_sitearch/grpcio-%version-py%python3_version.egg-info
%endif

%files -n gem-%name
%doc src/ruby/pb/README.md src/ruby/spec/testdata/README
%ruby_gemspecdir/*
%ruby_gemslibdir/*
%ruby_gemsextdir/*
%exclude %ruby_gemspecdir/%name-tools-*
%exclude %ruby_gemslibdir/%name-tools-*

%files -n gem-%name-devel

%files -n gem-%name-doc
%doc src/ruby/pb/README.md src/ruby/spec/testdata/README
%ruby_gemsdocdir/%name-*

%files -n gem-%name-tools
%doc README.md
%ruby_gemspecdir/%name-tools-*
%ruby_gemslibdir/%name-tools-*

%files tools-ruby-protoc
%doc README.md
%_bindir/grpc_tools_ruby_protoc

%changelog
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
