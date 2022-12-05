%define        gemname ffi-rzmq

Name:          gem-ffi-rzmq
Version:       2.0.7.1
Release:       alt0.1
Summary:       Wraps the ZeroMQ networking library using Ruby FFI
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/chuckremes/ffi-rzmq-core.git
Vcs:           https://github.com/chuckremes/ffi-rzmq-core.git.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 3.7 gem(rspec) < 4
BuildRequires: gem(rake) >= 0
BuildRequires: gem(ffi-rzmq-core) >= 1.0.7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version ffi-rzmq:2.0.7.1
Requires:      gem(ffi-rzmq-core) >= 1.0.7
Obsoletes:     ruby-ffi-rzmq < %EVR
Provides:      ruby-ffi-rzmq = %EVR
Provides:      gem(ffi-rzmq) = 2.0.7.1


%description
This gem wraps the ZeroMQ networking library using the ruby FFI (foreign
function interface). It's a pure ruby wrapper so this gem can be loaded and run
by any ruby runtime that supports FFI. That's all of the major ones - MRI,
Rubinius and JRuby.


%package       -n gem-ffi-rzmq-doc
Version:       2.0.7.1
Release:       alt0.1
Summary:       Wraps the ZeroMQ networking library using Ruby FFI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ffi-rzmq
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ffi-rzmq) = 2.0.7.1

%description   -n gem-ffi-rzmq-doc
Wraps the ZeroMQ networking library using Ruby FFI documentation files.

This gem wraps the ZeroMQ networking library using the ruby FFI (foreign
function interface). It's a pure ruby wrapper so this gem can be loaded and run
by any ruby runtime that supports FFI. That's all of the major ones - MRI,
Rubinius and JRuby.

%description   -n gem-ffi-rzmq-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ffi-rzmq.


%package       -n gem-ffi-rzmq-devel
Version:       2.0.7.1
Release:       alt0.1
Summary:       Wraps the ZeroMQ networking library using Ruby FFI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ffi-rzmq
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ffi-rzmq) = 2.0.7.1
Requires:      gem(rspec) >= 3.7 gem(rspec) < 4
Requires:      gem(rake) >= 0

%description   -n gem-ffi-rzmq-devel
Wraps the ZeroMQ networking library using Ruby FFI development package.

This gem wraps the ZeroMQ networking library using the ruby FFI (foreign
function interface). It's a pure ruby wrapper so this gem can be loaded and run
by any ruby runtime that supports FFI. That's all of the major ones - MRI,
Rubinius and JRuby.

%description   -n gem-ffi-rzmq-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ffi-rzmq.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc ext/README
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-ffi-rzmq-doc
%doc README.rdoc ext/README
%ruby_gemdocdir

%files         -n gem-ffi-rzmq-devel
%doc README.rdoc ext/README


%changelog
* Mon Dec 05 2022 Pavel Skrylev <majioa@altlinux.org> 2.0.7.1-alt0.1
- ^ 2.0.7 -> 2.0.7[1]

* Thu Jan 30 2020 Alexey Shabalin <shaba@altlinux.org> 2.0.7-alt1
- Initial build.
