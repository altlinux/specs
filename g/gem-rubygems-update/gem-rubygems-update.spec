%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_disable   devel
%define        gemname rubygems-update

Name:          gem-rubygems-update
Epoch:         2
Version:       3.5.9
Release:       alt1
Summary:       Library packaging and distribution for Ruby
License:       Ruby or MIT
Group:         Development/Ruby
Url:           https://rubygems.org/
Vcs:           https://github.com/rubygems/rubygems.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         add_exec_gem.patch
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-rubygems-update < %EVR
Provides:      ruby-rubygems-update = %EVR
Provides:      gem(rubygems-update) = 3.5.9


%description
RubyGems is a package management framework for Ruby.

A package (also known as a library) contains a set of functionality that can be
invoked by a Ruby program, such as reading and parsing an XML file. We call
these packages "gems" and RubyGems is a tool to install, create, manage and load
these packages in your Ruby environment.

RubyGems is also a client for RubyGems.org, a public repository of Gems that
allows you to publish a Gem that can be shared and used by other developers. See
our guide on publishing a Gem at guides.rubygems.org


%package       -n gem-bundler
Version:       2.5.9
Release:       alt1
Summary:       Library packaging and distribution for Ruby
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(bundler) = 2.5.9

%description   -n gem-bundler
Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably


%package       -n bundle
Version:       2.5.9
Release:       alt1
Summary:       Library packaging and distribution for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета bundler
Group:         Other
BuildArch:     noarch

Requires(pre): alternatives >= 0:0.2.0-alt0.12
Requires:      gem(bundler) = 2.5.9

%description   -n bundle
Library packaging and distribution for Ruby executable(s).

Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably

%description   -n bundle -l ru_RU.UTF-8
Исполнямка для самоцвета bundler.


%if_enabled    doc
%package       -n gem-bundler-doc
Version:       2.5.9
Release:       alt1
Summary:       Library packaging and distribution for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bundler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bundler) = 2.5.9

%description   -n gem-bundler-doc
Library packaging and distribution for Ruby documentation files.

Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably

%description   -n gem-bundler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bundler.
%endif


%if_enabled    devel
%package       -n gem-bundler-devel
Version:       2.5.9
Release:       alt1
Summary:       Library packaging and distribution for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bundler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bundler) = 2.5.9

%description   -n gem-bundler-devel
Library packaging and distribution for Ruby development package.

Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably

%description   -n gem-bundler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bundler.
%endif


%package       -n gem
Version:       3.5.9
Release:       alt1
Summary:       Library packaging and distribution for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rubygems-update
Group:         Development/Ruby
BuildArch:     noarch

Requires(pre): alternatives >= 0:0.2.0-alt0.12
Requires:      gem(rubygems-update) = 3.5.9

%description   -n gem
Library packaging and distribution for Ruby executable(s).

RubyGems is a package management framework for Ruby.

A package (also known as a library) contains a set of functionality that can be
invoked by a Ruby program, such as reading and parsing an XML file. We call
these packages "gems" and RubyGems is a tool to install, create, manage and load
these packages in your Ruby environment.

RubyGems is also a client for RubyGems.org, a public repository of Gems that
allows you to publish a Gem that can be shared and used by other developers. See
our guide on publishing a Gem at guides.rubygems.org

%description   -n gem -l ru_RU.UTF-8
Исполнямка для самоцвета rubygems-update.


%if_enabled    doc
%package       -n gem-rubygems-update-doc
Version:       3.5.9
Release:       alt1
Summary:       Library packaging and distribution for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubygems-update
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubygems-update) = 3.5.9

%description   -n gem-rubygems-update-doc
Library packaging and distribution for Ruby documentation files.

RubyGems is a package management framework for Ruby.

A package (also known as a library) contains a set of functionality that can be
invoked by a Ruby program, such as reading and parsing an XML file. We call
these packages "gems" and RubyGems is a tool to install, create, manage and load
these packages in your Ruby environment.

RubyGems is also a client for RubyGems.org, a public repository of Gems that
allows you to publish a Gem that can be shared and used by other developers. See
our guide on publishing a Gem at guides.rubygems.org

%description   -n gem-rubygems-update-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubygems-update.


%package       -n gem-rubygems-update-devel
Version:       3.5.9
Release:       alt1
Summary:       Library packaging and distribution for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubygems-update
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubygems-update) = 3.5.9

%description   -n gem-rubygems-update-devel
Library packaging and distribution for Ruby development package.

RubyGems is a package management framework for Ruby.

A package (also known as a library) contains a set of functionality that can be
invoked by a Ruby program, such as reading and parsing an XML file. We call
these packages "gems" and RubyGems is a tool to install, create, manage and load
these packages in your Ruby environment.

RubyGems is also a client for RubyGems.org, a public repository of Gems that
allows you to publish a Gem that can be shared and used by other developers. See
our guide on publishing a Gem at guides.rubygems.org

%description   -n gem-rubygems-update-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubygems-update.
%endif


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

rm -rf %buildroot%_bindir/*
mkdir -p %buildroot%_altdir/
cat <<EOF >>%buildroot%_altdir/gem
%{_bindir}/gem %ruby_gemlibdir/exe/gem 100
%{_bindir}/update_rubygems %ruby_gemlibdir/exe/update_rubygems 100
EOF
cat <<EOF >>%buildroot%_altdir/bundle
%{_bindir}/bundle %ruby_gemlibdir/exe/bundle 100
%{_bindir}/bundler %ruby_gemlibdir/exe/bundler 100
EOF

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-bundler
%doc README.md
%ruby_gemspecdir/bundler-2.5.9.gemspec
%ruby_gemslibdir/bundler-2.5.9

%files         -n bundle
%doc README.md
%_altdir/bundle

%if_enabled    doc
%files         -n gem-bundler-doc
%doc README.md
%ruby_gemsdocdir/bundler-2.5.9
%endif

%if_enabled    devel
%files         -n gem-bundler-devel
%doc README.md
%endif

%files         -n gem
%doc README.md
%_altdir/gem

%if_enabled    doc
%files         -n gem-rubygems-update-doc
%doc README.md
%endif

%if_enabled    devel
%files         -n gem-rubygems-update-devel
%doc README.md
%endif


%changelog
* Sun Apr 21 2024 Pavel Skrylev <majioa@altlinux.org> 2:3.5.9-alt1
- ^ 3.5.6 -> 3.5.9
- + added gem executable, replacing gem package with new epoch
- + added binary alternatives

* Fri Mar 15 2024 Pavel Skrylev <majioa@altlinux.org> 3.5.6-alt1
- ^ 3.2.19 -> 3.5.6

* Tue Jun 15 2021 Pavel Skrylev <majioa@altlinux.org> 3.2.19-alt1
- ^ 3.0.4 -> 3.2.19
- ! CVE-2020-36327, CVE-2021-24105

* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.4-alt1
- Bump to 3.0.4
- Fix spec to conform setup.rb

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.3-alt1
- Bump to 3.0.3
- Use Ruby Policy 2.0

* Sat Dec 29 2018 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus, packaged as a gem
