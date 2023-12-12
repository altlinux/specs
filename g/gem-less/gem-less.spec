%define        _unpackaged_files_terminate_build 1
%define        gemname less

Name:          gem-less
Version:       2.6.0.2
Release:       alt0.1
Summary:       Leaner CSS, in your browser or Ruby (via less.js)
License:       Apache 2.0
Group:         Development/Ruby
Url:           http://lesscss.org
Vcs:           https://github.com/cowboyd/less.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(therubyracer) >= 0.12.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 2.0
BuildRequires: gem(commonjs) >= 0.2.7
BuildConflicts: gem(therubyracer) >= 0.13
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(commonjs) >= 0.3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      gem(commonjs) >= 0.2.7
Conflicts:     gem(commonjs) >= 0.3
Provides:      gem(less) = 2.6.0.2

%ruby_use_gem_version less:2.6.0.2
%ruby_bindir_to %ruby_bindir

%description
The dynamic stylesheet language.

These are Ruby bindings for the next generation LESS, which is implemented in
JavaScript.


%package       -n lessc
Version:       2.6.0.2
Release:       alt0.1
Summary:       Leaner CSS, in your browser or Ruby (via less.js) executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета less
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(less) = 2.6.0.2
Conflicts:     lessjs

%description   -n lessc
Leaner CSS, in your browser or Ruby (via less.js) executable(s).

The dynamic stylesheet language.

These are Ruby bindings for the next generation LESS, which is implemented in
JavaScript.

%description   -n lessc -l ru_RU.UTF-8
Исполнямка для самоцвета less.


%package       -n gem-less-doc
Version:       2.6.0.2
Release:       alt0.1
Summary:       Leaner CSS, in your browser or Ruby (via less.js) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета less
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(less) = 2.6.0.2

%description   -n gem-less-doc
Leaner CSS, in your browser or Ruby (via less.js) documentation files.

The dynamic stylesheet language.

These are Ruby bindings for the next generation LESS, which is implemented in
JavaScript.

%description   -n gem-less-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета less.


%package       -n gem-less-devel
Version:       2.6.0.2
Release:       alt0.1
Summary:       Leaner CSS, in your browser or Ruby (via less.js) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета less
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(less) = 2.6.0.2
Requires:      gem(therubyracer) >= 0.12.0
Requires:      gem(therubyrhino) >= 2.0.2
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 2.0
Conflicts:     gem(therubyracer) >= 0.13
Conflicts:     gem(rspec) >= 4

%description   -n gem-less-devel
Leaner CSS, in your browser or Ruby (via less.js) development package.

The dynamic stylesheet language.

These are Ruby bindings for the next generation LESS, which is implemented in
JavaScript.

%description   -n gem-less-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета less.


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

%files         -n lessc
%doc README.md
%ruby_bindir/lessc

%files         -n gem-less-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-less-devel
%doc README.md


%changelog
* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 2.6.0.2-alt0.1
- ^ 2.6.0 -> 2.6.0p2

* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt2
- ! spec
 + + explicit conflict for bump to lessjs
 + * minor

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
