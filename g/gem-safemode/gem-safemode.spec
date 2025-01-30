%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname safemode

Name:          gem-safemode
Version:       1.5.0.1
Release:       alt1
Summary:       A library for safe evaluation of Ruby code based on ParseTree/RubyParser and Ruby2Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/svenfuchs/safemode
Vcs:           https://github.com/svenfuchs/safemode.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(ruby2ruby) >= 2.4.0
BuildRequires: gem(ruby_parser) >= 3.10.1
BuildRequires: gem(sexp_processor) >= 4.10.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ruby2ruby) >= 2.4.0
Requires:      gem(ruby_parser) >= 3.10.1
Requires:      gem(sexp_processor) >= 4.10.0
Obsoletes:     ruby-safemode < %EVR
Provides:      ruby-safemode = %EVR
Provides:      gem(safemode) = 1.5.0.1


%description
A library for safe evaluation of Ruby code based on ParseTree/RubyParser and
Ruby2Ruby.

Provides Rails ActionView template handlers for ERB and Haml.


%if_enabled    doc
%package       -n gem-safemode-doc
Version:       1.5.0.1
Release:       alt1
Summary:       A library for safe evaluation of Ruby code based on ParseTree/RubyParser and Ruby2Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета safemode
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(safemode) = 1.5.0.1

%description   -n gem-safemode-doc
A library for safe evaluation of Ruby code based on ParseTree/RubyParser and
Ruby2Ruby documentation files.

%description   -n gem-safemode-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета safemode.
%endif


%if_enabled    devel
%package       -n gem-safemode-devel
Version:       1.5.0.1
Release:       alt1
Summary:       A library for safe evaluation of Ruby code based on ParseTree/RubyParser and Ruby2Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета safemode
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(safemode) = 1.5.0.1
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-safemode-devel
A library for safe evaluation of Ruby code based on ParseTree/RubyParser and
Ruby2Ruby development package.

%description   -n gem-safemode-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета safemode.
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
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-safemode-doc
%doc README.markdown
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-safemode-devel
%doc README.markdown
%endif


%changelog
* Tue Oct 01 2024 Pavel Skrylev <majioa@altlinux.org> 1.5.0.1-alt1
- ^ 1.3.7 -> 1.5.0p1

* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 1.3.7-alt1
- ^ 1.3.6 -> 1.3.7

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.6-alt1
- ^ 1.3.5 -> 1.3.6
- ! spec tags

* Sat Mar 23 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.5-alt2
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.5-alt1
- Initial build for Sisyphus
