%define        gemname commonjs

Name:          gem-commonjs
Version:       0.2.7.1
Release:       alt0.1
Summary:       Common JS for Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/cowboyd/commonjs.rb
Vcs:           https://github.com/cowboyd/commonjs.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version commonjs:0.2.7.1
Provides:      gem(commonjs) = 0.2.7.1


%description
Host CommonJS JavaScript environments in Ruby.


%package       -n gem-commonjs-doc
Version:       0.2.7.1
Release:       alt0.1
Summary:       Common JS for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета commonjs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(commonjs) = 0.2.7.1

%description   -n gem-commonjs-doc
Common JS for Ruby documentation files.

Host CommonJS JavaScript environments in Ruby.

%description   -n gem-commonjs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета commonjs.


%package       -n gem-commonjs-devel
Version:       0.2.7.1
Release:       alt0.1
Summary:       Common JS for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета commonjs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(commonjs) = 0.2.7.1
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-commonjs-devel
Common JS for Ruby development package.

Host CommonJS JavaScript environments in Ruby.

%description   -n gem-commonjs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета commonjs.


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

%files         -n gem-commonjs-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-commonjs-devel
%doc README.md


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.7.1-alt0.1
- ^ 0.2.7 -> 0.2.7[.1]

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.7-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
