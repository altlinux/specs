%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubygems-bundler

Name:          gem-rubygems-bundler
Version:       1.4.5.3
Release:       alt0.1
Summary:       Stop using bundle exec
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://rvm.github.io/rubygems-bundler/
Vcs:           https://github.com/rvm/rubygems-bundler.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler-unload) >= 1.0.2
BuildRequires: gem(executable-hooks) >= 1.5.0
BuildRequires: gem(tf) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(bundler-unload) >= 1.0.2
Requires:      gem(executable-hooks) >= 1.5.0
Provides:      gem(rubygems-bundler) = 1.4.5.3

%ruby_use_gem_version rubygems-bundler:1.4.5.3

%description
Stop using bundle exec. Integrate Rubygems and Bundler. Make rubygems generate
bundler aware executable wrappers.


%if_enabled    doc
%package       -n gem-rubygems-bundler-doc
Version:       1.4.5.3
Release:       alt0.1
Summary:       Stop using bundle exec documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubygems-bundler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubygems-bundler) = 1.4.5.3

%description   -n gem-rubygems-bundler-doc
Stop using bundle exec documentation files.

Stop using bundle exec. Integrate Rubygems and Bundler. Make rubygems generate
bundler aware executable wrappers.

%description   -n gem-rubygems-bundler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubygems-bundler.
%endif


%if_enabled    devel
%package       -n gem-rubygems-bundler-devel
Version:       1.4.5.3
Release:       alt0.1
Summary:       Stop using bundle exec development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubygems-bundler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubygems-bundler) = 1.4.5.3
Requires:      gem(tf) >= 0

%description   -n gem-rubygems-bundler-devel
Stop using bundle exec development package.

Stop using bundle exec. Integrate Rubygems and Bundler. Make rubygems generate
bundler aware executable wrappers.

%description   -n gem-rubygems-bundler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubygems-bundler.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rubygems-bundler-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubygems-bundler-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Fri Oct 17 2025 Pavel Skrylev <majioa@altlinux.org> 1.4.5.3-alt0.1
- ^ 1.4.5 -> 1.4.5p3
- * rebased to master
- ! fixed usr/vcs in spec (closes ALT#49821)

* Wed Nov 22 2023 Pavel Skrylev <majioa@altlinux.org> 1.4.5-alt1
- + packaged gem with Ruby Policy 2.0
