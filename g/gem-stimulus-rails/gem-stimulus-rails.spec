%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname stimulus-rails

Name:          gem-stimulus-rails
Version:       1.3.4
Release:       alt1
Summary:       A modest JavaScript framework for the HTML you already have
License:       MIT
Group:         Development/Ruby
Url:           https://stimulus.hotwired.dev
Vcs:           https://github.com/hotwired/stimulus-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rails) >= 6.1.0
BuildRequires: gem(railties) >= 6.0.0
BuildConflicts: gem(rails) >= 8

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rails >= 7.1,rails < 8
Requires:      gem(rails) >= 6.1.0
Requires:      gem(railties) >= 6.0.0
Conflicts:     gem(rails) >= 8
Provides:      stimulus-rails = %EVR
Provides:      gem(stimulus-rails) = 1.3.4

%description
A modest JavaScript framework for the HTML you already have.


%if_enabled    doc
%package       -n gem-stimulus-rails-doc
Version:       1.3.4
Release:       alt1
Summary:       A modest JavaScript framework for the HTML you already have documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета stimulus-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(stimulus-rails) = 1.3.4

%description   -n gem-stimulus-rails-doc
A modest JavaScript framework for the HTML you already have documentation files.

%description   -n gem-stimulus-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета stimulus-rails.
%endif


%if_enabled    devel
%package       -n gem-stimulus-rails-devel
Version:       1.3.4
Release:       alt1
Summary:       A modest JavaScript framework for the HTML you already have development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета stimulus-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(stimulus-rails) = 1.3.4

%description   -n gem-stimulus-rails-devel
A modest JavaScript framework for the HTML you already have development package.

%description   -n gem-stimulus-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета stimulus-rails.
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
%doc MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-stimulus-rails-doc
%doc MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-stimulus-rails-devel
%doc MIT-LICENSE README.md
%endif


%changelog
* Thu Feb 06 2025 Pavel Skrylev <majioa@altlinux.org> 1.3.4-alt1
- ^ 1.3.3 -> 1.3.4

* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 1.3.3-alt1
- + packaged gem with Ruby Policy 2.0
