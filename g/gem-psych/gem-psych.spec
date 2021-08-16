%define        gemname psych

Name:          gem-psych
Version:       4.0.1
Release:       alt1
Summary:       A libyaml wrapper for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby/psych
Vcs:           https://github.com/ruby/psych.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names fixtures
Provides:      gem(psych) = 4.0.1


%description
Psych is a YAML parser and emitter. Psych leverages libyaml for its YAML parsing
and emitting capabilities. In addition to wrapping libyaml, Psych also knows how
to serialize and de-serialize most Ruby objects to and from the YAML format.


%package       -n gem-psych-doc
Version:       4.0.1
Release:       alt1
Summary:       A libyaml wrapper for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета psych
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(psych) = 4.0.1

%description   -n gem-psych-doc
A libyaml wrapper for Ruby documentation files.

Psych is a YAML parser and emitter. Psych leverages libyaml for its YAML parsing
and emitting capabilities. In addition to wrapping libyaml, Psych also knows how
to serialize and de-serialize most Ruby objects to and from the YAML format.

%description   -n gem-psych-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета psych.


%package       -n gem-psych-devel
Version:       4.0.1
Release:       alt1
Summary:       A libyaml wrapper for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета psych
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(psych) = 4.0.1

%description   -n gem-psych-devel
A libyaml wrapper for Ruby development package.

Psych is a YAML parser and emitter. Psych leverages libyaml for its YAML parsing
and emitting capabilities. In addition to wrapping libyaml, Psych also knows how
to serialize and de-serialize most Ruby objects to and from the YAML format.

%description   -n gem-psych-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета psych.


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
%ruby_gemextdir

%files         -n gem-psych-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-psych-devel
%doc README.md
%ruby_includedir/*


%changelog
* Tue Jun 29 2021 Pavel Skrylev <majioa@altlinux.org> 4.0.1-alt1
- ^ 3.2.0 -> 4.0.1

* Mon Nov 23 2020 Pavel Skrylev <majioa@altlinux.org> 3.2.0-alt1
- ^ 3.1.1pre -> 3.2.0

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.1-alt0.1
- ^ 3.1.0 -> 3.1.1pre
- ! spec syntax and tags

* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
