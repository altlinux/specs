%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname latest_ruby

Name:          gem-latest-ruby
Version:       3.3.0
Release:       alt1
Summary:       Answers the question of what the latest Ruby version is
License:       Zlib
Group:         Development/Ruby
Url:           https://github.com/kyrylo/latest_ruby
Vcs:           https://github.com/kyrylo/latest_ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         license.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-reporters) >= 0
BuildRequires: gem(vcr) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(versionomy) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names latest_ruby,latest-ruby
Provides:      gem(latest_ruby) = 3.3.0


%description
Knows about MRI, Rubinius, JRuby, MagLev and MacRuby.


%if_enabled    doc
%package       -n gem-latest-ruby-doc
Version:       3.3.0
Release:       alt1
Summary:       Answers the question of what the latest Ruby version is documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета latest_ruby
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(latest_ruby) = 3.3.0

%description   -n gem-latest-ruby-doc
Answers the question of what the latest Ruby version is documentation
files.

Knows about MRI, Rubinius, JRuby, MagLev and MacRuby.

%description   -n gem-latest-ruby-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета latest_ruby.
%endif


%if_enabled    devel
%package       -n gem-latest-ruby-devel
Version:       3.3.0
Release:       alt1
Summary:       Answers the question of what the latest Ruby version is development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета latest_ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(latest_ruby) = 3.3.0
Requires:      gem(rake) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-reporters) >= 0
Requires:      gem(vcr) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(versionomy) >= 0

%description   -n gem-latest-ruby-devel
Answers the question of what the latest Ruby version is development
package.

Knows about MRI, Rubinius, JRuby, MagLev and MacRuby.

%description   -n gem-latest-ruby-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета latest_ruby.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-latest-ruby-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-latest-ruby-devel
%doc README.md
%endif


%changelog
* Wed May 08 2024 Pavel Skrylev <majioa@altlinux.org> 3.3.0-alt1
- ^ 3.0.1 -> 3.3.0
- * relicensed

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- + packaged gem with Ruby Policy 2.0
