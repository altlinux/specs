%define        gemname ffi-compiler

Name:          gem-ffi-compiler
Version:       1.0.1
Release:       alt1
Summary:       Ruby FFI Rakefile generator
License:       Apache 2.0
Group:         Development/Ruby
Url:           http://wiki.github.com/ffi/ffi
Vcs:           https://github.com/ffi/ffi-compiler.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
BuildRequires: gem(ffi) >= 1.0.0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubygems-tasks) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rake) >= 0
Requires:      gem(ffi) >= 1.0.0
Provides:      gem(ffi-compiler) = 1.0.1


%description
ffi-compiler is a ruby library for automating compilation of native libraries
for use with ffi.

To use, define your own ruby->native API using ffi, implement it in C, then use
ffi-compiler to compile it.


%package       -n gem-ffi-compiler-doc
Version:       1.0.1
Release:       alt1
Summary:       Ruby FFI Rakefile generator documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ffi-compiler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ffi-compiler) = 1.0.1

%description   -n gem-ffi-compiler-doc
Ruby FFI Rakefile generator documentation files.

ffi-compiler is a ruby library for automating compilation of native libraries
for use with ffi.

To use, define your own ruby->native API using ffi, implement it in C, then use
ffi-compiler to compile it.

%description   -n gem-ffi-compiler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ffi-compiler.


%package       -n gem-ffi-compiler-devel
Version:       1.0.1
Release:       alt1
Summary:       Ruby FFI Rakefile generator development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ffi-compiler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ffi-compiler) = 1.0.1
Requires:      gem(rspec) >= 0
Requires:      gem(rubygems-tasks) >= 0

%description   -n gem-ffi-compiler-devel
Ruby FFI Rakefile generator development package.

ffi-compiler is a ruby library for automating compilation of native libraries
for use with ffi.

To use, define your own ruby->native API using ffi, implement it in C, then use
ffi-compiler to compile it.

%description   -n gem-ffi-compiler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ffi-compiler.


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

%files         -n gem-ffi-compiler-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ffi-compiler-devel
%doc README.md


%changelog
* Sun May 08 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
