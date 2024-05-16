%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname amq-protocol

Name:          gem-amq-protocol
Version:       2.3.2
Release:       alt1
Summary:       AMQP 0.9.1 encoding & decoding library
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/ruby-amqp/amq-protocol
Vcs:           https://github.com/ruby-amqp/amq-protocol.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(ruby-prof) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.8.0
BuildRequires: gem(rspec-its) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(byebug) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(amq-protocol) = 2.3.2

%ruby_use_gem_version amq-protocol:2.3.2

%description
amq-protocol is an AMQP 0.9.1 serialization library for Ruby. It is not a
client: the library only handles serialization and deserialization.


%if_enabled    doc
%package       -n gem-amq-protocol-doc
Version:       2.3.2
Release:       alt1
Summary:       AMQP 0.9.1 encoding & decoding library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета amq-protocol
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(amq-protocol) = 2.3.2

%description   -n gem-amq-protocol-doc
AMQP 0.9.1 encoding & decoding library documentation files.

amq-protocol is an AMQP 0.9.1 serialization library for Ruby. It is not a
client: the library only handles serialization and deserialization.

%description   -n gem-amq-protocol-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета amq-protocol.
%endif


%if_enabled    devel
%package       -n gem-amq-protocol-devel
Version:       2.3.2
Release:       alt1
Summary:       AMQP 0.9.1 encoding & decoding library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета amq-protocol
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(amq-protocol) = 2.3.2
Requires:      gem(ruby-prof) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.8.0
Requires:      gem(rspec-its) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(byebug) >= 0

%description   -n gem-amq-protocol-devel
AMQP 0.9.1 encoding & decoding library development package.

amq-protocol is an AMQP 0.9.1 serialization library for Ruby. It is not a
client: the library only handles serialization and deserialization.

%description   -n gem-amq-protocol-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета amq-protocol.
%endif


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

%if_enabled    doc
%files         -n gem-amq-protocol-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-amq-protocol-devel
%doc README.md
%endif


%changelog
* Wed Apr 24 2024 Pavel Skrylev <majioa@altlinux.org> 2.3.2-alt1
- + packaged gem with Ruby Policy 2.0
