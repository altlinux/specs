%define        gemname optimist

Name:          gem-optimist
Version:       3.0.1
Release:       alt1
Summary:       Optimist is a commandline option parser for Ruby that just gets out of your way
License:       MIT
Group:         Development/Ruby
Url:           http://manageiq.github.io/optimist/
Vcs:           https://github.com/manageiq/optimist.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.4.3 gem(minitest) < 6
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(chronic) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(optimist) = 3.0.1

%description
Optimist is a commandline option parser for Ruby that just gets out of your way.
One line of code per option is all you need to write. For that, you get a nice
automatically-generated help page, robust option parsing, and sensible defaults
for everything you don't specify.


%package       -n gem-optimist-doc
Version:       3.0.1
Release:       alt1
Summary:       Optimist is a commandline option parser for Ruby that just gets out of your way documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета optimist
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(optimist) = 3.0.1

%description   -n gem-optimist-doc
Optimist is a commandline option parser for Ruby that just gets out of your way
documentation files.

One line of code per option is all you need to write. For that, you get a nice
automatically-generated help page, robust option parsing, and sensible defaults
for everything you don't specify.

%description   -n gem-optimist-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета optimist.


%package       -n gem-optimist-devel
Version:       3.0.1
Release:       alt1
Summary:       Optimist is a commandline option parser for Ruby that just gets out of your way development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета optimist
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(optimist) = 3.0.1
Requires:      gem(minitest) >= 5.4.3 gem(minitest) < 6
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(chronic) >= 0

%description   -n gem-optimist-devel
Optimist is a commandline option parser for Ruby that just gets out of your way
development package.

One line of code per option is all you need to write. For that, you get a nice
automatically-generated help page, robust option parsing, and sensible defaults
for everything you don't specify.

%description   -n gem-optimist-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета optimist.


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

%files         -n gem-optimist-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-optimist-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- ^ 3.0.0 -> 3.0.1

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
