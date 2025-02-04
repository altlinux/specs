%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname terser

Name:          gem-terser
Version:       1.2.4
Release:       alt1
Summary:       Ruby wrapper for Terser JavaScript compressor
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/ahorek/terser-ruby
Vcs:           https://github.com/ahorek/terser-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(rake) >= 13.0
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(execjs) >= 0.3.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(sourcemap) >= 0.1.1
BuildConflicts: gem(execjs) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(sourcemap) >= 0.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
Requires:      ruby >= 2.3.0
Requires:      gem(execjs) >= 0.3.0
Conflicts:     gem(execjs) >= 3
Provides:      gem(terser) = 1.2.4

%description
Terser minifies JavaScript files by wrapping TerserJS to be accessible in Ruby


%if_enabled    doc
%package       -n gem-terser-doc
Version:       1.2.4
Release:       alt1
Summary:       Ruby wrapper for Terser JavaScript compressor documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета terser
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(terser) = 1.2.4

%description   -n gem-terser-doc
Ruby wrapper for Terser JavaScript compressor documentation files.

Terser minifies JavaScript files by wrapping TerserJS to be accessible in Ruby

%description   -n gem-terser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета terser.
%endif


%if_enabled    devel
%package       -n gem-terser-devel
Version:       1.2.4
Release:       alt1
Summary:       Ruby wrapper for Terser JavaScript compressor development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета terser
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(terser) = 1.2.4
Requires:      gem(bundler) >= 1.3
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(sourcemap) >= 0.1.1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(sourcemap) >= 0.2

%description   -n gem-terser-devel
Ruby wrapper for Terser JavaScript compressor development package.

Terser minifies JavaScript files by wrapping TerserJS to be accessible in Ruby

%description   -n gem-terser-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета terser.
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
%doc CHANGELOG.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-terser-doc
%doc CHANGELOG.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-terser-devel
%doc CHANGELOG.md CONTRIBUTING.md LICENSE.txt README.md
%endif


%changelog
* Mon Jan 13 2025 Pavel Skrylev <majioa@altlinux.org> 1.2.4-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
