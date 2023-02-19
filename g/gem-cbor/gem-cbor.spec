# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname cbor

Name:          gem-cbor
Version:       0.5.9.6
Release:       alt1.1
Summary:       CBOR (RFC 7049) extension for Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://cbor.io/
Vcs:           https://github.com/cabo/cbor-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
%ruby_use_gem_dependency json >= 2.3.0,json < 3
%ruby_use_gem_dependency yard >= 0.9.27,yard < 1
Provides:      gem(cbor) = 0.5.9.6


%description
CBOR (RFC 7049) extension for Ruby.


%package       -n gem-cbor-doc
Version:       0.5.9.6
Release:       alt1.1
Summary:       CBOR (RFC 7049) extension for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cbor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(cbor) = 0.5.9.6

%description   -n gem-cbor-doc
CBOR (RFC 7049) extension for Ruby documentation files.

%description   -n gem-cbor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cbor.


%package       -n gem-cbor-devel
Version:       0.5.9.6
Release:       alt1.1
Summary:       CBOR (RFC 7049) extension for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cbor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cbor) = 0.5.9.6
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(json) >= 0
Requires:      gem(yard) >= 0
Conflicts:     gem(yard) >= 1

%description   -n gem-cbor-devel
CBOR (RFC 7049) extension for Ruby development package.

%description   -n gem-cbor-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cbor.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-cbor-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-cbor-devel
%doc README.rdoc
%ruby_includedir/*


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 0.5.9.6-alt1.1
- ! closes build deps under check condition

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 0.5.9.6-alt1
- + packaged gem with usage Ruby Policy 2.0
