%define        gemname protocol-hpack

Name:          gem-protocol-hpack
Version:       1.4.2
Release:       alt1
Summary:       A compresssor and decompressor for HTTP 2.0 HPACK
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/http-hpack
Vcs:           https://github.com/socketry/http-hpack.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(protocol-hpack) = 1.4.2


%description
A compresssor and decompressor for HTTP 2.0 HPACK.


%package       -n gem-protocol-hpack-doc
Version:       1.4.2
Release:       alt1
Summary:       A compresssor and decompressor for HTTP 2.0 HPACK documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета protocol-hpack
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(protocol-hpack) = 1.4.2

%description   -n gem-protocol-hpack-doc
A compresssor and decompressor for HTTP 2.0 HPACK documentation files.

%description   -n gem-protocol-hpack-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета protocol-hpack.


%package       -n gem-protocol-hpack-devel
Version:       1.4.2
Release:       alt1
Summary:       A compresssor and decompressor for HTTP 2.0 HPACK development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета protocol-hpack
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(protocol-hpack) = 1.4.2
Requires:      gem(covered) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-protocol-hpack-devel
A compresssor and decompressor for HTTP 2.0 HPACK development package.

%description   -n gem-protocol-hpack-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета protocol-hpack.


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

%files         -n gem-protocol-hpack-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-protocol-hpack-devel
%doc README.md


%changelog
* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.2-alt1
- + packaged gem with Ruby Policy 2.0
