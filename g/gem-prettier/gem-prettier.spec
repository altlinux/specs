%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname prettier

Name:          gem-prettier
Version:       4.0.4
Release:       alt1
Summary:       prettier plugin for the Ruby programming language
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/prettier/plugin-ruby#readme
Vcs:           https://github.com/prettier/plugin-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(syntax_tree) >= 4.0.1
BuildRequires: gem(syntax_tree-haml) >= 2.0.0
BuildRequires: gem(syntax_tree-rbs) >= 0.2.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.7.0
Requires:      gem(syntax_tree) >= 4.0.1
Requires:      gem(syntax_tree-haml) >= 2.0.0
Requires:      gem(syntax_tree-rbs) >= 0.2.0
Provides:      gem(prettier) = 4.0.4

%description
@prettier/plugin-ruby is a prettier plugin for the Ruby programming language and
its ecosystem. prettier is an opinionated code formatter that supports multiple
languages and integrates with most editors. The idea is to eliminate discussions
of style in code review and allow developers to get back to thinking about code
design instead.

The @prettier/plugin-ruby plugin for prettier is a small wrapper around the
Syntax Tree gem that provides a Ruby formatter for prettier. It does this by
keeping a Ruby server running in that background that prettier can communicate
with when it needs to format a Ruby file. This means that in order to function,
you will need to have both the requisite node and ruby dependencies installed.
Because of this configuration, there are a couple of ways that you can get setup
to use this plugin.

* If you're already using prettier in your project to format other files in your
  project and want to install this as a plugin, you can install it using npm.
* If you're not using prettier yet in your project, then we recommend using the
  Syntax Tree gem directly instead of using this plugin.
* Note that this plugin also ships a gem named prettier which is a wrapper
  around the prettier CLI and includes this plugin by default, but we no longer
  recommend its use. If you're using that gem, you should migrate to using
  Syntax Tree instead.


%package       -n rbprettier
Version:       4.0.4
Release:       alt1
Summary:       prettier plugin for the Ruby programming language executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета prettier
Group:         Other
BuildArch:     noarch

Requires:      gem(prettier) = 4.0.4

%description   -n rbprettier
prettier plugin for the Ruby programming language executable(s).

@prettier/plugin-ruby is a prettier plugin for the Ruby programming language and
its ecosystem. prettier is an opinionated code formatter that supports multiple
languages and integrates with most editors. The idea is to eliminate discussions
of style in code review and allow developers to get back to thinking about code
design instead.

The @prettier/plugin-ruby plugin for prettier is a small wrapper around the
Syntax Tree gem that provides a Ruby formatter for prettier. It does this by
keeping a Ruby server running in that background that prettier can communicate
with when it needs to format a Ruby file. This means that in order to function,
you will need to have both the requisite node and ruby dependencies installed.
Because of this configuration, there are a couple of ways that you can get setup
to use this plugin.

* If you're already using prettier in your project to format other files in your
  project and want to install this as a plugin, you can install it using npm.
* If you're not using prettier yet in your project, then we recommend using the
  Syntax Tree gem directly instead of using this plugin.
* Note that this plugin also ships a gem named prettier which is a wrapper
  around the prettier CLI and includes this plugin by default, but we no longer
  recommend its use. If you're using that gem, you should migrate to using
  Syntax Tree instead.

%description   -n rbprettier -l ru_RU.UTF-8
Исполнямка для самоцвета prettier.


%if_enabled    doc
%package       -n gem-prettier-doc
Version:       4.0.4
Release:       alt1
Summary:       prettier plugin for the Ruby programming language documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета prettier
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(prettier) = 4.0.4

%description   -n gem-prettier-doc
prettier plugin for the Ruby programming language documentation files.

@prettier/plugin-ruby is a prettier plugin for the Ruby programming language and
its ecosystem. prettier is an opinionated code formatter that supports multiple
languages and integrates with most editors. The idea is to eliminate discussions
of style in code review and allow developers to get back to thinking about code
design instead.

The @prettier/plugin-ruby plugin for prettier is a small wrapper around the
Syntax Tree gem that provides a Ruby formatter for prettier. It does this by
keeping a Ruby server running in that background that prettier can communicate
with when it needs to format a Ruby file. This means that in order to function,
you will need to have both the requisite node and ruby dependencies installed.
Because of this configuration, there are a couple of ways that you can get setup
to use this plugin.

* If you're already using prettier in your project to format other files in your
  project and want to install this as a plugin, you can install it using npm.
* If you're not using prettier yet in your project, then we recommend using the
  Syntax Tree gem directly instead of using this plugin.
* Note that this plugin also ships a gem named prettier which is a wrapper
  around the prettier CLI and includes this plugin by default, but we no longer
  recommend its use. If you're using that gem, you should migrate to using
  Syntax Tree instead.

%description   -n gem-prettier-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета prettier.
%endif


%if_enabled    devel
%package       -n gem-prettier-devel
Version:       4.0.4
Release:       alt1
Summary:       prettier plugin for the Ruby programming language development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета prettier
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(prettier) = 4.0.4
Requires:      gem(bundler) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-prettier-devel
prettier plugin for the Ruby programming language development package.

@prettier/plugin-ruby is a prettier plugin for the Ruby programming language and
its ecosystem. prettier is an opinionated code formatter that supports multiple
languages and integrates with most editors. The idea is to eliminate discussions
of style in code review and allow developers to get back to thinking about code
design instead.

The @prettier/plugin-ruby plugin for prettier is a small wrapper around the
Syntax Tree gem that provides a Ruby formatter for prettier. It does this by
keeping a Ruby server running in that background that prettier can communicate
with when it needs to format a Ruby file. This means that in order to function,
you will need to have both the requisite node and ruby dependencies installed.
Because of this configuration, there are a couple of ways that you can get setup
to use this plugin.

* If you're already using prettier in your project to format other files in your
  project and want to install this as a plugin, you can install it using npm.
* If you're not using prettier yet in your project, then we recommend using the
  Syntax Tree gem directly instead of using this plugin.
* Note that this plugin also ships a gem named prettier which is a wrapper
  around the prettier CLI and includes this plugin by default, but we no longer
  recommend its use. If you're using that gem, you should migrate to using
  Syntax Tree instead.

%description   -n gem-prettier-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета prettier.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n rbprettier
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%_bindir/rbprettier

%if_enabled    doc
%files         -n gem-prettier-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-prettier-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%endif


%changelog
* Wed Dec 11 2024 Pavel Skrylev <majioa@altlinux.org> 4.0.4-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
