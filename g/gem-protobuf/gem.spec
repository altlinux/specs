%define        gemname protobuf

Name:          gem-protobuf
Version:       3.10.3
Release:       alt1
Summary:       Google Protocol Buffers serialization and RPC implementation for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/localshred/protobuf
Vcs:           https://github.com/localshred/protobuf.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 3.2
BuildRequires: gem(middleware) >= 0
BuildRequires: gem(thor) >= 0
BuildRequires: gem(thread_safe) >= 0
BuildRequires: gem(rake) >= 13.0.1 gem(rake) < 14
BuildRequires: gem(rubocop) >= 0.38.0 gem(rubocop) < 2
BuildRequires: gem(simplecov) >= 0 gem(simplecov) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(activesupport) >= 3.2
Requires:      gem(middleware) >= 0
Requires:      gem(thor) >= 0
Requires:      gem(thread_safe) >= 0
Provides:      gem(protobuf) = 3.10.3


%description
Google Protocol Buffers serialization and RPC implementation for Ruby.


%package       -n protoc-gen-ruby
Version:       3.10.3
Release:       alt1
Summary:       Google Protocol Buffers serialization and RPC implementation for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета protobuf
Group:         Other
BuildArch:     noarch

Requires:      gem(protobuf) = 3.10.3

%description   -n protoc-gen-ruby
Google Protocol Buffers serialization and RPC implementation for Ruby
executable(s).

Google Protocol Buffers serialization and RPC implementation for Ruby.

%description   -n protoc-gen-ruby -l ru_RU.UTF-8
Исполнямка для самоцвета protobuf.


%package       -n gem-protobuf-doc
Version:       3.10.3
Release:       alt1
Summary:       Google Protocol Buffers serialization and RPC implementation for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета protobuf
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(protobuf) = 3.10.3

%description   -n gem-protobuf-doc
Google Protocol Buffers serialization and RPC implementation for Ruby
documentation files.

Google Protocol Buffers serialization and RPC implementation for Ruby.

%description   -n gem-protobuf-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета protobuf.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n protoc-gen-ruby
%doc README.md
%_bindir/protoc-gen-ruby
%_bindir/rpc_server

%files         -n gem-protobuf-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Mon Jun 07 2021 Pavel Skrylev <majioa@altlinux.org> 3.10.3-alt1
- + packaged gem with Ruby Policy 2.0
