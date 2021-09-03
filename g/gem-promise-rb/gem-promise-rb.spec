%define        gemname promise.rb

Name:          gem-promise-rb
Version:       0.7.4.1
Release:       alt0.1
Summary:       Promises/A+ for Ruby
License:       Public Domain
Group:         Development/Ruby
Url:           https://github.com/lgierth/promise.rb
Vcs:           https://github.com/lgierth/promise.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(benchmark-ips) >= 0
# BuildRequires: gem(benchmark-memory) >= 0
# BuildRequires: gem(memory_profiler) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version promise.rb:0.7.4.1
%ruby_alias_names promise.rb,promise-rb
Provides:      gem(promise.rb) = 0.7.4.1


%description
Ruby implementation of the Promises/A+ spec. 100% mutation coverage, tested on
MRI 1.9, 2.0, 2.1, 2.2, Rubinius, and JRuby.


%package       -n gem-promise-rb-doc
Version:       0.7.4.1
Release:       alt0.1
Summary:       Promises/A+ for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета promise.rb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(promise.rb) = 0.7.4.1

%description   -n gem-promise-rb-doc
Promises/A+ for Ruby documentation files.

Ruby implementation of the Promises/A+ spec. 100% mutation coverage, tested on
MRI 1.9, 2.0, 2.1, 2.2, Rubinius, and JRuby.

%description   -n gem-promise-rb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета promise.rb.


%package       -n gem-promise-rb-devel
Version:       0.7.4.1
Release:       alt0.1
Summary:       Promises/A+ for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета promise.rb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(promise.rb) = 0.7.4.1
Requires:      gem(rspec) >= 0 gem(rspec) < 4
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(benchmark-memory) >= 0
Requires:      gem(memory_profiler) >= 0

%description   -n gem-promise-rb-devel
Promises/A+ for Ruby development package.

Ruby implementation of the Promises/A+ spec. 100% mutation coverage, tested on
MRI 1.9, 2.0, 2.1, 2.2, Rubinius, and JRuby.

%description   -n gem-promise-rb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета promise.rb.


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

%files         -n gem-promise-rb-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-promise-rb-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.7.4.1-alt0.1
- ^ 0.7.4 -> 0.7.4[.1]

* Wed Jun 05 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.4-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
