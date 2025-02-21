%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname psych

Name:          gem-psych
Version:       5.2.3
Release:       alt1
Summary:       A libyaml wrapper for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby/psych
Vcs:           https://github.com/ruby/psych.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libyaml-devel
%if_enabled check
BuildRequires: gem(date) >= 0
BuildRequires: gem(rake-compiler) >= 0.4.1
BuildRequires: gem(stringio) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.5.0
Requires:      gem(date) >= 0
Requires:      gem(stringio) >= 0
Provides:      gem(psych) = 5.2.3

%description
Psych is a YAML parser and emitter. Psych leverages libyaml for its YAML parsing
and emitting capabilities. In addition to wrapping libyaml, Psych also knows how
to serialize and de-serialize most Ruby objects to and from the YAML format.


%if_enabled    doc
%package       -n gem-psych-doc
Version:       5.2.3
Release:       alt1
Summary:       A libyaml wrapper for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета psych
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(psych) = 5.2.3

%description   -n gem-psych-doc
A libyaml wrapper for Ruby documentation files.

Psych is a YAML parser and emitter. Psych leverages libyaml for its YAML parsing
and emitting capabilities. In addition to wrapping libyaml, Psych also knows how
to serialize and de-serialize most Ruby objects to and from the YAML format.

%description   -n gem-psych-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета psych.
%endif


%if_enabled    devel
%package       -n gem-psych-devel
Version:       5.2.3
Release:       alt1
Summary:       A libyaml wrapper for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета psych
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(psych) = 5.2.3
Requires:      gem(rake-compiler) >= 0.4.1
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0

%description   -n gem-psych-devel
A libyaml wrapper for Ruby development package.

Psych is a YAML parser and emitter. Psych leverages libyaml for its YAML parsing
and emitting capabilities. In addition to wrapping libyaml, Psych also knows how
to serialize and de-serialize most Ruby objects to and from the YAML format.

%description   -n gem-psych-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета psych.
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
%doc CONTRIBUTING.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-psych-doc
%doc CONTRIBUTING.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-psych-devel
%doc CONTRIBUTING.md LICENSE README.md
%ruby_includedir/*
%endif


%changelog
* Sun Feb 16 2025 Pavel Skrylev <majioa@altlinux.org> 5.2.3-alt1
- ^ 4.0.6 -> 5.2.3

* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 4.0.6-alt1
- ^ 4.0.4 -> 4.0.6

* Thu Jul 07 2022 Pavel Skrylev <majioa@altlinux.org> 4.0.4-alt1
- ^ 4.0.1 -> 4.0.4

* Tue Jun 29 2021 Pavel Skrylev <majioa@altlinux.org> 4.0.1-alt1
- ^ 3.2.0 -> 4.0.1

* Mon Nov 23 2020 Pavel Skrylev <majioa@altlinux.org> 3.2.0-alt1
- ^ 3.1.1pre -> 3.2.0

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.1-alt0.1
- ^ 3.1.0 -> 3.1.1pre
- ! spec syntax and tags

* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
