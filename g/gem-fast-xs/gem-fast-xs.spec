%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fast_xs

Name:          gem-fast-xs
Version:       0.8.0.13
Release:       alt0.1
Summary:       fast_xs provides C extensions for escaping text
License:       Unlicense
Group:         Development/Ruby
Url:           http://rubyforge.org/projects/fast-xs
Vcs:           http://rubyforge.org/projects/fast-xs.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(hoe) >= 0
BuildRequires: gem(rack) >= 0
BuildRequires: gem(rake) >= 0.9.3
BuildRequires: gem(rdoc) >= 4.0
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_alias_names fast_xs,fast-xs
Requires:      gem(hoe) >= 0
Requires:      gem(rack) >= 0
Requires:      gem(rake) >= 0.9.3
Conflicts:     gem(rake) >= 14
Provides:      gem(fast_xs) = 0.8.0.13

%ruby_use_gem_version fast_xs:0.8.0.13

%description
fast_xs provides C extensions for escaping text.

The original String.


%if_enabled    doc
%package       -n gem-fast-xs-doc
Version:       0.8.0.13
Release:       alt0.1
Summary:       fast_xs provides C extensions for escaping text documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fast_xs
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(fast_xs) = 0.8.0.13

%description   -n gem-fast-xs-doc
fast_xs provides C extensions for escaping text documentation files.

%description   -n gem-fast-xs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fast_xs.
%endif


%if_enabled    devel
%package       -n gem-fast-xs-devel
Version:       0.8.0.13
Release:       alt0.1
Summary:       fast_xs provides C extensions for escaping text development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fast_xs
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(fast_xs) = 0.8.0.13
Requires:      gem(rdoc) >= 4.0

%description   -n gem-fast-xs-devel
fast_xs provides C extensions for escaping text development package.

%description   -n gem-fast-xs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fast_xs.
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
%doc History.rdoc README.rdoc LICENSE
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-fast-xs-doc
%doc History.rdoc README.rdoc LICENSE
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fast-xs-devel
%doc History.rdoc README.rdoc LICENSE
%ruby_includedir/*
%endif


%changelog
* Tue Nov 18 2025 Pavel Skrylev <majioa@altlinux.org> 0.8.0.13-alt0.1
- 0.8.0 -> 0.8.0p13

* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- + packaged gem with Ruby Policy 2.0
