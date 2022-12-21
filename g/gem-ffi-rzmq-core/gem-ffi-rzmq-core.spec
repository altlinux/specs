%define        gemname ffi-rzmq-core

Name:          gem-ffi-rzmq-core
Version:       1.0.7
Release:       alt3
Summary:       FFI wrapper for the ZeroMQ networking library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/chuckremes/ffi-rzmq-core.git
Vcs:           https://github.com/chuckremes/ffi-rzmq-core.git.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         fix-search-original-libzmq.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: libzeromq-devel
%if_with check
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(ffi) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ffi) >= 0
Requires:      libzeromq
Obsoletes:     ruby-ffi-rzmq-core < %EVR
Provides:      ruby-ffi-rzmq-core = %EVR
Provides:      gem(ffi-rzmq-core) = 1.0.7


%description
This gem provides only the FFI wrapper for the ZeroMQ (0mq) networking library.
Project can be used by any other zeromq gems that want to provide their own
high-level Ruby API.


%package       -n gem-ffi-rzmq-core-doc
Version:       1.0.7
Release:       alt3
Summary:       FFI wrapper for the ZeroMQ networking library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ffi-rzmq-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ffi-rzmq-core) = 1.0.7

%description   -n gem-ffi-rzmq-core-doc
FFI wrapper for the ZeroMQ networking library documentation files.

This gem provides only the FFI wrapper for the ZeroMQ (0mq) networking library.
Project can be used by any other zeromq gems that want to provide their own
high-level Ruby API.

%description   -n gem-ffi-rzmq-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ffi-rzmq-core.


%package       -n gem-ffi-rzmq-core-devel
Version:       1.0.7
Release:       alt3
Summary:       FFI wrapper for the ZeroMQ networking library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ffi-rzmq-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ffi-rzmq-core) = 1.0.7
Requires:      gem(rspec) >= 0
Requires:      gem(rake) >= 0
Requires:      libzeromq-devel

%description   -n gem-ffi-rzmq-core-devel
FFI wrapper for the ZeroMQ networking library development package.

This gem provides only the FFI wrapper for the ZeroMQ (0mq) networking library.
Project can be used by any other zeromq gems that want to provide their own
high-level Ruby API.

%description   -n gem-ffi-rzmq-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ffi-rzmq-core.


%prep
%setup
%autopatch

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

%files         -n gem-ffi-rzmq-core-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ffi-rzmq-core-devel
%doc README.md


%changelog
* Wed Dec 14 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt3
- ! loading original libzmq library with a digit without devel package

* Mon Dec 05 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt2.1
- ! spec

* Wed Feb 19 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.7-alt2
- fixed load libzmq.so.5
- add requires to libzeromq

* Thu Jan 30 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.7-alt1
- Initial build.
