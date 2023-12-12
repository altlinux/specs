%define        _unpackaged_files_terminate_build 1
%define        gemname with_env

Name:          gem-with-env
Version:       1.1.0
Release:       alt1
Summary:       WithEnv is an extremely small helper module for executing code with ENV variables
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mhs/with_env-rb
Vcs:           https://github.com/mhs/with_env-rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.10
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rspec) >= 3
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Provides:      gem(with_env) = 1.1.0


%description
WithEnv is an extremely small helper module for executing code with ENV
variables. It exists because I got tired of re-writing or copying over a
\#with_env helper method for the 131st time.


%package       -n gem-with-env-doc
Version:       1.1.0
Release:       alt1
Summary:       WithEnv is an extremely small helper module for executing code with ENV variables documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета with_env
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(with_env) = 1.1.0

%description   -n gem-with-env-doc
WithEnv is an extremely small helper module for executing code with ENV
variables documentation files.

WithEnv is an extremely small helper module for executing code with ENV
variables. It exists because I got tired of re-writing or copying over a
\#with_env helper method for the 131st time.

%description   -n gem-with-env-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета with_env.


%package       -n gem-with-env-devel
Version:       1.1.0
Release:       alt1
Summary:       WithEnv is an extremely small helper module for executing code with ENV variables development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета with_env
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(with_env) = 1.1.0
Requires:      gem(bundler) >= 1.10
Requires:      gem(rake) >= 10.0
Requires:      gem(rspec) >= 3
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-with-env-devel
WithEnv is an extremely small helper module for executing code with ENV
variables development package.

WithEnv is an extremely small helper module for executing code with ENV
variables. It exists because I got tired of re-writing or copying over a
\#with_env helper method for the 131st time.

%description   -n gem-with-env-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета with_env.


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

%files         -n gem-with-env-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-with-env-devel
%doc README.md


%changelog
* Tue Dec 05 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
